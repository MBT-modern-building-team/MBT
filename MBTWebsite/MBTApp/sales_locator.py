"""Wyszukiwanie opiekuna handlowego MBT na podstawie miejscowości lub powiatu.

Obsługuje:
1. Natychmiastowe dopasowanie z wbudowanego słownika miast i powiatów Polski (~450 pozycji)
2. Rozpoznawanie nazw województw i regionów (np. Mazowsze, Śląsk, Podkarpacie)
3. Geokodowanie przez OpenStreetMap Nominatim (wioski, sołectwa, gminy, np. "przewrotne powiat rzeszów")
4. Wikipedia API (wyszukiwanie encyklopedyczne artykułów o miejscowościach w Polsce)
5. Google Maps Geocoding API (opcjonalnie, gdy ustawiony jest klucz GOOGLE_MAPS_API_KEY)
"""

import json
import logging
import os
import re
import ssl
import urllib.parse
import urllib.request
from typing import Any, Dict, Optional, Tuple

from MBTApp import mbt_orm
from MBTApp import mbt_data

logger = logging.getLogger(__name__)

# Cache w pamięci podręcznej dla zapytań o lokalizację
_CACHE: Dict[str, Dict[str, Any]] = {}

# Mapowanie 16 województw na opiekunów MBT
VOIV_REP = {
    'dolnośląskie': 'Agnieszka Grzelak',
    'wielkopolskie': 'Agnieszka Grzelak',
    'lubuskie': 'Agnieszka Grzelak',

    'śląskie': 'Karol Pinoczek',
    'opolskie': 'Karol Pinoczek',
    'łódzkie': 'Karol Pinoczek',

    'mazowieckie': 'Marcin Kobryń',
    'warmińsko-mazurskie': 'Marcin Kobryń',
    'podlaskie': 'Marcin Kobryń',

    'podkarpackie': 'Jarosław Wawrzyk',
    'małopolskie': 'Jarosław Wawrzyk',
    'świętokrzyskie': 'Jarosław Wawrzyk',
    'lubelskie': 'Jarosław Wawrzyk',

    'zachodniopomorskie': 'Łukasz Liszka',
    'pomorskie': 'Łukasz Liszka',
    'kujawsko-pomorskie': 'Łukasz Liszka',
}

VOIV_NAMES = {
    'dolnośląskie': 'Dolnośląskie',
    'kujawsko-pomorskie': 'Kujawsko-Pomorskie',
    'lubelskie': 'Lubelskie',
    'lubuskie': 'Lubuskie',
    'łódzkie': 'Łódzkie',
    'małopolskie': 'Małopolskie',
    'mazowieckie': 'Mazowieckie',
    'opolskie': 'Opolskie',
    'podkarpackie': 'Podkarpackie',
    'podlaskie': 'Podlaskie',
    'pomorskie': 'Pomorskie',
    'śląskie': 'Śląskie',
    'świętokrzyskie': 'Świętokrzyskie',
    'warmińsko-mazurskie': 'Warmińsko-Mazurskie',
    'wielkopolskie': 'Wielkopolskie',
    'zachodniopomorskie': 'Zachodniopomorskie',
}

REP_COVERAGE = {
    'Łukasz Liszka': 'woj. zachodniopomorskie, pomorskie, kujawsko-pomorskie',
    'Agnieszka Grzelak': 'woj. dolnośląskie, wielkopolskie, lubuskie',
    'Karol Pinoczek': 'woj. śląskie, opolskie, łódzkie',
    'Marcin Kobryń': 'woj. mazowieckie, warmińsko-mazurskie, podlaskie',
    'Jarosław Wawrzyk': 'woj. małopolskie, podkarpackie, świętokrzyskie, lubelskie',
}

