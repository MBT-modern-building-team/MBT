"""Generuje MBTApp/mbt_data.py z aktualnej bazy danych (bez sekretów!).

Dlaczego: Vercel (serverless) nie ma lokalnej bazy SQLite (db.sqlite3 jest
w .gitignore), więc strona na produkcji korzysta z fallbacku mbt_data.py.
Po każdej zmianie w CMS (admin) trzeba zregenerować ten plik i pushnąć,
żeby Vercel pokazywał te same dane co localhost.

Uruchamianie:
    env -u PYTHONPATH .venv/bin/python scripts/gen_mbt_data.py

Uwaga: plik NIE zawiera żadnych sekretów — tylko dane publiczne strony.
Skrypt jest podpięty do sygnału post_save (MBTApp/signals.py), więc
generuje się automatycznie po zapisie w adminie.
"""
import json
import os
import sys

import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MBT.settings')
django.setup()

from django.utils.translation import gettext_lazy as _  # noqa: E402
from MBTApp.models import (  # noqa: E402
    Article, Job, Project, Reference, SiteConfig, SitePhotos, Worker, SalesRepresentative, Award
)

OUT = os.path.join(BASE_DIR, 'MBTApp', 'mbt_data.py')


def _dump(obj) -> str:
    """JSON z polskimi znakami, bez spacji — kompaktowo ale czytelnie."""
    return json.dumps(obj, ensure_ascii=False, indent=4)


def _section(name: str, items) -> str:
    body = ',\n'.join('    ' + _dump(it) for it in items)
    return f'{name} = [\n{body}\n]\n'


