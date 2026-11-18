"""Podstrona „Potencjał i referencje” — budowa kontekstu z portfolio_mbt.json.

JSON (MBTApp/portfolio_mbt.json) jest jedynym źródłem treści. Ten moduł:
  * czyści dane (null i znaczniki [DO UZUPEŁNIENIA]/[DO TŁUMACZENIA] nie trafiają do HTML),
  * wylicza liczniki i rozkłady z samych realizacji,
  * mapuje realizacje na istniejące rekordy /realizacje/ (link + miniatura z R2),
  * bierze dane opiekunów handlowych z sales_locator / mbt_orm (nadrzędne wobec JSON-a),
  * tłumaczy teksty przez auto_translate (cache; brak wpisu = wersja PL).
"""
import logging

logger = logging.getLogger(__name__)
import json
import os
import re
from collections import Counter, OrderedDict
from functools import lru_cache

from django.urls import reverse

from MBTApp import mbt_orm
from MBTApp.auto_translate import translate
from MBTApp.portfolio_records import REMOVED_SLUGS as _REMOVED

JSON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'portfolio_mbt.json')

_MARKER_RE = re.compile(r'\[DO (UZUPE[ŁL]NIENIA|T[ŁL]UMACZENIA)[^\]]*\]', re.I)

# nr realizacji (JSON) -> slug istniejącej realizacji w /realizacje/.
# Tylko pewne dopasowania; reszta nie ma jeszcze rekordu (brak linku i miniatury).
# Tyskie Browary (nr 40), Brembo (nr 37) i Fronton (nr 32) to karty scalone z kilku wpisów JSON.

# Nowe rekordy w /realizacje/ (tylko logo klienta, inwestycja zrealizowana): nr -> plik logo w static.
# Artus (nr 17) i Centrum Sportów Rakietowych UE (nr 50) istnieją już na produkcji (te same slugi) —
# komenda ich nie dubluje, a nakładka w mbt_orm pokazuje je też tam, gdzie rekordu jeszcze nie ma.
LOGOS = '/static/img/mbt/logos/'
NEW_RECORDS = {
    9: LOGOS + 'eurostyl-chelmek.svg',
    14: 'https://media.mbt.pl/media/uploads/7ad52ff95b94.webp',  # logo jak w realizacji Stokado Warszawa Targówek
    17: 'https://media.mbt.pl/uploads/1491284b28df.webp',  # Artus Aircraft (jak na produkcji)
    31: LOGOS + 'kbh-akord.png',
    37: LOGOS + 'brembo.png',
    50: 'https://media.mbt.pl/uploads/4fe7e40eb483.webp',  # Centrum Sportów Rakietowych UE Wrocław (jak na produkcji)
    51: LOGOS + 'zielona-dolina.png',
}
# Rekordy usunięte z serwisu całkowicie (baza + mbt_data.py) — lista w portfolio_records.py.
REMOVED_SLUGS = _REMOVED
# Wcześniej doklejone bloki opisu, które trzeba zdjąć przed doklejeniem nowej wersji (nr -> teksty).
LEGACY_BLOCKS = {
    32: ['Hala produkcyjno-magazynowa z częścią biurową\nPowierzchnia hali: 1 469 m² (kubatura: 10 244 m³), część biurowa: 271 m², instalacje wewnętrzne, sieci zewnętrzne, drogi wewnętrzne i place manewrowe.'],
}
EXISTING_SLUGS = {
    1: 'raben',
    2: 'in-post-w-legnicy',
    3: ('vesuvius-skawina', 'VESUVIUS'),
    4: 'bts-development-park-zielona-gora',
    5: ('warmet-hurtownia-alkoholi', 'warmet-hurtownia-alkocholi'),
    6: 'euro-trade-w-modlnicy',
    9: 'eurostyl-chelmek',
    10: ('epco-bytom', 'p1704'),
    11: 'stokado-self-storage-krakow',
    12: 'stokado-self-storage-warszawa-targowek',
    13: 'stokado-self-storage-warszawa-bemowo',
    14: 'stokado-gdansk',
    15: 'less-mess-storage-warszawa',
    16: 'less-mess-gdansk',
    17: ('artus-aircraft', 'artus-aircraft-gliwice'),
    18: 'huber-suhner-pisary',
    20: 'ponar-wadowice',
    21: 'fiolka-raciborz',
    22: 'herz-wieliczka',
    23: 'euronova-kokotow-gm-wieliczka',
    24: 'wessper',
    25: 'ecowipes-nowy-dwor-mazowiecki',
    26: 'bater-gliwice',
    27: 'att-kokotow',
    28: 'sutco-katowice',
    29: 'eurosleeve-zabrze',
    30: 'pumar',
    31: 'kbh-akord-siemianowice-slaskie',
    32: 'fronton-krakow',
    33: 'fabryka-park-katowice',
    34: 'scallier-zabrze',
    35: 'byd-dabrowscy-bytom',
    37: 'brembo-poland-dabrowa-gornicza',
    40: 'kompania-piwowarska-tychy',
    41: 'kompania-piwowarska',
    46: 'browar-zamkowy-raciborz',
    50: ('centrum-sportow-rakietowych-ue-wroclaw', 'uniwersytet-ekonomiczny-we-wroclawiu-centrum-sportow-rakietowych'),
    51: 'invest-tdj-estate-zabrze-zielona-dolina-4',
    47: 'canpack-bss-lab-brzesk',
    48: 'Canpack-BSS-Excellence-Centre-Brzesk',
}