# Rdzenie i odmiany nazw województw/regionów
VOIV_STEMS: Tuple[Tuple[str, str], ...] = (
    ('zachodniopomorsk', 'zachodniopomorskie'),
    ('warmińsko-mazursk', 'warmińsko-mazurskie'),
    ('kujawsko-pomorsk', 'kujawsko-pomorskie'),
    ('dolnośląsk', 'dolnośląskie'),
    ('wielkopolsk', 'wielkopolskie'),
    ('wielkopols', 'wielkopolskie'),
    ('świętokrzysk', 'świętokrzyskie'),
    ('podkarpack', 'podkarpackie'),
    ('podkarpac', 'podkarpackie'),
    ('małopolsk', 'małopolskie'),
    ('małopols', 'małopolskie'),
    ('mazowieck', 'mazowieckie'),
    ('mazowsz', 'mazowieckie'),
    ('podlask', 'podlaskie'),
    ('podlasi', 'podlaskie'),
    ('lubelszczyzn', 'lubelskie'),
    ('lubelsk', 'lubelskie'),
    ('lubusk', 'lubuskie'),
    ('opolsk', 'opolskie'),
    ('pomorsk', 'pomorskie'),
    ('pomorz', 'pomorskie'),
    ('śląsk', 'śląskie'),
    ('slask', 'śląskie'),
    ('łódzk', 'łódzkie'),
    ('lodzk', 'łódzkie'),
    ('warmi', 'warmińsko-mazurskie'),
    ('mazur', 'warmińsko-mazurskie'),
    ('kujaw', 'kujawsko-pomorskie'),
)

