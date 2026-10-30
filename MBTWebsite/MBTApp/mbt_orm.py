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



PROJECT_HERO_FALLBACKS = {
    'att-kokotow': '/static/img/mbt/ZREALIZOWANE-ATT-1-scaled-f12dacac.jpg',
    'pumar': '/static/img/mbt/hala-1024x672-eb7144c9.jpg',
    'less-mess-storage-warszawa': '/static/img/mbt/LessMess-1-3370ce84.jpg',
    'kompania-piwowarska-tychy': '/static/img/mbt/ZREALIZOWANE-ATT-6-scaled-e17253f9.jpg',
    'fabryka-park-katowice': '/static/img/mbt/DSC03726-scaled-04284a3e.jpeg',
    'eurosleeve-zabrze': '/static/img/mbt/Eurosleeve-12-scaled-a4ea9500.jpg',
    'stokado-self-storage-krakow': '/static/img/mbt/realizacja-stokado.jpg',
    'fronton-krakow': '/static/img/mbt/Fronton-1-scaled-42981731.jpg',
    'browar-zamkowy-raciborz': '/static/img/mbt/mbt-browar-raciborz-8-03eeadf7.jpg',
    'stokado-self-storage-warszawa-bemowo': '/static/img/mbt/DJI_0174-scaled-5106e265.jpeg',
    'huber-suhner-pisary': '/static/img/mbt/Huber-1-scaled-1d0326ab.jpg',
    'euronova-kokotow-gm-wieliczka': '/static/img/mbt/realizacja-euronova.jpg',
    'euro-trade-w-modlnicy': '/static/img/mbt/IMG_20220722_102111-scaled-1-ceffec28.jpg',
    'kompania-piwowarska': '/static/img/mbt/ZREALIZOWANE-ATT-5-scaled-b27ef1aa.jpg',
    'in-post-w-legnicy': '/static/img/mbt/IMG_20220406_131518-scaled-1-84d560cd.jpg',
    'sutco-katowice': '/static/img/mbt/jpg_22-1-1-3fa214ab.jpg',
    'canpack-bss-lab-brzesk': '/static/img/mbt/CANPACK-BSS-LAB-w-Brzesku-3-1-f34a5df7.jpg',
    'p1704': '/static/img/mbt/3-2-scaled-38947c85.jpg',
    'herz-wieliczka': '/static/img/mbt/Herz-docel-2-1-scaled-1-04664ed6.jpg',
    'toto-glogoczow': 'https://media.mbt.pl/uploads/realizacja-toto-glogoczow.webp',
    'bts-development-park-zielona-gora': '/static/img/mbt/DJI_0181-1-scaled-b366f7fb.jpeg',
    'byd-dabrowscy-bytom': '/static/img/mbt/DSC03980-scaled-ea8b4933.jpeg',
    'ecowipes-nowy-dwor-mazowiecki': '/static/img/mbt/DSC03738-scaled-c238f3f3.jpeg',
    'ponar-wadowice': '/static/img/mbt/DSC03730-scaled-ee7d1094.jpeg',
    'VESUVIUS': '/static/img/mbt/DSC03626-scaled-6f5bda4e.jpeg',
    'stokado-self-storage-warszawa-targowek': '/static/img/mbt/DJI_0174-scaled-5106e265.jpeg',
    'venus-brzegi': '/static/img/mbt/venusgotowe-3c7b87fa.png',
    'scallier-zabrze': '/static/img/mbt/scallier-logo-662a14b7.png',
    'fiolka-raciborz': '/static/img/mbt/IMG_20220722_102326-scaled-1-fdde92f8.jpg',
    'bater-gliwice': '/static/img/mbt/logo2-76e5c8f9.png',
    'wessper': '/static/img/mbt/1-scaled-f7ffa583.jpg',
    'warmet-hurtownia-alkocholi': '/static/img/mbt/6-scaled-8c1b1f01.jpg',
    'raben': '/static/img/mbt/7-scaled-3dfac3ae.jpg',
    'less-mess-gdansk': '/static/img/mbt/LessMess-5-9e410f12.jpg',
}