# Kto gdzie stoi w sekcji „Struktura” (kolejność = kolejność na stronie).
TREE_TOP = ['tomasz-kalisz', 'jacek-lewandowski']
TREE_DIRECTORS = ['jakub-walczak', 'amelia-mzyk', 'krzysztof-filipowski', 'katarzyna-knabel', 'marek-latos', 'piotr-burda']
TREE_REPORTS = {'jakub-walczak': ['bartlomiej-potuczko', 'dariusz-kudelko', 'michal-swoboda']}


def _clean(value):
    """None, puste i teksty ze znacznikami -> None; reszta bez zmian."""
    if value is None:
        return None
    if isinstance(value, str):
        v = value.strip()
        if not v or _MARKER_RE.search(v) or v.upper().startswith('DO WERYFIKACJI'):
            return None
        return v
    return value


@lru_cache(maxsize=1)
def _raw():
    with open(JSON_PATH, encoding='utf-8') as f:
        return json.load(f)


def _tr(text, lang):
    """Tłumaczenie z cache; brak wpisu = oryginał PL (fallback)."""
    text = _clean(text)
    if not text or lang == 'pl':
        return text
    return translate(text, 'pl', lang)


def _initials(name):
    parts = [p for p in re.split(r'\s+', name or '') if p]
    return ''.join(p[0] for p in parts[:2]).upper()


def _voiv_label(v):
    return v[:1].upper() + v[1:] if v else v


def _bars(counter_items, labeler=lambda k: k):
    items = [(labeler(k), v) for k, v in counter_items]
    peak = max((v for _, v in items), default=0) or 1
    return [{'label': k, 'value': v, 'pct': f'{v * 100 / peak:.1f}'} for k, v in items]


def _sales_team(lang):
    """Opiekunowie handlowi: kontakty z mbt_orm (CMS), regiony z sales_locator."""
    from MBTApp import sales_locator
    reps = {r['name']: r for r in mbt_orm.get_sales_reps(lang)}
    regions = {}
    for voiv, name in sales_locator.VOIV_REP.items():
        regions.setdefault(name, []).append(_voiv_label(voiv))
    return reps, {k: sorted(v) for k, v in regions.items()}


def _light_photo(path, limit=4_000_000):
    """Lokalne zdjęcie (/static/...) cięższe niż ~4 MB nie trafia na kartę (placeholder zamiast niego)."""
    if not path or not path.startswith('/static/'):
        return path
    from django.conf import settings
    fs = os.path.join(settings.BASE_DIR, 'MBTApp', path.lstrip('/'))
    try:
        return path if os.path.getsize(fs) <= limit else ''
    except OSError:
        return path


def _worker_photos(lang):
    out = {}
    try:
        for w in mbt_orm.get_workers(lang):
            name = re.sub(r'\s+', ' ', (w.get('name') or '')).strip()
            ph = w.get('photo') or w.get('image') or ''
            if name and ph:
                out[name] = ph
    except Exception:
        logger.warning('Fallback po błędzie', exc_info=True)
    return out


def _existing_project(nr, projects_by_slug):
    slugs = EXISTING_SLUGS.get(nr)
    if not slugs:
        return None
    for slug in ((slugs,) if isinstance(slugs, str) else slugs):
        if slug in projects_by_slug:
            return projects_by_slug[slug]
    return None


