"""Wyszukiwanie opiekuna handlowego MBT na podstawie miejscowości lub powiatu.

Obsługuje:
1. Natychmiastowe dopasowanie z wbudowanego słownika wszystkich miast, powiatów i gmin Polski (>1200 pozycji, 0ms latency)
2. Zaawansowane dopasowywanie odmian gramatycznych języka polskiego (np. "w Mikołajkach", "w Zabrzu", "w Bydgoszczy")
3. Rozpoznawanie nazw województw i krain historycznych (np. Kujawy, Mazowsze, Śląsk, Podkarpacie, Warmia, Mazury)
4. Geokodowanie awaryjne przez OpenStreetMap Nominatim, Photon (Komoot) oraz Wikipedię
5. Google Maps Geocoding API (opcjonalnie, gdy ustawiony jest klucz GOOGLE_MAPS_API_KEY)
"""

import json
import logging
import os
import re
import ssl
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

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

# Rdzenie i odmiany nazw województw i krain geograficznych (kolejność ma kluczowe znaczenie!)
VOIV_STEMS: Tuple[Tuple[str, str], ...] = (
    # Najpierw specyficzne wieloczłonowe i unikalne rdzenie, aby nie kolidowały z "pomorskie" czy "mazowieckie"
    ('kujawsko pomorsk', 'kujawsko-pomorskie'),
    ('kujawsk', 'kujawsko-pomorskie'),
    ('kujawk', 'kujawsko-pomorskie'),
    ('kujaw', 'kujawsko-pomorskie'),
    ('zachodniopomorsk', 'zachodniopomorskie'),
    ('zachodnio pomorsk', 'zachodniopomorskie'),
    ('warmińsko mazursk', 'warmińsko-mazurskie'),
    ('warminsko mazursk', 'warmińsko-mazurskie'),
    ('warmińsk', 'warmińsko-mazurskie'),
    ('warmia', 'warmińsko-mazurskie'),
    ('warmi', 'warmińsko-mazurskie'),
    ('mazur', 'warmińsko-mazurskie'),
    ('dolnośląsk', 'dolnośląskie'),
    ('dolnoslask', 'dolnośląskie'),
    ('dolny śląsk', 'dolnośląskie'),
    ('dolny slask', 'dolnośląskie'),
    ('wielkopolsk', 'wielkopolskie'),
    ('wielkopols', 'wielkopolskie'),
    ('świętokrzysk', 'świętokrzyskie'),
    ('swietokrzysk', 'świętokrzyskie'),
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
    ('górny śląsk', 'śląskie'),
    ('gorny slask', 'śląskie'),
    ('łódzk', 'łódzkie'),
    ('lodzk', 'łódzkie'),
)

