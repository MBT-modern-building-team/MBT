"""Widok Kiosku Dotykowego (mbt.pl/kiosk).

Zaprojektowany specjalnie dla 32-calowego monitora dotykowego 4K LG (webOS).
Udostępnia pełne portfolio MBT Modern Building Team, model 'Zaprojektuj i wybuduj',
interaktywny suwak Przed/Po, referencje oraz pełnowymiarowy Pitch Deck prezentacyjny.
"""
import json
from django.shortcuts import render
from MBTApp import mbt_orm


def _get_presentation_slides():
    """Zwraca pełną 23-slajdową oficjalną prezentację MBT z /static/img/prezentacja/."""
    slides = []
    for i in range(1, 24):
        slides.append({
            'id': i,
            'number': i,
            'image': f'/static/img/prezentacja/prezentacja-23022_{i}.jpg',
            'thumb': f'/static/img/prezentacja/thumb_{i}.jpg',
            'alt': f'Prezentacja Firmowa MBT – Slajd {i} z 23',
        })
    return slides


import re

def _project_paras(opis):
    """Podziel opis projektu na akapity (specyfikacja z XML jest jednym blokiem)."""
    opis = (opis or '').strip()
    if not opis:
        return []
    parts = re.split(r'(?=(?:Specyfikacja|Powierzchnia|Certyfikacja|Układ budynku|Infrastruktura|Konstrukcja|Elewacja|Zagospodarowanie|Inwestor|Lokalizacja))', opis)
    return [p.strip() for p in parts if p.strip()]


def kiosk_view(request):
    """Główny widok Kiosku Dotykowego MBT."""
    lang = 'pl'
    raw_projects = mbt_orm.get_projects(lang=lang)
    site = mbt_orm.get_site(lang=lang)
    references = mbt_orm.get_references(lang=lang)
    awards = mbt_orm.get_awards()
    photos = mbt_orm.get_photos()
    workers = mbt_orm.get_workers(lang=lang)
    sales_reps = mbt_orm.get_sales_reps(lang=lang)
    sectors = mbt_orm.get_sectors(lang=lang)

    # Wzbogacenie projektów identycznie jak w mbtViews.py dla /realizacje
    projects = []
    clean_projects = []
    for p in raw_projects:
        ep = dict(p)
        paras = _project_paras(p.get('opis', ''))
        ep['opis_paras'] = paras
        ep['formula_display'] = p.get('formula') or 'Generalne wykonawstwo'
        ep['czas_display'] = f"Czas realizacji: {p['czas']}" if p.get('czas') else "Realizacja pod klucz"
        projects.append(ep)

        clean_projects.append({
            'title': p.get('title', ''),
            'slug': p.get('slug', ''),
            'type': p.get('type', ''),
            'status': p.get('status', ''),
            'czas': p.get('czas', ''),
            'czas_display': ep['czas_display'],
            'formula': p.get('formula', ''),
            'formula_display': ep['formula_display'],
            'opis': p.get('opis', ''),
            'opis_paras': paras,
            'hero': p.get('hero', ''),
            'logo': p.get('logo', ''),
            'gallery': p.get('gallery', []) or [],
        })

    projects_json = json.dumps(clean_projects, ensure_ascii=False)

    # Slajdy do pełnoekranowej prezentacji MBT (23 oficjalne slajdy)
    presentation_slides = _get_presentation_slides()
    presentation_slides_json = json.dumps(presentation_slides, ensure_ascii=False)

    # Dane do suwaka Before & After (Przed i Po)
    before_after = {
        'title': 'Hala Produkcyjno-Magazynowa Eurosleeve',
        'subtitle': 'Przesuń palcem suwak, aby zobaczyć transformację z placu budowy do gotowego obiektu',
        'location': 'Wojkowice / Śląsk',
        'area': '8 500 m²',
        'formula': 'Zaprojektuj i wybuduj (Design & Build)',
        'before_image': '/static/img/mbt/DSC03738-scaled-c238f3f3.jpeg',
        'after_image': '/static/img/mbt/realizacja-eurosleeve.jpg',
        'before_label': 'Plac Budowy (Konstrukcja stalowa)',
        'after_label': 'Gotowy Obiekt (Oddany do użytku)',
    }

    # Zaufane marki (logotypy)
    trusted_brands = [
        {'name': 'Kompania Piwowarska', 'logo': '/static/img/mbt/trusted-us-kompania-piwowarska.svg'},
        {'name': 'Canpack', 'logo': '/static/img/mbt/trusted-us-canpack.svg'},
        {'name': 'Browar Zamkowy Racibórz', 'logo': '/static/img/mbt/trusted-us-browar-zamkowy.svg'},
        {'name': 'DL Invest Group', 'logo': '/static/img/mbt/trusted-us-dl-invest-group.svg'},
        {'name': 'Huber+Suhner', 'logo': '/static/img/mbt/trusted-us-huber-suhner.svg'},
        {'name': 'Less Mess Storage', 'logo': '/static/img/mbt/trusted-us-less-mess-storage.svg'},
        {'name': 'Euro-Trade', 'logo': '/static/img/mbt/trusted-us-euro-trade.svg'},
        {'name': 'Sutco Polska', 'logo': '/static/img/mbt/trusted-us-sutco-polska.svg'},
        {'name': 'Euronova', 'logo': '/static/img/mbt/trusted-us-euronova.svg'},
        {'name': 'Herz', 'logo': '/static/img/mbt/trusted-us-herz.svg'},
        {'name': 'Bater', 'logo': '/static/img/mbt/trusted-us-bater.svg'},
        {'name': 'Toto Hair Company', 'logo': '/static/img/mbt/trusted-us-toto.svg'},
        {'name': 'Epco', 'logo': '/static/img/mbt/trusted-us-epco.svg'},
        {'name': 'Pumar', 'logo': '/static/img/mbt/trusted-us-pumar.svg'},
        {'name': 'Stainless Steel', 'logo': '/static/img/mbt/trusted-us-stainless-steel-engineering.svg'},
        {'name': 'CDR', 'logo': '/static/img/mbt/trusted-us-cdr.svg'},
    ]

    context = {
        'site': site,
        'projects': projects,
        'projects_json': projects_json,
        'references': references,
        'awards': awards,
        'photos': photos,
        'workers': workers,
        'sales_reps': sales_reps,
        'sectors': sectors,
        'trusted_brands': trusted_brands,
        'presentation_slides': presentation_slides,
        'presentation_slides_json': presentation_slides_json,
        'before_after': before_after,
    }

    return render(request, 'pages/kiosk.html', context)