# Słownik miast i powiatów Polski pogrupowany według województw (~450 miast i powiatów)
VOIV_CITIES: Dict[str, Tuple[str, ...]] = {
    'dolnośląskie': (
        'wrocław', 'wałbrzych', 'legnica', 'jelenia góra', 'lubin', 'głogów', 'świdnica',
        'bolesławiec', 'oleśnica', 'dzierżoniów', 'oława', 'zgorzelec', 'bielawa', 'kłodzko',
        'jawor', 'świebodzice', 'polkowice', 'nowa ruda', 'kamienna góra', 'boguszów-gorce',
        'strzegom', 'złotoryja', 'bogatyń', 'ząbkowice śląskie', 'jelcz-laskowice', 'chojnów',
        'trzebnica', 'brzeg dolny', 'strzelin', 'wołów', 'góra', 'milicz', 'lubań', 'lwówek śląski'
    ),
    'kujawsko-pomorskie': (
        'bydgoszcz', 'toruń', 'włocławek', 'grudziądz', 'inowrocław', 'brodnica', 'świecie',
        'chełmno', 'nakło nad notecią', 'rypin', 'solec kujawski', 'chełmża', 'lipno', 'żnin',
        'tuchola', 'wąbrzeźno', 'golub-dobrzyń', 'aleksandrów kujawski', 'mogilno', 'koronowo',
        'ciechocinek', 'kruszwica', 'radziejów', 'sępólno krajeńskie'
    ),
    'lubelskie': (
        'lublin', 'zamość', 'chełm', 'biała podlaska', 'puławy', 'świdnik', 'kraśnik', 'łuków',
        'biłgoraj', 'lubartów', 'tomaszów lubelski', 'łęczna', 'krasnystaw', 'hrubieszów',
        'dęblin', 'radzyń podlaski', 'włodawa', 'janów lubelski', 'parczew', 'ryki', 'poniatowa',
        'opole lubelskie', 'bełżyce', 'szczebrzeszyn'
    ),
    'lubuskie': (
        'zielona góra', 'gorzów wielkopolski', 'nowa sól', 'żary', 'żagań', 'świebodzin',
        'międzyrzecz', 'kostrzyn nad odrą', 'słubice', 'gubin', 'lubsko', 'wschowa', 'szprotawa',
        'krosno odrzańskie', 'drezdenko', 'sulęcin', 'strzelce krajeńskie', 'skwierzyna'
    ),
    'łódzkie': (
        'łódź', 'piotrków trybunalski', 'pabianice', 'tomaszów mazowiecki', 'bełchatów', 'zgierz',
        'skierniewice', 'radomsko', 'kutno', 'sieradz', 'zduńska wola', 'łowicz',
        'aleksandrów łódzki', 'ozorków', 'wieluń', 'opoczno', 'konstantynów łódzki', 'rawa mazowiecka',
        'łask', 'głowno', 'łęczyca', 'koluszki', 'brzeziny', 'wieruszów', 'poddębice', 'pajęczno'
    ),
    'małopolskie': (
        'kraków', 'tarnów', 'nowy sącz', 'oświęcim', 'chrzanów', 'olkusz', 'nowy targ', 'bochnia',
        'gorlice', 'zakopane', 'skawina', 'andrychów', 'wieliczka', 'trzebinia', 'wadowice',
        'kęty', 'myślenice', 'libiąż', 'brzesko', 'limanowa', 'rabka-zdrój', 'miechów',
        'dąbrowa tarnowska', 'krynica-zdrój', 'sucha beskidzka', 'proszowice', 'niepołomice',
        'stary sącz', 'muszyna', 'szczawnica'
    ),
    'mazowieckie': (
        'warszawa', 'radom', 'płock', 'siedlce', 'pruszków', 'legionowo', 'ostrołęka', 'piaseczno',
        'otwock', 'ciechanów', 'żyrardów', 'mińsk mazowiecki', 'wołomin', 'sochaczew', 'ząbki',
        'mława', 'grodzisk mazowiecki', 'marki', 'nowy dwór mazowiecki', 'wyszków', 'piastów',
        'ostrów mazowiecka', 'płońsk', 'kobyłka', 'kozienice', 'sulejówek', 'pionki', 'pułtusk',
        'gostynin', 'sierpc', 'garwolin', 'przasnysz', 'sokołów podlaski', 'grójec', 'szydłowiec',
        'węgrów', 'błonie', 'konstancin-jeziorna', 'góra kalwaria', 'łomianki', 'zielonka'
    ),
    'opolskie': (
        'opole', 'kędzierzyn-koźle', 'nysa', 'brzeg', 'kluczbork', 'prudnik', 'strzelce opolskie',
        'krapkowice', 'namysłów', 'głuchołazy', 'głubczyce', 'zdzieszowice', 'olesno', 'ozimek',
        'grodków', 'paczków'
    ),
    'podkarpackie': (
        'rzeszów', 'mielec', 'przemyśl', 'stalowa wola', 'krosno', 'dębica', 'jarosław', 'sanok',
        'jasło', 'łańcut', 'ropczyce', 'przeworsk', 'nisko', 'leżajsk', 'lubaczów', 'kolbuszowa',
        'strzyżów', 'brzozów', 'lesko', 'ustrzyki dolne', 'przewrotne', 'głogów małopolski',
        'nowa dęba', 'tarnobrzeg', 'sędziszów małopolski', 'rudnik nad sanem', 'błażowa'
    ),
    'podlaskie': (
        'białystok', 'suwałki', 'łomża', 'augustów', 'bielsk podlaski', 'zambrów', 'grajewo',
        'hajnówka', 'sokółka', 'łapy', 'siemiatycze', 'wasilków', 'kolno', 'mońki', 'czarna białostocka',
        'wysokie mazowieckie', 'dąbrowa białostocka', 'sejny'
    ),
    'pomorskie': (
        'gdańsk', 'gdynia', 'słupsk', 'tczew', 'wejherowo', 'starogard gdański', 'chojnice', 'kwidzyn',
        'malbork', 'sopot', 'lębork', 'pruszcz gdański', 'kościerszyna', 'reda', 'rumia',
        'bytów', 'ustka', 'kartuzy', 'człuchów', 'puck', 'nowy dwór gdański', 'sztum', 'hel', 'władysławowo'
    ),
    'śląskie': (
        'katowice', 'częstochowa', 'sosnowiec', 'gliwice', 'zabrze', 'bielsko-biała', 'bytom',
        'ruda śląska', 'rybnik', 'tychy', 'dąbrowa górnicza', 'chorzów', 'jaworzno', 'jastrzębie-zdrój',
        'mysłowice', 'siemianowice śląskie', 'żory', 'tarnowskie góry', 'będzin', 'piekary śląskie',
        'racibórz', 'świętochłowice', 'zawiercie', 'wodzisław śląski', 'mikołów', 'knurów', 'cieszyn',
        'czechowice-dziedzice', 'myszków', 'żywiec', 'czerwionka-leszczyny', 'pszczyna', 'lubliniec',
        'łaziska górne', 'rydułtowy', 'kłobuck', 'bieruń', 'pyskowice', 'radlin', 'radzionków', 'lędziny'
    ),
    'świętokrzyskie': (
        'kielce', 'ostrowiec świętokrzyski', 'starachowice', 'skarżysko-kamienna', 'sandomierz',
        'końskie', 'busko-zdrój', 'staszów', 'jędrzejów', 'pińczów', 'włoszczowa', 'chęciny',
        'połaniec', 'opatów', 'sędziszów', 'stąporków', 'kazimierza wielka'
    ),
    'warmińsko-mazurskie': (
        'olsztyn', 'elbląg', 'ełk', 'iława', 'ostróda', 'giżycko', 'kętrzyn', 'szczytno', 'bartoszyce',
        'mrągowo', 'działdowo', 'pisz', 'braniewo', 'olecko', 'lidzbark warmiński', 'gołdap',
        'nidzica', 'morąg', 'pasłęk', 'węgorzewo', 'nowe miasto lubawskie', 'biskupiec', 'dobre miasto'
    ),
    'wielkopolskie': (
        'poznań', 'kalisz', 'konin', 'piła', 'ostrów wielkopolski', 'gniezno', 'leszno', 'luboń',
        'września', 'swarzędz', 'śrem', 'krotoszyn', 'turek', 'jarocin', 'wągrowiec',
        'kościan', 'koło', 'środa wielkopolska', 'rawicz', 'gostyń', 'chodzież', 'szamotuły',
        'złotów', 'oborniki', 'pleszew', 'trzcianka', 'nowy tomyśl', 'kępno', 'ostrzeszów',
        'słupca', 'grodzisk wielkopolski', 'wolsztyn', 'mosina', 'wronki', 'czarnków', 'międzychód'
    ),
    'zachodniopomorskie': (
        'szczecin', 'koszalin', 'stargard', 'kołobrzeg', 'świnoujście', 'szczecinek', 'police',
        'wałcz', 'białogard', 'goleniów', 'gryfino', 'nowogard', 'gryfice', 'świdwin',
        'choszczno', 'barlinek', 'dębno', 'złocieniec', 'pyrzyce', 'sławno', 'drawsko pomorskie',
        'myślibórz', 'łobez', 'kamień pomorski', 'połczyn-zdrój', 'chojna', 'czaplinek'
    ),
}

