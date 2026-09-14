"""Warstwa danych: ORM (baza) z fallbackiem do mbt_data.py.

Widoki używają get_projects()/get_site()/itd. i dostają dict o IDENTYCZNYM
kształcie jak w mbt_data.py — dzięki temu szablony nie znają źródła danych.
Jeśli baza jest pusta (np. świeża instalacja przed seedem), zwracamy dane
statyczne z mbt_data.py, więc strona zawsze działa.

Zdjęcia realizacji: można je też wrzucać do folderów na dysku:
    MBTApp/static/img/mbt/projekty/<slug>/
        main.jpg   (lub .png/.webp)  → zdjęcie główne (hero)
        1.jpg, 2.png, 3.webp ...      → galeria (kolejność wg numeru)
Jeśli folder istnieje i zawiera zdjęcia — wygrywają one z CMS-em.
Jeśli folder jest pusty lub nie istnieje — używane są dane z CMS (admin).
"""
import html
import os
import re

from django.conf import settings

from MBTApp import mbt_data

import time
from functools import wraps

_CACHE = {}
CACHE_TTL = 60  # 60 sekund

def _cached(key_prefix):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{key_prefix}_{args}_{kwargs}"
            now = time.time()
            if key in _CACHE:
                cached_time, data = _CACHE[key]
                if now - cached_time < CACHE_TTL:
                    return data
            data = func(*args, **kwargs)
            _CACHE[key] = (now, data)
            return data
        return wrapper
    return decorator

from MBTApp.models import Project, Job, Worker, Reference, Article, SiteConfig, SitePhotos, SalesRepresentative, Award


# ---------------------------------------------------------------------------
# Wielojęzyczność — zwraca tłumaczenie pola JSON (dict {lang: text}) lub fallback
# ---------------------------------------------------------------------------

def _t(trans_dict, lang='pl', fallback=''):
    """Zwraca tekst z dicta tłumaczeń dla danego języka, fallback na polski/PL.

    Przykład: _t(p.t_title, 'en', p.title) — zwróci angielskie tłumaczenie
    tytułu lub polski oryginał jeśli brak.
    """
    try:
        from MBTApp.auto_translate import translate
    except ImportError:
        translate = lambda text, source, target: text

    if not isinstance(trans_dict, dict):
        if fallback and lang != 'pl':
            return translate(fallback, source='pl', target=lang)
        return fallback

    val = trans_dict.get(lang)
    if val:
        return val

    pl_text = trans_dict.get('pl') or fallback
    if pl_text and lang != 'pl':
        return translate(pl_text, source='pl', target=lang)
    
    return pl_text


def _project_translate(p_dict, lang='pl'):
    """Fallback (gdy brak DB): tłumaczy pola rekordu z mbt_data (t_*) na aktywny język."""
    keys_to_translate = {
        'title': 't_t', 'position': 't_p', 'opis': 't_o', 'text': 't_x',
        'status': 't_s', 'czas': 't_c', 'formula': 't_f',
        'osoba': 't_o', 'stanowisko': 't_s', 'tresc': 't_r',
        'excerpt': 't_e',
    }
    for src_key, t_key in keys_to_translate.items():
        if src_key in p_dict and t_key in p_dict:
            t_dict = p_dict[t_key]
            if isinstance(t_dict, dict) and lang in t_dict:
                p_dict[src_key] = t_dict[lang]
    return p_dict


# ---------------------------------------------------------------------------
# Zdjęcia realizacji z folderów na dysku (projekty/<slug>/)
# ---------------------------------------------------------------------------

_PHOTO_EXTS = (".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif")
_MAIN_NAMES = ("main.jpg", "main.png", "main.webp", "main.jpeg", "main.gif", "main.avif")


def _projects_photo_dir():
    """Katalog bazowy ze zdjęciami realizacji (lokalnie i na Vercel w repo)."""
    return os.path.join(settings.BASE_DIR, "MBTApp", "static", "img", "mbt", "projekty")