PROJECT_GALLERY_FALLBACKS = {
    'att-kokotow': ['/static/img/mbt/ZREALIZOWANE-ATT-3-scaled-b0f20287.jpg', '/static/img/mbt/ZREALIZOWANE-ATT-4-scaled-ffc91418.jpg', '/static/img/mbt/ZREALIZOWANE-ATT-5-scaled-b27ef1aa.jpg', '/static/img/mbt/ZREALIZOWANE-ATT-6-scaled-e17253f9.jpg', '/static/img/mbt/ZREALIZOWANE-ATT-8-c1d848dd.jpg'],
    'less-mess-storage-warszawa': ['/static/img/mbt/LessMess-2-scaled-97b96a57.jpg', '/static/img/mbt/LessMess-3-scaled-8cef25bd.jpg', '/static/img/mbt/LessMess-4-18feb603.jpg', '/static/img/mbt/LessMess-5-9e410f12.jpg', '/static/img/mbt/LessMess-6-916e0c22.jpg'],
    'eurosleeve-zabrze': ['/static/img/mbt/Eurosleeve-2-scaled-c2ae0cee.jpg', '/static/img/mbt/Eurosleeve-3-scaled-d1365013.jpg', '/static/img/mbt/Eurosleeve-5-scaled-bc3730ed.jpg', '/static/img/mbt/Eurosleeve-6-scaled-73fe0a94.jpg', '/static/img/mbt/Eurosleeve-7-scaled-2e508c07.jpg', '/static/img/mbt/Eurosleeve-8-scaled-f259de88.jpg', '/static/img/mbt/Eurosleeve-9-scaled-9070a8d2.jpg', '/static/img/mbt/Eurosleeve-10-scaled-fd8f7247.jpg', '/static/img/mbt/Eurosleeve-11-scaled-cebef959.jpg'],
    'fronton-krakow': ['/static/img/mbt/Fronton-2-scaled-de057284.jpg', '/static/img/mbt/Fronton-3-scaled-1437922a.jpg', '/static/img/mbt/Fronton-4-scaled-d63c339b.jpg', '/static/img/mbt/Fronton-5-scaled-321d647a.jpg'],
    'huber-suhner-pisary': ['/static/img/mbt/Huber-2-scaled-0183eebd.jpg', '/static/img/mbt/Huber-3-scaled-9bd9b813.jpg', '/static/img/mbt/Huber-4-scaled-9c017841.jpg', '/static/img/mbt/Huber-5-scaled-45d0b018.jpg', '/static/img/mbt/Huber-6-scaled-b00b8b23.jpg'],
    'canpack-bss-lab-brzesk': ['/static/img/mbt/CANPACK-BSS-LAB-w-Brzesku-1-1-ee4bd957.jpg', '/static/img/mbt/CANPACK-BSS-LAB-w-Brzesku-2-1-13c84a96.jpg'],
    'herz-wieliczka': ['/static/img/mbt/Herz-docel-3-scaled-1-89b6538a.jpg'],
}