_DIACRITICS_MAP = {
    'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
    'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
}


def unaccent(text: str) -> str:
    """Usuwa polskie znaki diakrytyczne dla tolerancyjnego porównywania."""
    return ''.join(_DIACRITICS_MAP.get(c, c) for c in text.lower())


def _create_ssl_context():
    """Tworzy bezpieczny kontekst SSL z fallbackiem dla macOS Python 3.14."""
    try:
        return ssl.create_default_context()
    except Exception:
        return ssl._create_unverified_context()


def _match_voivodeship_from_text(text: str) -> Optional[str]:
    """Wyszukuje województwo na podstawie rdzeni tekstowych i odmian."""
    if not text:
        return None
    text_low = text.lower()
    for stem, voiv in VOIV_STEMS:
        if stem in text_low:
            return voiv
    # Próba bez polskich znaków
    text_unaccent = unaccent(text)
    for stem, voiv in VOIV_STEMS:
        stem_unaccent = unaccent(stem)
        if stem_unaccent in text_unaccent:
            return voiv
    return None


def _check_static_dictionary(query: str) -> Optional[Tuple[str, str]]:
    """Sprawdza wbudowany słownik miast Polski.

    Zwraca (voivodeship_slug, matched_city_name) lub None.
    """
    q_norm = query.lower().strip()
    q_unaccent = unaccent(q_norm)

    # 1. Dokładne dopasowanie całej frazy do miasta
    for voiv, cities in VOIV_CITIES.items():
        for c in cities:
            if c == q_norm or unaccent(c) == q_unaccent:
                return voiv, c.capitalize()

    # 2. Dopasowanie jako słowo wewnątrz zapytania (np. "przewrotne powiat rzeszow")
    words = re.findall(r'[\w\-]+', q_norm)
    for w in words:
        if len(w) < 3:
            continue
        w_unaccent = unaccent(w)
        for voiv, cities in VOIV_CITIES.items():
            for c in cities:
                if c == w or unaccent(c) == w_unaccent:
                    return voiv, c.capitalize()

    return None