def _apply_folder_photos(project):
    """Jeśli katalog projekty/<slug>/ ma zdjęcia, użyj ich jako fallback dla hero/gallery.
    Dane ustawione w CMS (baza danych) mają priorytet.
    """
    slug = (project.get("slug") or "").strip()
    if not slug:
        return project
    folder = os.path.join(_projects_photo_dir(), slug)
    if not os.path.isdir(folder):
        return project
    try:
        files = os.listdir(folder)
    except OSError:
        return project
    photos = [f for f in files if f.lower().endswith(_PHOTO_EXTS)]
    if not photos:
        return project

    base = f"/static/img/mbt/projekty/{slug}/"

    # Jeśli CMS nie ma zdjęcia hero, szukaj w folderze
    if not project.get("hero"):
        for f in photos:
            if f.lower() in _MAIN_NAMES:
                project["hero"] = base + f
                break

    # Jeśli CMS nie ma galerii, szukaj w folderze (pliki 1.jpg, 2.jpg...)
    if not project.get("gallery"):
        numbered = []
        for f in photos:
            stem = os.path.splitext(f)[0]
            if stem.isdigit():
                numbered.append((int(stem), f))
        numbered.sort(key=lambda x: x[0])
        if numbered:
            project["gallery"] = [base + f for _, f in numbered]

    return project



# ---------------------------------------------------------------------------
# Projekty (realizacje)
# ---------------------------------------------------------------------------

@_cached('projects')
def get_projects(lang='pl'):
    try:
        projects = []
        for p in Project.objects.all().order_by('order', 'title'):
            proj = {
                'title': _t(p.t_title, lang, p.title),
                'slug': p.slug,
                'type': p.type,
                'status': _t(p.t_status, lang, p.status),
                'czas': _t(p.t_czas, lang, p.czas),
                'formula': _t(p.t_formula, lang, p.formula),
                'opis': _t(p.t_opis, lang, p.opis),
                'logo': p.logo,
                'hero': p.hero,
                'gallery': p.gallery or [],
                'latitude': p.latitude,
                'longitude': p.longitude,
                'order': p.order,
            }
            projects.append(_apply_folder_photos(proj))
        if projects: return projects
    except Exception:
        pass
    return [_apply_folder_photos(_project_translate(dict(p), lang)) for p in mbt_data.PROJECTS]


def get_project_by_slug(slug, lang='pl'):
    try:
        try:
            p = Project.objects.get(slug=slug)
            proj = {
                'title': _t(p.t_title, lang, p.title),
                'slug': p.slug,
                'type': p.type,
                'status': _t(p.t_status, lang, p.status),
                'czas': _t(p.t_czas, lang, p.czas),
                'formula': _t(p.t_formula, lang, p.formula),
                'opis': _t(p.t_opis, lang, p.opis),
                'logo': p.logo,
                'hero': p.hero,
                'gallery': p.gallery or [],
                'latitude': p.latitude,
                'longitude': p.longitude,
            }
            return _apply_folder_photos(proj)
        except Project.DoesNotExist:
            return None
    except Exception:
        pass
    for p in mbt_data.PROJECTS:
        if p['slug'] == slug:
            d = _project_translate(dict(p), lang)
            return _apply_folder_photos(d)
    return None


# ---------------------------------------------------------------------------
# Oferty pracy (kariera)
# ---------------------------------------------------------------------------

def parse_job_text(text):
    if not text:
        return []
    text = text.replace(" ✓ ", "\n✓ ")
    headers = ["Twój zakres obowiązków", "Nasze wymagania", "To oferujemy", "Aplikuj na to stanowisko", "Proces rekrutacji prowadzimy", "Proces rekrutacji"]
    for h in headers:
        text = text.replace(h, f"\n{h}")
    lines = []
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("✓"):
            lines.append({"type": "item", "text": line[1:].strip()})
        else:
            lines.append({"type": "header", "text": line})
    return lines

@_cached('jobs')
def get_jobs(lang='pl'):
    try:
        res = []
        for j in Job.objects.all():
            job_dict = {'title': _t(j.t_title, lang, j.title), 'slug': j.slug, 'text': _t(j.t_text, lang, j.text)}
            job_dict['lines'] = parse_job_text(job_dict['text'])
            res.append(job_dict)
        if res: return res
    except Exception:
        pass
    
    fallback_res = []
    for j in mbt_data.JOBS:
        t_dict = _project_translate(dict(j), lang)
        t_dict['lines'] = parse_job_text(t_dict.get('text', ''))
        fallback_res.append(t_dict)
    return fallback_res