def main():
    # --- SITE: dane firmy z SiteConfig (fallback: istniejący mbt_data.SITE) ---
    site = None
    try:
        c = SiteConfig.objects.first()
        if c is not None:
            site = {
                'phone': c.phone,
                'phone_href': c.phone_href,
                'email': c.email,
                'hours': c.hours,
                'hours_long': c.hours_long,
                'office_zabrze': c.office_zabrze,
                'office_katowice': c.office_katowice,
                'office_krakow': c.office_krakow,
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
                'tagline': c.tagline,
                'about_short': c.about_short,
                'counter_years': c.counter_years,
                'counter_years_label': c.counter_years_label,
                'counter_projects': c.counter_projects,
                'counter_projects_label': c.counter_projects_label,
                'counter_ontime': c.counter_ontime,
                'counter_ontime_suffix': c.counter_ontime_suffix,
                'counter_ontime_label': c.counter_ontime_label,
                'counter_brands': c.counter_brands,
                'counter_brands_label': c.counter_brands_label,
            }
    except Exception:
        site = None
    if site is None:
        # brak rekordu — zachowaj ręcznie edytowany SITE z pliku
        try:
            from MBTApp import mbt_data as _old
            site = _old.SITE
        except Exception:
            site = {}

    # --- PROJECTS ---
    projects = []
    for p in Project.objects.all().order_by('order', 'title'):
        projects.append({
            'title': p.title,
            'type': p.type,
            'status': p.status,
            'slug': p.slug,
            'czas': p.czas,
            'formula': p.formula,
            'opis': p.opis,
            'logo': p.logo,
            'gallery': list(p.gallery or []),
            'hero': p.hero,
            'latitude': p.latitude,
            'longitude': p.longitude,
            'order': p.order,
            # tłumaczenia (z DB; puste = fallback PL)
            't_t': dict(p.t_title or {}),
            't_s': dict(p.t_status or {}),
            't_c': dict(p.t_czas or {}),
            't_f': dict(p.t_formula or {}),
            't_o': dict(p.t_opis or {}),
        })

    # --- JOBS ---
    jobs = []
    for j in Job.objects.all().order_by('order', 'title'):
        jobs.append({
            'title': j.title, 'slug': j.slug, 'text': j.text,
            't_t': dict(j.t_title or {}),
            't_x': dict(j.t_text or {}),
            'order': j.order,
        })

    # --- WORKERS ---
    workers = []
    for w in Worker.objects.all().order_by('order', 'name'):
        workers.append({
            'name': w.name,
            'position': w.position,
            'opis': w.opis,
            'photo': w.photo,
            'linkedin': w.linkedin,
            't_p': dict(w.t_position or {}),
            't_o': dict(w.t_opis or {}),
            'order': w.order,
        })

    # --- SALES REPS ---
    sales_reps = []
    for s in SalesRepresentative.objects.all().order_by('order', 'name'):
        sales_reps.append({
            'name': s.name,
            'position': s.position,
            'email': s.email,
            'phone': s.phone,
            'photo': s.photo,
            't_p': dict(s.t_position or {}),
            'order': s.order,
        })

    # --- REFERENCES ---
    refs = []
    for r in Reference.objects.all().order_by('order', 'firma'):
        refs.append({
            'firma': r.firma,
            'osoba': r.osoba,
            'stanowisko': r.stanowisko,
            'tresc': r.tresc,
            't_o': dict(r.t_osoba or {}),
            't_s': dict(r.t_stanowisko or {}),
            't_r': dict(r.t_tresc or {}),
            'order': r.order,
        })

    # --- ARTICLES ---
    arts = []
    for a in Article.objects.filter(published=True).order_by('-created'):
        arts.append({
            'title': a.title,
            'slug': a.slug,
            'excerpt': a.excerpt,
            'text': a.text,
            'image': a.image,
            't_t': dict(a.t_title or {}),
            't_e': dict(a.t_excerpt or {}),
            't_x': dict(a.t_text or {}),
        })


    # --- AWARDS ---
    awards = []
    for a in Award.objects.filter(is_active=True).order_by('order', 'name'):
        awards.append({
            'name': a.name,
            'image': a.image,
            'order': a.order,
        })

    # --- PHOTOS: zdjęcia z SitePhotos (fallback: domyślne z modelu) ---
    photos = {}
    for field in SitePhotos._meta.fields:
        if field.name == 'id':
            continue
        photos[field.name] = field.default if field.has_default() else ''

    try:
        sp = SitePhotos.objects.first()
        if sp is not None:
            for field in SitePhotos._meta.fields:
                if field.name == 'id':
                    continue
                val = getattr(sp, field.name, '')
                if val:
                    photos[field.name] = val
    except Exception as e:
        print(f'Błąd odczytu SitePhotos: {e}')

    header = '''"""
Autogenerowany plik danych (NIE edytuj ręcznie sekcji danych!).

Generowany przez: scripts/gen_mbt_data.py (po zapisie w CMS — sygnał post_save).
Vercel nie ma bazy SQLite, więc strona na produkcji korzysta z tego fallbacku.

Aby zaktualizować dane na produkcji:
    1. zapisz zmiany w /admin (lokalnie),
    2. mbt_data.py zregeneruje się automatycznie,
    3. git add MBTApp/mbt_data.py && git commit && git push origin main
"""
'''
    body = (
        header
        + '\n# ============================================================\n'
        + '# SITE — dane firmy\n'
        + '# ============================================================\n'
        + f'SITE = {_dump(site)}\n\n'
        + _section('PROJECTS', projects) + '\n'
        + _section('JOBS', jobs) + '\n'
        + _section('WORKERS', workers) + '\n'
        + _section('SALES_REPS', sales_reps) + '\n'
        + _section('REFERENCES', refs) + '\n'
        + _section('ARTICLES', arts) + '\n'
        + _section('AWARDS', awards) + '\n'
        + f'PHOTOS = {_dump(photos)}\n'
    )
    # WAŻNE: gettext_lazy musi być zaimportowane żeby mbt_data.py mógł być
    # zaimportowany w site_context (i18n processor). Dodajemy go na początku.
    import re as _re
    body = _re.sub(
        r'^("""\nAutogenerowany.*?\n""")',
        r'\1\nfrom django.utils.translation import gettext_lazy as _\n',
        body, count=1, flags=_re.S
    )

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(body)

    print(f'OK: {OUT}')
    print(f'  SITE       : {len(site)} pól')
    print(f'  PROJECTS   : {len(projects)}')
    print(f'  JOBS       : {len(jobs)}')
    print(f'  WORKERS    : {len(workers)}')
    print(f'  SALES_REPS : {len(sales_reps)}')
    print(f'  REFERENCES : {len(refs)}')
    print(f'  ARTICLES   : {len(arts)}')
    print(f'  AWARDS     : {len(awards)}')


if __name__ == '__main__':
    main()