def _geocode_nominatim(query: str) -> Optional[Tuple[str, str, str]]:
    """Geokodowanie przez OpenStreetMap Nominatim.

    Zwraca (voivodeship_slug, place_name, display_name) lub None.
    """
    ctx = _create_ssl_context()
    headers = {
        'User-Agent': 'MBTWebsiteSalesApp/1.0 (kontakt@mbt.pl; https://mbt.pl)'
    }
    encoded_q = urllib.parse.quote(query.strip())
    url = f'https://nominatim.openstreetmap.org/search?q={encoded_q}&countrycodes=pl&format=json&addressdetails=1&limit=1'

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=3.5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if not data:
                return None
            item = data[0]
            addr = item.get('address', {})
            state = addr.get('state', '')
            voiv = _match_voivodeship_from_text(state)
            if not voiv:
                # Spróbuj dopasować z całego display_name
                voiv = _match_voivodeship_from_text(item.get('display_name', ''))
            if voiv:
                place = (
                    addr.get('city')
                    or addr.get('town')
                    or addr.get('village')
                    or addr.get('municipality')
                    or query
                )
                return voiv, str(place), item.get('display_name', query)
    except Exception as e:
        logger.warning("Nominatim geocode failed for '%s': %s", query, e)
    return None


def _geocode_wikipedia(query: str) -> Optional[Tuple[str, str, str]]:
    """Wyszukiwanie artykułu w polskiej Wikipedii jako zapasowe źródło.

    Zwraca (voivodeship_slug, title, title) lub None.
    """
    ctx = _create_ssl_context()
    headers = {
        'User-Agent': 'MBTWebsiteSalesApp/1.0 (kontakt@mbt.pl; https://mbt.pl)'
    }
    encoded_q = urllib.parse.quote(query.strip())
    url = f'https://pl.wikipedia.org/w/api.php?action=query&list=search&srsearch={encoded_q}&format=json&utf8=1'

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=3.5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = data.get('query', {}).get('search', [])
            for res in results[:4]:
                full_text = f"{res.get('title', '')} {res.get('snippet', '')}"
                voiv = _match_voivodeship_from_text(full_text)
                if voiv:
                    return voiv, res.get('title', query), res.get('title', query)
    except Exception as e:
        logger.warning("Wikipedia search failed for '%s': %s", query, e)
    return None


def _geocode_google_maps(query: str, api_key: str) -> Optional[Tuple[str, str, str]]:
    """Opcjonalne geokodowanie Google Maps Geocoding API jeśli skonfigurowano klucz."""
    ctx = _create_ssl_context()
    encoded_q = urllib.parse.quote(query.strip())
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={encoded_q}&components=country:PL&language=pl&key={api_key}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'MBTWebsite/1.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=3.5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if data.get('status') == 'OK' and data.get('results'):
                first = data['results'][0]
                display_name = first.get('formatted_address', query)
                place_name = query
                for comp in first.get('address_components', []):
                    types = comp.get('types', [])
                    if 'administrative_area_level_1' in types:
                        voiv = _match_voivodeship_from_text(comp.get('long_name', ''))
                        if voiv:
                            return voiv, place_name, display_name
                    if 'locality' in types:
                        place_name = comp.get('long_name', place_name)
    except Exception as e:
        logger.warning("Google Maps geocode failed: %s", e)
    return None