def get_job_by_slug(slug, lang='pl'):
    try:
        j = Job.objects.get(slug=slug)
        job_dict = {'title': _t(j.t_title, lang, j.title), 'slug': j.slug, 'text': _t(j.t_text, lang, j.text)}
        job_dict['lines'] = parse_job_text(job_dict['text'])
        return job_dict
    except Job.DoesNotExist:
        return None
    except Exception:
        pass
    for j in mbt_data.JOBS:
        if j['slug'] == slug:
            t_dict = _project_translate(dict(j), lang)
            t_dict['lines'] = parse_job_text(t_dict.get('text', ''))
            return t_dict
    return None


# ---------------------------------------------------------------------------
# Pracownicy (zespół)
# ---------------------------------------------------------------------------

@_cached('workers')
def get_workers(lang='pl'):
    try:
        res = [
            {'name': w.name, 'position': _t(w.t_position, lang, w.position), 'opis': _t(w.t_opis, lang, w.opis),
             'photo': w.photo, 'linkedin': w.linkedin}
            for w in Worker.objects.all()
        ]
        if res: return res
    except Exception:
        pass
    return [_project_translate(dict(w), lang) for w in mbt_data.WORKERS]


@_cached('sales_reps')
def get_sales_reps(lang='pl'):
    try:
        res = [
            {'name': s.name, 'position': _t(s.t_position, lang, s.position),
             'email': s.email, 'phone': s.phone, 'photo': s.photo}
            for s in SalesRepresentative.objects.all().order_by('order', 'name')
        ]
        if res: return res
    except Exception:
        pass
    return [_project_translate(dict(s), lang) for s in getattr(mbt_data, 'SALES_REPS', [])]


# ---------------------------------------------------------------------------
# Opinie klientów
# ---------------------------------------------------------------------------

# Mapowanie nazwy firmy (z opinii) na plik logo — trusted-us-*.svg
_REFERENCE_LOGOS = {
    'browar zamkowy': '/static/img/mbt/trusted-us-browar-zamkowy.svg',
    'canpack': '/static/img/mbt/trusted-us-canpack.svg',
    'euronova': '/static/img/mbt/trusted-us-euronova.svg',
    'euro-trade': '/static/img/mbt/trusted-us-euro-trade.svg',
    'herz': '/static/img/mbt/trusted-us-herz.svg',
    'sutco': '/static/img/mbt/trusted-us-sutco-polska.svg',
    'toto': '/static/img/mbt/trusted-us-toto.svg',
    'pumar': '/static/img/mbt/trusted-us-pumar.svg',
    'less mess': '/static/img/mbt/trusted-us-less-mess-storage.svg',
    'huber': '/static/img/mbt/trusted-us-huber-suhner.svg',
    'kompania': '/static/img/mbt/trusted-us-kompania-piwowarska.svg',
    'bater': '/static/img/mbt/trusted-us-bater.svg',
    'cdr': '/static/img/mbt/trusted-us-cdr.svg',
    'dl invest': '/static/img/mbt/trusted-us-dl-invest-group.svg',
    'epco': '/static/img/mbt/trusted-us-epco.svg',
    'stainless': '/static/img/mbt/trusted-us-stainless-steel-engineering.svg',
}


def _reference_logo(firma: str) -> str:
    """Znajdź logo dla nazwy firmy (przybliżone dopasowanie, lowercase)."""
    if not firma:
        return ''
    low = firma.lower()
    for key, path in _REFERENCE_LOGOS.items():
        if key in low:
            return path
    return ''


@_cached('references')
def get_references(lang='pl'):
    try:
        refs = []
        for r in Reference.objects.all():
            refs.append({
                'firma': r.firma,
                'tresc': _t(r.t_tresc, lang, r.tresc),
                'osoba': _t(r.t_osoba, lang, r.osoba),
                'stanowisko': _t(r.t_stanowisko, lang, r.stanowisko),
                'logo': _reference_logo(r.firma),
            })
        if refs: return refs
    except Exception:
        pass
    refs = []
    for r in mbt_data.REFERENCES:
        d = _project_translate(dict(r), lang)
        d['logo'] = _reference_logo(d.get('firma', ''))
        refs.append(d)
    return refs


# ---------------------------------------------------------------------------
# Artykuły (blog)
# ---------------------------------------------------------------------------

def _plain_text(value: str) -> str:
    """Usuń tagi HTML i zamień encje (np. &nbsp; -> spacja) na czysty tekst."""
    if not value:
        return ''
    text = re.sub(r'<[^>]+>', ' ', value)
    return html.unescape(text)