# Kompletny słownik wszystkich miast w Polsce (~1013), powiatów (~380) i znanych miejscowości
VOIV_CITIES: Dict[str, Tuple[str, ...]] = {
    'dolnośląskie': (
        'wrocław', 'wałbrzych', 'legnica', 'jelenia góra', 'lubin', 'głogów', 'świdnica',
        'bolesławiec', 'oleśnica', 'dzierżoniów', 'oława', 'zgorzelec', 'bielawa', 'kłodzko',
        'jawor', 'świebodzice', 'polkowice', 'nowa ruda', 'kamienna góra', 'boguszów-gorce',
        'strzegom', 'złotoryja', 'bogatynia', 'ząbkowice śląskie', 'jelcz-laskowice', 'chojnów',
        'trzebnica', 'brzeg dolny', 'strzelin', 'wołów', 'góra', 'milicz', 'lubań', 'lwówek śląski',
        'bardo', 'bierutów', 'bolków', 'bystrzyca kłodzka', 'chocianów', 'duszniki-zdrój', 'głuszyca',
        'gryfów śląski', 'jaworzyna śląska', 'jedlina-zdrój', 'kamieniec ząbkowicki', 'karpacz',
        'kąty wrocławskie', 'kowary', 'kudowa-zdrój', 'lądek-zdrój', 'leśna', 'lubawka', 'lubomierz',
        'mieroszów', 'międzybórz', 'międzylesie', 'miękinia', 'mirsk', 'niemcza', 'nowogrodziec',
        'oborniki śląskie', 'olszyna', 'piechowice', 'pieńsk', 'pieszyce', 'piława górna',
        'polanica-zdrój', 'prochowice', 'prusice', 'przemków', 'radków', 'siechnice', 'sobótka',
        'stronie śląskie', 'syców', 'szczawno-zdrój', 'szczytna', 'szklarska poręba', 'ścinawa',
        'środa śląska', 'świeradów-zdrój', 'świerzawa', 'twardogóra', 'wąsosz', 'węgliniec',
        'wiązów', 'wleń', 'wojcieszów', 'zawidów', 'ziębice', 'złoty stok', 'żarów', 'żmigród',
        'karkonosze', 'kotlina kłodzka', 'karkonoski', 'kłodzki', 'lubański', 'lwówecki',
        'polkowicki', 'średzki', 'świdnicki', 'trzebnicki', 'wrocławski', 'zgorzelecki', 'złotoryjski'
    ),
    'kujawsko-pomorskie': (
        'bydgoszcz', 'toruń', 'włocławek', 'grudziądz', 'inowrocław', 'brodnica', 'świecie',
        'chełmno', 'nakło nad notecią', 'rypin', 'solec kujawski', 'chełmża', 'lipno', 'żnin',
        'tuchola', 'wąbrzeźno', 'golub-dobrzyń', 'aleksandrów kujawski', 'mogilno', 'koronowo',
        'ciechocinek', 'kruszwica', 'radziejów', 'sępólno krajeńskie', 'barcin', 'bobrowniki',
        'brześć kujawski', 'chodecz', 'dobrzyń nad wisłą', 'gąsawa', 'gniewkowo', 'górzno',
        'izbica kujawska', 'jabłonowo pomorskie', 'janikowo', 'janowiec wielkopolski',
        'kamień krajeński', 'kcynia', 'kikół', 'kowal', 'kowalewo pomorskie', 'lubień kujawski',
        'lubraniec', 'łabiszyn', 'łasin', 'mrocza', 'nieszawa', 'nowe', 'pakość',
        'piotrków kujawski', 'pruszcz', 'radzyń chełmiński', 'skępe', 'strzelno', 'szubin',
        'więcbork', 'bory tucholskie', 'pałuki', 'kujawy', 'aleksandrowski', 'brodnicki',
        'bydgoski', 'chełmiński', 'golubsko-dobrzyński', 'grudziądzki', 'inowrocławski',
        'lipnowski', 'mogileński', 'nakielski', 'radziejowski', 'rypiński', 'sępoleński',
        'świecki', 'toruński', 'tucholski', 'wąbrzeski', 'włocławski', 'żniński'
    ),
    'lubelskie': (
        'lublin', 'zamość', 'chełm', 'biała podlaska', 'puławy', 'świdnik', 'kraśnik', 'łuków',
        'biłgoraj', 'lubartów', 'tomaszów lubelski', 'łęczna', 'krasnystaw', 'hrubieszów',
        'dęblin', 'radzyń podlaski', 'włodawa', 'janów lubelski', 'parczew', 'ryki', 'poniatowa',
        'opole lubelskie', 'bełżyce', 'szczebrzeszyn', 'annopol', 'bychawa', 'frampol', 'józefów',
        'kazimierz dolny', 'kock', 'krasnobród', 'łaszczów', 'międzyrzec podlaski', 'nałęczów',
        'ostrów lubelski', 'piaski', 'rejowiec fabryczny', 'rejowiec', 'stoczek łukowski',
        'tarnogród', 'terespol', 'tyszowce', 'zwierzyniec', 'turobin', 'urzędów', 'wąwolnica',
        'czemierniki', 'brody', 'roztocze', 'bialski', 'biłgorajski', 'chełmski', 'hrubieszowski',
        'janowski', 'krasnostawski', 'kraśnicki', 'lubartowski', 'lubelski', 'łęczyński',
        'łukowski', 'parczewski', 'puławski', 'radzyński', 'rycki', 'świdnicki', 'tomaszowski',
        'włodawski', 'zamojski'
    ),
    'lubuskie': (
        'zielona góra', 'gorzów wielkopolski', 'nowa sól', 'żary', 'żagań', 'świebodzin',
        'międzyrzecz', 'kostrzyn nad odrą', 'słubice', 'gubin', 'lubsko', 'wschowa', 'szprotawa',
        'krosno odrzańskie', 'drezdenko', 'sulęcin', 'strzelce krajeńskie', 'skwierzyna',
        'babimost', 'brody', 'bytom odrzański', 'cybinka', 'czerwieńsk', 'dobiegniew', 'gozdnica',
        'iłowa', 'jasień', 'kargowa', 'kożuchów', 'lubniewice', 'łęknica', 'małomice',
        'nowe miasteczko', 'nowogród bobrzański', 'ośno lubuskie', 'otyń', 'rzepin', 'sława',
        'sulechów', 'szlichtyngowa', 'torzym', 'trzciel', 'witnica', 'zbąszynek',
        'gorzowski', 'krośnieński', 'międzyrzecki', 'nowosolski', 'słubicki',
        'strzelecko-drezdenecki', 'sulęciński', 'świebodziński', 'wschowski', 'zielonogórski',
        'żagański', 'żarski'
    ),
    'łódzkie': (
        'łódź', 'piotrków trybunalski', 'pabianice', 'tomaszów mazowiecki', 'bełchatów', 'zgierz',
        'skierniewice', 'radomsko', 'kutno', 'sieradz', 'zduńska wola', 'łowicz',
        'aleksandrów łódzki', 'ozorków', 'wieluń', 'opoczno', 'konstantynów łódzki', 'rawa mazowiecka',
        'łask', 'głowno', 'łęczyca', 'koluszki', 'brzeziny', 'wieruszów', 'poddębice', 'pajęczno',
        'biała rawska', 'błaszki', 'bolesławiec', 'drzewica', 'działoszyn', 'kamieńsk',
        'krośniewice', 'lututów', 'przedbórz', 'rzgów', 'stryków', 'sulejów', 'szadek', 'tuszyn',
        'uniejów', 'warta', 'złoczew', 'białaczów', 'bolimów', 'dąbrowice', 'grabów', 'inowłódz',
        'jeżów', 'kiernozia', 'lutomiersk', 'parzęczew', 'piątek', 'rozprza', 'ujazd', 'żarnów',
        'osjaków', 'będków', 'bełchatowski', 'brzeziński', 'kutnowski', 'łaski', 'łęczycki',
        'łowicki', 'łódzki wschodni', 'opoczyński', 'pabianicki', 'pajęczański', 'piotrkowski',
        'poddębicki', 'radomszczański', 'rawski', 'sieradzki', 'skierniewicki', 'tomaszowski',
        'wieluński', 'wieruszowski', 'zduńskowolski', 'zgierski'
    ),
    'małopolskie': (
        'kraków', 'tarnów', 'nowy sącz', 'oświęcim', 'chrzanów', 'olkusz', 'nowy targ', 'bochnia',
        'gorlice', 'zakopane', 'skawina', 'andrychów', 'wieliczka', 'trzebinia', 'wadowice',
        'kęty', 'myślenice', 'libiąż', 'brzesko', 'limanowa', 'rabka-zdrój', 'miechów',
        'dąbrowa tarnowska', 'krynica-zdrój', 'sucha beskidzka', 'proszowice', 'niepołomice',
        'stary sącz', 'muszyna', 'szczawnica', 'alwernia', 'biecz', 'bobowa', 'brzeszcze',
        'bukowno', 'chełmek', 'ciężkowice', 'czarny dunajec', 'czchów', 'dobczyce', 'grybów',
        'jordanów', 'kalwaria zebrzydowska', 'koszyce', 'krzeszowice', 'książ wielki',
        'maków podhalański', 'mszana dolna', 'nowe brzesko', 'nowy wiśnicz', 'piwniczna-zdrój',
        'radłów', 'ryglice', 'skała', 'słomniki', 'sułkowice', 'szczucin', 'świątniki górne',
        'tuchów', 'wojnicz', 'wolbrom', 'zakliczyn', 'zator', 'żabno', 'białka tatrzańska',
        'bukowina tatrzańska', 'poronin', 'kościelisko', 'chochołów', 'zawoja', 'krościenko nad dunajcem',
        'podhale', 'tatry', 'beskid wyspowy', 'beskid sądecki', 'gorce', 'bocheński', 'brzeski',
        'chrzanowski', 'dąbrowski', 'gorlicki', 'krakowski', 'limanowski', 'miechowski',
        'myślenicki', 'nowosądecki', 'nowotarski', 'olkuski', 'oświęcimski', 'proszowicki',
        'suski', 'tarnowski', 'tatrzański', 'wadowicki', 'wielicki'
    ),
    'mazowieckie': (
        'warszawa', 'radom', 'płock', 'siedlce', 'pruszków', 'legionowo', 'ostrołęka', 'piaseczno',
        'otwock', 'ciechanów', 'żyrardów', 'mińsk mazowiecki', 'wołomin', 'sochaczew', 'ząbki',
        'mława', 'grodzisk mazowiecki', 'marki', 'nowy dwór mazowiecki', 'wyszków', 'piastów',
        'ostrów mazowiecka', 'płońsk', 'kobyłka', 'kozienice', 'sulejówek', 'pionki', 'pułtusk',
        'gostynin', 'sierpc', 'garwolin', 'przasnysz', 'sokołów podlaski', 'grójec', 'szydłowiec',
        'węgrów', 'błonie', 'konstancin-jeziorna', 'góra kalwaria', 'łomianki', 'zielonka',
        'zwoleń', 'białobrzegi', 'bieżuń', 'bodzanów', 'brok', 'brwinów', 'cegłów', 'chorzele',
        'ciepielów', 'czerwińsk nad wisłą', 'dobre', 'drobin', 'gąbin', 'gielniów', 'glinojeck',
        'głowaczów', 'halinów', 'iłża', 'jadów', 'jastrząb', 'jedlnia-letnisko', 'józefów',
        'kałuszyn', 'karczew', 'kazanów', 'kosów lacki', 'latowicz', 'lipsko', 'lubowidz',
        'łaskarzew', 'łochów', 'łosice', 'maciejowice', 'magnuszew', 'maków mazowiecki',
        'małkinia górna', 'milanówek', 'mogielnica', 'mordy', 'mrozy', 'mszczonów', 'myszyniec',
        'nasielsk', 'nowe miasto nad pilicą', 'odrzywół', 'osieck', 'ożarów mazowiecki', 'pilawa',
        'podkowa leśna', 'przysucha', 'przytyk', 'raciąż', 'radzymin', 'różan', 'sanniki',
        'serock', 'siennica', 'sienno', 'skaryszew', 'sochocin', 'solec nad wisłą', 'stanisławów',
        'staroźreby', 'tarczyn', 'tłuszcz', 'warka', 'wiskitki', 'wyszogród', 'wyśmierzyce',
        'zakroczym', 'białobrzeski', 'ciechanowski', 'garwoliński', 'gostyniński', 'grodziski',
        'grójecki', 'kozienicki', 'legionowski', 'lipski', 'łosicki', 'makowski', 'miński',
        'mławski', 'nowodworski', 'ostrołęcki', 'ostrowski', 'otwocki', 'piaseczyński',
        'płocki', 'płoński', 'pruszkowski', 'przasnyski', 'przysuski', 'pułtuski', 'radomski',
        'siedlecki', 'sierpecki', 'sochaczewski', 'sokołowski', 'szydłowiecki',
        'warszawski zachodni', 'węgrowski', 'wołomiński', 'wyszkowski', 'zwoleński',
        'żuromiński', 'żyrardowski'
    ),
    'opolskie': (
        'opole', 'kędzierzyn-koźle', 'nysa', 'brzeg', 'kluczbork', 'prudnik', 'strzelce opolskie',
        'krapkowice', 'namysłów', 'głuchołazy', 'głubczyce', 'zdzieszowice', 'olesno', 'ozimek',
        'grodków', 'paczków', 'baborów', 'biała', 'byczyna', 'dobrodzień', 'głogówek', 'gogolin',
        'gorzów śląski', 'kietrz', 'kolonowskie', 'korfantów', 'leśnica', 'lewin brzeski',
        'niemodlin', 'otmuchów', 'praszka', 'prószków', 'strzeleczki', 'tułowice', 'ujazd',
        'wołczyn', 'zawadzkie', 'brzeski', 'głubczycki', 'kędzierzyńsko-kozielski', 'kluczborski',
        'krapkowicki', 'namysłowski', 'nyski', 'oleski', 'opolski', 'prudnicki', 'strzelecki'
    ),
    'podkarpackie': (
        'rzeszów', 'mielec', 'przemyśl', 'stalowa wola', 'krosno', 'dębica', 'jarosław', 'sanok',
        'jasło', 'łańcut', 'ropczyce', 'przeworsk', 'nisko', 'leżajsk', 'lubaczów', 'kolbuszowa',
        'strzyżów', 'brzozów', 'lesko', 'ustrzyki dolne', 'przewrotne', 'głogów małopolski',
        'nowa dęba', 'tarnobrzeg', 'sędziszów małopolski', 'rudnik nad sanem', 'błażowa',
        'baranów sandomierski', 'bircza', 'boguchwała', 'brzostek', 'cieszanów', 'dubiecko',
        'dukla', 'dynów', 'iwonicz-zdrój', 'jawornik polski', 'jedlicze', 'kańczuga', 'kołaczyce',
        'narol', 'nowa sarzyna', 'oleszyce', 'pilzno', 'pruchnik', 'przecław', 'radomyśl wielki',
        'radymno', 'rymanów', 'sieniawa', 'sokołów małopolski', 'tyczyn', 'ulanów', 'zagórz',
        'zaklików', 'solina', 'polańczyk', 'wetlina', 'cisna', 'lutowiska', 'ustrzyki górne',
        'bieszczady', 'bieszczadzki', 'brzozowski', 'dębicki', 'jarosławski', 'jasielski',
        'kolbuszowski', 'krośnieński', 'leski', 'leżajski', 'lubaczowski', 'łańcucki', 'mielecki',
        'niżański', 'przemyski', 'przeworski', 'ropczycko-sędziszowski', 'rzeszowski', 'sanocki',
        'stalowowolski', 'strzyżowski', 'tarnobrzeski'
    ),
    'podlaskie': (
        'białystok', 'suwałki', 'łomża', 'augustów', 'bielsk podlaski', 'zambrów', 'grajewo',
        'hajnówka', 'sokółka', 'łapy', 'siemiatycze', 'wasilków', 'kolno', 'mońki',
        'czarna białostocka', 'wysokie mazowieckie', 'dąbrowa białostocka', 'sejny', 'brańsk',
        'choroszcz', 'ciechanowiec', 'czyżew', 'drohiczyn', 'goniądz', 'jedwabne', 'kleszczele',
        'knyszyn', 'krynki', 'lipsk', 'michałowo', 'nowogród', 'rajgród', 'stawiski', 'suchowola',
        'supraśl', 'suraż', 'szczuczyn', 'szepietowo', 'tykocin', 'zabłudów', 'augustowski',
        'białostocki', 'bielski', 'grajewski', 'hajnowski', 'kolneński', 'łomżyński', 'moniecki',
        'sejneński', 'siemiatycki', 'sokólski', 'suwalski', 'wysokomazowiecki', 'zambrowski'
    ),
    'pomorskie': (
        'gdańsk', 'gdynia', 'słupsk', 'tczew', 'wejherowo', 'starogard gdański', 'chojnice',
        'kwidzyn', 'malbork', 'sopot', 'lębork', 'pruszcz gdański', 'kościerzyna', 'reda',
        'rumia', 'bytów', 'ustka', 'kartuzy', 'człuchów', 'puck', 'nowy dwór gdański', 'sztum',
        'hel', 'władysławowo', 'brusy', 'czarna woda', 'czarne', 'czersk', 'debrzno', 'dzierzgoń',
        'gniew', 'jastarnia', 'kępice', 'kobylnica', 'krynica morska', 'łeba', 'miastko',
        'nowy staw', 'pelplin', 'prabuty', 'skarszewy', 'skórcz', 'żukowo', 'chłapowo',
        'jastrzębia góra', 'jurata', 'chałupy', 'dębki', 'karwia', 'rowy', 'stegna', 'sztutowo',
        'kąty rybackie', 'kaszuby', 'mierzeja wiślana', 'bytowski', 'chojnicki', 'człuchowski',
        'gdański', 'kartuski', 'kościerski', 'kwidzyński', 'lęborski', 'malborski', 'nowodworski',
        'pucki', 'słupski', 'starogardzki', 'sztumski', 'tczewski', 'wejherowski'
    ),
    'śląskie': (
        'katowice', 'częstochowa', 'sosnowiec', 'gliwice', 'zabrze', 'bielsko-biała', 'bytom',
        'ruda śląska', 'rybnik', 'tychy', 'dąbrowa górnicza', 'chorzów', 'jaworzno',
        'jastrzębie-zdrój', 'mysłowice', 'siemianowice śląskie', 'żory', 'tarnowskie góry',
        'będzin', 'piekary śląskie', 'racibórz', 'świętochłowice', 'zawiercie', 'wodzisław śląski',
        'mikołów', 'knurów', 'cieszyn', 'czechowice-dziedzice', 'myszków', 'żywiec',
        'czerwionka-leszczyny', 'pszczyna', 'lubliniec', 'łaziska górne', 'rydułtowy', 'kłobuck',
        'bieruń', 'pyskowice', 'radlin', 'radzionków', 'lędziny', 'blachownia', 'czeladź',
        'imielin', 'janów', 'kalety', 'koniecpol', 'koziegłowy', 'krzanowice', 'krzepice',
        'kuźnia raciborska', 'łazy', 'miasteczko śląskie', 'ogrodzieniec', 'olsztyn koło częstochowy', 'orzesze',
        'pilica', 'poręba', 'przyrów', 'pszów', 'siewierz', 'skoczów', 'sławków', 'sośnicowice',
        'strumień', 'szczekociny', 'szczyrk', 'toszek', 'ustroń', 'wilamowice', 'wisła',
        'włodowice', 'wojkowice', 'woźniki', 'żarki', 'beskid śląski', 'beskid żywiecki',
        'jura krakowsko-częstochowska', 'zagłębie dąbrowskie', 'będziński', 'bielski',
        'bieruńsko-lędziński', 'cieszyński', 'częstochowski', 'gliwicki', 'kłobucki',
        'lubliniecki', 'mikołowski', 'myszkowski', 'pszczyński', 'raciborski', 'rybnicki',
        'tarnogórski', 'wodzisławski', 'zawierciański', 'żywiecki'
    ),
    'świętokrzyskie': (
        'kielce', 'ostrowiec świętokrzyski', 'starachowice', 'skarżysko-kamienna', 'sandomierz',
        'końskie', 'busko-zdrój', 'staszów', 'jędrzejów', 'pińczów', 'włoszczowa', 'chęciny',
        'połaniec', 'opatów', 'sędziszów', 'stąporków', 'kazimierza wielka', 'suchedniów',
        'ożarów', 'małogoszcz', 'chmielnik', 'piekoszów', 'radoszyce', 'ćmielów', 'kunów',
        'daleszyce', 'wąchock', 'koprzywnica', 'bodzentyn', 'osiek', 'klimontów', 'oleśnica',
        'morawica', 'zawichost', 'łagów', 'stopnica', 'łopuszno', 'nowa słupia', 'skalbmierz',
        'iwaniska', 'pierzchnica', 'pacanów', 'wodzisław', 'szydłów', 'nowy korczyn',
        'działoszyce', 'wiślica', 'opatowiec', 'gowarczów', 'secemin', 'święta katarzyna',
        'bałtów', 'kurozwęki', 'solec-zdrój', 'góry świętokrzyskie', 'buski', 'jędrzejowski',
        'kazimierski', 'kielecki', 'konecki', 'opatowski', 'ostrowiecki', 'pińczowski',
        'sandomierski', 'skarżyski', 'starachowicki', 'staszowski', 'włoszczowski'
    ),
    'warmińsko-mazurskie': (
        'olsztyn', 'elbląg', 'ełk', 'iława', 'ostróda', 'giżycko', 'kętrzyn', 'szczytno',
        'bartoszyce', 'mrągowo', 'działdowo', 'pisz', 'braniewo', 'olecko', 'lidzbark warmiński',
        'gołdap', 'nidzica', 'morąg', 'pasłęk', 'węgorzewo', 'nowe miasto lubawskie', 'biskupiec',
        'dobre miasto', 'barczewo', 'biała piska', 'bisztynek', 'frombork', 'górowo iławeckie',
        'jeziorany', 'kisielice', 'korsze', 'lidzbark', 'lubawa', 'mikołajki', 'miłakowo',
        'miłomłyn', 'młynary', 'olsztynek', 'orneta', 'orzysz', 'pasym', 'pieniężno', 'reszel',
        'ryn', 'sępopol', 'susz', 'tolkmicko', 'wielbark', 'zalewo', 'ruciane-nida', 'krutyń',
        'kraina wielkich jezior', 'mazury', 'warmia', 'bartoszycki', 'braniewski', 'działdowski',
        'elbląski', 'ełcki', 'giżycki', 'gołdapski', 'iławski', 'kętrzyński', 'lidzbarski',
        'mrągowski', 'nidzicki', 'nowomiejski', 'olecki', 'olsztyński', 'ostródzki', 'piski',
        'szczycieński', 'węgorzewski'
    ),
    'wielkopolskie': (
        'poznań', 'kalisz', 'konin', 'piła', 'ostrów wielkopolski', 'gniezno', 'leszno', 'luboń',
        'września', 'swarzędz', 'śrem', 'krotoszyn', 'turek', 'jarocin', 'wągrowiec',
        'kościan', 'koło', 'środa wielkopolska', 'rawicz', 'gostyń', 'chodzież', 'szamotuły',
        'złotów', 'oborniki', 'pleszew', 'trzcianka', 'nowy tomyśl', 'kępno', 'ostrzeszów',
        'słupca', 'grodzisk wielkopolski', 'wolsztyn', 'mosina', 'wronki', 'czarnków',
        'międzychód', 'bojanowo', 'buk', 'czempiń', 'dobra', 'golina', 'kórnik', 'puszczykowo',
        'czerniejewo', 'dąbie', 'grabów nad prosną', 'jastrowie', 'jutrosin', 'kleczew', 'kłecko',
        'kobylin', 'kostrzyn', 'krajenka', 'krzywiń', 'krzyż wielkopolski', 'lwówek', 'margonin',
        'miejska górka', 'mikstat', 'nekla', 'nowe skalmierzyce', 'odolanów', 'okonek',
        'osieczna', 'ostroróg', 'pobiedziska', 'pogorzela', 'poniec', 'przedecz', 'pyzdry',
        'rakoniewice', 'raszków', 'rydzyna', 'skoki', 'sompolno', 'stawiszyn', 'stęszew',
        'sulmierzyce', 'śmigiel', 'ujsko', 'wielichowo', 'witkowo', 'wyrzysk', 'wysoka',
        'zagórów', 'zbąszyń', 'zduny', 'żerków', 'chodzieski', 'czarnkowsko-trzcianecki',
        'gnieźnieński', 'gostyński', 'grodziski', 'jarociński', 'kaliski', 'kępiński', 'kolski',
        'koniński', 'kościański', 'krotoszyński', 'leszczyński', 'międzychodzki', 'nowotomyski',
        'obornicki', 'ostrowski', 'ostrzeszowski', 'pilski', 'pleszewski', 'poznański',
        'rawicki', 'słupecki', 'szamotulski', 'średzki', 'śremski', 'turecki', 'wągrowiecki',
        'wolsztyński', 'wrzesiński', 'złotowski'
    ),
    'zachodniopomorskie': (
        'szczecin', 'koszalin', 'stargard', 'kołobrzeg', 'świnoujście', 'szczecinek', 'police',
        'wałcz', 'białogard', 'goleniów', 'gryfino', 'nowogard', 'gryfice', 'świdwin',
        'choszczno', 'barlinek', 'dębno', 'złocieniec', 'pyrzyce', 'sławno', 'drawsko pomorskie',
        'myślibórz', 'łobez', 'kamień pomorski', 'połczyn-zdrój', 'chojna', 'czaplinek',
        'barwice', 'biały bór', 'bobolice', 'borne sulinowo', 'cedynia', 'chociwel', 'człopa',
        'darłowo', 'dobra', 'dobrzany', 'drawno', 'dziwnów', 'golczewo', 'gościno', 'ińsko',
        'kalisz pomorski', 'karlino', 'lipiany', 'maszewo', 'mielno', 'mieszkowice', 'międzyzdroje',
        'mirosławiec', 'moryń', 'nowe warpno', 'pełczyce', 'płoty', 'polanów', 'recz', 'resko',
        'sianów', 'stepnica', 'suchań', 'trzcińsko-zdrój', 'trzebiatów', 'tuczno', 'tychowo',
        'węgorzyno', 'wolin', 'rewal', 'pobierowo', 'niechorze', 'dźwirzyno', 'sarbinowo',
        'ustronie morskie', 'jarosławiec', 'wyspa wolin', 'wyspa uznam', 'białogardzki',
        'choszczeński', 'drawski', 'goleniowski', 'gryficki', 'gryfiński', 'kamieński',
        'kołobrzeski', 'koszaliński', 'łobeski', 'myśliborski', 'policki', 'pyrzycki',
        'sławieński', 'stargardzki', 'szczecinecki', 'świdwiński', 'wałecki'
    ),
}