def resolve_sales_rep(query: str, lang: str = 'pl') -> Dict[str, Any]:
    """Główna funkcja: zamienia zapytanie tekstowe na opiekuna handlowego MBT."""
    clean_q = query.strip()
    if not clean_q:
        return {
            'success': False,
            'error': 'Wpisz miejscowość lub powiat, aby wyszukać doradcę.'
        }

    cache_key = f"{clean_q.lower()}_{lang}"
    if cache_key in _CACHE:
        return _CACHE[cache_key]

    voiv_slug: Optional[str] = None
    place_name: str = clean_q
    display_name: str = clean_q

    # 1. Sprawdź czy zapytanie to bezpośrednio nazwa województwa lub regionu
    direct_voiv = _match_voivodeship_from_text(clean_q)
    if direct_voiv:
        voiv_slug = direct_voiv
        place_name = VOIV_NAMES.get(direct_voiv, clean_q)
        display_name = f"Województwo {VOIV_NAMES.get(direct_voiv, clean_q)}"

    # 2. Sprawdź wbudowany słownik polskich miast (~450 pozycji, 0ms latency)
    if not voiv_slug:
        dict_match = _check_static_dictionary(clean_q)
        if dict_match:
            voiv_slug, matched_city = dict_match
            place_name = matched_city
            display_name = f"{matched_city}, woj. {VOIV_NAMES.get(voiv_slug, '')}"

    # 3. Opcjonalnie Google Maps jeśli ustawiono klucz
    google_key = os.getenv('GOOGLE_MAPS_API_KEY') or os.getenv('GOOGLE_API_KEY')
    if not voiv_slug and google_key:
        g_match = _geocode_google_maps(clean_q, google_key)
        if g_match:
            voiv_slug, place_name, display_name = g_match

    # 4. OpenStreetMap Nominatim (dokładne dane dla gmin, wiosek, powiatów w PL)
    if not voiv_slug:
        osm_match = _geocode_nominatim(clean_q)
        if osm_match:
            voiv_slug, place_name, display_name = osm_match

    # 5. Wikipedia API fallback
    if not voiv_slug:
        wiki_match = _geocode_wikipedia(clean_q)
        if wiki_match:
            voiv_slug, place_name, display_name = wiki_match

    # Jeśli nie udało się ustalić województwa
    if not voiv_slug or voiv_slug not in VOIV_REP:
        res = {
            'success': False,
            'query': clean_q,
            'error': f'Nie udało się jednoznacznie zlokalizować miejscowości "{clean_q}". Wybierz swoje województwo na mapie poniżej.'
        }
        _CACHE[cache_key] = res
        return res

    rep_name = VOIV_REP[voiv_slug]
    voiv_display = VOIV_NAMES.get(voiv_slug, voiv_slug.capitalize())

    # Pobierz pełne dane doradcy z ORM / mbt_data
    rep_obj: Optional[Dict[str, Any]] = None
    try:
        all_reps = mbt_orm.get_sales_reps(lang)
        for r in all_reps:
            if r.get('name') == rep_name:
                rep_obj = r
                break
    except Exception:
        pass

    if not rep_obj:
        for r in getattr(mbt_data, 'SALES_REPS', []):
            if r.get('name') == rep_name:
                rep_obj = r
                break

    if not rep_obj:
        rep_obj = {
            'name': rep_name,
            'position': 'Dział Handlowy',
            'phone': '',
            'email': '',
            'photo': ''
        }

    phone = rep_obj.get('phone', '')
    phone_clean = re.sub(r'[^\d+]', '', phone)

    result = {
        'success': True,
        'query': clean_q,
        'place': place_name,
        'location_display': display_name,
        'voivodeship': voiv_display,
        'voivodeship_slug': voiv_slug,
        'rep': {
            'name': rep_obj.get('name', rep_name),
            'position': rep_obj.get('position', 'Dział Handlowy'),
            'phone': phone,
            'phone_href': f"tel:{phone_clean}" if phone_clean else "#",
            'email': rep_obj.get('email', ''),
            'photo': rep_obj.get('photo', ''),
            'coverage': REP_COVERAGE.get(rep_name, ''),
        }
    }

    _CACHE[cache_key] = result
    return result