@_cached('articles')
def get_articles(lang='pl'):
    try:
        arts = []
        for a in Article.objects.filter(published=True):
            title = _t(a.t_title, lang, a.title)
            excerpt = _t(a.t_excerpt, lang, a.excerpt)
            arts.append({
                'title': title,
                'slug': a.slug,
                'excerpt': excerpt,
                'excerpt_plain': _plain_text(excerpt),
                'text': _t(a.t_text, lang, a.text),
                'image': a.image,
                'gallery': a.gallery,
            })
        if arts: return arts
    except Exception:
        pass
    arts = []
    for a in mbt_data.ARTICLES:
        d = _project_translate(dict(a), lang)
        d['excerpt_plain'] = _plain_text(d.get('excerpt', ''))
        arts.append(d)
    return arts


def get_article_by_slug(slug, lang='pl'):
    try:
        a = Article.objects.get(slug=slug, published=True)
        return {
            'title': _t(a.t_title, lang, a.title), 'slug': a.slug,
            'excerpt': _t(a.t_excerpt, lang, a.excerpt), 'text': _t(a.t_text, lang, a.text), 'image': a.image, 'gallery': a.gallery,
        }
    except Article.DoesNotExist:
        return None
    except Exception:
        pass
    for a in mbt_data.ARTICLES:
        if a['slug'] == slug:
            d = _project_translate(dict(a), lang)
            d['excerpt_plain'] = _plain_text(d.get('excerpt', ''))
            return d
    return None


# ---------------------------------------------------------------------------
# Dane firmy (SITE)
# ---------------------------------------------------------------------------

@_cached('site')
def get_site(lang='pl'):
    try:
        try:
            c = SiteConfig.objects.first()
        except Exception:
            c = None
        if c is not None:
            return {
                'phone': c.phone,
                'phone_href': c.phone_href,
                'email': c.email,
                'hours': _t(c.t_hours, lang, c.hours),
                'hours_long': _t(c.t_hours_long, lang, c.hours_long),
                'office_zabrze': _t(c.t_office_zabrze, lang, c.office_zabrze),
                'office_katowice': _t(c.t_office_katowice, lang, c.office_katowice),
                'office_krakow': _t(c.t_office_krakow, lang, c.office_krakow),
                'office_zabrze_photo': c.office_zabrze_photo,
                'office_katowice_photo': c.office_katowice_photo,
                'office_krakow_photo': c.office_krakow_photo,
                'office_site_label': c.office_site_label,
                'office_site_adres': c.office_site_adres,
                'office_site_photo': c.office_site_photo,
                'nip': c.nip,
                'regon': c.regon,
                'krs': c.krs,
                'founded': c.founded,
                'tagline': _t(c.t_tagline, lang, c.tagline),
                'about_short': _t(c.t_about_short, lang, c.about_short),
                'counter_years': c.counter_years,
                'counter_years_label': _t(c.t_counter_years_label, lang, c.counter_years_label),
                'counter_projects': c.counter_projects,
                'counter_projects_label': _t(c.t_counter_projects_label, lang, c.counter_projects_label),
                'counter_ontime': c.counter_ontime,
                'counter_ontime_suffix': c.counter_ontime_suffix,
                'counter_ontime_label': _t(c.t_counter_ontime_label, lang, c.counter_ontime_label),
                'counter_brands': c.counter_brands,
                'counter_brands_label': _t(c.t_counter_brands_label, lang, c.counter_brands_label),
                'hero_subtitle': _t(c.t_hero_subtitle, lang, c.hero_subtitle),
                'hero_title1': _t(c.t_hero_title1, lang, c.hero_title1),
                'hero_title2': _t(c.t_hero_title2, lang, c.hero_title2),
                'hero_text': _t(c.t_hero_text, lang, c.hero_text),
                'social_linkedin': c.social_linkedin,
                'social_youtube': c.social_youtube,
                'social_facebook': c.social_facebook,
                'hero_video': c.hero_video,
            }
    except Exception:
        pass
    # Fallback z mbt_data.py z tłumaczeniem gettext dla etykiet
    s = dict(mbt_data.SITE)
    from django.utils.translation import override as _override, gettext as _gettext
    with _override(lang):
        s['tagline'] = _gettext(s.get('tagline', ''))
        s['about_short'] = _gettext(s.get('about_short', ''))
        s['hours'] = _gettext(s.get('hours', ''))
        s['hours_long'] = _gettext(s.get('hours_long', ''))
        s['counter_years_label'] = _gettext(s.get('counter_years_label', ''))
        s['counter_projects_label'] = _gettext(s.get('counter_projects_label', ''))
        s['counter_ontime_label'] = _gettext(s.get('counter_ontime_label', ''))
        s['counter_brands_label'] = _gettext(s.get('counter_brands_label', ''))
        s['office_site_label'] = _gettext(s.get('office_site_label', ''))
        s['office_site_adres'] = _gettext(s.get('office_site_adres', ''))
        
        s['hero_subtitle'] = _gettext('Od 20 lat z pasją budujemy Wasze biznesy')
        s['hero_title1'] = _gettext('Twój Generalny')
        s['hero_title2'] = _gettext('Wykonawca')
        s['hero_text'] = _gettext('Jeden team – pełna realizacja. <strong>Od projektu aż po dach!</strong> Budujemy hale magazynowe, produkcyjne i usługowe pod klucz.')
    return s