_DIACRITICS_MAP = {
    'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
    'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
}


def unaccent(text: str) -> str:
    """Usuwa polskie znaki diakrytyczne dla tolerancyjnego porównywania."""
    return ''.join(_DIACRITICS_MAP.get(c, c) for c in text.lower())


def normalize_query_text(query: str) -> str:
    """Normalizuje zapytanie, usuwając zbędne przedrostki i ujednolicając separatory."""
    t = query.lower().strip()
    prefixes = (
        'w ', 'we ', 'do ', 'koło ', 'kolo ', 'blisko ', 'okolice ',
        'gmina ', 'gm. ', 'gm ', 'powiat ', 'pow. ', 'pow ', 'm. ', 'm ', 'miasto '
    )
    changed = True
    while changed:
        changed = False
        for p in prefixes:
            if t.startswith(p):
                t = t[len(p):].strip()
                changed = True
    # Zamień myślniki, kropki, przecinki na spacje
    t_clean = re.sub(r'[\-_,./]+', ' ', t)
    return ' '.join(t_clean.split())


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
    norm = normalize_query_text(text)
    for stem, voiv in VOIV_STEMS:
        if stem in norm:
            return voiv
    # Próba bez polskich znaków
    norm_un = unaccent(norm)
    for stem, voiv in VOIV_STEMS:
        stem_un = unaccent(stem)
        if stem_un in norm_un:
            return voiv
    return None