def _sanitize_project_photos(proj):
    if not proj:
        return proj
    slug = proj.get('slug', '')
    hero = proj.get('hero') or ''
    if not hero or 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev' in hero:
        proj['hero'] = PROJECT_HERO_FALLBACKS.get(slug, '/static/img/mbt/hala-1024x672-eb7144c9.jpg')

    logo = proj.get('logo') or ''
    if not logo or 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev' in logo:
        proj['logo'] = '/static/img/mbt/icon.svg'

    gallery = proj.get('gallery') or []
    clean_gallery = [g for g in gallery if 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev' not in g]
    if not clean_gallery and slug in PROJECT_GALLERY_FALLBACKS:
        clean_gallery = PROJECT_GALLERY_FALLBACKS[slug]
    proj['gallery'] = clean_gallery
    return proj

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
            projects.append(_sanitize_project_photos(_apply_folder_photos(proj)))
        if projects: return projects
    except Exception:
        pass
    return [_sanitize_project_photos(_apply_folder_photos(_project_translate(dict(p), lang))) for p in mbt_data.PROJECTS]


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
            return _sanitize_project_photos(_apply_folder_photos(proj))
        except Project.DoesNotExist:
            return None
    except Exception:
        pass
    for p in mbt_data.PROJECTS:
        if p['slug'] == slug:
            return _sanitize_project_photos(_apply_folder_photos(_project_translate(dict(p), lang)))
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
    reps_by_name = {}
    for s in getattr(mbt_data, 'SALES_REPS', []):
        trans_s = _project_translate(dict(s), lang)
        reps_by_name[trans_s['name']] = trans_s

    try:
        for s in SalesRepresentative.objects.all().order_by('order', 'name'):
            reps_by_name[s.name] = {
                'name': s.name,
                'position': _t(s.t_position, lang, s.position),
                'email': s.email,
                'phone': s.phone,
                'photo': s.photo,
                'order': s.order
            }
    except Exception:
        pass

    res = list(reps_by_name.values())
    res.sort(key=lambda x: (x.get('order', 999), x.get('name', '')))
    return res


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
                'office_zabrze_photo': '/static/img/mbt/o-nas-1.jpg' if (not c.office_zabrze_photo or 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev' in str(c.office_zabrze_photo)) else c.office_zabrze_photo,
                'office_katowice_photo': '/static/img/mbt/o-nas-zespol.jpg' if (not c.office_katowice_photo or 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev' in str(c.office_katowice_photo)) else c.office_katowice_photo,
                'office_krakow_photo': '/static/img/mbt/o-nas-2.jpg' if (not c.office_krakow_photo or 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev' in str(c.office_krakow_photo)) else c.office_krakow_photo,
                'office_site_label': c.office_site_label,
                'office_site_adres': c.office_site_adres,
                'office_site_photo': '/static/img/mbt/DSC03738-scaled-c238f3f3.jpeg' if (not c.office_site_photo or 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev' in str(c.office_site_photo)) else c.office_site_photo,
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
                'social_instagram': c.social_instagram,
                'hero_video': c.hero_video,
            }
    except Exception:
        pass
    # Fallback z mbt_data.py z tłumaczeniem gettext dla etykiet
    s = dict(mbt_data.SITE)
    if 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev' in str(s.get('office_zabrze_photo', '')):
        s['office_zabrze_photo'] = '/static/img/mbt/o-nas-1.jpg'
    if 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev' in str(s.get('office_katowice_photo', '')):
        s['office_katowice_photo'] = '/static/img/mbt/o-nas-zespol.jpg'
    if 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev' in str(s.get('office_krakow_photo', '')):
        s['office_krakow_photo'] = '/static/img/mbt/o-nas-2.jpg'
    if 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev' in str(s.get('office_site_photo', '')):
        s['office_site_photo'] = '/static/img/mbt/DSC03738-scaled-c238f3f3.jpeg'
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
        
        s['hero_subtitle'] = _gettext('Z pasją budujemy Wasze biznesy')
        s['hero_title1'] = _gettext('Twój Generalny')
        s['hero_title2'] = _gettext('Wykonawca')
        s['hero_text'] = _gettext('Jeden team – pełna realizacja. <strong>Od projektu aż po dach!</strong> Budujemy hale magazynowe, produkcyjne i usługowe pod klucz.')
    return s


# ---------------------------------------------------------------------------
# Fotografie strony (SitePhotos) — podmienialne z admina (upload na R2)
# ---------------------------------------------------------------------------

FALLBACK_PHOTOS = {
    'hale_przemyslowe_hero': 'https://media.mbt.pl/uploads/41003d4cca6e.webp',
    'hale_przemyslowe_1': 'https://media.mbt.pl/uploads/a8d6d2908191.webp',
    'hale_przemyslowe_2': '/static/img/mbt/breem-e659b8f2.jpg',
    'hale_magazynowe_hero': 'https://media.mbt.pl/uploads/1648f91ebdc2.webp',
    'hale_magazynowe_1': '/static/img/mbt/LessMess-4-18feb603.jpg',
    'obiekty_komercyjne_hero': 'https://media.mbt.pl/uploads/04bfb07ae41b.webp',
    'obiekty_komercyjne_1': '/static/img/mbt/CANPACK-BSS-LAB-w-Brzesku-1-1-ee4bd957.jpg',
    'obiekty_komercyjne_2': '/static/img/mbt/3-2-scaled-38947c85.jpg',
    'gw_hero': 'https://media.mbt.pl/uploads/41003d4cca6e.webp',
    'gw_1': '/static/img/mbt/ZREALIZOWANE-ATT-1-scaled-f12dacac.jpg',
    'gw_2': '/static/img/mbt/ZREALIZOWANE-ATT-3-scaled-b0f20287.jpg',
    'gw_3': 'https://media.mbt.pl/uploads/a8d6d2908191.webp',
    'gw_4': '/static/img/mbt/ZREALIZOWANE-ATT-5-scaled-b27ef1aa.jpg',
    'gw_5': '/static/img/mbt/ZREALIZOWANE-ATT-6-scaled-e17253f9.jpg',
    'gw_6': '/static/img/mbt/Fronton-1-scaled-42981731.jpg',
    'gw_7': '/static/img/mbt/Fronton-2-scaled-de057284.jpg',
    'gw_8': '/static/img/mbt/Huber-6-scaled-b00b8b23.jpg',
    'gw_9': '/static/img/mbt/3-2-scaled-38947c85.jpg',
    'gw_10': '/static/img/mbt/breem-e659b8f2.jpg',
    'gw_11': '/static/img/mbt/hala-1024x672-eb7144c9.jpg',
    'gw_12': '/static/img/mbt/realizacja-stokado.jpg',
    'home_hero_bg': '/static/img/hero/hero_bg_3_1.png',
    'home_att8': 'https://media.mbt.pl/uploads/a8d6d2908191.webp',
    'home_bg_cta': '/static/img/bg/cta-bg3-1.png',
    'home_bg_contact': '/static/img/bg/contact-bg3-1.png',
    'home_bg_why': '/static/img/bg/why-bg3-1.png',
    'home_client_group': '',
    'home_testi_2': '/static/img/testimonial/testi_2_2.png',
    'home_o_nas_2': '/static/img/mbt/o-nas-2.jpg',
    'home_o_nas_zespol': 'https://media.mbt.pl/uploads/c4f9f468d740.webp',
    'home_realizacja': '/static/img/mbt/realizacja-eurosleeve.jpg',
    'bg_header': '/static/img/bg/header-1-bg.png',
    'bg_footer': '/static/img/bg/footer-bg1-1.png',
    'bg_breadcrumb': '/static/img/bg/breadcrumb-bg.png',
    'about_1': '/static/img/mbt/o-nas-1.jpg',
    'service_1': '/static/img/mbt/Eurosleeve-10-scaled-fd8f7247.jpg',
    'service_2': '/static/img/mbt/IMG_20220722_102326-scaled-1-fdde92f8.jpg',
    'general_contracting_1': '/static/img/mbt/LessMess-1-3370ce84.jpg',
    'general_contracting_2': '/static/img/mbt/realizacja-stokado.jpg',
    'work_gallery': [
        '/static/img/mbt/DSC03626-scaled-6f5bda4e.jpeg',
        '/static/img/mbt/DSC03726-scaled-04284a3e.jpeg',
        '/static/img/mbt/DSC03730-scaled-ee7d1094.jpeg',
        '/static/img/mbt/DSC03738-scaled-c238f3f3.jpeg',
        '/static/img/mbt/DSC03980-scaled-ea8b4933.jpeg',
        '/static/img/mbt/DJI_0174-scaled-5106e265.jpeg',
        '/static/img/mbt/DJI_0181-1-scaled-b366f7fb.jpeg',
        '/static/img/mbt/DJI_3-03272d0f.jpg',
    ],
}

@_cached('photos')
def get_photos():
    """Zwróć dict fotografie strony: klucz -> URL.

    Wartości z mbt_data.PHOTOS stanowią oficjalną bazę produkcyjnych zdjęć.
    Wartości z bazy danych mają priorytet, jeśli nie są zablokowanym r2.dev.
    Wszystkie zablokowane adresy r2.dev są automatycznie zastępowane przez FALLBACK_PHOTOS.
    """
    out = dict(getattr(mbt_data, 'PHOTOS', {}))
    try:
        c = SitePhotos.objects.first()
        if c is not None:
            for field in SitePhotos._meta.fields:
                if field.name == 'id':
                    continue
                val = getattr(c, field.name, None)
                if not val:
                    continue
                # Jeśli w bazie jest zablokowane r2.dev, ignoruj
                if isinstance(val, str) and 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev' in val:
                    continue
                if isinstance(val, list):
                    val = [x for x in val if 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev' not in str(x)]
                    if not val:
                        continue
                out[field.name] = val
    except Exception:
        pass

    # Bezpieczeństwo: żaden klucz nie może wskazywać na zablokowane r2.dev ani być pusty
    for k, v in FALLBACK_PHOTOS.items():
        cur = out.get(k)
        if not cur or 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev' in str(cur):
            out[k] = v
        elif isinstance(cur, list):
            clean_list = [x for x in cur if 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev' not in str(x)]
            out[k] = clean_list if clean_list else v

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


SECTOR_FALLBACK_IMAGES = {
    'biurowce': '/static/img/mbt/Fronton-2-scaled-de057284.jpg',
    'obiekty-self-storage': '/static/img/mbt/realizacja-stokado.jpg',
    'mieszkaniowka': '/static/img/mbt/Fronton-1-scaled-42981731.jpg',
    'galerie-handlowe': '/static/img/mbt/Fronton-2-scaled-de057284.jpg',
}

def _sanitize_sector_image(slug, img):
    if not img or 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev' in str(img):
        return SECTOR_FALLBACK_IMAGES.get(slug, '/static/img/mbt/hala-1024x672-eb7144c9.jpg')
    return img


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
                        'image': _sanitize_sector_image(s.slug, s.image),
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
                "image": _sanitize_sector_image(s.get("slug"), s.get("image")),
                "order": s.get("order"),
            })
    return res