# ---------------------------------------------------------------------------
# Fotografie strony (SitePhotos) — podmienialne z admina (upload na R2)
# ---------------------------------------------------------------------------

@_cached('photos')
def get_photos():
    """Zwróć dict fotografie strony: klucz -> URL.

    Wartości z bazy (admin → upload na R2) mają priorytet; puste pole
    oznacza domyślną ścieżkę statyczną zdefiniowaną w modelu. Fallback
    (baza pusta/niedostępna) — same domyślne ścieżki z mbt_data.PHOTOS.
    """
    out = dict(getattr(mbt_data, 'PHOTOS', {}))
    try:
        try:
            c = SitePhotos.objects.first()
        except Exception:
            c = None
        if c is not None:
            for field in SitePhotos._meta.fields:
                if field.name == 'id':
                    continue
                val = getattr(c, field.name, '')
                default_val = field.default if field.has_default() else ''
                out[field.name] = val or default_val or out.get(field.name, '')
            return out
    except Exception:
        pass
    return out

@_cached('awards')
def get_awards():
    try:
        res = [{'name': a.name, 'image': a.image if a.image else ''} for a in Award.objects.filter(is_active=True)]
        if res: return res
    except Exception:
        pass
    
    # Fallback to mbt_data on Vercel
    awards = []
    for a in getattr(mbt_data, 'AWARDS', []):
        awards.append(a)
    return awards


def get_sectors(lang='pl'):
    try:
        from MBTApp.models import Sector
        from django.urls import reverse
        from django.db.utils import OperationalError
        try:
            db_sectors = list(Sector.objects.all().order_by('order'))
            if db_sectors:
                res = []
                for s in db_sectors:
                    title = _t(s.t_title, lang, s.title)
                    opis = _t(s.t_opis, lang, s.opis)
                    
                    # Bezpieczne generowanie URL
                    if s.view_name.startswith('#') or s.view_name.startswith('http') or s.view_name.startswith('/'):
                        resolved_url = s.view_name
                    else:
                        try:
                            if s.slug:
                                resolved_url = reverse(s.view_name, args=[s.slug])
                            else:
                                resolved_url = reverse(s.view_name)
                        except Exception:
                            resolved_url = '#'

                    res.append({
                        'title': title,
                        'slug': s.slug,
                        'view_name': s.view_name,
                        'url': resolved_url,
                        'opis': opis,
                        'icon': s.icon,
                        'image': s.image,
                        'order': s.order,
                    })
                return res

        except OperationalError:
            pass
    except Exception:
        pass
    
    # Fallback to mbt_data
    res = []
    if hasattr(mbt_data, "SECTORS"):
        for s in mbt_data.SECTORS:
            title = _t(s.get("t_t"), lang, s.get("title"))
            opis = _t(s.get("t_o"), lang, s.get("opis"))
            resolved_url = s.get("view_name")
            if resolved_url and not (resolved_url.startswith("#") or resolved_url.startswith("http") or resolved_url.startswith("/")):
                try:
                    from django.urls import reverse
                    if s.get("slug"):
                        resolved_url = reverse(resolved_url, args=[s.get("slug")])
                    else:
                        resolved_url = reverse(resolved_url)
                except Exception:
                    resolved_url = "#"
            elif not resolved_url:
                resolved_url = "#"

            res.append({
                "title": title,
                "slug": s.get("slug"),
                "view_name": s.get("view_name"),
                "url": resolved_url,
                "opis": opis,
                "icon": s.get("icon"),
                "image": s.get("image"),
                "order": s.get("order"),
            })
    return res