def _check_static_dictionary(query: str) -> Optional[Tuple[str, str]]:
    """Sprawdza wbudowany słownik miast, powiatów i gmin Polski.

    Zwraca (voivodeship_slug, matched_city_name) lub None.
    """
    q_norm = query.lower().strip()
    q_unaccent = unaccent(q_norm)
    q_cleaned = normalize_query_text(query)
    q_cleaned_unaccent = unaccent(q_cleaned)

    # 1. Dokładne dopasowanie całej frazy do miasta / powiatu
    for voiv, cities in VOIV_CITIES.items():
        for c in cities:
            c_un = unaccent(c)
            if c == q_norm or c_un == q_unaccent or c == q_cleaned or c_un == q_cleaned_unaccent:
                return voiv, c.title()

    # 2. Sprawdzenie czy wielowyrazowa nazwa miasta/powiatu znajduje się w zapytaniu
    # Sortujemy po długości malejąco, aby "nowy targ" wyprzedził "targ", "gorzów wielkopolski" wyprzedził "gorzów"
    for voiv, cities in VOIV_CITIES.items():
        sorted_cities = sorted(cities, key=len, reverse=True)
        for c in sorted_cities:
            c_un = unaccent(c)
            # Sprawdzenie z granicami słów (np. "gmina Mikołajki", "powiat mrągowski")
            pattern_accent = r'(?:\b|^)' + re.escape(c) + r'(?:\b|$)'
            pattern_unaccent = r'(?:\b|^)' + re.escape(c_un) + r'(?:\b|$)'
            if (re.search(pattern_accent, q_norm) or re.search(pattern_accent, q_cleaned) or
                    re.search(pattern_unaccent, q_unaccent) or re.search(pattern_unaccent, q_cleaned_unaccent)):
                return voiv, c.title()

    # 3. Dopasowanie fleksyjne (końcówki miejscownika / dopełniacza, np. "Mikołajkach" -> "mikołajki", "Zabrzu" -> "zabrze")
    words = re.findall(r'[\w]+', q_cleaned)
    suffixes = ('ach', 'ego', 'ym', 'im', 'ej', 'em', 'ie', 'iu', 'owi', 'ow', 'om', 'e', 'a', 'y', 'i', 'u')
    for w in words:
        if len(w) < 4:
            continue
        w_stems = [w]
        for s in suffixes:
            if len(w) > len(s) + 3 and w.endswith(s):
                w_stems.append(w[:-len(s)])

        for stem in w_stems:
            stem_un = unaccent(stem)
            for voiv, cities in VOIV_CITIES.items():
                for c in cities:
                    c_un = unaccent(c)
                    if c.startswith(stem) or c_un.startswith(stem_un):
                        return voiv, c.title()

    return None