def project_description(r, old_opis=''):
    """Nowy opis do /realizacje/: typ obiektu + parametry z JSON (reguły publiczności jak na stronie)."""
    params = _clean(r.get('parametry_publiczne'))
    if not params and not r.get('do_weryfikacji'):
        params = _clean(r.get('parametry'))
    parts = [p for p in (_clean(r.get('typ')), params) if p]
    old_opis = (old_opis or '').strip()
    for block in LEGACY_BLOCKS.get(r.get('nr'), []):
        if old_opis.startswith(block):
            old_opis = old_opis[len(block):].strip()
    if not parts or (params and params in old_opis):
        return old_opis
    return '\n'.join(parts + ([old_opis] if old_opis else []))


def _thumb(project):
    """Zdjęcie z /realizacje/ (to samo co lista realizacji: hero, a gdy brak — pierwsze z galerii)."""
    project = project or {}
    src = project.get('hero') or ((project.get('gallery') or [''])[0])
    return _light_photo(src)


def build_context(lang='pl'):
    d = _raw()
    t = lambda x: _tr(x, lang)
    firma = d['firma']

    # ---------- Realizacje (liczniki wyliczane z danych) ----------
    sectors = d['sektory']
    sector_by_slug = {s['slug']: s for s in sectors}
    sector_order = [s['slug'] for s in sectors]

    projects_by_slug = {}
    try:
        projects_by_slug = {p['slug']: p for p in mbt_orm.get_projects(lang)}
    except Exception:
        logger.warning('Fallback po błędzie', exc_info=True)

    projects = []
    for r in d['realizacje']:
        nr = r['nr']
        ex = _existing_project(nr, projects_by_slug)
        # parametry_publiczne ma pierwszeństwo przed parametry; do_weryfikacji nigdy nie jest publiczne,
        # a gdy istnieje, surowe `parametry` (sprzeczne metraże) też nie wychodzą na stronę.
        params = _clean(r.get('parametry_publiczne'))
        if not params and not r.get('do_weryfikacji'):
            params = _clean(r.get('parametry'))
        url = reverse('realizacjaDetail', args=[ex['slug']]) if ex else ''
        projects.append({
            'nr': nr,
            'sector': r['sektor'],
            'name': r['nazwa'],
            'type': t(r.get('typ')),
            'meta': ' · '.join(x for x in [t(r.get('lokalizacja')), t(r.get('formula'))] if x),
            'kpi': [t(k) for k in (r.get('kpi') or []) if _clean(k)],
            'in_progress': r.get('status') == 'w_realizacji',
            'params': t(params),
            'voivodeship': r.get('wojewodztwo'),
            'url': url,
            'thumb': _thumb(ex),
            'contain': bool(ex) and (ex.get('type') == 'realizacja-w-trakcie' or '/logos/' in (ex.get('hero') or '')),
        })

    by_sector = OrderedDict()
    for slug in sector_order:
        s = sector_by_slug[slug]
        by_sector[slug] = {
            'slug': slug,
            'code': s['kod'],
            'name': t(s['nazwa_krotka']),
            'full_name': t(s['nazwa']),
            'projects': [p for p in projects if p['sector'] == slug],
        }
    for g in by_sector.values():
        g['count'] = len(g['projects'])

    total = len(projects)
    voiv_counter = Counter(p['voivodeship'] for p in projects if p['voivodeship'])
    sector_counter = [(g['name'], g['count']) for g in by_sector.values()]
    in_progress = sum(1 for p in projects if p['in_progress'])

    stats = [
        {'key': 'projects', 'value': total},
        {'key': 'sectors', 'value': len([g for g in by_sector.values() if g['count']])},
    ]

    # ---------- Kompetencje ----------
    competencies = [{'name': t(c['nazwa']), 'proof': t(c.get('potwierdzenie'))} for c in d['kompetencje']]

    # ---------- Firma ----------
    cap = firma['kapital']
    capital = {
        'basic': cap['podstawowy']['wyswietl'], 'basic_paid': cap['podstawowy'].get('w_pelni_oplacony'),
        'reserve': cap['zapasowy']['wyswietl'], 'reserve_paid': cap['zapasowy'].get('w_pelni_oplacony'),
        'total': cap['lacznie_wyswietl'],
    }
    reg = firma.get('rejestr') or {}
    register_rows = [(k, v) for k, v in [
        ('KRS', _clean(reg.get('krs'))), ('NIP', _clean(reg.get('nip'))), ('REGON', _clean(reg.get('regon')))] if v]
    fin = firma.get('finanse') or {}
    revenue = {y: v for y, v in (fin.get('przychody_netto') or {}).items() if _clean(v)}
    finance = {
        'revenue': revenue,
        'oc': _clean(fin.get('oc_suma_gwarancyjna')),
        'guarantees': _clean(fin.get('limity_gwarancji_kontraktowych')),
    }
    finance_visible = bool(revenue or finance['oc'] or finance['guarantees'])

    # ---------- Struktura ----------
    st = d['struktura']
    def dept(x):
        return {'name': t(x['nazwa']), 'head': _clean(x.get('kierownik')), 'scope': t(x.get('zakres'))}
    depts_left = [dept(x) for x in st['dzialy'] if x.get('kolumna_desktop') == 'lewa']
    depts_right = [dept(x) for x in st['dzialy'] if x.get('kolumna_desktop') != 'lewa']

    # ---------- Kadra ----------
    reps, regions = _sales_team(lang)
    photos = _worker_photos(lang)
    cards = {}
    for k in d['kadra']:
        name = k['imie_nazwisko']
        rep = reps.get(name) or {}
        cards[k['slug']] = {
            'slug': k['slug'],
            'name': name,
            'initials': _initials(name),
            'role': t(k['stanowisko']),
            'desc': t(k.get('opis')),
            'photo': _light_photo(_clean(k.get('foto')) or photos.get(name) or _clean(rep.get('photo')) or ''),
            'linkedin': _clean(k.get('linkedin')),
        }
    pick = lambda slugs: [dict(cards[s]) for s in slugs if s in cards]
    directors = pick(TREE_DIRECTORS)
    for m in directors:
        m['reports'] = pick(TREE_REPORTS.get(m['slug'], []))
    people = {'board': pick(TREE_TOP), 'directors': directors}

    # ---------- Kadra techniczna ----------
    tech_rows = [{
        'role': t(r['stanowisko']),
        'qual': t(r.get('kwalifikacje')),
        'count': _clean(r.get('liczba_osob')),
    } for r in d['kadra_techniczna']]
    tech_has_count = any(r['count'] is not None for r in tech_rows)
    tech_has_qual = any(r['qual'] for r in tech_rows)

    bhp = d['bhp_jakosc']
    tech = d['technologie']

    return {
        'p': {
            'texts': {k: re.sub(r'\b54\b', str(total), t(v)) if isinstance(t(v), str) else t(v)
                      for k, v in d['teksty'].items()},
            'company_name': firma['nazwa'],
            'legal_form': t(firma.get('forma_prawna')),
            'since': firma['na_rynku_od'],
            'president': firma.get('prezes_zarzadu'),
            'slogan': t(firma.get('haslo')),
            'register_rows': register_rows,
            'capital': capital,
            'finance': finance, 'finance_visible': finance_visible,
            'specializations': [t(s) for s in firma['specjalizacje']],
            'awards': [t(s) for s in firma['wyroznienia']],
            'memberships': [t(s) for s in firma['czlonkostwa']],
            'offices': firma['biura'],
            'contact': firma['kontakt'],
            'stats': stats,
            'total': total,
            'in_progress': in_progress,
            'sectors': [g for g in by_sector.values() if g['count']],
            'sector_bars': _bars(sector_counter),
            'voiv_bars': _bars(sorted(voiv_counter.items(), key=lambda kv: (-kv[1], kv[0])), _voiv_label),
            'competencies': competencies,
            'org_head': t(st['zarzad']['nazwa']),
            'org_head_people': st['zarzad']['sklad'],
            'org_note': t(st.get('podleglosc')),
            'depts_left': depts_left, 'depts_right': depts_right, 'dept_count': len(st['dzialy']),
            'site_crew': t(st.get('kadra_budow')),
            'board': people['board'], 'directors': people['directors'],
            'tech_rows': tech_rows, 'tech_has_count': tech_has_count, 'tech_has_qual': tech_has_qual,
            'formulas': [{'name': t(f['nazwa']), 'desc': t(f['opis'])} for f in d['formuly']],
            'process': [t(s) for s in d['proces']],
            'bhp': t(bhp.get('bhp')), 'warranty': t(bhp.get('gwarancja')),
            'accident_rates': t(bhp.get('wskazniki_wypadkowosci')),
            'iso': [t(x) for x in (bhp.get('certyfikaty_iso') or []) if _clean(x)] if isinstance(bhp.get('certyfikaty_iso'), list) else [],
            'tools': [{'cat': t(x['kategoria']), 'name': x['nazwa'], 'desc': t(x['opis']), 'icon': x['ikona']}
                      for x in tech['narzedzia']],
            'backup': t(tech.get('zaplecze')),
            'own_equipment': t(tech.get('wykaz_sprzetu_wlasnego')),
            'exec_tech': [t(x) for x in tech['technologie_wykonawcze']],
            'methodology': [{'name': x['nazwa'], 'desc': t(x['opis'])} for x in tech['metodyka']],
        },
    }