def _geocode_photon(query: str) -> Optional[Tuple[str, str, str]]:
    """Geokodowanie przez otwarte API Photon (Komoot OSM).

    Zwraca (voivodeship_slug, place_name, display_name) lub None.
    """
    ctx = _create_ssl_context()
    encoded_q = urllib.parse.quote(query.strip())
    url = f"https://photon.komoot.io/api/?q={encoded_q}&limit=1"
    headers = {
        'User-Agent': 'MBTWebsite-SalesAdvisor/1.0 (kontakt@mbt.pl)'
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=3.0) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            features = data.get('features', [])
            if not features:
                return None
            props = features[0].get('properties', {})
            state = props.get('state', '')
            county = props.get('county', '')
            voiv = _match_voivodeship_from_text(f"{state} {county}")
            if voiv:
                place = props.get('name') or props.get('city') or query
                display = f"{place}, woj. {VOIV_NAMES.get(voiv, '')}"
                return voiv, str(place), display
    except Exception as e:
        logger.debug("Photon geocode failed: %s", e)
    return None


def _geocode_nominatim(query: str) -> Optional[Tuple[str, str, str]]:
    """Geokodowanie przez OpenStreetMap Nominatim.

    Zwraca (voivodeship_slug, place_name, display_name) lub None.
    """
    ctx = _create_ssl_context()
    headers = {
        'User-Agent': 'MBTWebsite-SalesAdvisor/1.0 (kontakt@mbt.pl; https://mbt.pl)'
    }
    encoded_q = urllib.parse.quote(query.strip())
    url = f'https://nominatim.openstreetmap.org/search?q={encoded_q}&countrycodes=pl&format=json&addressdetails=1&limit=1'

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=3.0) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if not data:
                return None
            item = data[0]
            addr = item.get('address', {})
            state = addr.get('state', '')
            voiv = _match_voivodeship_from_text(state)
            if not voiv:
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
        logger.debug("Nominatim geocode failed for '%s': %s", query, e)
    return None


def _geocode_wikipedia(query: str) -> Optional[Tuple[str, str, str]]:
    """Wyszukiwanie artykułu w polskiej Wikipedii jako zapasowe źródło.

    Zwraca (voivodeship_slug, title, title) lub None.
    """
    ctx = _create_ssl_context()
    headers = {
        'User-Agent': 'MBTWebsite-SalesAdvisor/1.0 (kontakt@mbt.pl; https://mbt.pl)'
    }
    encoded_q = urllib.parse.quote(query.strip())
    url = f'https://pl.wikipedia.org/w/api.php?action=query&list=search&srsearch={encoded_q}&format=json&utf8=1'

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=3.0) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = data.get('query', {}).get('search', [])
            for res in results[:4]:
                full_text = f"{res.get('title', '')} {res.get('snippet', '')}"
                voiv = _match_voivodeship_from_text(full_text)
                if voiv:
                    return voiv, res.get('title', query), res.get('title', query)
    except Exception as e:
        logger.debug("Wikipedia search failed for '%s': %s", query, e)
    return None


def _geocode_google_maps(query: str, api_key: str) -> Optional[Tuple[str, str, str]]:
    """Opcjonalne geokodowanie Google Maps Geocoding API jeśli skonfigurowano klucz."""
    ctx = _create_ssl_context()
    encoded_q = urllib.parse.quote(query.strip())
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={encoded_q}&components=country:PL&language=pl&key={api_key}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'MBTWebsite/1.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=3.0) as resp:
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
        logger.debug("Google Maps geocode failed: %s", e)
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

    # 1. Sprawdź wbudowany słownik polskich miast i powiatów (>1200 pozycji, 0ms latency)
    # Dzięki temu miasta takie jak "Gorzów Wielkopolski" (woj. lubuskie) czy "Biała Podlaska" (woj. lubelskie)
    # trafiają do właściwego województwa, zamiast być mylone z przymiotnikiem województwa.
    dict_match = _check_static_dictionary(clean_q)
    if dict_match:
        voiv_slug, matched_city = dict_match
        place_name = matched_city
        display_name = f"{matched_city}, woj. {VOIV_NAMES.get(voiv_slug, '')}"

    # 2. Jeśli to nie miasto, sprawdź czy zapytanie to bezpośrednio nazwa województwa lub krainy
    if not voiv_slug:
        direct_voiv = _match_voivodeship_from_text(clean_q)
        if direct_voiv:
            voiv_slug = direct_voiv
            place_name = VOIV_NAMES.get(direct_voiv, clean_q)
            display_name = f"Województwo {VOIV_NAMES.get(direct_voiv, clean_q)}"

    # 3. Opcjonalnie Google Maps jeśli ustawiono klucz
    google_key = os.getenv('GOOGLE_MAPS_API_KEY') or os.getenv('GOOGLE_API_KEY')
    if not voiv_slug and google_key:
        g_match = _geocode_google_maps(clean_q, google_key)
        if g_match:
            voiv_slug, place_name, display_name = g_match

    # 4. OpenStreetMap Photon (Komoot)
    if not voiv_slug:
        photon_match = _geocode_photon(clean_q)
        if photon_match:
            voiv_slug, place_name, display_name = photon_match

    # 5. OpenStreetMap Nominatim
    if not voiv_slug:
        osm_match = _geocode_nominatim(clean_q)
        if osm_match:
            voiv_slug, place_name, display_name = osm_match

    # 6. Wikipedia API fallback
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
