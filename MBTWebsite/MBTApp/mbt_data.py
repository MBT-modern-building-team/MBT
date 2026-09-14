"""
Autogenerowany plik danych (NIE edytuj ręcznie sekcji danych!).

Generowany przez: scripts/gen_mbt_data.py (po zapisie w CMS — sygnał post_save).
Vercel nie ma bazy SQLite, więc strona na produkcji korzysta z tego fallbacku.

Aby zaktualizować dane na produkcji:
    1. zapisz zmiany w /admin (lokalnie),
    2. mbt_data.py zregeneruje się automatycznie,
    3. git add MBTApp/mbt_data.py && git commit && git push origin main
"""
from django.utils.translation import gettext_lazy as _


# ============================================================
# SITE — dane firmy
# ============================================================
SITE = {
    "phone": "+48 881 444 333",
    "phone_href": "+48881444333",
    "email": "biuro@mbt.pl",
    "hours": "Pon - Pt / 8:00 - 16:00",
    "hours_long": "Pon-Pt: 8:00 do 16:00",
    "office_zabrze": "Roosevelta 81, 41-800 Zabrze",
    "office_katowice": "Jankego 176/1A, 40-663 Katowice",
    "office_krakow": "Zawiła 65, bud. X lok. 5, 30-390 Kraków",
    "office_zabrze_photo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/4e175fa5f07a.webp",
    "office_katowice_photo": "/static/img/mbt/o-nas-zespol.jpg",
    "office_krakow_photo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/4f6ea4c1b231.webp",
    "office_site_label": "Twój plac budowy",
    "office_site_adres": "Adres Twojej inwestycji",
    "office_site_photo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/4f8eaf7bbb8a.webp",
    "nip": "9542788822",
    "regon": "369557780",
    "krs": "0000720424",
    "founded": "2005",
    "tagline": "Od 20 lat z pasją budujemy Wasze biznesy. Jeden team – pełna realizacja. Od projektu aż po dach!",
    "about_short": "MBT Modern Building Team — generalny wykonawca hal magazynowych, produkcyjnych i usługowych. Terminowa budowa obiektów przemysłowych pod klucz.",
    "counter_years": "20",
    "counter_years_label": "Lat doświadczenia",
    "counter_projects": "100",
    "counter_projects_label": "Zrealizowanych inwestycji",
    "counter_ontime": "100",
    "counter_ontime_suffix": "%",
    "counter_ontime_label": "Terminowości",
    "counter_brands": "16",
    "counter_brands_label": "Zaufanych marek"
}

PROJECTS = [
    {
    "title": "ATT - Kokotów",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "att-kokotow",
    "czas": "16 miesięcy",
    "formula": "Buduj",
    "opis": "Powierzchnia hali produkcyjnej: około 6500 m² Trzykondygnacyjny budynek biurowo-socjalny o powierzchni 1500 m² Place manewrowe, drogi dojazdowe, uzbrojenie podziemne Zagospodarowanie terenu wokół obiektu Wyposażenie wszystkich naw w suwnice Konstrukcja hali mieszana: słupy prefabrykowane, żelbetowe dach w konstrukcji stalowej",
    "logo": "/static/img/mbt/1718005265186-2efb17dd-48b4-4732-ac49-4f435ead9e69_1-acf11eeb.jpg",
    "gallery": [
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/59554a51bfd4.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/f6af6fd925eb.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/e1860085210d.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/c1f5cbc83f42.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/10adbef6ea88.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/c0cbaa631e5c.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/419521a19211.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/5db8fc52720e.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/ca3b50a75413.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/b9fd7af25348.webp"
    ],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/bd7222b47df1.webp",
    "latitude": 50.0199155,
    "longitude": 20.0948933,
    "order": 1,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Production hall area: approximately 6,500 m² Three-storey office-social building with an area of 1,500 m² Manoeuvring areas, access roads, underground utilities Land development around the facility Equipping all bays with overhead cranes Mixed hall structure: prefabricated columns, reinforced concrete, roof in steel structure",
        "cs": "Plocha výrobní haly: přibližně 6500 m² Třípatrová kancelářsko-sociální budova o ploše 1500 m² Manévrovací plochy, příjezdové komunikace, podzemní vedení Úprava terénu kolem objektu Vybavení všech polí jeřáby Smíšená konstrukce haly: prefabrikované sloupy, železobetonové, střecha v ocelové konstrukci",
        "sk": "Plocha výrobnej haly: približne 6500 m² Trojpodlažná kancelársko-sociálna budova s plochou 1500 m² Manévrovacie plochy, príjazdové cesty, podzemné vedenia Úprava terénu okolo objektu Vybavenie všetkých polí žeriavmi Zmiešaná konštrukcia haly: prefabrikované stĺpy, železobetónové, strecha v oceľovej konštrukcii",
        "de": "Produktionshallenfläche: ca. 6.500 m² Dreigeschossiges Büro- und Sozialgebäude mit einer Fläche von 1.500 m² Rangierflächen, Zufahrtsstraßen, unterirdische Erschließung Gestaltung des Geländes um das Objekt Ausstattung aller Felder mit Kranen Gemischte Hallenkonstruktion: vorgefertigte Stützen, Stahlbeton, Dach in Stahlkonstruktion",
        "hu": "Gyártócsarnok alapterülete: kb. 6500 m² Háromszintes iroda-szociális épület 1500 m² alapterülettel Manőverezési területek, bekötő utak, földalatti közművek A telek rendezése az objektum körül Minden mező felszerelése darukkal Vegyes csarnokszerkezet: előregyártott oszlopok, vasbeton, acélszerkezetű tető"
    }
},
    {
    "title": "Pumar - Siemianowice",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "pumar",
    "czas": "",
    "formula": "zaprojektuj - wybuduj",
    "opis": "Budowa hali magazynowo – produkcyjnej z zapleczem socjalno-biurowym.\r\n\r\nPowierzchnia hali wynosi około 2700 m²\r\nPowierzchnia części administracyjno-biurowej wynosi około 300 m²\r\n\r\nkonstrukcja hali w pełni stalowa",
    "logo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/fb6676b754f8.webp",
    "gallery": [
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/2939e412daee.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/f5fb318c8128.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/f2107da0ac72.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/585f2a82ce57.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/1ae05fac1c6f.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/309cd02db637.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/271371fbe400.webp",
        "https://media.mbt.pl/uploads/c9cded91e7fa.webp"
    ],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/0b5b6f5c26b1.webp",
    "latitude": 50.3232916,
    "longitude": 19.0131504,
    "order": 2,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Construction of a warehouse and production hall with social and office facilities.\n\nHall area of approximately 2,700 m²\nAdministrative and office area of approximately 300 m²\n\nFully steel structure of the hall",
        "cs": "Výstavba skladově-výrobní haly se sociálně-kancelářským zázemím.\n\nPlocha haly činí přibližně 2 700 m²\nPlocha administrativně-kancelářské části činí přibližně 300 m²\n\nkonstrukce haly je kompletně ocelová",
        "sk": "Výstavba skladovo-výrobnej haly so sociálno-kancelárskym zázemím.\n\nPlocha haly je približne 2 700 m²\nPlocha administratívno-kancelárskej časti je približne 300 m²\n\nkonštrukcia haly je celooková",
        "de": "Bau einer Lager- und Produktionshalle mit Sozial- und Büroräumen.\n\nHallenfläche ca. 2.700 m²\nVerwaltungs- und Bürofläche ca. 300 m²\n\nHallenkonstruktion vollständig in Stahl",
        "hu": "Raktár- és termelőcsarnok építése szociális és irodai kiszolgálórésszel.\n\nA csarnok alapterülete kb. 2 700 m²\nAz adminisztratív-irodai rész alapterülete kb. 300 m²\n\na csarnok szerkezete teljes egészében acél"
    }
},
    {
    "title": "Less Mess Storage – Warszawa",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "less-mess-storage-warszawa",
    "czas": "11 miesięcy",
    "formula": "Zaprojektuj-wybuduj",
    "opis": "Konstrukcja: żelbetowa, z optymalizacją zużycia stali Obudowa: płyty warstwowe Strop: strop żelbetowy pełniący funkcję podłogi o wysokiej jakości wykończenia Ogrzewanie: pompy ciepła, wymagające wcześniejszych odwiertów Wyposażenie: zróżnicowane boxy do przechowywania, rozmieszczone zgodnie z harmonogramem dostaw i montażu",
    "logo": "/static/img/mbt/preloader-56f61948.png",
    "gallery": [
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/22ef7443d42f.webp",
        "/static/img/mbt/LessMess-6-916e0c22.jpg",
        "/static/img/mbt/LessMess-5-9e410f12.jpg",
        "/static/img/mbt/LessMess-4-18feb603.jpg",
        "/static/img/mbt/LessMess-3-scaled-8cef25bd.jpg",
        "/static/img/mbt/LessMess-2-scaled-97b96a57.jpg",
        "/static/img/mbt/LessMess-1-3370ce84.jpg"
    ],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/252a53665bfa.webp",
    "latitude": 52.3437589,
    "longitude": 20.9503183,
    "order": 3,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Structure: reinforced concrete, with optimised steel consumption. Envelope: sandwich panels. Floor: reinforced concrete slab serving as a high-quality finished floor. Heating: heat pumps requiring prior boreholes. Equipment: varied storage boxes arranged in line with the delivery and installation schedule.",
        "cs": "Konstrukce: železobetonová, s optimalizací spotřeby oceli. Plášť: sendvičové panely. Strop: železobetonový strop plnící funkci podlahy s vysoce kvalitní povrchovou úpravou. Vytápění: tepelná čerpadla vyžadující předchozí vrty. Vybavení: rozmanité boxy pro skladování, rozmístěné dle harmonogramu dodávek a montáže.",
        "sk": "Konštrukcia: železobetónová, s optimalizáciou spotreby ocele. Plášť: sendvičové panely. Strop: železobetónový strop plniaci funkciu podlahy s vysoko kvalitnou povrchovou úpravou. Vykurovanie: tepelné čerpadlá vyžadujúce predchádzajúce vrty. Vybavenie: rozmanité boxy na skladovanie, rozmiestnené podľa harmonogramu dodávok a montáže.",
        "de": "Konstruktion: Stahlbeton, mit optimiertem Stahlverbrauch. Hülle: Sandwichpaneele. Decke: Stahlbeton-Decke als hochwertig ausgeführter Boden. Heizung: Wärmepumpen, die vorherige Bohrungen erfordern. Ausstattung: unterschiedliche Lagerboxen, angeordnet nach Liefer- und Montageplan.",
        "hu": "Szerkezet: vasbeton, optimalizált acélfelhasználással. Burkolat: szendvicspanelek. Födém: vasbeton födém, amely kiváló minőségű padlóburkolatként funkcionál. Fűtés: hőszivattyúk, amelyek előzetes fúrásokat igényelnek. Felszerelés: változatos tárolóboxok, a szállítási és szerelési ütemterv szerint elhelyezve."
    }
},
    {
    "title": "Kompania Piwowarska Tychy",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "kompania-piwowarska-tychy",
    "czas": "",
    "formula": "",
    "opis": "Na terenie zakładu Kampanii Piwowarskiej realizowaliśmy przebudowę starej hali. Projekt zrealizowaliśmy w taki sposób aby jak najbardziej nawiązywał do historycznej architektury browaru.",
    "logo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/d0028e1be0ff.webp",
    "gallery": [
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/17b9961f0ef4.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/0c4bdef57c89.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/9d3261b2a1b3.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/402fc9261140.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/2cd375f208af.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/29d1c38c6a62.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/4b6c6cbcd744.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/55219aceb865.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/f33c64967077.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/c3c02d2f26e0.webp"
    ],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/7ba1ed4fdb7c.webp",
    "latitude": 50.1329145,
    "longitude": 18.9865084,
    "order": 4,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Within the Kompania Piwowarska brewery facility, we carried out the reconstruction of an old hall. We delivered the project in a way that refers as much as possible to the historic architecture of the brewery.",
        "cs": "V areálu pivovaru Kompania Piwowarska jsme realizovali přestavbu staré haly. Projekt jsme provedli tak, aby co nejvíce navazoval na historickou architekturu pivovaru.",
        "sk": "V areáli pivovaru Kompania Piwowarska sme realizovali prestavbu starej haly. Projekt sme zrealizovali tak, aby čo najviac nadväzoval na historickú architektúru pivovaru.",
        "de": "Auf dem Gelände der Brauerei Kompania Piwowarska haben wir den Umbau einer alten Halle realisiert. Wir haben das Projekt so umgesetzt, dass es möglichst stark an die historische Architektur der Brauerei anknüpft.",
        "hu": "A Kompania Piwowarska sörgyár területén egy régi csarnok átépítését valósítottuk meg. A projektet úgy valósítottuk meg, hogy a lehető legjobban illeszkedjen a sörgyár történelmi építészetéhez."
    }
},
    {
    "title": "Fabryka Park Katowice",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "fabryka-park-katowice",
    "czas": "10 Miesięcy",
    "formula": "Generalne wykonawstwo",
    "opis": "Jako Generalny Wykonawca zakończyliśmy budowę kolejnego etapu kompleksu Fabryka Park. Zrealizowaliśmy trzykondygnacyjną bryłę o charakterze biurowym, która pełni funkcję nowoczesnego parku handlowo-usługowego. Inwestycja została oddana, a obecnie wewnątrz trwają prace fit-out prowadzone przez najemców.\r\n\r\nParametry inwestycji:\r\n\r\nFormuła: Generalne Wykonawstwo\r\n\r\nCzas realizacji: 06.2025 – 04.2026\r\n\r\nPowierzchnia użytkowa: 2 490,14 m² (pow. wewnętrzna: 3 191,5 m²)\r\n\r\nKubatura: 17 231,9 m³\r\n\r\nKonstrukcja: Mieszana\r\n\r\nNajemcy:\r\nGłówną część obiektu zajmą placówka medyczna MEDICOVER oraz klub XTREME FITNESS. Ofertę uzupełniają mniejsze lokale: KROWA MAĆ, DR MATERAC i LIKE A PET.\r\n\r\nTechnologia i Wyzwania:\r\n\r\nElewacja: Zastosowano nowoczesną fasadę z siatki cięto-ciągnionej.\r\n\r\nEkologia: Na dachu zainstalowano panele fotowoltaiczne. Obiekt jest w trakcie procedowania certyfikatu BREEAM.\r\n\r\nLogistyka: Największym wyzwaniem była skomplikowana konstrukcja, napięty harmonogram oraz prowadzenie prac w bezpośrednim sąsiedztwie czynnego parku handlowego i linii kolejowej.",
    "logo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/f7dbcc9a7d55.webp",
    "gallery": [
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/b8f522564cd5.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/2b1b03be6f86.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/cdab5738115c.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/2676543c835e.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/2ffd70ab108d.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/18624e7ecbda.webp"
    ],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/afe891827322.webp",
    "latitude": 50.214195,
    "longitude": 18.9753366,
    "order": 5,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "As the General Contractor, we have completed the construction of the next stage of the Fabryka Park complex. We have delivered a three-storey office-style building that serves as a modern retail and service park. The investment has been handed over, and tenants are currently carrying out fit-out works inside.\n\nInvestment parameters:\n\nFormula: General Contracting\n\nImplementation period: 06.2025 – 04.2026\n\nUsable area: 2,490.14 m² (internal area: 3,191.5 m²)\n\nVolume: 17,231.9 m³\n\nStructure: Mixed\n\nTenants:\nThe main part of the building will be occupied by the MEDICOVER medical facility and the XTREME FITNESS club. Smaller premises – KROWA MAĆ, DR MATERAC and LIKE A PET – complement the offering.\n\nTechnology and Challenges:\n\nFaçade: A modern façade made of expanded metal mesh was used.\n\nEcology: Photovoltaic panels have been installed on the roof. The facility is currently undergoing BREEAM certification.\n\nLogistics: The biggest challenges were the complex structure, a tight schedule and conducting works in the immediate vicinity of an operating retail park and a railway line.",
        "cs": "Jako Generální dodavatel jsme dokončili výstavbu další etapy komplexu Fabryka Park. Realizovali jsme třípatrovou budovu kancelářského charakteru, která plní funkci moderního obchodně-služebního parku. Investice byla předána a v současné době probíhají uvnitř fit-out práce nájemců.\n\nParametry investice:\n\nFormule: Generální dodavatelství\n\nDoba realizace: 06.2025 – 04.2026\n\nUžitková plocha: 2 490,14 m² (vnitřní plocha: 3 191,5 m²)\n\nObjem: 17 231,9 m³\n\nKonstrukce: Smíšená\n\nNájemci:\nHlavní část objektu obsadí zdravotnické zařízení MEDICOVER a klub XTREME FITNESS. Nabídku doplňují menší provozovny: KROWA MAĆ, DR MATERAC a LIKE A PET.\n\nTechnologie a výzvy:\n\nFasáda: Byla použita moderní fasáda z taženého a řezaného kovového pletiva.\n\nEkologie: Na střeše byly instalovány fotovoltaické panely. Objekt je v procesu certifikace BREEAM.\n\nLogistika: Největší výzvou byla složitá konstrukce, napjatý harmonogram a provádění prací v bezprostřední blízkosti aktivního obchodního parku a železniční trati.",
        "sk": "Ako Generálny dodávateľ sme dokončili výstavbu ďalšej etapy komplexu Fabryka Park. Zrealizovali sme trojpodlažnú budovu kancelárskeho charakteru, ktorá plní funkciu moderného obchodno-služobného parku. Investícia bola odovzdaná a v súčasnosti prebiehajú vo vnútri fit-out práce nájomcov.\n\nParametre investície:\n\nFormul: Generálne dodávateľstvo\n\nDoba realizácie: 06.2025 – 04.2026\n\nÚžitková plocha: 2 490,14 m² (vnútorná plocha: 3 191,5 m²)\n\nObjem: 17 231,9 m³\n\nKonštrukcia: Zmiešaná\n\nNájomcovia:\nHlavnú časť objektu obsadí zdravotnícke zariadenie MEDICOVER a klub XTREME FITNESS. Ponuku dop�ňajú menšie prevádzky: KROWA MAĆ, DR MATERAC a LIKE A PET.\n\nTechnológia a výzvy:\n\nFasáda: Bola použitá moderná fasáda z ťahaného a rezaného kovového pletiva.\n\nEkológia: Na streche boli inštalované fotovoltické panely. Objekt je v procese certifikácie BREEAM.\n\nLogistika: Najväčšou výzvou bola zložitá konštrukcia, napätý harmonogram a vykonávanie prác v bezprostrednej blízkosti aktívneho obchodného parku a železničnej trate.",
        "de": "Als Generalunternehmer haben wir den Bau der nächsten Etappe des Komplexes Fabryka Park abgeschlossen. Wir haben einen dreigeschossigen Baukörper mit Bürocharakter realisiert, der als moderner Handels- und Dienstleistungspark fungiert. Die Investition wurde übergeben, derzeit laufen im Inneren die Mieterausbauten.\n\nInvestitionsparameter:\n\nFormel: Generalunternehmer\n\nRealisierungszeitraum: 06.2025 – 04.2026\n\nNutzfläche: 2.490,14 m² (Innenfläche: 3.191,5 m²)\n\nVolumen: 17.231,9 m³\n\nKonstruktion: Gemischt\n\nMieter:\nDen Hauptteil des Objekts belegen die medizinische Einrichtung MEDICOVER und der XTREME FITNESS Club. Kleinere Einheiten – KROWA MAĆ, DR MATERAC und LIKE A PET – ergänzen das Angebot.\n\nTechnologie und Herausforderungen:\n\nFassade: Eine moderne Fassade aus Streckmetall wurde eingesetzt.\n\nÖkologie: Auf dem Dach wurden Photovoltaikmodule installiert. Das Objekt befindet sich im BREEAM-Zertifizierungsprozess.\n\nLogistik: Die größten Herausforderungen waren die komplexe Konstruktion, ein enger Zeitplan und die Durchführung der Arbeiten in unmittelbarer Nähe eines aktiven Handelsparks und einer Bahnlinie.",
        "hu": "Mint Fővállalkozó befejeztük a Fabryka Park komplexum következő ütemének építését. Megvalósítottunk egy háromszintes, irodai jellegű épülettömböt, amely modern kereskedelmi-szolgáltató park funkcióját tölti be. A beruházás átadásra került, jelenleg a bérlők fit-out munkálatai zajlanak az épületen belül.\n\nA beruházás paraméterei:\n\nForma: Fővállalkozás\n\nMegvalósítás időtartama: 06.2025 – 04.2026\n\nHasznos alapterület: 2 490,14 m² (belső terület: 3 191,5 m²)\n\nTérfogat: 17 231,9 m³\n\nSzerkezet: Vegyes\n\nBérlők:\nAz objektum fő részét a MEDICOVER egészségügyi intézmény és az XTREME FITNESS klub foglalja el. A kínálatot kisebb egységek egészítik ki: KROWA MAĆ, DR MATERAC és LIKE A PET.\n\nTechnológia és kihívások:\n\nHomlokzat: Modern, nyújtott és vágott fémhálós homlokzatot alkalmaztunk.\n\nÖkológia: A tetőn napelemeket telepítettünk. Az objektum jelenleg BREEAM tanúsítási folyamatban van.\n\nLogisztika: A legnagyobb kihívást az összetett szerkezet, a feszített ütemezés és a munkavégzés volt egy működő kereskedelmi park és vasútvonal közvetlen közelében."
    }
},
    {
    "title": "Eurosleeve – Zabrze",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "eurosleeve-zabrze",
    "czas": "14 miesięcy",
    "formula": "Buduj",
    "opis": "Powierzchnia hali: 2333,43 m² Powierzchnia części socjalno-biurowej: 449,93 m² Sieci i instalacje na potrzeby realizowanej inwestycji Zagospodarowanie terenu Konstrukcja: Konstrukcja hali w słupy żelbetowe prefabrykowane Konstrukcja dachu hali stalowa Elewacja z płyt warstwowych Pokrycie dachu z izolacją z PIR i pokryciem membraną PCV Konstrukcja budynku biurowego mieszana (murowana, stropy i płyta żelbetowa)",
    "logo": "/static/img/mbt/Projekt-bez-nazwy-16-737059f4.png",
    "gallery": [
        "/static/img/mbt/Eurosleeve-12-scaled-a4ea9500.jpg",
        "/static/img/mbt/Eurosleeve-11-scaled-cebef959.jpg",
        "/static/img/mbt/Eurosleeve-10-scaled-fd8f7247.jpg",
        "/static/img/mbt/Eurosleeve-9-scaled-9070a8d2.jpg",
        "/static/img/mbt/Eurosleeve-8-scaled-f259de88.jpg",
        "/static/img/mbt/Eurosleeve-7-scaled-2e508c07.jpg",
        "/static/img/mbt/Eurosleeve-6-scaled-73fe0a94.jpg",
        "/static/img/mbt/Eurosleeve-5-scaled-bc3730ed.jpg",
        "/static/img/mbt/Eurosleeve-3-scaled-d1365013.jpg",
        "/static/img/mbt/Eurosleeve-2-scaled-c2ae0cee.jpg"
    ],
    "hero": "/static/img/mbt/Eurosleeve-12-scaled-a4ea9500.jpg",
    "latitude": 50.3461723,
    "longitude": 18.8076197,
    "order": 6,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Hall area: 2,333.43 m²\nSocial and office area: 449.93 m²\nNetworks and installations for the needs of the project\nSite development\nStructure:\nHall structure with precast reinforced concrete columns\nSteel roof structure of the hall\nFaçade made of sandwich panels\nRoof covering with PIR insulation and PVC membrane\nMixed structure of the office building (masonry, reinforced concrete floors and slab)",
        "cs": "Plocha haly: 2 333,43 m²\nPlocha sociálně-kancelářské části: 449,93 m²\nSítě a instalace pro potřeby realizované investice\nKrajinářské úpravy pozemku\nKonstrukce:\nKonstrukce haly s prefabrikovanými železobetonovými sloupy\nOcelová konstrukce střechy haly\nFasáda ze sendvičových panelů\nStřešní krytina s izolací z PIR a membránou z PVC\nSmíšená konstrukce kancelářské budovy (zděná, stropy a železobetonová deska)",
        "sk": "Plocha haly: 2 333,43 m²\nPlocha sociálno-kancelárskej časti: 449,93 m²\nSiete a inštalácie pre potreby realizovanej investície\nKrajinné úpravy pozemku\nKonštrukcia:\nKonštrukcia haly s prefabrikovanými železobetónovými stĺpmi\nOceľová konštrukcia strechy haly\nFasáda zo sendvičových panelov\nStrešná krytina s izoláciou z PIR a membránou z PVC\nZmiešaná konštrukcia kancelárskej budovy (murovaná, stropy a železobetónová doska)",
        "de": "Hallenfläche: 2.333,43 m²\nSozial- und Bürofläche: 449,93 m²\nNetze und Installationen für die Anforderungen der Investition\nFreiflächengestaltung\nKonstruktion:\nHallenkonstruktion mit Stahlbeton-Fertigteilstützen\nStahldachkonstruktion der Halle\nFassade aus Sandwichpaneelen\nDacheindeckung mit PIR-Dämmung und PVC-Membran\nGemischte Konstruktion des Bürogebäudes (Mauerwerk, Stahlbetondecken und -platte)",
        "hu": "Csarnok területe: 2 333,43 m²\nSzociális-irodai rész területe: 449,93 m²\nHálózatok és installációk a megvalósított beruházás igényei szerint\nTelekrendezés\nSzerkezet:\nA csarnok szerkezete előregyártott vasbeton oszlopokkal\nAcél tetőszerkezetű csarnok\nHomlokzat szendvicspanelekből\nTetőfedés PIR hőszigeteléssel és PVC membránnal\nAz irodaépület vegyes szerkezetű (falazott, vasbeton födémek és lemez)"
    }
},
    {
    "title": "Stokado Self-Storage Kraków",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "stokado-self-storage-krakow",
    "czas": "1 rok",
    "formula": "Zaprojektuj i wybuduj",
    "opis": "Specyfikacja Powierzchnia użytkowa (łącznie): ok. 4 631 m² , w tym: • Powierzchnia pod najem: 3 230,17 m² • Powierzchnia komunikacji: 1 296,71 m² • Powierzchnia pomieszczeń technicznych: 44,88 m² • Powierzchnia biurowo-recepcyjna: 59,28 m² Powierzchnia terenu: 4 150,00 m² Certyfikacja: BREEAM (Very Good) Układ budynku: Budynek na planie pięcioboku (zbliżony do prostokąta ze ścięciem), usytuowany w kierunku płd.-wsch. oraz płn.-zach. Dach płaski Charakterystyczne przeszklenie na elewacji biegnące przez cztery kondygnacje Infrastruktura techniczna: Instalacje OZE: Pompa ciepła, fotowoltaika Podziemny zbiornik przeciwpożarowy oraz zbiornik retencyjny na wody deszczowe Przebudowa istniejącej sieci wodociągowej Konstrukcja: Część podziemna: Płyta fundamentowa monolityczna, żelbetowa Część nadziemna: 5-kondygnacyjna, żelbetowa, w układzie słupowo-płytowym Stropy płaskie z lokalnymi pogrubieniami i belkami krawędziowymi Sztywność zapewniona przez monolityczny trzon komunikacyjny oraz tarczę żelbetową przy ścianie południowej Elewacja: Płyty warstwowe w układzie pionowym (kolor szary i pomarańczowy) Fragmenty wykończone tynkiem w kolorze antracytowym Zagospodarowanie terenu: Drogi wewnętrzne, chodniki i miejsca postojowe Oświetlenie zewnętrzne",
    "logo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/4070af82833b.webp",
    "gallery": [
        "/static/img/mbt/7-scaled-3dfac3ae.jpg",
        "/static/img/mbt/6-scaled-8c1b1f01.jpg",
        "/static/img/mbt/3-2-scaled-38947c85.jpg",
        "/static/img/mbt/1-scaled-f7ffa583.jpg"
    ],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/ed67bb1b2b03.webp",
    "latitude": 50.0621679,
    "longitude": 20.0025483,
    "order": 7,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Specification Usable area (total): approx. 4,631 m², including: • Rental area: 3,230.17 m² • Circulation area: 1,296.71 m² • Technical rooms area: 44.88 m² • Office and reception area: 59.28 m² Plot area: 4,150.00 m² Certification: BREEAM (Very Good) Building layout: A pentagonal building plan (close to a rectangle with a cut), oriented towards SE and NW. Flat roof. Characteristic glazing on the façade running through four storeys. Technical infrastructure: RES installations: Heat pump, photovoltaics. Underground fire water tank and rainwater retention tank. Reconstruction of the existing water supply network. Structure: Underground part: Monolithic reinforced concrete foundation slab. Above-ground part: 5-storey, reinforced concrete, in column-slab layout. Flat ceilings with local thickenings and edge beams. Stiffness provided by a monolithic communication core and a reinforced concrete diaphragm at the south wall. Façade: Sandwich panels in a vertical layout (grey and orange colour). Fragments finished with anthracite-coloured plaster. Land development: Internal roads, pavements and parking spaces. Outdoor lighting.",
        "cs": "Specifikace Užitková plocha (celkem): cca 4 631 m², z toho: • Plocha k pronájmu: 3 230,17 m² • Komunikační plocha: 1 296,71 m² • Plocha technických místností: 44,88 m² • Kancelářsko-recepční plocha: 59,28 m² Plocha pozemku: 4 150,00 m² Certifikace: BREEAM (Very Good) Dispozice budovy: Budova na pětiúhelníkovém půdorysu (blízký obdélníku se seříznutím), orientovaná směrem JV a SZ. Plochá střecha. Charakteristické prosklení na fasádě probíhající přes čtyři podlaží. Technická infrastruktura: Instalace OZE: Tepelné čerpadlo, fotovoltaika. Podzemní požární nádrž a retenční nádrž na dešťovou vodu. Přestavba stávající vodovodní sítě. Konstrukce: Podzemní část: Monolitická železobetonová základová deska. Nadzemní část: 5podlažní, železobetonová, ve sloupovo-deskovém uspořádání. Ploché stropy s lokálními zesíleními a krajními nosníky. Tuhost zajištěna monolitickým komunikačním jádrem a železobetonovou stěnou u jižní stěny. Fasáda: Sendvičové panely ve svislém uspořádání (šedá a oranžová barva). Fragmenty dokončené omítkou v antracitové barvě. Úprava terénu: Vnitřní komunikace, chodníky a parkovací stání. Venkovní osvětlení.",
        "sk": "Špecifikácia Úžitková plocha (spolu): cca 4 631 m², z toho: • Plocha na prenájom: 3 230,17 m² • Komunikačná plocha: 1 296,71 m² • Plocha technických miestností: 44,88 m² • Kancelársko-recepčná plocha: 59,28 m² Plocha pozemku: 4 150,00 m² Certifikácia: BREEAM (Very Good) Dispozícia budovy: Budova na päťuholníkovom pôdoryse (blízky obd�žniku so skosením), orientovaná smerom JV a SZ. Plochá strecha. Charakteristické presklenie na fasáde prebiehajúce cez štyri podlažia. Technická infraštruktúra: Inštalácie OZE: Tepelné čerpadlo, fotovoltika. Podzemný požiarny zásobník a retenčný zásobník na dažďovú vodu. Prestavba existujúcej vodovodnej siete. Konštrukcia: Podzemná časť: Monolitická železobetonová základová doska. Nadzemná časť: 5-podlažná, železobetonová, v stĺpovo-doskovom usporiadaní. Ploché stropy s lokálnymi zhrubnutiami a krajnými nosníkmi. Tuhosť zabezpečená monolitickým komunikačným jadrom a železobetónovou stenou pri južnej stene. Fasáda: Sendvičové panely vo zvislom usporiadaní (sivá a oranžová farba). Fragmenty dokončené omietkou v antracitovej farbe. Úprava terénu: Vnútorné komunikácie, chodníky a parkovacie miesta. Vonkajšie osvetlenie.",
        "de": "Spezifikation Nutzfläche (insgesamt): ca. 4.631 m², davon: • Mietfläche: 3.230,17 m² • Verkehrsfläche: 1.296,71 m² • Fläche der Technikräume: 44,88 m² • Büro- und Empfangsfläche: 59,28 m² Grundstücksfläche: 4.150,00 m² Zertifizierung: BREEAM (Very Good) Gebäudegrundriss: Gebäude auf fünfeckigem Grundriss (annahernd Rechteck mit Abschrägung), orientiert in Richtung SO und NW. Flachdach. Charakteristische Verglasung an der Fassade über vier Geschosse. Technische Infrastruktur: EE-Anlagen: Wärmepumpe, Photovoltaik. Unterirdischer Löschwassertank und Regenwasserrückhaltebecken. Umbau des bestehenden Wasserversorgungsnetzes. Konstruktion: Unterirdischer Teil: Monolithische Stahlbeton-Fundamentplatte. Oberirdischer Teil: 5-geschossig, Stahlbeton, in Stützen-Platten-Anordnung. Flache Decken mit lokalen Verstärkungen und Randträgern. Steifigkeit durch monolithischen Erschließungskern und Stahlbeton-Scheibe an der Südwand. Fassade: Sandwichpaneele in vertikaler Anordnung (grau und orange). Fragmente in anthrazitfarbenem Putz. Geländegestaltung: Innenstraßen, Gehwege und Parkplätze. Außenbeleuchtung.",
        "hu": "Specifikáció Hasznos alapterület (összesen): kb. 4 631 m², ebből: • Bérbe adható terület: 3 230,17 m² • Közlekedési terület: 1 296,71 m² • Műszaki helyiségek területe: 44,88 m² • Iroda és recepció területe: 59,28 m² Telek területe: 4 150,00 m² Tanúsítás: BREEAM (Very Good) Épület elrendezése: Ötszögletű alaprajzú épület (téglalaphoz közeli levágással), DK és ÉNy irányba tájolva. Lapos tető. Jellegzetes üvegezés a homlokzaton, négy szinten átívelve. Műszaki infrastruktúra: Megújuló energia berendezések: Hőszivattyú, napelemes rendszer. Földalatti tűzivíz-tartály és esővíz-visszatartó tartály. Meglévő vízellátó hálózat átépítése. Szerkezet: Földalatti rész: Monolit vasbeton alaplemez. Föld feletti rész: 5 szintes, vasbeton, oszlop-lemez elrendezésben. Lapos födémek helyi vastagításokkal és szélső gerendákkal. A merevséget monolitikus közlekedő mag és déli falnál lévő vasbeton fal biztosítja. Homlokzat: Szendvicspanelek függőleges elrendezésben (szürke és narancssárga szín). Töredékek antracit színű vakolattal. Telekrendezés: Belső utak, járdák és parkolóhelyek. Kültéri világítás."
    }
},
    {
    "title": "Fronton – Kraków",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "fronton-krakow",
    "czas": "1 rok",
    "formula": "Buduj",
    "opis": "Powierzchnia użytkowa:&nbsp; 1468,70 m² Wysokość hali:&nbsp; 8,72 m Kubatura hali:&nbsp; 10 244 m³ Część biurowa o&nbsp;powierzchni:&nbsp; 271,2 m² Parkingi i&nbsp;place manewrowe Zbiornik przeciwpożarowy (PPOŻ) Rozbudowa i&nbsp;budowa infrastruktury technicznej: Kanalizacja deszczowa ze zbiornikiem retencyjnym Kanalizacja sanitarna z&nbsp;oczyszczalnią ścieków Sieć grzewcza preizolowana Zagospodarowanie terenu wokół obiektu Konstrukcja: Posadowienie bezpośrednio na stopach fundamentowych, Konstrukcja hali wykonana w&nbsp;technologii prefabrykowanej żelbetowej, dźwigary dachowe sprężone Obudowa hali z&nbsp;płyt warstwowych z&nbsp;rdzeniem z&nbsp;wełny skalnej",
    "logo": "/static/img/mbt/Projekt-bez-nazwy-8-4d387861.png",
    "gallery": [
        "/static/img/mbt/Fronton-1-scaled-42981731.jpg",
        "/static/img/mbt/Fronton-2-scaled-de057284.jpg",
        "/static/img/mbt/Fronton-5-scaled-321d647a.jpg",
        "/static/img/mbt/Fronton-3-scaled-1437922a.jpg",
        "/static/img/mbt/Fronton-4-scaled-d63c339b.jpg"
    ],
    "hero": "/static/img/mbt/Fronton-1-scaled-42981731.jpg",
    "latitude": 50.075889,
    "longitude": 19.9411511,
    "order": 8,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Usable area: 1,468.70 m²\nHall height: 8.72 m\nHall volume: 10,244 m³\nOffice area of: 271.2 m²\nParking and manoeuvring areas\nFire-water tank (PPOŻ)\nExtension and construction of technical infrastructure:\nStormwater drainage with retention tank\nSanitary sewerage with wastewater treatment plant\nPre-insulated heating network\nLandscaping of the area around the building\nStructure:\nDirect foundation on pad footings,\nHall structure made using precast reinforced concrete technology, prestressed roof beams\nHall cladding made of sandwich panels with a rock-wool core",
        "cs": "Užitková plocha: 1 468,70 m²\nVýška haly: 8,72 m\nObjem haly: 10 244 m³\nKancelářská část o ploše: 271,2 m²\nParkoviště a manipulační plochy\nPožární nádrž (PPOŽ)\nRozšíření a výstavba technické infrastruktury:\nDešťová kanalizace s retenční nádrží\nSanitární kanalizace s čistírnou odpadních vod\nPředizolovaná tepelná síť\nKrajinářské úpravy okolí objektu\nKonstrukce:\nPřímé založení na patkových základech,\nKonstrukce haly provedena v prefabrikované železobetonové technologii, střešní vazníky předpjaté\nOpláštění haly ze sendvičových panelů s jádrem ze skalní vlny",
        "sk": "Úžitková plocha: 1 468,70 m²\nVýška haly: 8,72 m\nObjem haly: 10 244 m³\nKancelárska časť s plochou: 271,2 m²\nParkoviská a manipulačné plochy\nPožiarna nádrž (PPOŽ)\nRozšírenie a výstavba technickej infraštruktúry:\nDažďová kanalizácia s retenčnou nádržou\nSanitárna kanalizácia s čistiarňou odpadových vôd\nPreizolovaná tepelná sieť\nKrajinné úpravy okolia objektu\nKonštrukcia:\nPriame založenie na pätkových základoch,\nKonštrukcia haly vyhotovená v prefabrikovanej železobetónovej technológii, strešné väzníky predpäté\nOpláštenie haly zo sendvičových panelov s jadrom zo skalnej vlny",
        "de": "Nutzfläche: 1.468,70 m²\nHallenhöhe: 8,72 m\nHallen-Volumen: 10.244 m³\nBürofläche von: 271,2 m²\nParkplätze und Manövrierflächen\nLöschwassertank (PPOŻ)\nErweiterung und Bau der technischen Infrastruktur:\nRegenwasserkanalisation mit Rückhaltebecken\nSchmutzwasserkanalisation mit Kläranlage\nVorgedämmtes Fernwärmenetz\nGestaltung der Außenanlagen rund um das Gebäude\nKonstruktion:\nDirekte Gründung auf Einzelfundamenten,\nHallenkonstruktion in Stahlbeton-Fertigteilbauweise, vorgespannte Dachbinder\nHallenverkleidung aus Sandwichpaneelen mit Kern aus Steinwolle",
        "hu": "Hasznos alapterület: 1 468,70 m²\nCsarnokmagasság: 8,72 m\nCsarnok térfogata: 10 244 m³\nIrodai rész alapterülete: 271,2 m²\nParkolók és manőverező területek\nTűzivíztározó (PPOŻ)\nA műszaki infrastruktúra bővítése és építése:\nCsapadékvíz-csatorna visszatartó tározóval\nSzennyvíz-csatorna szennyvíztisztítóval\nElőszigetelt távhőhálózat\nAz épület környezetének rendezése\nSzerkezet:\nKözvetlen alapozás pontalapokon,\nA csarnok szerkezete előregyártott vasbeton technológiával készült, feszített tetőgerendák\nA csarnok burkolata kőzetgyapot magos szendvicspanelekből"
    }
},
    {
    "title": "Browar Zamkowy - Racibórz",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "browar-zamkowy-raciborz",
    "czas": "8 miesięcy",
    "formula": "Zaprojektuj-wybuduj",
    "opis": "Hala magazynowa w konstrukcji stalowej Obudowa z płyt warstwowych Powierzchnia posadzki: około 400,0 m² Posadowienie bezpośrednie z lokalną wymianą gruntu",
    "logo": "/static/img/mbt/logo-browar-3708c41b.jpg",
    "gallery": [
        "/static/img/mbt/mbt-browar-raciborz-8-03eeadf7.jpg",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/23f653996b58.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/942c1ffca3a1.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/6097dd073ebc.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/90a36e61fa56.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/b8ef1178df1c.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/830528646291.webp"
    ],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/7de95267e6b8.webp",
    "latitude": 50.0965337,
    "longitude": 18.2200745,
    "order": 9,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Warehouse hall in steel structure\nCladding made of sandwich panels\nFloor area: approximately 400.0 m²\nDirect foundation with localised soil replacement",
        "cs": "Skladová hala v ocelové konstrukci\nOpláštění ze sendvičových panelů\nPlocha podlahy: přibližně 400,0 m²\nPřímé založení s lokální výměnou zeminy",
        "sk": "Skladová hala v oceľovej konštrukcii\nOpláštenie zo sendvičových panelov\nPlocha podlahy: približne 400,0 m²\nPriame založenie s lokálnou výmenou zeminy",
        "de": "Lagerhalle in Stahlkonstruktion\nVerkleidung aus Sandwichpaneelen\nBodenfläche: ca. 400,0 m²\nDirekte Gründung mit lokalem Bodenaustausch",
        "hu": "Raktárcsarnok acélszerkezettel\nBurkolat szendvicspanelekből\nPadlófelület: kb. 400,0 m²\nKözvetlen alapozás helyi talajcserével"
    }
},
    {
    "title": "Stokado Self-Storage Warszawa Bemowo",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "stokado-self-storage-warszawa-bemowo",
    "czas": "13 miesięcy",
    "formula": "Buduj",
    "opis": "Specyfikacja Powierzchnia użytkowa: 6818,21 m² Powierzchnia terenu: 9142,00 m² Certyfikacja: BREEAM (Very Good) Układ budynku: 3 kondygnacje naziemne oraz podpiwniczenie, budynek kryty dachem płaskim Przeznaczenie i zagospodarowanie terenu: Obiekt usługowy typu self-storage (wynajem powierzchni do przechowywania dla klientów indywidualnych) Działalność wspierająca nowoczesną zabudowę wielorodzinną (dodatkowa przestrzeń magazynowa dla mieszkańców osiedli) Konstrukcja: Konstrukcja żelbetowa, słupowa Sztywność przestrzenna zapewniona przez trzony żelbetowe klatek schodowych oraz szachty wind ze ścianami ogniowymi Elewacja: Zasadnicza część elewacji wykonana z płyt warstwowych, z wypełnieniem z wełny mineralnej Systemowe obróbki, uszczelnienia i elementy montażowe",
    "logo": "/static/img/mbt/logo-stokado-CMYK.ai_01-scaled-a32efdb4.jpg",
    "gallery": [
        "/static/img/mbt/DJI_0174-scaled-5106e265.jpeg",
        "/static/img/mbt/DSC03626-scaled-6f5bda4e.jpeg",
        "/static/img/mbt/DSC03730-scaled-ee7d1094.jpeg",
        "/static/img/mbt/DSC03980-scaled-ea8b4933.jpeg",
        "/static/img/mbt/DSC03738-scaled-c238f3f3.jpeg",
        "/static/img/mbt/DJI_0181-1-scaled-b366f7fb.jpeg",
        "/static/img/mbt/DSC03726-scaled-04284a3e.jpeg"
    ],
    "hero": "/static/img/mbt/DJI_0174-scaled-5106e265.jpeg",
    "latitude": 52.2177584,
    "longitude": 20.895744,
    "order": 11,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Specification\nUsable area: 6,818.21 m²\nLand area: 9,142.00 m²\nCertification: BREEAM (Very Good)\nBuilding layout: 3 above-ground storeys plus a basement, building covered by a flat roof\nPurpose and site development:\nService facility of the self-storage type (rental of storage space to individual customers)\nOperations supporting modern multi-family housing development (additional storage space for residents of the estates)\nStructure:\nReinforced concrete column structure\nSpatial stiffness provided by reinforced concrete stairwell cores and lift shafts with fire-rated walls\nFaçade:\nMain part of the façade made of sandwich panels with mineral wool core\nSystem flashings, sealants and assembly components",
        "cs": "Specifikace\nUžitková plocha: 6 818,21 m²\nPlocha pozemku: 9 142,00 m²\nCertifikace: BREEAM (Very Good)\nDispozice budovy: 3 nadzemní podlaží a podsklepení, budova krytá plochou střechou\nUrčení a využití pozemku:\nSlužební objekt typu self-storage (pronájem skladovacích prostor individuálním zákazníkům)\nČinnost podporující moderní vícepodlažní bytovou výstavbu (dodatečný skladovací prostor pro obyvatele sídlišť)\nKonstrukce:\nŽelezobetonová sloupová konstrukce\nProstorová tuhost zajištěna železobetonovými jádry schodišť a šachtami výtahů s požárně odolnými stěnami\nFasáda:\nHlavní část fasády provedena ze sendvičových panelů s výplní z minerální vlny\nSystémové oplechování, těsnění a montážní prvky",
        "sk": "Špecifikácia\nÚžitková plocha: 6 818,21 m²\nPlocha pozemku: 9 142,00 m²\nCertifikácia: BREEAM (Very Good)\nDispozícia budovy: 3 nadzemné podlažia a podpivničenie, budova krytá plochou strechou\nUrčenie a využitie pozemku:\nSlužobný objekt typu self-storage (prenájom skladovacích priestorov individuálnym zákazníkom)\nČinnosť podporujúca modernú viacpodlažnú bytovú výstavbu (dodatočný skladovací priestor pre obyvateľov sídlisk)\nKonštrukcia:\nŽelezobetónová stĺpová konštrukcia\nPriestorová tuhosť zabezpečená železobetónovými jadrami schodísk a šachtami výťahov s požiarne odolnými stenami\nFasáda:\nHlavná časť fasády vyhotovená zo sendvičových panelov s výplňou z minerálnej vlny\nSystémové oplechovanie, tesnenia a montážne prvky",
        "de": "Spezifikation\nNutzfläche: 6.818,21 m²\nGrundstücksfläche: 9.142,00 m²\nZertifizierung: BREEAM (Very Good)\nGebäudestruktur: 3 Obergeschosse sowie ein Untergeschoss, Flachdach\nNutzung und Erschließung:\nGewerbliche Anlage vom Typ Self-Storage (Vermietung von Lagerflächen an Privatkunden)\nUnterstützung des modernen Geschosswohnungsbaus (zusätzliche Lagerfläche für die Bewohner der Siedlungen)\nKonstruktion:\nStützenbauweise in Stahlbeton\nRäumliche Steifigkeit durch Stahlbeton-Treppenhauskerne und Aufzugsschächte mit Brandwänden\nFassade:\nHauptteil der Fassade aus Sandwichpaneelen mit Mineralwollkern\nSystem-Verblechungen, Dichtungen und Montageelemente",
        "hu": "Specifikáció\nHasznos alapterület: 6 818,21 m²\nTelek területe: 9 142,00 m²\nTanúsítás: BREEAM (Very Good)\nÉpület elrendezése: 3 föld feletti szint és pinceszint, lapostetős épület\nRendeltetés és telekhasználat:\nÖnkiszolgáló raktár (self-storage) típusú szolgáltató létesítmény (tárolóterület bérbeadása magánszemélyeknek)\nA modern többlakásos lakóépületeket kiegészítő tevékenység (kiegészítő tárolóterület a lakótelepi lakók számára)\nSzerkezet:\nVasbeton pillérvázas szerkezet\nTérbeli merevséget a vasbeton lépcsőház-magok és a tűzgátló falú liftaknák biztosítják\nHomlokzat:\nA homlokzat fő része ásványgyapot kitöltésű szendvicspanelekből készül\nRendszer-illesztések, tömítések és szerelési elemek"
    }
},
    {
    "title": "Huber + Suhner – Pisary",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "huber-suhner-pisary",
    "czas": "14 miesięcy",
    "formula": "Buduj",
    "opis": "Powierzchnia użytkowa: 3002 m² Wysokość hali: 7,5 m Kubatura hali: 19 300 m³ Obciążenie ogniowe, nie przekraczające 500MJ/m² Dwukondygnacyjny budynek biurowy o powierzchni 600m² Parkingi i place manewrowe Zagospodarowanie terenu wokół obiektu Konstrukcja: posadowienie bezpośrednio na płycie fundamentowej, żelbetowe w technologii betonu wodoszczelnego konstrukcja nośna obiektu „mieszana” (prefabrykowane słupy betonowe, konstrukcja dachu stalowa)",
    "logo": "/static/img/mbt/HS_Logo_blue-scaled-c772a155.jpg",
    "gallery": [
        "/static/img/mbt/Huber-6-scaled-b00b8b23.jpg",
        "/static/img/mbt/Huber-5-scaled-45d0b018.jpg",
        "/static/img/mbt/Huber-4-scaled-9c017841.jpg",
        "/static/img/mbt/Huber-3-scaled-9bd9b813.jpg",
        "/static/img/mbt/Huber-2-scaled-0183eebd.jpg",
        "/static/img/mbt/Huber-1-scaled-1d0326ab.jpg",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/8d8dcfd2b3c9.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/170c3c473338.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/902daf2e9102.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/9f53bfa208ce.webp"
    ],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/1d2cd76b899f.webp",
    "latitude": 50.1304881,
    "longitude": 19.685079,
    "order": 12,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Usable area: 3,002 m² Hall height: 7.5 m Volume: 19,300 m³ Fire load not exceeding 500 MJ/m² Two-storey office building with an area of 600 m² Parking lots and manoeuvring areas Land development around the facility Structure: foundation directly on a foundation slab, reinforced concrete in waterproof concrete technology; load-bearing structure of the facility is \"mixed\" (prefabricated concrete columns, steel roof structure)",
        "cs": "Užitková plocha: 3002 m² Výška haly: 7,5 m Objem haly: 19 300 m³ Požární zatížení nepřekračující 500 MJ/m² Dvoupodlažní kancelářská budova o ploše 600 m² Parkoviště a manévrovací plochy Úprava terénu kolem objektu Konstrukce: založení přímo na základové desce, železobetonová v technologii vodostavebního betonu; nosná konstrukce objektu „smíšená\" (prefabrikované betonové sloupy, ocelová konstrukce střechy)",
        "sk": "Úžitková plocha: 3002 m² Výška haly: 7,5 m Objem haly: 19 300 m³ Požiarne zaťaženie neprekračujúce 500 MJ/m² Dvojpodlažná kancelárska budova s plochou 600 m² Parkoviská a manévrovacie plochy Úprava terénu okolo objektu Konštrukcia: založenie priamo na základovej doske, železobetónová v technológii vodostavebného betónu; nosná konštrukcia objektu „zmiešaná\" (prefabrikované betónové stĺpy, oceľová konštrukcia strechy)",
        "de": "Nutzfläche: 3.002 m² Hallenhöhe: 7,5 m Volumen: 19.300 m³ Brandlast, die 500 MJ/m² nicht überschreitet Zweigeschossiges Bürogebäude mit einer Fläche von 600 m² Parkplätze und Rangierflächen Gestaltung des Geländes um das Objekt Konstruktion: Gründung direkt auf einer Fundamentplatte, Stahlbeton in WU-Beton-Technologie; Tragkonstruktion des Objekts „gemischt\" (vorgefertigte Betonstützen, Stahltragwerk des Daches)",
        "hu": "Hasznos alapterület: 3002 m² Csarnok magassága: 7,5 m Térfogat: 19 300 m³ Tűzterhelés, nem haladja meg az 500 MJ/m²-t Kétszintes irodaépület 600 m² alapterülettel Parkolók és manőverezési területek A telek rendezése az objektum körül Szerkezet: alapozás közvetlenül alaplemezre, vasbeton vízzáró beton technológiával; az objektum teherhordó szerkezete „vegyes\" (előregyártott betonoszlopok, acél tetőszerkezet)"
    }
},
    {
    "title": "Euronova – Kokotów, gm. Wieliczka",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "euronova-kokotow-gm-wieliczka",
    "czas": "10 miesięcy",
    "formula": "Zaprojektuj-wybuduj",
    "opis": "Konstrukcja: budynek produkcyjny w technologii prefabrykowanej budynek biurowy wykonany w pełnym żelbecie Elewacja: płyty warstwowe na części przemysłowej technologia lekka-mokra na części biurowej Dach: hala produkcyjna: kratownice, blacha trapezowa, izolacja, membrana część biurowa: klasyczny stropodach, izolacja, membrana Wnętrza: industrialne, surowe wykończenia, odsłonięte instalacje, beton na stropach Ogrzewanie: technologia nadmuchowa Podłogi: gres oraz wykładzina w wybranych przestrzeniach",
    "logo": "/static/img/mbt/eu_logo-scaled-9014591f.jpg",
    "gallery": [
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/eeec5134af66.webp",
        "/static/img/mbt/jpg-4-ecfca2a2.jpg",
        "/static/img/mbt/jpg-16-111-17362cd9.jpg",
        "/static/img/mbt/jpg-55-453122db.jpg"
    ],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/366af5fc0ffe.webp",
    "latitude": 50.0235169,
    "longitude": 20.0861011,
    "order": 13,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Structure: production building in precast technology; office building executed entirely in reinforced concrete. Façade: sandwich panels on the industrial section; lightweight-wet technology on the office section. Roof: production hall: trusses, trapezoidal sheet, insulation, membrane; office section: classic flat roof, insulation, membrane. Interiors: industrial, raw finishes, exposed installations, concrete on ceilings. Heating: blown-air technology. Floors: stoneware tiles and carpet in selected areas.",
        "cs": "Konstrukce: výrobní budova v prefabrikované technologii; kancelářská budova provedena v plném železobetonu. Fasáda: sendvičové panely v průmyslové části; lehká mokrá technologie v kancelářské části. Střecha: výrobní hala: příhradové vazníky, trapézový plech, izolace, membrána; kancelářská část: klasický plochý střešní plášť, izolace, membrána. Interiéry: industriální, surové povrchové úpravy, odhalené instalace, beton na stropech. Vytápění: technologie teplovzdušného ofukování. Podlahy: slinutá dlažba a koberce ve vybraných prostorech.",
        "sk": "Konštrukcia: výrobná budova v prefabrikovanej technológii; kancelárska budova realizovaná v plnom železobetóne. Fasáda: sendvičové panely v priemyselnej časti; ľahká mokrá technológia v kancelárskej časti. Strecha: výrobná hala: priehradové väzníky, trapézový plech, izolácia, membrána; kancelárska časť: klasický plochý strešný plášť, izolácia, membrána. Interiéry: industriálne, surové povrchové úpravy, odhalené inštalácie, betón na stropoch. Vykurovanie: technológia teplovzdušného fúkania. Podlahy: slinutá dlažba a koberce vo vybraných priestoroch.",
        "de": "Konstruktion: Produktionsgebäude in Fertigteil-Bauweise; Bürogebäude in Massiv-Stahlbetonbauweise. Fassade: Sandwichpaneele im industriellen Teil; Leichtbau-Nassputz-Technologie im Büroteil. Dach: Produktionshalle: Fachwerkbinder, Trapezblech, Dämmung, Membran; Büroteil: klassisches Flachdach, Dämmung, Membran. Innenräume: industriell, rohe Oberflächen, sichtbare Installationen, Beton an den Decken. Heizung: Luftumwälztechnik. Böden: Feinsteinzeug und Teppichboden in ausgewählten Bereichen.",
        "hu": "Szerkezet: előre gyártott technológiájú gyártócsarnok; teljes vasbeton szerkezetű irodaház. Homlokzat: szendvicspanelek az ipari részen; könnyű-nedves technológia az irodai részen. Tető: gyártócsarnok: rácsos tartók, trapézlemez, szigetelés, membrán; irodai rész: klasszikus lapostető, szigetelés, membrán. Belső terek: ipari, nyers felületek, látható telepítések, beton a födémeken. Fűtés: befúvásos technológia. Padlók: kőporcelán és szőnyegpadló a kiválasztott terekben."
    }
},
    {
    "title": "Euro-Trade - Modlnica",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "euro-trade-w-modlnicy",
    "czas": "8 miesięcy",
    "formula": "Generalny Wykonawca",
    "opis": "Powierzchnia magazynowa: 6 650 m² Powierzchnia socjalno-biurowa: 550 m² Układ komunikacyjny: 4 718 m² Posadowienie bezpośrednie na gruncie stabilizowanym cementem Konstrukcja hali mieszana (słupy żelbetowe, prefabrykowane; dźwigary i płatwie stalowe) Obudowa ścian z płyty warstwowej",
    "logo": "/static/img/mbt/ET_logo-ada4c441.png",
    "gallery": [
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/8e7a85eb7be6.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/1ce92fe371a1.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/c1005bfea89f.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/0f4fa456dc0c.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/43e712db1c79.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/754871bb9a0c.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/b391eefdff20.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/dbd4bfe96548.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/f9898b65dde6.webp"
    ],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/0c4f48e81c2e.webp",
    "latitude": 50.1202424,
    "longitude": 19.8737154,
    "order": 14,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Warehouse area: 6 650 m². Welfare and office area: 550 m². Transport layout: 4 718 m². Direct foundation on cement-stabilised ground. Mixed hall structure (precast reinforced concrete columns; steel beams and purlins). Wall cladding with sandwich panels.",
        "cs": "Skladová plocha: 6 650 m². Sociální a kancelářská plocha: 550 m². Dopravní řešení: 4 718 m². Přímé založení na zemině stabilizované cementem. Smíšená konstrukce haly (železobetonové prefabrikované sloupy; ocelové vaznice a průvlaky). Plášť stěn ze sendvičových panelů.",
        "sk": "Skladová plocha: 6 650 m². Sociálna a kancelárska plocha: 550 m². Dopravné riešenie: 4 718 m². Priame založenie na podloží stabilizovanom cementom. Zmiešaná konštrukcia haly (železobetónové prefabrikované stĺpy; oceľové nosníky a väznice). Plášť stien zo sendvičových panelov.",
        "de": "Lagerfläche: 6 650 m². Sozial- und Bürofläche: 550 m². Verkehrserschließung: 4 718 m². Direkte Gründung auf zementstabilisiertem Boden. Gemischte Hallenkonstruktion (Stahlbeton-Fertigteilstützen; Stahlbinder und Pfetten). Wandverkleidung aus Sandwichpaneelen.",
        "hu": "Raktárterület: 6 650 m². Szociális és irodai terület: 550 m². Közlekedési kialakítás: 4 718 m². Közvetlen alapozás cementtel stabilizált talajon. Vegyes csarnokszerkezet (előre gyártott vasbeton oszlopok; acél főtartók és szelemenek). Falburkolat szendvicspanelekből."
    }
},
    {
    "title": "Browar Lech - Poznań",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "kompania-piwowarska",
    "czas": "",
    "formula": "Wybuduj",
    "opis": "Budowa Magazynu Aromatów z infrastrukturą techniczną i drogową na terenie Lech Browary Wielkopolski dla Kompanii Piwowarskiej.\r\n\r\n•  Hala wyposażona w zaawansowane instalacje sanitarne, elektryczne i techniczne \r\n•  Zagospodarowanie terenu wraz z przebudową istniejącej infrastruktury \r\n•  Praca w wysokim reżimie BHP na terenie działającego zakładu przemysłowego \r\n•  Powierzchnia zabudowy budynku 722 m2",
    "logo": "/static/img/mbt/realizacje-kompania-piwowarska-logo-c686aab0.png",
    "gallery": [],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/95014a152c55.webp",
    "latitude": 52.3853423,
    "longitude": 16.9971062,
    "order": 15,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Construction of the Aromatics Warehouse with technical and road infrastructure on the premises of Lech Browary Wielkopolski for Kompania Piwowarska.\n\n•  Hall equipped with advanced sanitary, electrical and technical installations \n•  Site development including reconstruction of the existing infrastructure \n•  Work carried out under strict H&S standards on the premises of an operating industrial facility \n•  Building area: 722 m²",
        "cs": "Výstavba Skladu Aromatů s technickou a dopravní infrastrukturou v areálu Lech Browary Wielkopolski pro Kompania Piwowarska.\n\n•  Hala vybavená pokročilými sanitárními, elektrickými a technickými instalacemi \n•  Úprava území včetně přestavby stávající infrastruktury \n•  Práce probíhající ve vysokém režimu BOZP v areálu fungujícího průmyslového závodu \n•  Zastavěná plocha budovy 722 m²",
        "sk": "Výstavba Skladu Aromatov s technickou a dopravnou infraštruktúrou v areáli Lech Browary Wielkopolski pre Kompania Piwowarska.\n\n•  Hala vybavená pokročilými sanitárnymi, elektrickými a technickými inštaláciami \n•  Úprava územia vrátane prestavby existujúcej infraštruktúry \n•  Práca vo vysokom režime BOZP v areáli fungujúceho priemyselného závodu \n•  Zastavaná plocha budovy 722 m²",
        "de": "Bau des Aromen-Lagers mit technischer und Straßeninfrastruktur auf dem Gelände von Lech Browary Wielkopolski für Kompania Piwowarska.\n\n•  Halle mit fortschrittlichen Sanitär-, Elektro- und technischen Installationen \n•  Geländegestaltung einschließlich Umbau der bestehenden Infrastruktur \n•  Arbeiten unter strengen Arbeitsschutzauflagen auf dem Gelände eines in Betrieb befindlichen Industrieunternehmens \n•  Grundstücksfläche des Gebäudes: 722 m²",
        "hu": "Az Aromaraktár építése műszaki és közlekedési infrastruktúrával a Lech Browary Wielkopolski területén, a Kompania Piwowarska számára.\n\n•  Fejlett higiéniai, elektromos és műszaki telepítésekkel felszerelt csarnok \n•  Területrendezés a meglévő infrastruktúra átépítésével együtt \n•  Munkavégzés szigorú munkavédelmi előírások mellett egy működő ipari üzem területén \n•  Beépített terület: 722 m²"
    }
},
    {
    "title": "InPost - Legnica",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "in-post-w-legnicy",
    "czas": "6 miesięcy",
    "formula": "Obiekt na posadowieniu bezpośrednim",
    "opis": "Powierzchnia produkcyjno-magazynowa: 5331,79 m 2 Powierzchnia utwardzeń-układ komunikacyjny: około 18000 m 2 Konstrukcja: Obiekt na posadowieniu bezpośrednim Konstrukcja mieszana żelbetowo-stalowa Obudowa w technologii płyty warstwowej Dach w konstrukcji stalowej z pokryciem wełną mineralna i membraną PVC Obiekt wykończony zgodnie ze standardem Użytkownika i oddany do użytkowania",
    "logo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/7ab29f71ec4a.svg",
    "gallery": [
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/5f70be1acf06.webp",
        "/static/img/mbt/IMG_20220722_102326-scaled-1-fdde92f8.jpg",
        "/static/img/mbt/IMG_20220722_102111-scaled-1-ceffec28.jpg",
        "/static/img/mbt/IMG_20220406_131518-scaled-1-84d560cd.jpg"
    ],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/945dd3d54da9.webp",
    "latitude": 51.1731582,
    "longitude": 16.1811487,
    "order": 16,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Production and warehouse area: 5,331.79 m². Hardstand area – transport layout: approx. 18 000 m². Structure: Building on a direct foundation. Mixed reinforced concrete and steel structure. Sandwich panel envelope. Steel roof structure covered with mineral wool and PVC membrane. Building finished to the User's standard and commissioned.",
        "cs": "Výrobně-skladovací plocha: 5 331,79 m². Plocha zpevnění – dopravní řešení: přibližně 18 000 m². Konstrukce: Objekt na přímém založení. Smíšená železobeton-ocelová konstrukce. Plášť v technologii sendvičových panelů. Střecha v ocelové konstrukci s krytinou z minerální vlny a PVC membrány. Objekt dokončený dle standardu Uživatele a předaný do užívání.",
        "sk": "Výrobná a skladová plocha: 5 331,79 m². Plocha spevnenia – dopravné riešenie: približne 18 000 m². Konštrukcia: Objekt na priamom založení. Zmiešaná železobetónovo-oceľová konštrukcia. Plášť v technológii sendvičových panelov. Strecha v oceľovej konštrukcii s krytinou z minerálnej vlny a PVC membrány. Objekt dokončený podľa štandardu Užívateľa a odovzdaný do užívania.",
        "de": "Produktions- und Lagerfläche: 5.331,79 m². Befestigte Fläche – Verkehrserschließung: ca. 18 000 m². Konstruktion: Gebäude auf direkter Gründung. Gemischte Stahlbeton-Stahl-Konstruktion. Sandwichpaneel-Hülle. Stahldachkonstruktion mit Mineralwolldämmung und PVC-Membran. Gebäude nach dem Standard des Nutzers fertiggestellt und in Betrieb genommen.",
        "hu": "Gyártási és raktározási terület: 5 331,79 m². Burkolt felület – közlekedési kialakítás: kb. 18 000 m². Szerkezet: Az objektum közvetlen alapozású. Vegyes vasbeton-acél szerkezet. Szendvicspanel burkolat. Acél tetőszerkezet ásványgyapot és PVC membrán szigeteléssel. Az objektum a Használó szabványa szerint kivitelezve és átadva."
    }
},
    {
    "title": "Sutco - Katowice",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "sutco-katowice",
    "czas": "8 miesięcy",
    "formula": "Projektuj-wybuduj",
    "opis": "Powierzchnia produkcyjno-magazynowa: 3800m² Hala wyposażona w 4 suwnice 8T Zagospodarowanie terenu wokół nowego obiektu Konstrukcja: Obiekt na posadowieniu bezpośrednim Konstrukcja stalowa ścian i dachu Obudowa w technologii płyty warstwowej Dach w konstrukcji stalowej z pokryciem płytami PIR i membraną PVC Obiekt przystosowany do wymagań produkcji konstrukcji stalowych",
    "logo": "/static/img/mbt/realizacje-sutco-logo-a5df22a7.png",
    "gallery": [
        "/static/img/mbt/jpg_22-1-1-3fa214ab.jpg",
        "/static/img/mbt/img_-14-1-1-7d2214b5.jpg",
        "/static/img/mbt/img_-1-1-1-2ad7c229.jpg",
        "/static/img/mbt/img_-1-of-3-1-3-e5f05c96.jpg",
        "/static/img/mbt/jpg-2-of-3-1-1-2bd95761.jpg",
        "/static/img/mbt/jpg-3-of-3-1-1-393a147b.jpg"
    ],
    "hero": "/static/img/mbt/jpg_22-1-1-3fa214ab.jpg",
    "latitude": 50.2559561,
    "longitude": 19.0571593,
    "order": 17,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Production and warehouse area: 3 800 m². Hall equipped with 4 overhead cranes of 8 t. Site development around the new building. Structure: Building on a direct foundation. Steel structure of walls and roof. Sandwich panel envelope. Steel roof structure covered with PIR panels and PVC membrane. Building adapted to the requirements of steel structure production.",
        "cs": "Výrobně-skladovací plocha: 3 800 m². Hala vybavená 4 mostovými jeřáby o nosnosti 8 t. Úprava území v okolí nového objektu. Konstrukce: Objekt na přímém založení. Ocelová konstrukce stěn a střechy. Plášť v technologii sendvičových panelů. Střecha v ocelové konstrukci s krytinou z PIR panelů a PVC membrány. Objekt přizpůsobený požadavkům výroby ocelových konstrukcí.",
        "sk": "Výrobná a skladová plocha: 3 800 m². Hala vybavená 4 mostovými žeriavmi s nosnosťou 8 t. Úprava územia okolo nového objektu. Konštrukcia: Objekt na priamom založení. Oceľová konštrukcia stien a strechy. Plášť v technológii sendvičových panelov. Strecha v oceľovej konštrukcii s krytinou z PIR panelov a PVC membrány. Objekt prispôsobený požiadavkám výroby oceľových konštrukcií.",
        "de": "Produktions- und Lagerfläche: 3 800 m². Halle mit 4 Kranen zu je 8 t. Geländegestaltung rund um das neue Gebäude. Konstruktion: Gebäude auf direkter Gründung. Stahlkonstruktion der Wände und des Daches. Sandwichpaneel-Hülle. Stahldachkonstruktion mit PIR-Platten und PVC-Membran. Gebäude an die Anforderungen der Stahlbaufertigung angepasst.",
        "hu": "Gyártási és raktározási terület: 3 800 m². A csarnok 4 darab 8 tonnás daruval felszerelt. Az új objektum környékének tereprendezése. Szerkezet: Az objektum közvetlen alapozású. Falak és tető acélszerkezete. Szendvicspanel burkolat. Acél tetőszerkezet PIR panelekkel és PVC membránnal. Az objektum az acélszerkezet-gyártás követelményeihez igazítva."
    }
},
    {
    "title": "CanPack BSS LAB - Brzesk",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "canpack-bss-lab-brzesk",
    "czas": "8 miesięcy",
    "formula": "Generalny Wykonawca",
    "opis": "Powierzchnia użytkowa pomieszczeń laboratoryjnych i socjalnych: ok. 420,0 m² Rozbiórki ścian i instalacji Wykonanie nowej posadzki Wykonanie antresoli stalowej Wykonanie fundamentu pod prasę Roboty wykończeniowe Termomodernizacja dachu i elewacji Nowa stolarka okienna Wykonanie instalacji HVAC oraz elektrycznych",
    "logo": "/static/img/mbt/logo-canpack2-db627ab0.jpg",
    "gallery": [
        "/static/img/mbt/CANPACK-BSS-LAB-w-Brzesku-3-1-f34a5df7.jpg",
        "/static/img/mbt/CANPACK-BSS-LAB-w-Brzesku-2-1-13c84a96.jpg",
        "/static/img/mbt/CANPACK-BSS-LAB-w-Brzesku-1-1-ee4bd957.jpg"
    ],
    "hero": "/static/img/mbt/CANPACK-BSS-LAB-w-Brzesku-3-1-f34a5df7.jpg",
    "latitude": 49.9771894,
    "longitude": 20.6219206,
    "order": 18,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Usable area of laboratory and staff facilities: approx. 420.0 m²\nDemolition of walls and installations\nNew floor slab\nSteel mezzanine structure\nFoundation for the press\nFinishing works\nThermal modernisation of the roof and façade\nNew window joinery\nHVAC and electrical installations",
        "cs": "Užitková plocha laboratorních a sociálních místností: cca 420,0 m²\nDemolice stěn a instalací\nProvedení nové podlahy\nProvedení ocelové mezipatrové konstrukce\nProvedení základu pod lis\nDokončovací práce\nTepelná modernizace střechy a fasády\nNová okenní tesařská a zámečnická konstrukce\nProvedení HVAC a elektrických instalací",
        "sk": "Úžitková plocha laboratórnych a sociálnych priestorov: cca 420,0 m²\nDemolície stien a inštalácií\nVyhotovenie novej podlahy\nVyhotovenie oceľovej medziposchodovej konštrukcie\nVyhotovenie základu pod lis\nDokončovacie práce\nTepelná modernizácia strechy a fasády\nNové okenné konštrukcie\nVyhotovenie HVAC a elektrických inštalácií",
        "de": "Nutzfläche der Labor- und Sozialräume: ca. 420,0 m²\nAbriss von Wänden und Installationen\nHerstellung eines neuen Bodenbelags\nHerstellung einer Stahl-Zwischendecke\nHerstellung des Fundaments für die Presse\nAusbauarbeiten\nThermische Modernisierung von Dach und Fassade\nNeue Fensterelemente\nHerstellung von HVAC- und Elektroinstallationen",
        "hu": "Laboratóriumi és szociális helyiségek hasznos alapterülete: kb. 420,0 m²\nFalak és installációk bontása\nÚj padlóburkolat kivitelezése\nAcél félemeleti szint kivitelezése\nPrésalap kivitelezése\nBefejező munkák\nTető és homlokzat hőszigetelő korszerűsítése\nÚj nyílászárók\nHVAC és elektromos installációk kivitelezése"
    }
},
    {
    "title": "Canpack BSS Excellence Centre - Brzesk",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "Canpack-BSS-Excellence-Centre-Brzesk",
    "czas": "8 miesięcy",
    "formula": "Projektuj-wybuduj",
    "opis": "Powierzchnia użytkowa: około 2865 m²\r\nRoboty rozbiórkowe i wyburzeniowe\r\nDemontaż starych instalacji\r\nRoboty murarskie i konstrukcyjne\r\nKonstrukcja stalowa antresoli\r\nWykonanie nowej posadzki\r\nMontaż nowych instalacji sanitarnych i elektrycznych\r\nWymiana stolarki okiennej, bramowej i drzwiowej\r\nRoboty wykończeniowe\r\nTermomodernizacja dachu i elewacji\r\nZagospodarowanie terenów przyległych",
    "logo": "/static/img/mbt/logo-canpack2-db627ab0.jpg",
    "gallery": [
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/9ce3601c8ae7.webp"
    ],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/a36919918dd2.webp",
    "latitude": 49.9771894,
    "longitude": 20.6219206,
    "order": 19,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Usable area: approximately 2 865 m²\nDemolition works\nDismantling of old installations\nMasonry and structural works\nSteel structure of the mezzanine\nNew floor screed\nInstallation of new sanitary and electrical systems\nReplacement of windows, gates and doors\nFinishing works\nThermal upgrade of the roof and façade\nDevelopment of adjacent areas",
        "cs": "Užitková plocha: přibližně 2 865 m²\nDemolice a bourací práce\nDemontáž starých instalací\nZednické a konstrukční práce\nOcelová konstrukce mezipatra\nProvedení nové podlahy\nMontáž nových sanitárních a elektrických instalací\nVýměna oken, vrat a dveří\nDokončovací práce\nTepelná modernizace střechy a fasády\nÚprava přilehlých ploch",
        "sk": "Úžitková plocha: približne 2 865 m²\nBúracie práce\nDemontáž starých inštalácií\nMurovské a konštrukčné práce\nOceľová konštrukcia mezanínu\nRealizácia novej podlahy\nMontáž nových sanitárnych a elektrických inštalácií\nVýmena okien, brán a dverí\nDokončovacie práce\nTepelná modernizácia strechy a fasády\nÚprava priľahlých plôch",
        "de": "Nutzfläche: ca. 2 865 m²\nAbbrucharbeiten\nDemontage alter Installationen\nMauer- und Konstruktionsarbeiten\nStahlkonstruktion des Zwischengeschosses\nHerstellung des neuen Estrichs\nMontage neuer Sanitär- und Elektroinstallationen\nAustausch von Fenstern, Toren und Türen\nAusbauarbeiten\nThermische Sanierung von Dach und Fassade\nGestaltung der angrenzenden Flächen",
        "hu": "Hasznos alapterület: kb. 2 865 m²\nBontási munkálatok\nRégi telepítések leszerelése\nFalazó és szerkezeti munkák\nA félemelet acélszerkezete\nÚj padlóburkolat kivitelezése\nÚj higiéniai és elektromos telepítések szerelése\nAblakok, kapuk és ajtók cseréje\nBefejező munkák\nA tető és a homlokzat hőszigetelése\nA szomszédos területek rendezése"
    }
},
    {
    "title": "Epco - Bytom",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "p1704",
    "czas": "8 miesięcy",
    "formula": "Generalny Wykonawca",
    "opis": "Rozbudowa wymagająca zarówno rozbiórek obecnego układu drogowego, jak i elementów hali Prace wykonywane na czynnym zakładzie z zachowaniem obowiązujących standardów BHP Dobudowa do istniejącej hali z zachowaniem formy i kolorystyki obiektu istniejącego",
    "logo": "/static/img/mbt/Epcologo-7badc63b.png",
    "gallery": [],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/7d213c49a73d.webp",
    "latitude": 50.3847018,
    "longitude": 18.8759491,
    "order": 20,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Extension requiring demolition of the existing road layout as well as selected hall elements\nWorks carried out on an operating facility in compliance with applicable H&S standards\nExtension to the existing hall, matching the form and colour scheme of the existing building",
        "cs": "Rozšíření vyžadující jak demolice stávajícího dopravního uspořádání, tak i vybraných prvků haly\nPráce prováděné na provozovaném závodě při dodržení platných norem BOZP\nPřístavba ke stávající hale se zachováním tvaru a barevnosti stávajícího objektu",
        "sk": "Rozšírenie vyžadujúce ako demolície súčasného dopravného usporiadania, tak aj vybraných prvkov haly\nPráce vykonávané na prevádzkovanom závode pri dodržaní platných noriem BOZP\nPrístavba k jestvujúcej hale so zachovaním tvaru a farebnosti jestvujúceho objektu",
        "de": "Erweiterung mit erforderlichem Abriss der bestehenden Verkehrsführung sowie ausgewählter Hallenelemente\nArbeiten an einem in Betrieb befindlichen Werk unter Einhaltung der geltenden Arbeitsschutzstandards\nAnbau an die bestehende Halle unter Wahrung von Form und Farbgebung des bestehenden Objekts",
        "hu": "Bővítés, amely a meglévő úthálózat és a csarnok egyes elemeinek elbontását egyaránt megköveteli\nMunkavégzés üzemelő gyár területén a hatályos munkavédelmi előírások betartásával\nHozzáépítés a meglévő csarnokhoz a meglévő épület formájának és színvilágának megőrzésével"
    }
},
    {
    "title": "HERZ - Wieliczka",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "herz-wieliczka",
    "czas": "8 miesięcy",
    "formula": "Zaprojektuj-wybuduj",
    "opis": "Powierzchnia produkcyjno-magazynowa: 4 500 m2 Powierzchnia małej hali produkcyjnej: 500m2 Układ komunikacyjny: 2 500m2 Posadowienie bezpośrednie na gruncie rodzimym Konstrukcja hali w całości stalowa Obudowa hali z płyt warstwowych",
    "logo": "/static/img/mbt/2e7538dfbcb3865df6ea9a1138c99e1c-79db89e5.jpg",
    "gallery": [
        "/static/img/mbt/Herz-docel-2-1-scaled-1-04664ed6.jpg",
        "/static/img/mbt/Herz-docel-3-scaled-1-89b6538a.jpg"
    ],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/6dcb891fb91a.webp",
    "latitude": 49.9949198,
    "longitude": 20.0730015,
    "order": 21,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Production and warehouse area: 4,500 m²\nSmall production hall area: 500 m²\nTraffic layout: 2,500 m²\nDirect foundation on native soil\nFully steel structure of the hall\nWall cladding made of sandwich panels",
        "cs": "Výrobní a skladová plocha: 4 500 m²\nPlocha malé výrobní haly: 500 m²\nKomunikační uspořádání: 2 500 m²\nPřímé založení na rostlé zemině\nKonstrukce haly je kompletně ocelová\nOpláštění haly ze sendvičových panelů",
        "sk": "Výrobná a skladová plocha: 4 500 m²\nPlocha malej výrobnej haly: 500 m²\nKomunikačné usporiadanie: 2 500 m²\nPriame založenie na rastlom teréne\nKonštrukcia haly je celooková\nOpláštenie haly zo sendvičových panelov",
        "de": "Produktions- und Lagerfläche: 4.500 m²\nFläche der kleinen Produktionshalle: 500 m²\nVerkehrsfläche: 2.500 m²\nDirekte Gründung auf gewachsenem Boden\nHallenkonstruktion vollständig in Stahl\nHallenverkleidung aus Sandwichpaneelen",
        "hu": "Termelő és raktározási terület: 4 500 m²\nKis termelőcsarnok területe: 500 m²\nKözlekedési rendszer: 2 500 m²\nKözvetlen alapozás anyaföldön\nA csarnok szerkezete teljes egészében acél\nA csarnok burkolata szendvicspanelekből"
    }
},
    {
    "title": "ToTo - Głogoczów",
    "type": "realizacja-zrealizow",
    "status": "Zrealizowane",
    "slug": "toto-golgoczow",
    "czas": "9 miesięcy",
    "formula": "Generalny Wykonawca",
    "opis": "Powierzchnia magazynowa: 2 220 m² Powierzchnia socjalno-biurowa: 55 m² Układ komunikacyjny o powierzchni: 1 700 m² Posadowienie hali na płycie fundamentowej, wykonanej na gruncie stabilizowanym cementem Konstrukcja hali w całości stalowa Obudowa ścian i dachu z płyt warstwowych",
    "logo": "/static/img/mbt/toto_logo-611681aa.jpg",
    "gallery": [],
    "hero": "/static/img/mbt/realizacja-euronova.jpg",
    "latitude": 49.914,
    "longitude": 19.897,
    "order": 22,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Warehouse area: 2 220 m². Welfare and office area: 55 m². Transport layout area: 1 700 m². Hall founded on a foundation slab cast on cement-stabilised ground. Hall structure entirely in steel. Wall and roof cladding in sandwich panels.",
        "cs": "Skladová plocha: 2 220 m². Sociální a kancelářská plocha: 55 m². Plocha dopravního řešení: 1 700 m². Hala založená na základové desce provedené na zemině stabilizované cementem. Konstrukce haly zcela ocelová. Plášť stěn a střechy ze sendvičových panelů.",
        "sk": "Skladová plocha: 2 220 m². Sociálna a kancelárska plocha: 55 m². Plocha dopravného riešenia: 1 700 m². Hala založená na základovej doske realizovanej na podloží stabilizovanom cementom. Konštrukcia haly celá oceľová. Plášť stien a strechy zo sendvičových panelov.",
        "de": "Lagerfläche: 2 220 m². Sozial- und Bürofläche: 55 m². Verkehrserschließungsfläche: 1 700 m². Halle auf einer Fundamentplatte auf zementstabilisiertem Boden gegründet. Hallenkonstruktion vollständig in Stahl. Wand- und Dachverkleidung aus Sandwichpaneelen.",
        "hu": "Raktárterület: 2 220 m². Szociális és irodai terület: 55 m². Közlekedési kialakítás területe: 1 700 m². A csarnok alapozása cementtel stabilizált talajon készített alaplemezen. A csarnok szerkezete teljes egészében acél. Fal- és tetőburkolat szendvicspanelekből."
    }
},
    {
    "title": "BTS Development Park Zielona góra",
    "type": "realizacja-w-trakcie",
    "status": "W trakcie realizacji",
    "slug": "bts-development-park-zielona-gora",
    "czas": "",
    "formula": "",
    "opis": "Jako Generalny Wykonawca realizujemy nowoczesny obiekt dla BTS Development Park. Docelowo cały kompleks zaoferuje 10 000 m² zaawansowanej powierzchni biznesowej, przeznaczonej pod działalność produkcyjną, magazynową i logistyczną.\r\n\r\nInwestycja została zaprojektowana z myślą o maksymalnej elastyczności. Przestrzeń pozwala na podział na 4 niezależne moduły o powierzchni od 850 m² do 3 330 m². Takie rozwiązanie umożliwia precyzyjne dopasowanie układu funkcjonalnego do indywidualnych potrzeb operacyjnych przyszłych najemców.\r\n\r\nObecnie nasze prace na placu budowy koncentrują się na sprawnej realizacji pierwszej z hal. Zgodnie ze standardami MBT, kładziemy maksymalny nacisk na precyzyjne wykonanie każdego detalu technicznego oraz rygorystyczne przestrzeganie założonego harmonogramu inwestycji.",
    "logo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/399402210852.svg",
    "gallery": [],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/b04e4b92e0f0.svg",
    "latitude": 51.9825434,
    "longitude": 15.4178416,
    "order": 23,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "As the General Contractor, we are delivering a modern facility for BTS Development Park. Ultimately, the entire complex will offer 10,000 m² of advanced business space, intended for production, warehousing and logistics operations.\n\nThe investment has been designed with maximum flexibility in mind. The space can be divided into 4 independent modules with areas ranging from 850 m² to 3,330 m². Such a solution enables precise tailoring of the functional layout to the individual operational needs of future tenants.\n\nCurrently, our work on the construction site focuses on the efficient delivery of the first of the halls. In line with MBT's standards, we place maximum emphasis on the precise execution of every technical detail and strict adherence to the assumed investment schedule.",
        "cs": "Jako Generální dodavatel realizujeme moderní objekt pro BTS Development Park. V konečném důsledku celý komplex nabídne 10 000 m² pokročilé obchodní plochy určené pro výrobní, skladovou a logistickou činnost.\n\nInvestice byla navržena s ohledem na maximální flexibilitu. Prostor umožňuje rozdělení na 4 nezávislé moduly s plochou od 850 m² do 3 330 m². Takové řešení umožňuje přesné přizpůsobení funkčního uspořádání individuálním provozním potřebám budoucích nájemců.\n\nV současné době se naše práce na staveništi soustředí na efektivní realizaci první z hal. V souladu se standardy MBT klademe maximální důraz na přesné provedení každého technického detailu a důsledné dodržování stanoveného harmonogramu investice.",
        "sk": "Ako Generálny dodávateľ realizujeme moderný objekt pre BTS Development Park. V konečnom dôsledku celý komplex ponúkne 10 000 m² pokročilej obchodnej plochy určenej na výrobnú, skladovú a logistickú činnosť.\n\nInvestícia bola navrhnutá s ohľadom na maximálnu flexibilitu. Priestor umožňuje rozdelenie na 4 nezávislé moduly s plochou od 850 m² do 3 330 m². Takéto riešenie umožňuje presné prispôsobenie funkčného usporiadania individuálnym prevádzkovým potrebám budúcich nájomcov.\n\nV súčasnosti sa naše práce na stavenisku sústreďujú na efektívnu realizáciu prvej z hál. V súlade so štandardmi MBT kladieme maximálny dôraz na presné vykonanie každého technického detailu a dôsledné dodržiavanie stanoveného harmonogramu investície.",
        "de": "Als Generalunternehmer realisieren wir ein modernes Objekt für den BTS Development Park. Letztendlich wird der gesamte Komplex 10.000 m² hochwertige Geschäftsfläche bieten, die für Produktions-, Lager- und Logistikaktivitäten bestimmt ist.\n\nDie Investition wurde mit Blick auf maximale Flexibilität konzipiert. Die Fläche lässt sich in 4 unabhängige Module mit Flächen zwischen 850 m² und 3.330 m² unterteilen. Eine solche Lösung ermöglicht die präzise Anpassung des Funktionslayouts an die individuellen betrieblichen Anforderungen der künftigen Mieter.\n\nDerzeit konzentrieren sich unsere Arbeiten auf der Baustelle auf die reibungslose Realisierung der ersten Halle. Gemäß den MBT-Standards legen wir höchsten Wert auf die präzise Ausführung jedes technischen Details und die strikte Einhaltung des festgelegten Investitionszeitplans.",
        "hu": "Mint Fővállalkozó modern objektumot valósítunk meg a BTS Development Park számára. Végső soron a teljes komplexum 10 000 m² fejlett üzleti területet kínál majd, amely gyártási, raktározási és logisztikai tevékenységekre lesz alkalmas.\n\nA beruházást a maximális rugalmasság szem előtt tartásával terveztük. A tér 4 független modulra osztható, 850 m² és 3 330 m² közötti alapterülettel. Ez a megoldás lehetővé teszi a funkcionális elrendezés pontos testreszabását a jövőbeli bérlők egyedi működési igényeihez.\n\nJelenleg az építkezésen végzett munkánk az első csarnok hatékony megvalósítására összpontosít. Az MBT szabványainak megfelelően maximális hangsúlyt fektetünk minden műszaki részlet precíz kivitelezésére és a beruházás tervezett ütemezésének szigorú betartására."
    }
},
    {
    "title": "BYD Dąbrowscy - Bytom",
    "type": "realizacja-w-trakcie",
    "status": "W trakcie realizacji",
    "slug": "byd-dabrowscy-bytom",
    "czas": "",
    "formula": "",
    "opis": "Realizujemy budowę nowoczesnego obiektu dealerskiego dla marki BYD, na zlecenie Grupy Dąbrowscy. Inwestycja obejmuje stworzenie kompleksowego salonu samochodowego nowej generacji.\r\n\r\nCała nowoczesna przestrzeń została zaprojektowana od podstaw, w rygorystycznej zgodności z najnowszym, globalnym standardem architektonicznym i wizualnym marki – BYD CI 7.\r\n\r\nZakres realizacji obejmuje:\r\n\r\nNowoczesną salę sprzedaży (Showroom): Reprezentacyjna przestrzeń ekspozycyjna, dostosowana do najwyższych standardów prezentacji pojazdów oraz obsługi klienta.\r\n\r\nZaawansowany serwis motoryzacyjny: Technologicznie przystosowana hala warsztatowa, przygotowana do specjalistycznej diagnostyki i naprawy pojazdów elektrycznych oraz hybrydowych.\r\n\r\nKompleksową obsługę posprzedażową: W pełni zintegrowane zaplecze dedykowane doradcom serwisowym, zapewniające sprawną realizację usług (after-sales) w komfortowych warunkach.\r\n\r\nNaszym zadaniem jest precyzyjne wykonanie obiektu, który zapewni Inwestorowi optymalne warunki operacyjne oraz w pełni odda innowacyjny charakter marki BYD.",
    "logo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/a491138f9a7b.webp",
    "gallery": [],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/125d6a00ce04.webp",
    "latitude": 50.36019,
    "longitude": 18.90364,
    "order": 24,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "We are constructing a modern dealership facility for the BYD brand, commissioned by Grupa Dąbrowscy. The investment covers the creation of a comprehensive, next-generation car showroom.\n\nThe entire modern space has been designed from scratch, in strict compliance with the latest global architectural and visual standard of the brand – BYD CI 7.\n\nScope of work includes:\n\nModern showroom (Showroom): A representative exhibition space, tailored to the highest standards of vehicle presentation and customer service.\n\nAdvanced automotive service: A technologically equipped workshop hall, prepared for specialist diagnostics and repair of electric and hybrid vehicles.\n\nComprehensive after-sales support: A fully integrated facility dedicated to service advisors, ensuring efficient delivery of services (after-sales) in comfortable conditions.\n\nOur task is to precisely deliver a facility that will provide the Investor with optimal operational conditions and fully reflect the innovative character of the BYD brand.",
        "cs": "Realizujeme výstavbu moderního dealerství pro značku BYD, na objednávku skupiny Dąbrowscy. Investice zahrnuje vytvoření komplexního autosalonu nové generace.\n\nCelý moderní prostor byl navržen od základu, v přísném souladu s nejnovějším globálním architektonickým a vizuálním standardem značky – BYD CI 7.\n\nRozsah realizace zahrnuje:\n\nModerní prodejní sal (Showroom): Reprezentativní výstavní prostor přizpůsobený nejvyšším standardům prezentace vozidel a zákaznického servisu.\n\nPokročilý autoservis: Technologicky vybavená dílenská hala připravená pro specializovanou diagnostiku a opravy elektrických a hybridních vozidel.\n\nKomplexní poprodejní služby: Plně integrované zázemí určené servisním poradcům, zajišťující efektivní poskytování služeb (after-sales) v komfortních podmínkách.\n\nNaším úkolem je precizní provedení objektu, který investorovi poskytne optimální provozní podmínky a plně vyjádří inovativní charakter značky BYD.",
        "sk": "Realizujeme výstavbu moderného dealerského objektu pre značku BYD, na objednávku skupiny Dąbrowscy. Investícia zahŕňa vytvorenie komplexného autosalónu novej generácie.\n\nCelý moderný priestor bol navrhnutý od základu, v prísnom súlade s najnovším globálnym architektonickým a vizuálnym štandardom značky – BYD CI 7.\n\nRozsah realizácie zahŕňa:\n\nModernú predajnú sálu (Showroom): Reprezentatívny výstavný priestor prispôsobený najvyšším štandardom prezentácie vozidiel a zákazníckeho servisu.\n\nPokročilý autoservis: Technologicky vybavená dielenská hala pripravená na špecializovanú diagnostiku a opravu elektrických a hybridných vozidiel.\n\nKomplexný popredajný servis: Plne integrované zázemie určené servisným poradcom, zabezpečujúce efektívne poskytovanie služieb (after-sales) v komfortných podmienkach.\n\nNašou úlohou je precízne vykonanie objektu, ktorý investorovi poskytne optimálne prevádzkové podmínky a plne vyjadrí inovatívny charakter značky BYD.",
        "de": "Wir realisieren den Bau eines modernen Händlerobjekts für die Marke BYD, im Auftrag der Gruppe Dąbrowscy. Die Investition umfasst die Errichtung eines umfassenden Autohauses der neuen Generation.\n\nDer gesamte moderne Raum wurde von Grund auf geplant, in strikter Übereinstimmung mit dem neuesten globalen Architektur- und Visualstandard der Marke – BYD CI 7.\n\nDer Realisierungsumfang umfasst:\n\nModerner Showroom (Showroom): Ein repräsentativer Ausstellungsraum, der den höchsten Standards für Fahrzeugpräsentation und Kundenservice entspricht.\n\nFortschrittlicher Automobilservice: Eine technologisch ausgestattete Werkstatthalle, die für die fachgerechte Diagnose und Reparatur von Elektro- und Hybridfahrzeugen vorbereitet ist.\n\nUmfassender After-Sales-Service: Ein voll integriertes Backoffice für Serviceberater, das eine effiziente Abwicklung der Dienstleistungen (After-Sales) unter komfortablen Bedingungen gewährleistet.\n\nUnsere Aufgabe ist die präzise Ausführung eines Objekts, das dem Investor optimale Betriebsbedingungen bietet und den innovativen Charakter der Marke BYD vollständig zum Ausdruck bringt.",
        "hu": "Modern márkakereskedelmi objektumot építünk a BYD márka számára, a Dąbrowscy Csoport megbízásából. A beruházás egy új generációs, komplex autószalon létrehozását foglalja magában.\n\nA teljes modern teret a nulláról terveztük, szigorúan a márka legújabb globális építészeti és vizuális szabványának – BYD CI 7 – megfelelően.\n\nA megvalósítás terjedelme:\n\nModern értékesítési terem (Showroom): Reprezentatív kiállítási tér, a járművek bemutatásának és az ügyfélkiszolgálásnak a legmagasabb színvonalához igazítva.\n\nFejlett gépjárműszerviz: Technológiailag felszerelt műhelycsarnok, amely elektromos és hibrid járművek speciális diagnosztikájára és javítására készült.\n\nÁtfogó értékesítés utáni szolgáltatás: Teljes mértékben integrált háttér a szerviz-tanácsadók számára, amely kényelmes körülmények között biztosítja a szolgáltatások (after-sales) hatékony megvalósítását.\n\nFeladatunk egy olyan objektum precíz kivitelezése, amely optimális működési feltételeket biztosít a befektető számára, és teljes mértékben tükrözi a BYD márka innovatív jellegét."
    }
},
    {
    "title": "EcoWipes Nowy Dwór Mazowiecki",
    "type": "realizacja-w-trakcie",
    "status": "W trakcie Realizacji",
    "slug": "ecowipes-nowy-dwor-mazowiecki",
    "czas": "",
    "formula": "",
    "opis": "",
    "logo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/5f295318db8b.webp",
    "gallery": [],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/5c9ca71ccb20.webp",
    "latitude": 52.4305024,
    "longitude": 20.7349408,
    "order": 25,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {}
},
    {
    "title": "Ponar Wadowice",
    "type": "realizacja-w-trakcie",
    "status": "W trakcie realizacji",
    "slug": "ponar-wadowice",
    "czas": "",
    "formula": "",
    "opis": "",
    "logo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/444dc913cea9.webp",
    "gallery": [],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/39e49a9d540c.webp",
    "latitude": 50.1494206,
    "longitude": 18.8517032,
    "order": 26,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {}
},
    {
    "title": "VESUVIUS Skawina",
    "type": "realizacja-w-trakcie",
    "status": "W trakcie realizacji",
    "slug": "VESUVIUS",
    "czas": "",
    "formula": "",
    "opis": "Specyfikacja Powierzchnia i parametry (Łącznie): Powierzchnia całkowita: 6 650,00 m² Powierzchnia użytkowa: 6 405,00 m² Powierzchnia zabudowy: 6 413,00 m² Kubatura: 109 795 m³ Budynek biurowo-socjalny: Powierzchnia: ok. 347 m² Kondygnacje: 2 Konstrukcja (Hala magazynowa): Posadowienie: Pale betonowe Słupy: Prefabrykaty żelbetowe (wysokość 20 m) Dach: Konstrukcja prefabrykowana (rozpiętość 33 m), poszycie z blachy trapezowej z izolacją termiczną i przeciwwodną Ściany: Obudowa z płyt warstwowych Płyta fundamentowa: Żelbetowa, dostosowana pod regały i układnice magazynu wysokiego składowania Posadzka: Przemysłowa, betonowa, zacierana na gładko Konstrukcja i wykończenie (Budynek biurowo-socjalny): Konstrukcja: Murowana ze stropami strunobetonowymi Elewacja: Płyty warstwowe Wykończenie (wysoki standard): Sufity akustyczne, sucha zabudowa, wykładziny dywanowe i PCV, płytki gresowe, witryny aluminiowe Urządzenia i technologia magazynowa: 6 doków przeładunkowych z rampami, w większości wyposażonych w system automatycznej blokady kół Instalacja automatycznego składowania (część wysoka) Regały do składowania manualnego \"Magazyn ciepły\" z precyzyjną kontrolą parametrów temperaturowych Instalacje i infrastruktura (Wewnętrzna i Zewnętrzna): Instalacje sanitarne: Wodociągowa, kanalizacja sanitarna i deszczowa, centralne ogrzewanie Instalacje HVAC: Wentylacja mechaniczna, klimatyzacja Instalacje elektryczne i teletechniczne: Pełny zakres Ochrona PPOŻ: System Sygnalizacji Pożaru (SSP), instalacja gaszenia gazem, zewnętrzny zbiornik wody pożarowej, zestaw hydroforowy Infrastruktura zewnętrzna: Przebudowa i rozbudowa instalacji (w tym sieci cieplnej), mury oporowe, zadaszenie zewnętrzne Układ komunikacyjny: Przebudowa istniejącego wewnętrznego układu dróg i stanowisk postojowych",
    "logo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/75844a90de04.webp",
    "gallery": [],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/c03c5bacba61.webp",
    "latitude": 49.9782175,
    "longitude": 19.8201712,
    "order": 27,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Specification\nAreas and parameters (Total):\nTotal area: 6,650.00 m²\nUsable area: 6,405.00 m²\nBuilding area: 6,413.00 m²\nVolume: 109,795 m³\nOffice and welfare building:\nArea: approx. 347 m²\nStoreys: 2\nStructure (Warehouse hall):\nFoundation: Concrete piles\nColumns: Precast reinforced concrete (height 20 m)\nRoof: Precast structure (span 33 m), trapezoidal sheet metal cladding with thermal and waterproof insulation\nWalls: Sandwich panel cladding\nFoundation slab: Reinforced concrete, designed for high-bay racking and storage/retrieval systems\nFloor: Industrial concrete floor, power-trowelled to a smooth finish\nStructure and finishes (Office and welfare building):\nStructure: Masonry with prestressed concrete floors\nFaçade: Sandwich panels\nFinishes (high standard): Acoustic ceilings, drywall, carpet and PVC floor coverings, stoneware tiles, aluminium storefronts\nEquipment and storage technology:\n6 loading docks with ramps, mostly equipped with automatic wheel-locking systems\nAutomated storage installation (high-bay section)\nManual storage racking\n\"Heated warehouse\" with precise temperature parameter control\nInstallations and infrastructure (Internal and External):\nSanitary installations: Water supply, sanitary and stormwater drainage, central heating\nHVAC installations: Mechanical ventilation, air conditioning\nElectrical and teletechnical installations: Full scope\nFire protection: Fire alarm system (SSP), gas extinguishing system, external fire-water tank, booster set\nExternal infrastructure: Reconstruction and extension of installations (including heating network), retaining walls, external canopies\nTraffic layout: Reconstruction of the existing internal road and parking layout",
        "cs": "Specifikace\nPlochy a parametry (Celkem):\nCelková plocha: 6 650,00 m²\nUžitková plocha: 6 405,00 m²\nZastavěná plocha: 6 413,00 m²\nObjem: 109 795 m³\nKancelářsko-sociální budova:\nPlocha: cca 347 m²\nPodlaží: 2\nKonstrukce (Skladová hala):\nZaložení: betonové piloty\nSloupy: prefabrikované železobetonové (výška 20 m)\nStřecha: prefabrikovaná konstrukce (rozpětí 33 m), opláštění z trapézového plechu s tepelnou a protivodní izolací\nStěny: opláštění ze sendvičových panelů\nZákladová deska: železobetonová, přizpůsobená pro regály a zakladače vysokého skladu\nPodlaha: průmyslová betonová, hladce zahlazená\nKonstrukce a dokončení (Kancelářsko-sociální budova):\nKonstrukce: zděná se stropy z předpjatého betonu\nFasáda: sendvičové panely\nDokončení (vysoký standard): akustické podhledy, suchá výstavba, kobercové a PVC krytiny, gresové dlaždice, hliníkové výlohy\nZařízení a skladovací technologie:\n6 překládacích doků s rampami, převážně vybavených systémem automatického blokování kol\nInstalace automatického skladování (vysoká část)\nRegály pro manuální skladování\n\"Teplý sklad\" s přesnou kontrolou teplotních parametrů\nInstalace a infrastruktura (Vnitřní i vnější):\nSanitární instalace: vodovod, kanalizace sanitární a dešťová, ústřední vytápění\nHVAC instalace: mechanická ventilace, klimatizace\nElektrické a slaboproudé instalace: v plném rozsahu\nPO požární ochrana: systém požární signalizace (EPS), instalace plynového hašení, vnější nádrž požární vody, hydroforová sestava\nVnější infrastruktura: přestavba a rozšíření instalací (včetně teplovodní sítě), opěrné zdi, vnější přístřešky\nDopravní uspořádání: přestavba stávajícího vnitřního uspořádání komunikací a parkovacích stání",
        "sk": "Špecifikácia\nPlochy a parametre (Spolu):\nCelková plocha: 6 650,00 m²\nÚžitková plocha: 6 405,00 m²\nZastavaná plocha: 6 413,00 m²\nObjem: 109 795 m³\nKancelársko-sociálna budova:\nPlocha: cca 347 m²\nPodlažia: 2\nKonštrukcia (Skladová hala):\nZaloženie: betónové pilóty\nStĺpy: prefabrikované železobetónové (výška 20 m)\nStrecha: prefabrikovaná konštrukcia (rozpätie 33 m), opláštenie z trapézového plechu s tepelnou a protivodnou izoláciou\nSteny: opláštenie zo sendvičových panelov\nZákladová doska: železobetónová, prispôsobená pre regále a zakladače vysokého skladu\nPodlaha: priemyselná betónová, hladko zahladená\nKonštrukcia a dokončenie (Kancelársko-sociálna budova):\nKonštrukcia: murovaná so stropmi z predpätého betónu\nFasáda: sendvičové panely\nDokončenie (vysoký štandard): akustické podh�ady, suchá výstavba, kobercové a PVC krytiny, gresové dlaždice, hliníkové výklady\nZariadenia a skladovacia technológia:\n6 prekladaných dokov s rampami, prevažne vybavených systémom automatického blokovania kolies\nInštalácia automatického skladovania (vysoká časť)\nRegále pre manuálne skladovanie\n\"Teplý sklad\" s presnou kontrolou teplotných parametrov\nInštalácie a infraštruktúra (Vnútorná a vonkajšia):\nSanitárne inštalácie: vodovod, kanalizácia sanitárna a dažďová, ústredné vykurovanie\nHVAC inštalácie: mechanická ventilácia, klimatizácia\nElektrické a slaboprúdové inštalácie: v plnom rozsahu\nPO protipožiarna ochrana: systém požiarnej signalizácie (EPS), inštalácia plynového hasenia, vonkajšia nádrž požiarnej vody, hydroforová zostava\nVonkajšia infraštruktúra: prestavba a rozšírenie inštalácií (vrátane teplovodnej siete), oporné múry, vonkajšie prístrešky\nDopravné usporiadanie: prestavba jestvujúceho vnútorného usporiadania komunikácií a parkovacích státí",
        "de": "Spezifikation\nFlächen und Parameter (Gesamt):\nGesamtfläche: 6.650,00 m²\nNutzfläche: 6.405,00 m²\nGrundstücksfläche: 6.413,00 m²\nVolumen: 109.795 m³\nBüro- und Sozialgebäude:\nFläche: ca. 347 m²\nGeschosszahl: 2\nKonstruktion (Lagerhalle):\nGründung: Betonpfähle\nStützen: Stahlbeton-Fertigteile (Höhe 20 m)\nDach: Fertigteilkonstruktion (Spannweite 33 m), Trapezblechverkleidung mit Wärmedämmung und Abdichtung\nWände: Verkleidung aus Sandwichpaneelen\nBodenplatte: Stahlbeton, ausgelegt für Hochregal-Lager und Regalbediengeräte\nBoden: Industriebeton, glatt maschinengeschliffen\nKonstruktion und Ausbau (Büro- und Sozialgebäude):\nKonstruktion: Mauerwerk mit Spannbetondecken\nFassade: Sandwichpaneele\nAusbau (hochwertig): Akustikdecken, Trockenbau, Teppich- und PVC-Beläge, Feinsteinzeugfliesen, Aluminium-Schaufenster\nAusstattung und Lagertechnik:\n6 Verladedocks mit Rampen, überwiegend mit automatischer Radblockierung ausgestattet\nAutomatische Lagereinrichtung (Hochregalbereich)\nRegale für manuelle Lagerung\n„Warmes Lager\" mit präziser Temperaturparameter-Überwachung\nInstallationen und Infrastruktur (Innen und Außen):\nSanitärinstallationen: Wasserleitung, Schmutz- und Regenwasserkanalisation, Zentralheizung\nHVAC-Installationen: Mechanische Lüftung, Klimatisierung\nElektro- und Fernmeldetechnik: Vollständiger Umfang\nBrandschutz: Brandmeldeanlage (BMA), Gaslöschanlage, außenliegender Löschwassertank, Druckerhöhungsanlage\nAußenanlagen: Umbau und Erweiterung der Installationen (einschließlich Wärmenetz), Stützmauern, Außenüberdachungen\nVerkehrsanlagen: Umbau der bestehenden inneren Wege- und Stellplatzanordnung",
        "hu": "Specifikáció\nTerületek és paraméterek (Összesen):\nTeljes terület: 6 650,00 m²\nHasznos alapterület: 6 405,00 m²\nBeépített terület: 6 413,00 m²\nTérfogat: 109 795 m³\nIrodai és szociális épület:\nTerület: kb. 347 m²\nSzintek: 2\nSzerkezet (Raktárcsarnok):\nAlapozás: beton cölöpök\nOszlopok: előregyártott vasbeton (magasság 20 m)\nTető: előregyártott szerkezet (fesztáv 33 m), trapézlemez burkolat hő- és vízszigeteléssel\nFalak: szendvicspanel burkolat\nAlaplemez: vasbeton, magasraktári állványokhoz és rakodógépekhez igazítva\nPadló: ipari beton, simára csiszolt\nSzerkezet és kivitelezés (Irodai és szociális épület):\nSzerkezet: falazott, feszített beton födémekkel\nHomlokzat: szendvicspanelek\nKivitelezés (magas színvonalú): akusztikus álmennyezetek, szárazépítészet, szőnyeg- és PVC padlóburkolatok, greslapok, alumínium kirakatok\nBerendezések és raktártechnológia:\n6 átfejtő dokk rámpákkal, többnyire automata kerékblokkoló rendszerrel felszerelve\nAutomata tároló berendezés (magas rész)\nKézi tárolásra szolgáló állványok\n„Meleg raktár\" precíz hőmérséklet-paraméter ellenőrzéssel\nInstallációk és infrastruktúra (Belső és külső):\nSzaniter installációk: vízvezeték, szennyvíz- és csapadékvíz-csatorna, központi fűtés\nHVAC installációk: gépi szellőzés, klíma\nElektromos és gyengeáramú installációk: teljes körű\nTűzvédelem: tűzjelző rendszer (SSP), gázzal oltó rendszer, külső tűzivíztározó, hidrofor egység\nKülső infrastruktúra: installációk át- és kiépítése (beleértve a távhőhálózatot), támfalak, külső előtetők\nKözlekedési rendszer: a meglévő belső út- és parkolóelrendezés átépítése"
    }
},
    {
    "title": "Stokado Self-Storage – Warszawa Targówek",
    "type": "realizacja-w-trakcie",
    "status": "W trakcie realizacji",
    "slug": "stokado-self-storage-warszawa-targowek",
    "czas": "",
    "formula": "",
    "opis": "Budowa budynku self storage przy ul. Bystrej i Kolejarskiej w Warszawie. \r\n\r\n•\tBudynek 6 kondygnacyjny wyposażony w duże windy towarowo-osobowe oraz ewakuacyjną klatkę schodową. \r\n•\tCałkowita powierzchnia budynku self storge 8 269,03 m² o kubaturze 24 458 m3\r\n•\tBudynek powstaje jako konstrukcja betonowa monolityczna posadowiony na stopach fundamentowych.\r\n•\tElewacja z płyt warstwowych, poszycie dachy wykonane z membrany EPDM na warstwach termoizolacyjnych. \r\n•\tZagospodarowanie terenu wraz z zbiornikiem retencyjnym oraz infrastrukturą towarzyszącą.",
    "logo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/4d8667558baa.webp",
    "gallery": [],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/7ad52ff95b94.webp",
    "latitude": 52.2917104,
    "longitude": 21.0761354,
    "order": 28,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Construction of a self-storage building at ul. Bystra and Kolejarska in Warsaw.\n\n• 6-storey building equipped with large cargo and passenger lifts and an evacuation staircase.\n• Total area of the self-storage building 8,269.03 m² with a volume of 24,458 m3\n• The building is being built as a monolithic concrete structure founded on foundation footings.\n• Façade of sandwich panels, roof covering made of EPDM membrane on thermal insulation layers.\n• Land development including a retention tank and accompanying infrastructure.",
        "cs": "Výstavba budovy self storage u ul. Bystréj a Kolejarské ve Varšavě.\n\n• 6podlažní budova vybavená velkými nákladně-osobními výtahy a únikovým schodištěm.\n• Celková plocha budovy self storage 8 269,03 m² o objemu 24 458 m3\n• Budova je realizována jako monolitická betonová konstrukce založená na základových patkách.\n• Fasáda ze sendvičových panelů, opláštění střechy provedeno z EPDM membrány na tepelněizolačních vrstvách.\n• Úprava terénu včetně retenční nádrže a doprovodné infrastruktury.",
        "sk": "Výstavba budovy self storage pri ul. Bystrej a Kolejarskej vo Varšave.\n\n• 6-podlažná budova vybavená veľkými nákladno-osobnými výťahmi a únikovým schodiskom.\n• Celková plocha budovy self storage 8 269,03 m² s objemom 24 458 m3\n• Budova je realizovaná ako monolitická betónová konštrukcia založená na základových pätkách.\n• Fasáda zo sendvičových panelov, opláštenie strechy vykonané z EPDM membrány na tepelnoizolačných vrstvách.\n• Úprava terénu vrátane retenčnej nádrže a sprievodnej infraštruktúry.",
        "de": "Bau eines Self-Storage-Gebäudes an der ul. Bystra und Kolejarska in Warschau.\n\n• 6-geschossiges Gebäude, ausgestattet mit großen Lasten- und Personenaufzügen sowie einem Fluchttreppenhaus.\n• Gesamtfläche des Self-Storage-Gebäudes 8.269,03 m² mit einem Volumen von 24.458 m3\n• Das Gebäude wird als monolithische Betonkonstruktion auf Punktfundamenten errichtet.\n• Fassade aus Sandwichpaneelen, Dacheindeckung aus EPDM-Membran auf Wärmedämmschichten.\n• Geländegestaltung einschließlich Rückhaltetank und zugehöriger Infrastruktur.",
        "hu": "Önkiszolgáló tároló (self storage) épület építése a varsói ul. Bystra és Kolejarska utcánál.\n\n• 6 szintes épület, nagy teher- és személyfelvonókkal, valamint menekülési lépcsőházzal felszerelve.\n• A self storage épület teljes alapterülete 8 269,03 m², térfogata 24 458 m3\n• Az épület monolitikus betonszerkezetként készül, pontalapokon.\n• Szendvicspanel homlokzat, a tetőfedés EPDM membránból készült hőszigetelő rétegeken.\n• Telekrendezés visszatartó tartállyal és kísérő infrastruktúrával."
    }
},
    {
    "title": "VENUS - Brzegi",
    "type": "realizacja-w-trakcie",
    "status": "W trakcie realizacji",
    "slug": "venus-brzegi",
    "czas": "",
    "formula": "",
    "opis": "Zagospodarowanie terenu – PZT • Powierzchnia terenu inwestycji: ok. 13 300 m² • Powierzchnia utwardzona: ok. 850 m² Hala magazynowa + biurowiec • Powierzchnia zabudowy: ok. 3200 m² • Powierzchnia użytkowa: ok. 3800 m² • Kubatura: ok. 33 500 m³ • Ilość kondygnacji: 1 i 3 Konstrukcja • Konstrukcja mieszana: słupy i stropy żelbetowe, konstrukcja dachu stalowa, ściany zewnętrzne jako wypełnienie murem oraz płyty warstwowe, stropy monolityczne i prefabrykowane Elewacja • W hali system płyt warstwowych, natomiast w biurowcu system płyt warstwowych oraz jako reprezentatywna część obiektu, zastosowanie dużych przeszkleń oraz płyt kompozytowych Dach • Membrana dachowa PVC Sieci i instalacje zewnętrzne i wewnętrzne • Na potrzeby realizowanej inwestycji: ○ Sieci wod-kan, gaz, elektryczne ○ Kanalizacja sanitarna i deszczowa ○ Budowa zbiornika retencyjnego W naszych mediach społecznościowych znajdują się fotorelacje, aktualizowane na bieżąco.",
    "logo": "/static/img/mbt/venusgotowe-3c7b87fa.png",
    "gallery": [],
    "hero": "/static/img/mbt/venusgotowe-3c7b87fa.png",
    "latitude": 50.03319,
    "longitude": 20.0895646,
    "order": 29,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Site development – PZT • Investment site area: approx. 13 300 m² • Paved area: approx. 850 m². Warehouse hall + office building • Building area: approx. 3 200 m² • Usable area: approx. 3 800 m² • Volume: approx. 33 500 m³ • Number of storeys: 1 and 3. Structure • Mixed structure: reinforced concrete columns and slabs, steel roof structure, external walls as masonry infill with sandwich panels, monolithic and precast slabs. Façade • Sandwich panel system in the hall; in the office building, sandwich panel system combined, as a representative feature of the building, with large glazing and composite panels. Roof • PVC roofing membrane. External and internal networks and installations • For the needs of the investment: ○ Water and sewage, gas and electrical networks ○ Sanitary and stormwater drainage ○ Construction of a retention tank. Photo updates from our social media are posted on an ongoing basis.",
        "cs": "Zastavovací plán – PZT • Plocha pozemku investice: cca 13 300 m² • Zpevněná plocha: cca 850 m². Skladová hala + kancelářská budova • Zastavěná plocha: cca 3 200 m² • Užitková plocha: cca 3 800 m² • Objem: cca 33 500 m³ • Počet podlaží: 1 a 3. Konstrukce • Smíšená konstrukce: železobetonové sloupy a stropy, ocelová střešní konstrukce, vnější stěny jako zděná výplň se sendvičovými panely, monolitické a prefabrikované stropy. Fasáda • V hale systém sendvičových panelů, v kancelářské budově systém sendvičových panelů a jako reprezentativní část objektu velké prosklené plochy a kompozitní panely. Střecha • Střešní PVC membrána. Vnější a vnitřní sítě a instalace • Pro potřeby realizované investice: ○ Vodovodní a kanalizační, plynové a elektrické sítě ○ Splašková a dešťová kanalizace ○ Výstavba retenční nádrže. Fotogalerie jsou průběžně aktualizovány na našich sociálních sítích.",
        "sk": "Zastavovací plán – PZT • Plocha pozemku investície: cca 13 300 m² • Spevnená plocha: cca 850 m². Skladová hala + kancelárska budova • Zastavaná plocha: cca 3 200 m² • Úžitková plocha: cca 3 800 m² • Objem: cca 33 500 m³ • Počet podlaží: 1 a 3. Konštrukcia • Zmiešaná konštrukcia: železobetónové stĺpy a stropy, oce�ová strešná konštrukcia, vonkajšie steny ako murovaná výplň so sendvičovými panelmi, monolitické a prefabrikované stropy. Fasáda • V hale systém sendvičových panelov, v kancelárskej budove systém sendvičových panelov a ako reprezentatívna časť objektu veľké presklené plochy a kompozitné panely. Strecha • Strešná PVC membrána. Vonkajšie a vnútorné siete a inštalácie • Pre potreby realizovanej investície: ○ Vodovodné a kanalizačné, plynové a elektrické siete ○ Splášková a dažďová kanalizácia ○ Výstavba retenčnej nádrže. Aktuálne fotogalérie nájdete priebežne dopĺňané na našich sociálnych sieťach.",
        "de": "Geländegestaltung – B-Plan • Grundstücksfläche der Investition: ca. 13 300 m² • Befestigte Fläche: ca. 850 m². Lagerhalle + Bürogebäude • Grundstücksfläche: ca. 3 200 m² • Nutzfläche: ca. 3 800 m² • Volumen: ca. 33 500 m³ • Anzahl der Geschosse: 1 und 3. Konstruktion • Gemischte Konstruktion: Stahlbetonstützen und -decken, Stahl-Dachkonstruktion, Außenwände als Mauerwerksausfachung mit Sandwichpaneelen, monolitische und vorgefertigte Decken. Fassade • Sandwichpaneelsystem in der Halle; im Bürogebäude Sandwichpaneelsystem und, als repräsentativer Teil des Gebäudes, großflächige Verglasungen und Verbundpaneele. Dach • PVC-Dachmembran. Außen- und Innen-Netze und -Installationen • Für die Bedürfnisse der Investition: ○ Wasser-, Kanal-, Gas- und Stromnetze ○ Schmutz- und Regenwasserkanalisation ○ Bau eines Rückhaltebeckens. Aktuelle Fotoreportagen werden laufend auf unseren Social-Media-Kanälen veröffentlicht.",
        "hu": "Területrendezés – Terv • A beruházás területének nagysága: kb. 13 300 m² • Burkolt felület: kb. 850 m². Raktárcsarnok + irodaház • Beépített terület: kb. 3 200 m² • Hasznos alapterület: kb. 3 800 m² • Térfogat: kb. 33 500 m³ • Szintek száma: 1 és 3. Szerkezet • Vegyes szerkezet: vasbeton oszlopok és födémek, acél tetőszerkezet, külső falak falazott kitöltéssel és szendvicspanelekkel, monolit és előre gyártott födémek. Homlokzat • A csarnokban szendvicspanel rendszer, az irodaházban szendvicspanel rendszer, valamint – az épület reprezentatív részeként – nagyméretű üvegezések és kompozit panelek. Tető • PVC tetőmembrán. Külső és belső hálózatok és telepítések • A megvalósuló beruházás igényeihez: ○ Víz-, csatorna-, gáz- és elektromos hálózatok ○ Szennyvíz- és csapadékcsatorna ○ Csapadékvíz-visszatartó tározó építése. Folyamatosan frissített fotóbeszámolók találhatók a közösségi média felületeinken."
    }
},
    {
    "title": "Scallier - Zabrze",
    "type": "realizacja-w-trakcie",
    "status": "W trakcie realizacji",
    "slug": "scallier-zabrze",
    "czas": "",
    "formula": "",
    "opis": "• Powierzchnia użytkowa: • Budynek A: 1 358,90 m² • Budynek B: 943,70 m² • Powierzchnia terenu: 9 263,44 m² Układ przestrzenny: • Dwa parterowe budynki rozdzielone drogą wjazdową, formą podążającą za linią zabudowy • Wejścia główne dla klientów od strony parkingu (wschód) • Strefa dostaw i zaplecza techniczno-magazynowego od strony zachodniej • Wydzielone strefy: lokale usługowe (sala sprzedaży + zaplecze), ogólnodostępne sanitariaty, pomieszczenia techniczne Konstrukcja: • Ustrój mieszany • Posadowienie bezpośrednie: żelbetowe ławy i stopy fundamentowe • Słupy: żelbetowe prefabrykowane • Dach: konstrukcja stalowa Elewacja: • Płyty warstwowe Zagospodarowanie terenu: • Parking dla samochodów osobowych wraz z chodnikami • Podziemny zbiornik na wodę pożarową • Podziemny zbiornik retencyjny na wodę deszczową W naszych mediach społecznościowych znajdują się fotorelacje, aktualizowane na bieżąco.",
    "logo": "/static/img/mbt/scallier-logo-662a14b7.png",
    "gallery": [],
    "hero": "/static/img/mbt/scallier-logo-662a14b7.png",
    "latitude": 50.2963029,
    "longitude": 18.8264414,
    "order": 30,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "• Usable area: • Building A: 1,358.90 m² • Building B: 943.70 m² • Land area: 9,263.44 m²\nSpatial layout: • Two single-storey buildings separated by an access road, following the building line • Main customer entrances from the parking side (east) • Delivery and technical/back-of-house zone on the west side • Separated zones: retail units (sales floor + back-of-house), public restrooms, technical rooms\nStructure: • Mixed structural system • Direct foundation: reinforced-concrete strip and pad footings • Columns: precast reinforced concrete • Roof: steel structure\nFaçade: • Sandwich panels\nSite development: • Car park with pedestrian walkways • Underground fire-water tank • Underground stormwater retention tank\nOur social media channels feature regular photo updates from the project.",
        "cs": "• Užitková plocha: • Budova A: 1 358,90 m² • Budova B: 943,70 m² • Plocha pozemku: 9 263,44 m²\nProstorové uspořádání: • Dva jednopodlažní objekty oddělené příjezdovou komunikací, tvarově sledující linii zástavby • Hlavní vstupy pro zákazníky ze strany parkoviště (východ) • Zóna zásobování a technicko-skladového zázemí ze západní strany • Vymezené zóny: obchodní jednotky (prodejní sál + zázemí), veřejně přístupné toalety, technické místnosti\nKonstrukce: • Smíšený nosný systém • Přímé založení: železobetonové pasy a patky • Sloupy: prefabrikované železobetonové • Střecha: ocelová konstrukce\nFasáda: • Sendvičové panely\nKrajinářské úpravy: • Parkoviště pro osobní automobily včetně chodníků • Podzemní požární nádrž na vodu • Podzemní retenční nádrž na dešťovou vodu\nNa našich sociálních sítích naleznete průběžně aktualizované fotoreportáže.",
        "sk": "• Úžitková plocha: • Budova A: 1 358,90 m² • Budova B: 943,70 m² • Plocha pozemku: 9 263,44 m²\nPriestorové usporiadanie: • Dva jednopodlažné objekty oddelené príjazdovou komunikáciou, tvarovo sledujúce líniu zástavby • Hlavné vstupy pre zákazníkov zo strany parkoviska (východ) • Zóna zásobovania a technicko-skladového zázemia zo západnej strany • Vymedzené zóny: obchodné jednotky (predajný priestor + zázemie), verejne prístupné toalety, technické miestnosti\nKonštrukcia: • Zmiešaný nosný systém • Priame založenie: železobetónové pásy a pätky • Stĺpy: prefabrikované železobetónové • Strecha: oceľová konštrukcia\nFasáda: • Sendvičové panely\nKrajinné úpravy: • Parkovisko pre osobné automobily vrátane chodníkov • Podzemná požiarna nádrž na vodu • Podzemná retenčná nádrž na dažďovú vodu\nNa našich sociálnych sieťach nájdete priebežne aktualizované fotoreportáže.",
        "de": "• Nutzfläche: • Gebäude A: 1.358,90 m² • Gebäude B: 943,70 m² • Grundstücksfläche: 9.263,44 m²\nRäumliche Anordnung: • Zwei eingeschossige Gebäude, getrennt durch eine Zufahrtsstraße, deren Form der Bebauungslinie folgt • Haupteingänge für Kunden von der Parkplatzseite (Osten) • Anlieferungs- und Technik-/Lagerzone auf der Westseite • Abgegrenzte Zonen: Geschäftseinheiten (Verkaufsraum + Back-of-House), öffentlich zugängliche Sanitärräume, Technikräume\nKonstruktion: • Gemischtes Tragsystem • Direkte Gründung: Stahlbeton-Streifen- und Punktfundamente • Stützen: Stahlbeton-Fertigteile • Dach: Stahlkonstruktion\nFassade: • Sandwichpaneele\nFreiflächengestaltung: • PKW-Parkplatz mit Gehwegen • Unterirdischer Löschwassertank • Unterirdischer Regenwasserrückhaltetank\nIn unseren sozialen Medien finden Sie laufend aktualisierte Fotodokumentationen.",
        "hu": "• Hasznos alapterület: • A épület: 1 358,90 m² • B épület: 943,70 m² • Telek területe: 9 263,44 m²\nTérbeli elrendezés: • Két földszintes épület, amelyeket behajtó út választ el, a beépítési vonalat követő formával • Főbejáratok az ügyfelek számára a parkoló felől (kelet) • Áruátvételi és műszaki-raktári zóna a nyugati oldalon • Elkülönített zónák: üzlethelyiségek (értékesítési tér + kiszolgálórész), nyilvános mosdók, műszaki helyiségek\nSzerkezet: • Vegyes tartószerkezet • Közvetlen alapozás: vasbeton sávalapok és pontalapok • Oszlopok: előregyártott vasbeton • Tető: acélszerkezet\nHomlokzat: • Szendvicspanelek\nTelekrendezés: • Személygépkocsi-parkoló járdákkal • Föld alatti tűzivíztározó • Föld alatti csapadékvíz-visszatartó tározó\nKözösségi média felületeinken rendszeresen frissített fotódokumentációt talál."
    }
},
    {
    "title": "Fiołka Racibórz",
    "type": "realizacja-w-trakcie",
    "status": "W trakcie realizacji",
    "slug": "fiolka-raciborz",
    "czas": "",
    "formula": "",
    "opis": "Budowa hali montażowo-magazynowej wraz z zapleczem socjalno-biurowym oraz odźwigowieniem dla działalności produkcyjnej polegającej na prefabrykacji rozdzielni silnoprądowych. \r\n\r\n•\tPowierzchnia produkcyjno-magazynowa – 3634 m2 \r\n•\tPowierzchnia socjalno-biurowa – 250,52 m2\r\n•\tHala projektowana pod dwie suwnice o łącznym udźwigu 20 T\r\n•\tSieci i instalacje na potrzeby realizowanej inwestycji\r\n•\tZagospodarowanie terenu wokół obiektu \r\n•\tKonstrukcja: \r\no\tObiekt o posadowieniu pośrednim na kolumnach betonowych\r\no\tKonstrukcja ścian i dachu hali w technologii stalowej\r\no\tObudowa hali w technologii płyt warstwowych\r\no\tPokrycie dachu hali w konstrukcji stalowej z użyciem blachy trapezowej, izolacją z wełny mineralnej i membraną PVC \r\no\tKonstrukcja budynku biurowego mieszana (murowana, rdzenie i wieńce żelbetowe, prefabrykowane stopy z użyciem płyt kanałowych typu HC)",
    "logo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/dbbea2e8e99b.webp",
    "gallery": [],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/f6e1ae46d58d.webp",
    "latitude": 50.0974579,
    "longitude": 18.2342209,
    "order": 31,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Construction of an assembly and warehouse hall with social and office facilities and crane equipment for production activities involving the prefabrication of high-voltage switchgears.\n\n• Production and warehouse area – 3,634 m2\n• Social and office area – 250.52 m2\n• Hall designed for two overhead cranes with a total lifting capacity of 20 T\n• Networks and installations for the needs of the implemented investment\n• Land development around the facility\n• Structure:\no Facility with indirect foundation on concrete columns\no Wall and roof structure of the hall in steel technology\no Hall cladding in sandwich panel technology\no Hall roof covering in steel structure using trapezoidal sheet metal, mineral wool insulation and PVC membrane\no Mixed structure of the office building (masonry, reinforced concrete cores and ring beams, prefabricated footings using HC-type channel slabs)",
        "cs": "Výstavba montážně-skladové haly se sociálně-kancelářským zázemím a jeřábovým vybavením pro výrobní činnost spočívající v prefabrikaci silnoproudých rozvoden.\n\n• Výrobně-skladová plocha – 3634 m2\n• Sociálně-kancelářská plocha – 250,52 m2\n• Hala navržena pro dvě jeřáby o celkové nosnosti 20 T\n• Sítě a instalace pro potřeby realizované investice\n• Úprava terénu kolem objektu\n• Konstrukce:\no Objekt s nepřímým založením na betonových sloupech\no Konstrukce stěn a střechy haly v ocelové technologii\no Opláštění haly v technologii sendvičových panelů\no Krytina střechy haly v ocelové konstrukci s použitím trapézového plechu, izolace z minerální vlny a PVC membrány\no Smíšená konstrukce kancelářské budovy (zděná, železobetonová jádra a věnce, prefabrikované patky s použitím kanálových desek typu HC)",
        "sk": "Výstavba montážno-skladovej haly so sociálno-kancelárskym zázemím a žeriavovým vybavením pre výrobnú činnosť spočívajúcu v prefabrikácii silnoprúdových rozvodní.\n\n• Výrobno-skladová plocha – 3634 m2\n• Sociálno-kancelárska plocha – 250,52 m2\n• Hala navrhnutá pre dva žeriavy s celkovou nosnosťou 20 T\n• Siete a inštalácie pre potreby realizovanej investície\n• Úprava terénu okolo objektu\n• Konštrukcia:\no Objekt s nepriamym založením na betónových stĺpoch\no Konštrukcia stien a strechy haly v oceľovej technológii\no Opláštenie haly v technológii sendvičových panelov\no Krytina strechy haly v oceľovej konštrukcii s použitím trapézového plechu, izolácie z minerálnej vlny a PVC membrány\no Zmiešaná konštrukcia kancelárskej budovy (murovaná, železobetónové jadrá a vence, prefabrikované pätky s použitím kanálových dosiek typu HC)",
        "de": "Bau einer Montage- und Lagerhalle mit Sozial- und Büroräumen sowie Kranausrüstung für die Produktionstätigkeit im Bereich der Vorfertigung von Hochspannungsschaltanlagen.\n\n• Produktions- und Lagerfläche – 3.634 m2\n• Sozial- und Bürofläche – 250,52 m2\n• Halle ausgelegt für zwei Krane mit einer Gesamtragfähigkeit von 20 T\n• Netze und Installationen für die Bedürfnisse der realisierten Investition\n• Geländegestaltung um das Objekt\n• Konstruktion:\no Objekt mit indirekter Gründung auf Betonstützen\no Wand- und Dachkonstruktion der Halle in Stahltechnologie\no Hallenverkleidung in Sandwichpaneel-Technologie\no Dachdeckung der Halle in Stahlkonstruktion unter Verwendung von Trapezblech, Mineralwolldämmung und PVC-Membran\no Gemischte Konstruktion des Bürogebäudes (Mauerwerk, Stahlbetonkerne und Ringbalken, vorgefertigte Punktfundamente unter Verwendung von HC-Kanalplatten)",
        "hu": "Összeszerelő-raktár csarnok építése szociális-irodai kiegészítőkkel és daruzással, nagyfeszültségű kapcsolóberendezések előregyártására irányuló gyártási tevékenységhez.\n\n• Gyártási-raktározási terület – 3634 m2\n• Szociális-irodai terület – 250,52 m2\n• A csarnok két daru befogadására van méretezve, 20 T összterhelhetőséggel\n• Hálózatok és telepítések a megvalósított beruházás igényeihez\n• A telek rendezése az objektum körül\n• Szerkezet:\no Közvetett alapozású objektum betonoszlopokon\no A csarnok fal- és tetőszerkezete acél technológiával\no Csarnok burkolat szendvicspanel technológiával\no A csarnok tetőfedése acélszerkezettel trapézlemez, ásványgyapot szigetelés és PVC membrán felhasználásával\no Az irodaépület vegyes szerkezete (falazott, vasbeton magok és koszorúk, előregyártott talpak HC típusú csatorna lemezek felhasználásával)"
    }
},
    {
    "title": "Bater - Gliwice",
    "type": "realizacja-w-trakcie",
    "status": "W trakcie realizacji",
    "slug": "bater-gliwice",
    "czas": "",
    "formula": "",
    "opis": "Kubatura całkowita nowego obiektu wynosi 28 342 m³ Budynek biurowy dwukondygnacyjny, z wydzieloną kondygnacją magazynową oraz antresolą magazynową nad częścią produkcyjną, a także z powierzchnią biurowo-socjalną na drugiej kondygnacji Zagospodarowanie terenu wokół nowego obiektu Konstrukcja: posadowienie „mieszane” (bezpośrednie oraz w części pośrednie) konstrukcja nośna obiektu „mieszana” (prefabrykowane żelbetowe słupy, elementy murowe oraz stalowa konstrukcja dachu) obudowa obiektu „mieszana” ( tradycyjna murowa obudowa z płyty warstwowej ,w części biurowej fasada szklana) pokrycie dachu płytami z wełny skalnej i membraną PVC W naszych mediach społecznościowych znajdują się fotorelacje, aktualizowane na bieżąco.",
    "logo": "/static/img/mbt/logo2-76e5c8f9.png",
    "gallery": [],
    "hero": "/static/img/mbt/logo2-76e5c8f9.png",
    "latitude": 50.2689683,
    "longitude": 18.7209159,
    "order": 32,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Total volume of the new building: 28 342 m³. Two-storey office building with a separate warehouse level and a storage mezzanine above the production section, as well as office and welfare space on the first floor. Site development around the new building. Structure: \"mixed\" foundation (direct and, in part, indirect); \"mixed\" load-bearing structure (precast reinforced concrete columns, masonry elements and steel roof structure); \"mixed\" envelope (traditional masonry cladding with sandwich panels, glass façade in the office section); roof covered with stone wool panels and PVC membrane. Photo updates from our social media are posted on an ongoing basis.",
        "cs": "Celkový objem nového objektu činí 28 342 m³. Dvoupodlažní kancelářská budova s vyčleněným skladovým podlažím a skladovým mezipatrovým prostorem nad výrobní částí, jakož i s kancelářskými a sociálními plochami v prvním patře. Úprava území v okolí nového objektu. Konstrukce: „smíšené\" založení (přímé a částečně nepřímé); „smíšená\" nosná konstrukce objektu (prefabrikované železobetonové sloupy, zděné prvky a ocelová střešní konstrukce); „smíšený\" plášť objektu (tradiční zděný plášť se sendvičovými panely, v kancelářské části prosklená fasáda); zastřešení deskami z kamenné vlny a PVC membránou. Fotogalerie jsou průběžně aktualizovány na našich sociálních sítích.",
        "sk": "Celkový objem nového objektu je 28 342 m³. Dvojpodlažná kancelárska budova s vyčleneným skladovým podlažím a skladovým mezanínom nad výrobnou časťou, ako aj s kancelárskymi a sociálnymi plochami na prvom poschodí. Úprava územia okolo nového objektu. Konštrukcia: „zmiešané\" založenie (priame a čiastočne nepriame); „zmiešaná\" nosná konštrukcia objektu (prefabrikované železobetonové stĺpy, murované prvky a oceľová strešná konštrukcia); „zmiešaný\" plášť objektu (tradičný murovaný plášť so sendvičovými panelmi, v kancelárskej časti presklená fasáda); zastrešenie doskami z kamennej vlny a PVC membránou. Aktuálne fotogalérie nájdete priebežne dopĺňané na našich sociálnych sieťach.",
        "de": "Gesamtvolumen des neuen Objekts: 28 342 m³. Zweigeschossiges Bürogebäude mit einem separaten Geschoss für Lager und einer Lagerzwischenebene über dem Produktionsteil sowie Büro- und Sozialflächen im ersten Obergeschoss. Geländegestaltung rund um das neue Gebäude. Konstruktion: „gemischte\" Gründung (direkt und teilweise indirekt); „gemischte\" Tragstruktur (vorgefertigte Stahlbetonstützen, Mauerwerkselemente und Stahl-Dachkonstruktion); „gemischte\" Gebäudehülle (traditionelle Mauerwerksverkleidung mit Sandwichpaneelen, Glasfassade im Büroteil); Dacheindeckung mit Steinwollplatten und PVC-Membran. Aktuelle Fotoreportagen werden laufend auf unseren Social-Media-Kanälen veröffentlicht.",
        "hu": "Az új objektum teljes térfogata 28 342 m³. Kétszintes irodaház különálló raktárszinttel és raktári félemelettel a gyártási rész felett, valamint irodai és szociális terekkel az első emeleten. Az új objektum környékének tereprendezése. Szerkezet: „vegyes\" alapozás (közvetlen és részben közvetett); „vegyes\" teherhordó szerkezet (előre gyártott vasbeton oszlopok, falazott elemek és acél tetőszerkezet); „vegyes\" épületburkolat (hagyományos falazott burkolat szendvicspanelekkel, az irodai részben üvegezett homlokzat); tetőfedés kőzetgyapot táblákkal és PVC membránnal. Folyamatosan frissített fotóbeszámolók találhatók a közösségi média felületeinken."
    }
},
    {
    "title": "Wessper",
    "type": "realizacja-w-trakcie",
    "status": "W trakcie realizacji",
    "slug": "wessper",
    "czas": "",
    "formula": "",
    "opis": "",
    "logo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/8c6b51ed721a.webp",
    "gallery": [],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/cf989e76f981.webp",
    "latitude": 50.0019853,
    "longitude": 20.5066441,
    "order": 33,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {}
},
    {
    "title": "Warmet Hurtownia Alkocholi",
    "type": "realizacja-w-trakcie",
    "status": "W trakcie realizacji",
    "slug": "warmet-hurtownia-alkocholi",
    "czas": "",
    "formula": "",
    "opis": "Firma Warmet – doskonale znana i ceniona hurtownia alkoholi – zyskuje nową przestrzeń do rozwoju. Realizowany przez zespół Generalnego Wykonawcy MBT obiekt to nowoczesna hala, która będzie pełnić funkcję głównego centrum dystrybucji naszego Inwestora.\r\n\r\nW branży FMCG oraz dystrybucji napojów kluczowa jest bezbłędna logistyka i zachowanie odpowiednich warunków magazynowania. Z myślą o tych wymaganiach budujemy przestrzeń w pełni dostosowaną do specyfiki operacyjnej firmy Warmet. Nowy obiekt pozwoli na zoptymalizowanie procesów logistycznych, sprawniejszą obsługę zamówień i zapewni solidne zaplecze dla dalszego rozwoju biznesu.\r\n\r\nObecnie jesteśmy po etapie symbolicznego wmurowania fundamentów. Prace na placu budowy postępują zgodnie z harmonogramem i naszym inżynieryjnym standardem. Dziękujemy firmie Warmet za zaufanie i powierzenie MBT realizacji tego strategicznego projektu.",
    "logo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/bb10f93000a3.webp",
    "gallery": [],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/2db86077caef.webp",
    "latitude": 52.6153422,
    "longitude": 21.5111711,
    "order": 34,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {
        "en": "Warmet – a well-known and respected alcohol wholesaler – is gaining new space for development. The facility being delivered by MBT's General Contractor team is a modern hall that will serve as the main distribution centre for our Investor.\n\nIn the FMCG and beverage distribution industry, flawless logistics and maintaining proper storage conditions are essential. With these requirements in mind, we are building a space fully tailored to the operational specifics of Warmet. The new facility will enable optimised logistics processes, more efficient order handling and provide a solid backbone for further business growth.\n\nWe have just completed the symbolic cornerstone-laying stage. Works on the construction site are progressing according to schedule and our engineering standard. We thank Warmet for the trust and for entrusting MBT with the delivery of this strategic project.",
        "cs": "Firma Warmet – dobře známý a ceněný velkoobchod s alkoholem – získává nový prostor pro rozvoj. Objekt realizovaný týmem Generálního dodavatele MBT je moderní hala, která bude plnit funkci hlavního distribučního centra našeho investora.\n\nV odvětví FMCG a distribuce nápojů je klíčová bezchybná logistika a dodržování odpovídajících skladovacích podmínek. S ohledem na tyto požadavky budujeme prostor plně přizpůsobený provozní specifice firmy Warmet. Nový objekt umožní optimalizaci logistických procesů, efektivnější vyřizování objednávek a poskytne solidní zázemí pro další rozvoj podnikání.\n\nV současné době jsme po etapě symbolického položení základního kamene. Práce na staveništi postupují podle harmonogramu a našeho inženýrského standardu. Děkujeme firmě Warmet za důvěru a svěření realizace tohoto strategického projektu společnosti MBT.",
        "sk": "Firma Warmet – dobre známy a cenený veľkoobchod s alkoholom – získava nový priestor pre rozvoj. Objekt realizovaný tímom Generálneho dodávateľa MBT je moderná hala, ktorá bude plniť funkciu hlavného distribučného centra nášho investora.\n\nV odvetví FMCG a distribúcie nápojov je kľúčová bezchybná logistika a dodržiavanie primeraných skladovacích podmienok. S ohľadom na tieto požiadavky budujeme priestor plne prispôsobený prevádzkovej špecifikácii firmy Warmet. Nový objekt umožní optimalizáciu logistických procesov, efektívnejšie vybavovanie objednávok a poskytne solídne zázemie pre ďalší rozvoj podnikania.\n\nV súčasnosti sme po etape symbolického položenia základného kameňa. Práce na stavenisku postupujú podľa harmonogramu a nášho inžinierskeho štandardu. Ďakujeme firme Warmet za dôveru a zverenie realizácie tohto strategického projektu spoločnosti MBT.",
        "de": "Das Unternehmen Warmet – ein bekannter und angesehener Großhändler für Alkohol – erhält neuen Raum für Wachstum. Das vom Generalunternehmer-Team MBT realisierte Objekt ist eine moderne Halle, die als Hauptvertriebszentrum unseres Investors dienen wird.\n\nIn der FMCG- und Getränkedistribution sind eine reibungslose Logistik und die Einhaltung geeigneter Lagerbedingungen entscheidend. Mit Blick auf diese Anforderungen bauen wir einen Raum, der vollständig auf die betrieblichen Besonderheiten von Warmet zugeschnitten ist. Das neue Objekt ermöglicht optimierte Logistikprozesse, eine effizientere Auftragsabwicklung und bietet eine solide Basis für weiteres Geschäftswachstum.\n\nWir haben gerade die symbolische Grundsteinlegung abgeschlossen. Die Arbeiten auf der Baustelle verlaufen planmäßig und nach unserem Ingenieurstandard. Wir bedanken uns bei Warmet für das Vertrauen und die Übertragung der Realisierung dieses strategischen Projekts an MBT.",
        "hu": "A Warmet – jól ismert és elismert alkohol-nagykereskedő – új teret kap a fejlődéshez. Az MBT Fővállalkozói csapata által megvalósított objektum egy modern csarnok, amely befektetőnk fő elosztóközpontjaként fog működni.\n\nAz FMCG és az italelosztás iparágában a hibátlan logisztika és a megfelelő tárolási feltételek betartása kulcsfontosságú. Ezeket az igényeket szem előtt tartva olyan teret építünk, amely teljes mértékben a Warmet működési sajátosságaihoz igazodik. Az új objektum optimalizálja a logisztikai folyamatokat, hatékonyabbá teszi a rendelések kezelését, és szilárd alapot biztosít a további üzleti fejlődéshez.\n\nJelenleg az alapkőletétel szimbolikus szakaszánál tartunk. Az építkezésen a munkálatok az ütemezés és mérnöki színvonalunk szerint haladnak. Köszönjük a Warmet cég bizalmát, hogy ezt a stratégiai projektet az MBT-re bízta."
    }
},
    {
    "title": "Raben",
    "type": "realizacja-w-trakcie",
    "status": "W trakcie realizacji",
    "slug": "raben",
    "czas": "",
    "formula": "",
    "opis": "",
    "logo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/e257f7ae4ed2.webp",
    "gallery": [],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/00065b4a0f4f.webp",
    "latitude": 51.177,
    "longitude": 16.237,
    "order": 35,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {}
},
    {
    "title": "Less Mess Gdańsk",
    "type": "realizacja-w-trakcie",
    "status": "W trakcie realizacji",
    "slug": "less-mess-gdansk",
    "czas": "",
    "formula": "",
    "opis": "",
    "logo": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/0b6a2afd6d97.webp",
    "gallery": [],
    "hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/28beeb5e020f.webp",
    "latitude": 54.3445279,
    "longitude": 18.5456996,
    "order": 36,
    "t_t": {},
    "t_s": {},
    "t_c": {},
    "t_f": {},
    "t_o": {}
}
]

JOBS = [
    {
    "title": "Inżynier Budowy",
    "slug": "inzynier-budowy-m-k-generalny-wykonawca",
    "text": "Twój zakres obowiązków ✓ analiza dokumentacji projektowej, ✓ realizacja zadań powierzonych przez Kierownika Budowy, ✓ koordynacja prac Podwykonawców i Dostawców na budowie, ✓ sporządzanie raportów, protokołów i rozliczeń, ✓ wykonywanie odbiorów robót. Nasze wymagania ✓ wykształcenie techniczne (ukończone lub w trakcie) np. Budownictwo, Architektura, Inżynieria Środowiska, ✓ biegła obsługa pakietu MS Office i AutoCAD, ✓ umiejętność pracy w zespole, ✓ chęć do nauki i zdobywania doświadczenia na budowie. To oferujemy ✓ stabilne zatrudnienie w oparciu o umowę o pracę lub B2B, ✓ atrakcyjne wynagrodzenie adekwatne do podejmowanych zadań, ✓ wsparcie doświadczonej kadry zarządzającej, ✓ możliwość rozwoju i pracy przy unikatowych projektach dla czołowych i prestiżowych Inwestorów na polskim rynku, ✓ szkolenia i kursy podnoszące kwalifikacje, ✓ możliwość korzystania z samochodu służbowego, ✓ prywatną opiekę medyczną Medicover, ✓ ubezpieczenie grupowe WARTA, ✓ spotkania integracyjne, ✓ brak dress code’u, ✓ kawa / herbata. Aplikuj na to stanowisko Proces rekrutacji prowadzimy w systemie eRecruiter. Kliknij poniższy przycisk, aby wypełnić formularz. Przejdź do formularza aplikacji",
    "t_t": {
        "en": "Site Engineer",
        "de": "Bauleiter",
        "hu": "Építésvezető mérnök",
        "cs": "Stavební inženýr",
        "sk": "Stavebný inžinier"
    },
    "t_x": {
        "en": "Your responsibilities ✓ analysis of design documentation, ✓ execution of tasks assigned by the Construction Manager, ✓ coordination of Subcontractor and Supplier works on site, ✓ preparing reports, protocols and settlements, ✓ carrying out work acceptance procedures. Our requirements ✓ technical education (completed or in progress), e.g. Civil Engineering, Architecture, Environmental Engineering, ✓ proficient command of the MS Office suite and AutoCAD, ✓ ability to work in a team, ✓ willingness to learn and gain experience on the construction site. What we offer ✓ stable employment based on a contract of employment or a B2B contract, ✓ attractive remuneration commensurate with the tasks undertaken, ✓ support from an experienced management team, ✓ opportunity for development and work on unique projects for leading and prestigious Investors on the Polish market, ✓ training and courses to improve qualifications, ✓ company car available for use, ✓ private medical care with Medicover, ✓ group insurance with WARTA, ✓ team-building events, ✓ no dress code, ✓ coffee / tea. Apply for this position Our recruitment process is conducted in the eRecruiter system. Click the button below to fill in the application form. Go to the application form",
        "de": "Ihre Aufgaben ✓ Erstellung von Zeitplänen und Berichten, ✓ Leitung und Koordination der Bauprozesse in jeder Phase, ✓ Überwachung der Qualität und Termintreue der ausgeführten Bauarbeiten, ✓ Führung des Teams aus Ingenieuren und Bauleitern, ✓ aktive Teilnahme am Verhandlungs- und Vertragsprozess mit Subunternehmern und Lieferanten, ✓ Führung von Abstimmungen mit dem Investor und den Subunternehmern, ✓ Erstellung von Protokollen und Bauabrechnungen. Unsere Anforderungen ✓ abgeschlossenes technisches Hochschulstudium, ✓ uneingeschränkte Baugenehmigung zur Leitung von Bauarbeiten, ✓ mindestens 2 Jahre Berufserfahrung als Bauleiter im Industriebau, ✓ Fähigkeit zur Lektüre technischer Dokumentation, ✓ gute Kenntnisse in AutoCAD sowie MS Office (MS Excel, MS Project), ✓ Verfügbarkeit, ✓ Teamfähigkeit, Kommunikationsstärke, ✓ sehr gute Arbeitsorganisation, Engagement und Selbstständigkeit bei der Aufgabenerfüllung. Wir bieten ✓ stabile Anstellung auf Basis eines Arbeitsvertrags oder B2B-Vertrags, ✓ attraktive, den Aufgaben angemessene Vergütung, ✓ Unterstützung durch ein erfahrenes Führungsteam, ✓ Entwicklungsmöglichkeiten und die Arbeit an einzigartigen Projekten für führende und renommierte Investoren auf dem polnischen Markt, ✓ Schulungen und Kurse zur Qualifizierung, ✓ Möglichkeit zur Nutzung eines Dienstwagens, ✓ private medizinische Versorgung Medicover, ✓ Gruppenversicherung WARTA, ✓ Teamevents, ✓ kein Dresscode, ✓ Kaffee/Tee. Jetzt auf diese Stelle bewerben Den Einstellungsprozess führen wir im eRecruiter-System durch. Klicken Sie auf die Schaltfläche unten, um das Formular auszufüllen. Zum Bewerbungsformular",
        "hu": "Feladatkör ✓ a projekt-tervdokumentáció elemzése, ✓ az Építésvezető által megbízott feladatok megvalósítása, ✓ az Alvállalkozók és Beszállítók munkájának koordinációja az építkezésen, ✓ jelentések, jegyzőkönyvek és elszámolások készítése, ✓ munkák átvétele. Elvárásaink ✓ műszaki végzettség (befejezett vagy folyamatban), pl. Építészet, Építőmérnöki, Környezetmérnöki, ✓ az MS Office és AutoCAD magabiztos kezelése, ✓ csapatmunka-készség, ✓ tanulási és tapasztalatszerzési hajlandóság az építkezésen. Amit kínálunk ✓ stabil foglalkoztatás munkaszerződés vagy B2B alapján, ✓ vonzó, a feladatokhoz igazított javadalmazás, ✓ tapasztalt vezetői támogatás, ✓ fejlődési lehetőség és egyedi projektekben való részvétel a lengyel piac vezető és presztízsű Befektetői számára, ✓ képesítést növelő képzések és tanfolyamok, ✓ cégautó használatának lehetősége, ✓ Medicover magán-egészségbiztosítás, ✓ WARTA csoportos biztosítás, ✓ csapatépítő összejövetelek, ✓ dress code-mentes munkahely, ✓ kávé / tea. Jelentkezzen erre a pozícióra A toborzási folyamatot az eRecruiter rendszerben bonyolítjuk. Kattintson az alábbi gombra az űrlap kitöltéséhez. Ugrás a jelentkezési űrlapra",
        "cs": "Tvoje náplň práce ✓ analýza projektové dokumentace, ✓ realizace úkolů svěřených stavbyvedoucím, ✓ koordinace prací subdodavatelů a dodavatelů na stavbě, ✓ vypracování reportů, protokolů a vyúčtování, ✓ provádění přejímek prací. Naše požadavky ✓ technické vzdělání (ukončené nebo probíhající) např. stavebnictví, architektura, environmentální inženýrství, ✓ plynulá obsluha balíku MS Office a AutoCADu, ✓ schopnost týmové práce, ✓ chuť učit se a získávat zkušenosti na stavbě. Nabízíme ✓ stabilní zaměstnání na základě pracovní smlouvy nebo B2B, ✓ atraktivní ohodnocení odpovídající přijímaným úkolům, ✓ podporu zkušeného manažerského týmu, ✓ možnost rozvoje a práce na unikátních projektech pro přední a prestižní investory na polském trhu, ✓ školení a kurzy zvyšující kvalifikaci, ✓ možnost využití služebního vozu, ✓ soukromou zdravotní péči Medicover, ✓ skupinové pojištění WARTA, ✓ teambuildingové akce, ✓ žádný dress code, ✓ kávu / čaj. Ucházet se o tuto pozici Náborový proces vedeme v systému eRecruiter. Klikněte na níže uvedené tlačítko a vyplňte formulář. Přejít na přihlašovací formulář",
        "sk": "Vaša náplň práce ✓ analýza projektovej dokumentácie, ✓ realizácia úloh zadaných Vedúcim stavby, ✓ koordinácia prác Subdodávateľov a Dodávateľov na stavbe, ✓ vypracovávanie reportov, protokolov a vyúčtovaní, ✓ vykonávanie preberacích konaní prác. Naše požiadavky ✓ technické vzdelanie (ukončené alebo v procese) napr. Stavebníctvo, Architektúra, Environmentálne inžinierstvo, ✓ pokročilá znalosť balíka MS Office a AutoCAD, ✓ schopnosť pracovať v tíme, ✓ chuť učiť sa a získavať skúsenosti na stavbe. Čo ponúkame ✓ stabilné zamestnanie na základe pracovnej zmluvy alebo B2B, ✓ atraktívne ohodnotenie zodpovedajúce prijímaným úlohám, ✓ podporu skúseného manažmentu, ✓ možnosť rozvoja a prácu na unikátnych projektoch pre popredných a prestížnych Investorov na poľskom trhu, ✓ školenia a kurzy zvyšujúce kvalifikáciu, ✓ možnosť využívania služobného auta, ✓ súkromné zdravotné poistenie Medicover, ✓ skupinové poistenie WARTA, ✓ integračné stretnutia, ✓ žiaden dress code, ✓ káva / čaj. Aplikujte na túto pozíciu Náborový proces realizujeme v systéme eRecruiter. Kliknite na tlačidlo nižšie a vyplňte formulár. Prejsť na prihláškový formulár"
    },
    "order": 0
},
    {
    "title": "Kierownik Budowy",
    "slug": "kierownik-budowy",
    "text": "Twój zakres obowiązków ✓ tworzenie harmonogramów i raportów, ✓ kierowanie i koordynacja procesami budowy na każdym jej etapie, ✓ nadzorowanie jakości i terminowości wykonywanych robót budowlanych, ✓ przywództwo zespołowi Inżynierów i Kierowników Robót, ✓ czynny udział w procesie negocjacji i kontraktacji Podwykonawców i Dostawców, ✓ prowadzenie uzgodnień z Inwestorem i Podwykonawcami, ✓ sporządzanie protokołów i rozliczeń budowy. Nasze wymagania ✓ wykształcenie wyższe techniczne, ✓ uprawnienia budowlane bez ograniczeń do kierowania robotami budowlanymi, ✓ min. 2-letnie doświadczenie zawodowe na stanowisku Kierownika Budowy w branży budownictwa przemysłowego, ✓ umiejętność czytania dokumentacji technicznej, ✓ dobra znajomość AutoCAD oraz MS Office (MS Excel, MS Project), ✓ dyspozycyjność, ✓ umiejętność pracy w zespole, komunikatywność, ✓ bardzo dobra organizacja pracy, zaangażowanie i samodzielność w wykonywaniu zadań. To oferujemy ✓ stabilne zatrudnienie w oparciu o umowę o pracę lub B2B, ✓ atrakcyjne wynagrodzenie adekwatne do podejmowanych zadań, ✓ wsparcie doświadczonej kadry zarządzającej, ✓ możliwość rozwoju i pracy przy unikatowych projektach dla czołowych i prestiżowych Inwestorów na polskim rynku, ✓ szkolenia i kursy podnoszące kwalifikacje, ✓ możliwość korzystania z samochodu służbowego, ✓ prywatną opiekę medyczną Medicover, ✓ ubezpieczenie grupowe WARTA, ✓ spotkania integracyjne, ✓ brak dress code’u, ✓ kawa / herbata. Aplikuj na to stanowisko Proces rekrutacji prowadzimy w systemie eRecruiter. Kliknij poniższy przycisk, aby wypełnić formularz. Przejdź do formularza aplikacji",
    "t_t": {
        "en": "Construction Manager",
        "de": "Bauingenieur",
        "hu": "Építésvezető",
        "cs": "Stavbyvedoucí",
        "sk": "Vedúci stavby"
    },
    "t_x": {
        "en": "Your responsibilities ✓ preparing schedules and reports, ✓ managing and coordinating the construction processes at every stage, ✓ supervising the quality and timeliness of the executed construction works, ✓ leading the team of Engineers and Site Managers, ✓ active participation in the negotiation and contracting process with Subcontractors and Suppliers, ✓ conducting arrangements with the Investor and Subcontractors, ✓ drawing up site protocols and settlements. Our requirements ✓ higher technical education, ✓ unlimited construction licence to manage construction works, ✓ minimum 2 years of professional experience as a Construction Manager in the industrial construction sector, ✓ ability to read technical documentation, ✓ good command of AutoCAD and MS Office (MS Excel, MS Project), ✓ availability, ✓ ability to work in a team, good communication skills, ✓ very good work organisation, commitment and independence in performing tasks. What we offer ✓ stable employment based on a contract of employment or a B2B contract, ✓ attractive remuneration commensurate with the tasks undertaken, ✓ support from an experienced management team, ✓ opportunity for development and work on unique projects for leading and prestigious Investors on the Polish market, ✓ training and courses to improve qualifications, ✓ company car available for use, ✓ private medical care with Medicover, ✓ group insurance with WARTA, ✓ team-building events, ✓ no dress code, ✓ coffee / tea. Apply for this position Our recruitment process is conducted in the eRecruiter system. Click the button below to fill in the application form. Go to the application form",
        "de": "Ihre Aufgaben ✓ Analyse der Projektdokumentation, ✓ Umsetzung der vom Bauleiter übertragenen Aufgaben, ✓ Koordination der Arbeiten von Subunternehmern und Lieferanten auf der Baustelle, ✓ Erstellung von Berichten, Protokollen und Abrechnungen, ✓ Durchführung der Abnahmen von Bauleistungen. Unsere Anforderungen ✓ Technische Ausbildung (abgeschlossen oder laufend), z. B. Bauingenieurwesen, Architektur, Umweltingenieurwesen, ✓ sichere Beherrschung des MS-Office-Pakets und AutoCAD, ✓ Teamfähigkeit, ✓ Lernbereitschaft und Bereitschaft, Erfahrung auf der Baustelle zu sammeln. Wir bieten ✓ stabile Anstellung auf Basis eines Arbeitsvertrags oder B2B-Vertrags, ✓ attraktive, den Aufgaben angemessene Vergütung, ✓ Unterstützung durch ein erfahrenes Führungsteam, ✓ Entwicklungsmöglichkeiten und die Arbeit an einzigartigen Projekten für führende und renommierte Investoren auf dem polnischen Markt, ✓ Schulungen und Kurse zur Qualifizierung, ✓ Möglichkeit zur Nutzung eines Dienstwagens, ✓ private medizinische Versorgung Medicover, ✓ Gruppenversicherung WARTA, ✓ Teamevents, ✓ kein Dresscode, ✓ Kaffee/Tee. Jetzt auf diese Stelle bewerben Den Einstellungsprozess führen wir im eRecruiter-System durch. Klicken Sie auf die Schaltfläche unten, um das Formular auszufüllen. Zum Bewerbungsformular",
        "hu": "Feladatkör ✓ ütemtervek és jelentések készítése, ✓ az építési folyamatok irányítása és koordinációja minden szakaszban, ✓ a kivitelezési munkák minőségének és határidejének felügyelete, ✓ a Mérnökök és Munkavezetők csapatának vezetése, ✓ aktív részvétel az Alvállalkozók és Beszállítók kiválasztásának és szerződéskötésének folyamatában, ✓ egyeztetések vezetése a Befektetővel és az Alvállalkozókkal, ✓ jegyzőkönyvek és elszámolások készítése. Elvárásaink ✓ felsőfokú műszaki végzettség, ✓ korlátozás nélküli építési jogosítvány építési munkák irányítására, ✓ legalább 2 éves szakmai tapasztalat Építésvezetői pozícióban az ipari építés területén, ✓ műszaki dokumentáció olvasásának képessége, ✓ AutoCAD és MS Office (MS Excel, MS Project) magas szintű ismerete, ✓ rendelkezésre állás, ✓ csapatmunka-készség, kommunikáció, ✓ kiváló munkaszervezés, elkötelezettség és önállóság a feladatok végrehajtásában. Amit kínálunk ✓ stabil foglalkoztatás munkaszerződés vagy B2B alapján, ✓ vonzó, a feladatokhoz igazított javadalmazás, ✓ tapasztalt vezetői támogatás, ✓ fejlődési lehetőség és egyedi projektekben való részvétel a lengyel piac vezető és presztízsű Befektetői számára, ✓ képesítést növelő képzések és tanfolyamok, ✓ cégautó használatának lehetősége, ✓ Medicover magán-egészségbiztosítás, ✓ WARTA csoportos biztosítás, ✓ csapatépítő összejövetelek, ✓ dress code-mentes munkahely, ✓ kávé / tea. Jelentkezzen erre a pozícióra A toborzási folyamatot az eRecruiter rendszerben bonyolítjuk. Kattintson az alábbi gombra az űrlap kitöltéséhez. Ugrás a jelentkezési űrlapra",
        "cs": "Tvoje náplň práce ✓ vytváření harmonogramů a reportů, ✓ řízení a koordinace stavebních procesů v každé jejich fázi, ✓ dohled nad kvalitou a včasností prováděných stavebních prací, ✓ vedení týmu inženýrů a vedoucích prací, ✓ aktivní účast na vyjednávání a smluvním zajištění subdodavatelů a dodavatelů, ✓ vedení dohod s investorem a subdodavateli, ✓ vypracování protokolů a vyúčtování stavby. Naše požadavky ✓ vysokoškolské technické vzdělání, ✓ neomezená stavební oprávnění k řízení stavebních prací, ✓ min. 2letá odborná praxe na pozici stavbyvedoucího v oblasti průmyslového stavitelství, ✓ schopnost čtení technické dokumentace, ✓ dobrá znalost AutoCADu a MS Office (MS Excel, MS Project), ✓ disponibilita, ✓ schopnost týmové práce, komunikativnost, ✓ velmi dobrá organizace práce, angažovanost a samostatnost při plnění úkolů. Nabízíme ✓ stabilní zaměstnání na základě pracovní smlouvy nebo B2B, ✓ atraktivní ohodnocení odpovídající přijímaným úkolům, ✓ podporu zkušeného manažerského týmu, ✓ možnost rozvoje a práce na unikátních projektech pro přední a prestižní investory na polském trhu, ✓ školení a kurzy zvyšující kvalifikaci, ✓ možnost využití služebního vozu, ✓ soukromou zdravotní péči Medicover, ✓ skupinové pojištění WARTA, ✓ teambuildingové akce, ✓ žádný dress code, ✓ kávu / čaj. Ucházet se o tuto pozici Náborový proces vedeme v systému eRecruiter. Klikněte na níže uvedené tlačítko a vyplňte formulář. Přejít na přihlašovací formulář",
        "sk": "Vaša náplň práce ✓ tvorba harmonogramov a reportov, ✓ riadenie a koordinácia stavebných procesov v každej ich fáze, ✓ dohľad nad kvalitou a včasnosťou vykonávaných stavebných prác, ✓ vedenie tímu Inžinierov a Vedúcich prác, ✓ aktívna účasť na procese vyjednávania a kontraktácie Subdodávateľov a Dodávateľov, ✓ vedenie rokovaní s Investorom a Subdodávateľmi, ✓ vypracovávanie protokolov a vyúčtovaní stavby. Naše požiadavky ✓ vysokoškolské technické vzdelanie, ✓ stavebné oprávnenie bez obmedzení na riadenie stavebných prác, ✓ min. 2-ročná pracovná skúsenosť na pozícii Vedúceho stavby v oblasti priemyselného stavebníctva, ✓ schopnosť čítať technickú dokumentáciu, ✓ dobrá znalosť AutoCADu a MS Office (MS Excel, MS Project), ✓ disponibilita, ✓ schopnosť pracovať v tíme, komunikatívnosť, ✓ veľmi dobrá organizácia práce, angažovanosť a samostatnosť pri plnení úloh. Čo ponúkame ✓ stabilné zamestnanie na základe pracovnej zmluvy alebo B2B, ✓ atraktívne ohodnotenie zodpovedajúce prijímaným úlohám, ✓ podporu skúseného manažmentu, ✓ možnosť rozvoja a prácu na unikátnych projektoch pre popredných a prestížnych Investorov na poľskom trhu, ✓ školenia a kurzy zvyšujúce kvalifikáciu, ✓ možnosť využívania služobného auta, ✓ súkromné zdravotné poistenie Medicover, ✓ skupinové poistenie WARTA, ✓ integračné stretnutia, ✓ žiaden dress code, ✓ káva / čaj. Aplikujte na túto pozíciu Náborový proces realizujeme v systéme eRecruiter. Kliknite na tlačidlo nižšie a vyplňte formulár. Prejsť na prihláškový formulár"
    },
    "order": 0
},
    {
    "title": "Kierownik Robót",
    "slug": "kierownik-robot",
    "text": "Twój zakres obowiązków ✓ tworzenie harmonogramów i raportów, ✓ kierowanie i koordynacja procesami budowy na każdym jej etapie, ✓ nadzorowanie jakości i terminowości wykonywanych robót budowlanych, ✓ przywództwo zespołowi Inżynierów, ✓ czynny udział w procesie negocjacji i kontraktacji Podwykonawców i Dostawców, ✓ prowadzenie uzgodnień z Inwestorem i Podwykonawcami, ✓ sporządzanie protokołów i rozliczeń budowy. Nasze wymagania ✓ wykształcenie wyższe techniczne, ✓ uprawnienia budowlane bez ograniczeń do kierowania robotami budowlanymi, ✓ minimum roczne doświadczenie na stanowisku Kierownika Robót, ✓ umiejętność czytania dokumentacji technicznej, ✓ dobra znajomość AutoCAD oraz MS Office (MS Excel, MS Project), ✓ dyspozycyjność, ✓ umiejętność pracy w zespole, komunikatywność, ✓ bardzo dobra organizacja pracy, zaangażowanie i samodzielność w wykonywaniu zadań. To oferujemy ✓ stabilne zatrudnienie w oparciu o umowę o pracę lub B2B, ✓ atrakcyjne wynagrodzenie adekwatne do podejmowanych zadań, ✓ wsparcie doświadczonej kadry zarządzającej, ✓ możliwość rozwoju i pracy przy unikatowych projektach dla czołowych i prestiżowych Inwestorów na polskim rynku, ✓ szkolenia i kursy podnoszące kwalifikacje, ✓ możliwość korzystania z samochodu służbowego, ✓ prywatną opiekę medyczną Medicover, ✓ ubezpieczenie grupowe WARTA, ✓ spotkania integracyjne, Aplikuj na to stanowisko Proces rekrutacji prowadzimy w systemie eRecruiter. Kliknij poniższy przycisk, aby wypełnić formularz. Przejdź do formularza aplikacji",
    "t_t": {
        "en": "Site Manager",
        "de": "Bauleiter (Kierownik Robót)",
        "hu": "Munkavezető",
        "cs": "Vedoucí prací",
        "sk": "Vedúci prác"
    },
    "t_x": {
        "en": "Your responsibilities ✓ preparing schedules and reports, ✓ managing and coordinating the construction processes at every stage, ✓ supervising the quality and timeliness of the executed construction works, ✓ leading the team of Engineers, ✓ active participation in the negotiation and contracting process with Subcontractors and Suppliers, ✓ conducting arrangements with the Investor and Subcontractors, ✓ drawing up site protocols and settlements. Our requirements ✓ higher technical education, ✓ unlimited construction licence to manage construction works, ✓ minimum one year of experience as a Site Manager, ✓ ability to read technical documentation, ✓ good command of AutoCAD and MS Office (MS Excel, MS Project), ✓ availability, ✓ ability to work in a team, good communication skills, ✓ very good work organisation, commitment and independence in performing tasks. What we offer ✓ stable employment based on a contract of employment or a B2B contract, ✓ attractive remuneration commensurate with the tasks undertaken, ✓ support from an experienced management team, ✓ opportunity for development and work on unique projects for leading and prestigious Investors on the Polish market, ✓ training and courses to improve qualifications, ✓ company car available for use, ✓ private medical care with Medicover, ✓ group insurance with WARTA, ✓ team-building events, Apply for this position Our recruitment process is conducted in the eRecruiter system. Click the button below to fill in the application form. Go to the application form",
        "de": "Ihre Aufgaben ✓ Erstellung von Zeitplänen und Berichten, ✓ Leitung und Koordination der Bauprozesse in jeder Phase, ✓ Überwachung der Qualität und Termintreue der ausgeführten Bauarbeiten, ✓ Führung des Ingenieurteams, ✓ aktive Teilnahme am Verhandlungs- und Vertragsprozess mit Subunternehmern und Lieferanten, ✓ Führung von Abstimmungen mit dem Investor und den Subunternehmern, ✓ Erstellung von Protokollen und Bauabrechnungen. Unsere Anforderungen ✓ abgeschlossenes technisches Hochschulstudium, ✓ uneingeschränkte Baugenehmigung zur Leitung von Bauarbeiten, ✓ mindestens einjährige Erfahrung als Bauleiter (Kierownik Robót), ✓ Fähigkeit zur Lektüre technischer Dokumentation, ✓ gute Kenntnisse in AutoCAD sowie MS Office (MS Excel, MS Project), ✓ Verfügbarkeit, ✓ Teamfähigkeit, Kommunikationsstärke, ✓ sehr gute Arbeitsorganisation, Engagement und Selbstständigkeit bei der Aufgabenerfüllung. Wir bieten ✓ stabile Anstellung auf Basis eines Arbeitsvertrags oder B2B-Vertrags, ✓ attraktive, den Aufgaben angemessene Vergütung, ✓ Unterstützung durch ein erfahrenes Führungsteam, ✓ Entwicklungsmöglichkeiten und die Arbeit an einzigartigen Projekten für führende und renommierte Investoren auf dem polnischen Markt, ✓ Schulungen und Kurse zur Qualifizierung, ✓ Möglichkeit zur Nutzung eines Dienstwagens, ✓ private medizinische Versorgung Medicover, ✓ Gruppenversicherung WARTA, ✓ Teamevents. Jetzt auf diese Stelle bewerben Den Einstellungsprozess führen wir im eRecruiter-System durch. Klicken Sie auf die Schaltfläche unten, um das Formular auszufüllen. Zum Bewerbungsformular",
        "hu": "Feladatkör ✓ ütemtervek és jelentések készítése, ✓ az építési folyamatok irányítása és koordinációja minden szakaszban, ✓ a kivitelezési munkák minőségének és határidejének felügyelete, ✓ a Mérnökök csapatának vezetése, ✓ aktív részvétel az Alvállalkozók és Beszállítók kiválasztásának és szerződéskötésének folyamatában, ✓ egyeztetések vezetése a Befektetővel és az Alvállalkozókkal, ✓ jegyzőkönyvek és elszámolások készítése. Elvárásaink ✓ felsőfokú műszaki végzettség, ✓ korlátozás nélküli építési jogosítvány építési munkák irányítására, ✓ legalább egyéves tapasztalat Munkavezetői pozícióban, ✓ műszaki dokumentáció olvasásának képessége, ✓ AutoCAD és MS Office (MS Excel, MS Project) magas szintű ismerete, ✓ rendelkezésre állás, ✓ csapatmunka-készség, kommunikáció, ✓ kiváló munkaszervezés, elkötelezettség és önállóság a feladatok végrehajtásában. Amit kínálunk ✓ stabil foglalkoztatás munkaszerződés vagy B2B alapján, ✓ vonzó, a feladatokhoz igazított javadalmazás, ✓ tapasztalt vezetői támogatás, ✓ fejlődési lehetőség és egyedi projektekben való részvétel a lengyel piac vezető és presztízsű Befektetői számára, ✓ képesítést növelő képzések és tanfolyamok, ✓ cégautó használatának lehetősége, ✓ Medicover magán-egészségbiztosítás, ✓ WARTA csoportos biztosítás, ✓ csapatépítő összejövetelek. Jelentkezzen erre a pozícióra A toborzási folyamatot az eRecruiter rendszerben bonyolítjuk. Kattintson az alábbi gombra az űrlap kitöltéséhez. Ugrás a jelentkezési űrlapra",
        "cs": "Tvoje náplň práce ✓ vytváření harmonogramů a reportů, ✓ řízení a koordinace stavebních procesů v každé jejich fázi, ✓ dohled nad kvalitou a včasností prováděných stavebních prací, ✓ vedení týmu inženýrů, ✓ aktivní účast na vyjednávání a smluvním zajištění subdodavatelů a dodavatelů, ✓ vedení dohod s investorem a subdodavateli, ✓ vypracování protokolů a vyúčtování stavby. Naše požadavky ✓ vysokoškolské technické vzdělání, ✓ neomezená stavební oprávnění k řízení stavebních prací, ✓ minimálně roční praxe na pozici vedoucího prací, ✓ schopnost čtení technické dokumentace, ✓ dobrá znalost AutoCADu a MS Office (MS Excel, MS Project), ✓ disponibilita, ✓ schopnost týmové práce, komunikativnost, ✓ velmi dobrá organizace práce, angažovanost a samostatnost při plnění úkolů. Nabízíme ✓ stabilní zaměstnání na základě pracovní smlouvy nebo B2B, ✓ atraktivní ohodnocení odpovídající přijímaným úkolům, ✓ podporu zkušeného manažerského týmu, ✓ možnost rozvoje a práce na unikátních projektech pro přední a prestižní investory na polském trhu, ✓ školení a kurzy zvyšující kvalifikaci, ✓ možnost využití služebního vozu, ✓ soukromou zdravotní péči Medicover, ✓ skupinové pojištění WARTA, ✓ teambuildingové akce, Ucházet se o tuto pozici Náborový proces vedeme v systému eRecruiter. Klikněte na níže uvedené tlačítko a vyplňte formulář. Přejít na přihlašovací formulář",
        "sk": "Vaša náplň práce ✓ tvorba harmonogramov a reportov, ✓ riadenie a koordinácia stavebných procesov v každej ich fáze, ✓ dohľad nad kvalitou a včasnosťou vykonávaných stavebných prác, ✓ vedenie tímu Inžinierov, ✓ aktívna účasť na procese vyjednávania a kontraktácie Subdodávateľov a Dodávateľov, ✓ vedenie rokovaní s Investorom a Subdodávateľmi, ✓ vypracovávanie protokolov a vyúčtovaní stavby. Naše požiadavky ✓ vysokoškolské technické vzdelanie, ✓ stavebné oprávnenie bez obmedzení na riadenie stavebných prác, ✓ minimálne ročná skúsenosť na pozícii Vedúceho prác, ✓ schopnosť čítať technickú dokumentáciu, ✓ dobrá znalosť AutoCADu a MS Office (MS Excel, MS Project), ✓ disponibilita, ✓ schopnosť pracovať v tíme, komunikatívnosť, ✓ veľmi dobrá organizácia práce, angažovanosť a samostatnosť pri plnení úloh. Čo ponúkame ✓ stabilné zamestnanie na základe pracovnej zmluvy alebo B2B, ✓ atraktívne ohodnotenie zodpovedajúce prijímaným úlohám, ✓ podporu skúseného manažmentu, ✓ možnosť rozvoja a prácu na unikátnych projektoch pre popredných a prestížnych Investorov na poľskom trhu, ✓ školenia a kurzy zvyšujúce kvalifikáciu, ✓ možnosť využívania služobného auta, ✓ súkromné zdravotné poistenie Medicover, ✓ skupinové poistenie WARTA, ✓ integračné stretnutia, Aplikujte na túto pozíciu Náborový proces realizujeme v systéme eRecruiter. Kliknite na tlačidlo nižšie a vyplňte formulár. Prejsť na prihláškový formulár"
    },
    "order": 0
},
    {
    "title": "Kosztorysant / Specjalista ds. ofert",
    "slug": "kosztorysant-specjalista-ds-ofert",
    "text": "Twój zakres obowiązków ✓ analiza dokumentacji projektowej, ✓ przedmiarowanie robót, ✓ opracowywanie i prowadzenie dokumentacji ofertowej, ✓ pozyskiwanie i analiza ofert od podwykonawców/dostawców, ✓ przygotowywanie zestawień i porównań ofert, ✓ przygotowywanie kosztorysów/wycen zgodnie z dokumentacją projektową. Nasze wymagania ✓ wykształcenie wyższe lub w trakcie – budownictwo, architektura, inżynieria środowiska lub pokrewne, ✓ doświadczenie na porównywalnym stanowisku przy ofertowaniu lub kontraktowaniu robót dla budowy obiektów przemysłowych, ✓ znajomość pakietu MS Office (biegła obsługa MS Excel), ✓ umiejętność czytania rysunków i dokumentacji technicznej, ✓ samodzielność, zaangażowanie i dobra organizacja pracy. To oferujemy ✓ stabilne zatrudnienie w oparciu o umowę o pracę lub B2B, ✓ atrakcyjne wynagrodzenie adekwatne do podejmowanych zadań, ✓ wsparcie doświadczonej kadry zarządzającej, ✓ możliwość rozwoju i pracy przy unikatowych projektach dla czołowych i prestiżowych Inwestorów na polskim rynku, ✓ szkolenia i kursy podnoszące kwalifikacje, ✓ możliwość korzystania z samochodu służbowego, ✓ prywatną opiekę medyczną Medicover, ✓ ubezpieczenie grupowe WARTA, ✓ spotkania integracyjne, ✓ brak dress code’u, ✓ kawa / herbata. Aplikuj na to stanowisko Proces rekrutacji prowadzimy w systemie eRecruiter. Kliknij poniższy przycisk, aby wypełnić formularz. Przejdź do formularza aplikacji",
    "t_t": {
        "en": "Cost Estimator / Tender Specialist",
        "de": "Kalkulator / Angebotsspezialist",
        "hu": "Költségvetés-készítő / Ajánlat-szakreferő",
        "cs": "Rozpočtář / Specialista nabídek",
        "sk": "Rozpočtár / Špecialista na ponuky"
    },
    "t_x": {
        "en": "Your responsibilities ✓ analysis of design documentation, ✓ taking off quantities, ✓ preparing and maintaining tender documentation, ✓ obtaining and analysing offers from subcontractors/suppliers, ✓ preparing offer comparisons and summaries, ✓ preparing cost estimates/valuations in accordance with the design documentation. Our requirements ✓ higher education or in progress – civil engineering, architecture, environmental engineering or related, ✓ experience in a comparable position in tendering or contracting works for the construction of industrial buildings, ✓ command of the MS Office suite (proficient use of MS Excel), ✓ ability to read drawings and technical documentation, ✓ independence, commitment and good work organisation. What we offer ✓ stable employment based on a contract of employment or a B2B contract, ✓ attractive remuneration commensurate with the tasks undertaken, ✓ support from an experienced management team, ✓ opportunity for development and work on unique projects for leading and prestigious Investors on the Polish market, ✓ training and courses to improve qualifications, ✓ company car available for use, ✓ private medical care with Medicover, ✓ group insurance with WARTA, ✓ team-building events, ✓ no dress code, ✓ coffee / tea. Apply for this position Our recruitment process is conducted in the eRecruiter system. Click the button below to fill in the application form. Go to the application form",
        "de": "Ihre Aufgaben ✓ Analyse der Projektdokumentation, ✓ Vormessung der Bauleistungen, ✓ Erstellung und Führung der Angebotsdokumentation, ✓ Einholung und Analyse von Angeboten von Subunternehmern/Lieferanten, ✓ Erstellung von Angebotszusammenstellungen und -vergleichen, ✓ Erstellung von Kostenvoranschlägen/Kalkulationen gemäß der Projektdokumentation. Unsere Anforderungen ✓ abgeschlossenes oder laufendes Hochschulstudium – Bauingenieurwesen, Architektur, Umweltingenieurwesen oder verwandte Bereiche, ✓ Erfahrung in einer vergleichbaren Position in der Angebotserstellung oder Vertragsvergabe von Bauleistungen für Industrieobjekte, ✓ sichere Beherrschung des MS-Office-Pakets (insbesondere MS Excel), ✓ Fähigkeit zur Lektüre von Zeichnungen und technischer Dokumentation, ✓ Selbstständigkeit, Engagement und gute Arbeitsorganisation. Wir bieten ✓ stabile Anstellung auf Basis eines Arbeitsvertrags oder B2B-Vertrags, ✓ attraktive, den Aufgaben angemessene Vergütung, ✓ Unterstützung durch ein erfahrenes Führungsteam, ✓ Entwicklungsmöglichkeiten und die Arbeit an einzigartigen Projekten für führende und renommierte Investoren auf dem polnischen Markt, ✓ Schulungen und Kurse zur Qualifizierung, ✓ Möglichkeit zur Nutzung eines Dienstwagens, ✓ private medizinische Versorgung Medicover, ✓ Gruppenversicherung WARTA, ✓ Teamevents, ✓ kein Dresscode, ✓ Kaffee/Tee. Jetzt auf diese Stelle bewerben Den Einstellungsprozess führen wir im eRecruiter-System durch. Klicken Sie auf die Schaltfläche unten, um das Formular auszufüllen. Zum Bewerbungsformular",
        "hu": "Feladatkör ✓ a projekt-tervdokumentáció elemzése, ✓ mennyiségi kimutatások készítése, ✓ az ajánlati dokumentáció kidolgozása és vezetése, ✓ alvállalkozói/beszállítói ajánlatok beszerzése és elemzése, ✓ ajánlati összesítések és összehasonlítások készítése, ✓ költségvetések/árajánlatok készítése a projekt-tervdokumentációnak megfelelően. Elvárásaink ✓ felsőfokú végzettség vagy folyamatban – építészet, építőmérnöki, környezetmérnöki vagy kapcsolódó terület, ✓ tapasztalat hasonló pozícióban ipari létesítmények kivitelezésének ajánlásában vagy szerződéskötésében, ✓ MS Office csomag ismerete (MS Excel magabiztos kezelése), ✓ műszaki rajzok és dokumentáció olvasásának képessége, ✓ önállóság, elkötelezettség és jó munkaszervezés. Amit kínálunk ✓ stabil foglalkoztatás munkaszerződés vagy B2B alapján, ✓ vonzó, a feladatokhoz igazított javadalmazás, ✓ tapasztalt vezetői támogatás, ✓ fejlődési lehetőség és egyedi projektekben való részvétel a lengyel piac vezető és presztízsű Befektetői számára, ✓ képesítést növelő képzések és tanfolyamok, ✓ cégautó használatának lehetősége, ✓ Medicover magán-egészségbiztosítás, ✓ WARTA csoportos biztosítás, ✓ csapatépítő összejövetelek, ✓ dress code-mentes munkahely, ✓ kávé / tea. Jelentkezzen erre a pozícióra A toborzási folyamatot az eRecruiter rendszerben bonyolítjuk. Kattintson az alábbi gombra az űrlap kitöltéséhez. Ugrás a jelentkezési űrlapra",
        "cs": "Tvoje náplň práce ✓ analýza projektové dokumentace, ✓ výkazy výměr, ✓ zpracování a vedení nabídkové dokumentace, ✓ získávání a analýza nabídek od subdodavatelů/dodavatelů, ✓ příprava srovnání nabídek, ✓ příprava rozpočtů/kalkulací v souladu s projektovou dokumentací. Naše požadavky ✓ vysokoškolské vzdělání nebo probíhající – stavebnictví, architektura, environmentální inženýrství nebo příbuzné obory, ✓ zkušenosti na srovnatelné pozici v nabídkování nebo smluvním zajištění prací pro výstavbu průmyslových objektů, ✓ znalost balíku MS Office (pokročilá obsluha MS Excel), ✓ schopnost čtení výkresů a technické dokumentace, ✓ samostatnost, angažovanost a dobrá organizace práce. Nabízíme ✓ stabilní zaměstnání na základě pracovní smlouvy nebo B2B, ✓ atraktivní ohodnocení odpovídající přijímaným úkolům, ✓ podporu zkušeného manažerského týmu, ✓ možnost rozvoje a práce na unikátních projektech pro přední a prestižní investory na polském trhu, ✓ školení a kurzy zvyšující kvalifikaci, ✓ možnost využití služebního vozu, ✓ soukromou zdravotní péči Medicover, ✓ skupinové pojištění WARTA, ✓ teambuildingové akce, ✓ žádný dress code, ✓ kávu / čaj. Ucházet se o tuto pozici Náborový proces vedeme v systému eRecruiter. Klikněte na níže uvedené tlačítko a vyplňte formulář. Přejít na přihlašovací formulář",
        "sk": "Vaša náplň práce ✓ analýza projektovej dokumentácie, ✓ výkaz výmer prác, ✓ spracovanie a vedenie ponukovej dokumentácie, ✓ získavanie a analýza ponúk od subdodávateľov/dodávateľov, ✓ príprava súpisov a porovnaní ponúk, ✓ príprava rozpočtov/ocenení v súlade s projektovou dokumentáciou. Naše požiadavky ✓ vysokoškolské vzdelanie alebo v procese – stavebníctvo, architektúra, environmentálne inžinierstvo alebo príbuzné odbory, ✓ skúsenosť na porovnateľnej pozícii pri ponukovom konaní alebo kontraktácii prác pre výstavbu priemyselných objektov, ✓ znalosť balíka MS Office (pokročilá znalosť MS Excel), ✓ schopnosť čítať výkresy a technickú dokumentáciu, ✓ samostatnosť, angažovanosť a dobrá organizácia práce. Čo ponúkame ✓ stabilné zamestnanie na základe pracovnej zmluvy alebo B2B, ✓ atraktívne ohodnotenie zodpovedajúce prijímaným úlohám, ✓ podporu skúseného manažmentu, ✓ možnosť rozvoja a prácu na unikátnych projektoch pre popredných a prestížnych Investorov na poľskom trhu, ✓ školenia a kurzy zvyšujúce kvalifikáciu, ✓ možnosť využívania služobného auta, ✓ súkromné zdravotné poistenie Medicover, ✓ skupinové poistenie WARTA, ✓ integračné stretnutia, ✓ žiaden dress code, ✓ káva / čaj. Aplikujte na túto pozíciu Náborový proces realizujeme v systéme eRecruiter. Kliknite na tlačidlo nižšie a vyplňte formulár. Prejsť na prihláškový formulár"
    },
    "order": 0
},
    {
    "title": "Manager ds. handlowych",
    "slug": "manager-ds-handlowych",
    "text": "Twój zakres obowiązków ✓ aktywne pozyskiwanie nowych klientów w sektorze budowlanym, ✓ analiza rynku inwestycji przemysłowych, magazynowych i usługowych, ✓ budowanie i utrzymywanie długofalowych relacji z potencjalnymi klientami, ✓ identyfikacja nowych szans sprzedażowych i zdobywanie kontaktów biznesowych, ✓ reprezentowanie firmy na targach, konferencjach i wydarzeniach branżowych, ✓ ścisła współpraca z działem marketingu w zakresie działań wizerunkowych i lead generation, ✓ współtworzenie strategii PR i sprzedażowej wraz z Dyrektorem Handlowym, ✓ przygotowywanie ofert, prezentacji oraz materiałów handlowych. Nasze wymagania ✓ doświadczenie w pracy na stanowisku o podobnym charakterze, ✓ znajomość rynku budowlanego, ✓ wykształcenie techniczne, ✓ znajomość rynku nieruchomości komercyjnych (hale przemysłowe, magazyny, obiekty usługowe), ✓ wysoko rozwinięte umiejętności komunikacyjne i negocjacyjne, ✓ proaktywność, samodzielność i umiejętność budowania relacji biznesowych, ✓ nastawienie na realizację celów sprzedażowych, ✓ umiejętność reprezentowania firmy w kontaktach z klientami oraz podczas wydarzeń branżowych, ✓ prawo jazdy kat. B, ✓ gotowość do krótkoterminowych wyjazdów. To oferujemy ✓ stabilne zatrudnienie w oparciu o umowę o pracę lub B2B, ✓ atrakcyjne wynagrodzenie adekwatne do podejmowanych zadań (stała podstawa wynagrodzenia), ✓ wsparcie doświadczonej kadry zarządzającej, ✓ możliwość rozwoju i pracy przy unikatowych projektach dla czołowych i prestiżowych Inwestorów na polskim rynku, ✓ certyfikowane szkolenia i kursy podnoszące kwalifikacje, ✓ samochód służbowy, ✓ możliwość pracy hybrydowej, ✓ prywatną opiekę medyczną Medicover, ✓ ubezpieczenia grupowe WARTA, ✓ spotkania integracyjne, ✓ brak dress code’u, ✓ kawa / herbata w biurze. Aplikuj na to stanowisko Proces rekrutacji prowadzimy w systemie eRecruiter. Kliknij poniższy przycisk, aby wypełnić formularz. Przejdź do formularza aplikacji",
    "t_t": {
        "en": "Sales Manager",
        "de": "Junior HR-Spezialist",
        "hu": "Kereskedelmi Manager",
        "cs": "Obchodní manažer",
        "sk": "Obchodný manažér"
    },
    "t_x": {
        "en": "Your responsibilities ✓ actively acquiring new clients in the construction sector, ✓ analysing the industrial, warehouse and service investment market, ✓ building and maintaining long-term relationships with potential clients, ✓ identifying new sales opportunities and developing business contacts, ✓ representing the company at trade fairs, conferences and industry events, ✓ close cooperation with the marketing department on image-building and lead generation activities, ✓ co-creating the PR and sales strategy together with the Sales Director, ✓ preparing offers, presentations and sales materials. Our requirements ✓ experience in a position of a similar nature, ✓ knowledge of the construction market, ✓ technical education, ✓ knowledge of the commercial real estate market (industrial halls, warehouses, service buildings), ✓ highly developed communication and negotiation skills, ✓ proactivity, independence and ability to build business relationships, ✓ focus on achieving sales targets, ✓ ability to represent the company in contacts with clients and during industry events, ✓ category B driving licence, ✓ readiness for short-term business trips. What we offer ✓ stable employment based on a contract of employment or a B2B contract, ✓ attractive remuneration commensurate with the tasks undertaken (fixed base salary), ✓ support from an experienced management team, ✓ opportunity for development and work on unique projects for leading and prestigious Investors on the Polish market, ✓ certified training and courses to improve qualifications, ✓ company car, ✓ hybrid work option, ✓ private medical care with Medicover, ✓ group insurance with WARTA, ✓ team-building events, ✓ no dress code, ✓ coffee / tea in the office. Apply for this position Our recruitment process is conducted in the eRecruiter system. Click the button below to fill in the application form. Go to the application form",
        "de": "Ihre Aufgaben ✓ Führung von Einstellungsprozessen, ✓ Unterstützung des Onboarding-Prozesses (Erstellung von Verträgen und einstellungsbezogenen Dokumenten, Koordination von ärztlichen Untersuchungen, Arbeitsschutzunterweisungen sowie Maßnahmen zur Arbeitsplatzvorbereitung), ✓ Führung und Aktualisierung der Personalakten gemäß den geltenden Vorschriften, ✓ Überwachung der Gültigkeitsfristen von ärztlichen Untersuchungen und Arbeitsschutzunterweisungen, ✓ Führung und Aktualisierung der Dokumentation des Qualitätsmanagementsystems, ✓ Unterstützung bei der Organisation von Schulungen und Teamevents, ✓ Organisation von Schulungen und Kursen sowie Teamevents, ✓ laufende Bearbeitung von Mitarbeiterangelegenheiten und HR-Prozessen. Unsere Anforderungen ✓ mindestens einjährige Erfahrung im Bereich Personal/HR, ✓ Grundkenntnisse im Arbeitsrecht, ✓ sehr gute Selbstorganisation, ✓ Selbstständigkeit und Verantwortungsbewusstsein bei der Aufgabenerfüllung, ✓ Genauigkeit und Liebe zum Detail, ✓ ausgeprägte Kommunikationsfähigkeiten, ✓ zusätzlicher Vorteil sind abgeschlossene Kurse oder Schulungen im Bereich Personal und Lohnbuchhaltung. Wir bieten ✓ stabile Anstellung auf Basis eines Arbeitsvertrags, ✓ Entwicklungsmöglichkeiten, ✓ Schulungen und Kurse zur Qualifizierung, ✓ freundliche Atmosphäre, ✓ sehr gute Arbeitsbedingungen in einem modernen Büro mit Küchen- und Sozialbereich, ✓ Arbeit von Montag bis Freitag, 8:00 – 16:00 Uhr, ✓ private medizinische Versorgung Medicover, Gruppenversicherung WARTA. Jetzt auf diese Stelle bewerben Den Einstellungsprozess führen wir im eRecruiter-System durch. Klicken Sie auf die Schaltfläche unten, um das Formular auszufüllen. Zum Bewerbungsformular",
        "hu": "Feladatkör ✓ új ügyfelek aktív felkutatása az építőipari szektorban, ✓ az ipari, raktári és szolgáltató beruházások piacának elemzése, ✓ hosszú távú kapcsolatok építése és fenntartása a potenciális ügyfelekkel, ✓ új értékesítési lehetőségek azonosítása és üzleti kapcsolatok szerzése, ✓ a vállalat képviselete vásárokon, konferenciákon és szakmai rendezvényeken, ✓ szoros együttműködés a marketing osztállyal az imázs- és lead-generálási tevékenységek terén, ✓ a PR- és értékesítési stratégia közös kialakítása a Kereskedelmi Igazgatóval, ✓ ajánlatok, prezentációk és kereskedelmi anyagok készítése. Elvárásaink ✓ tapasztalat hasonló jellegű pozícióban, ✓ az építési piac ismerete, ✓ műszaki végzettség, ✓ a kereskedelmi ingatlanok piacának ismerete (ipari csarnokok, raktárak, szolgáltató létesítmények), ✓ fejlett kommunikációs és tárgyalási készségek, ✓ proaktivitás, önállóság és az üzleti kapcsolatok építésének képessége, ✓ értékesítési célok teljesítésére való törekvés, ✓ a vállalat ügyfelekkel és szakmai rendezvényeken való képviseleti képessége, ✓ B kategóriás jogosítvány, ✓ rövid távú utazásokra való hajlandóság. Amit kínálunk ✓ stabil foglalkoztatás munkaszerződés vagy B2B alapján, ✓ vonzó, a feladatokhoz igazított javadalmazás (alapfizetés), ✓ tapasztalt vezetői támogatás, ✓ fejlődési lehetőség és egyedi projektekben való részvétel a lengyel piac vezető és presztízsű Befektetői számára, ✓ tanúsított képesítést növelő képzések és tanfolyamok, ✓ cégautó, ✓ hibrid munkavégzés lehetősége, ✓ Medicover magán-egészségbiztosítás, ✓ WARTA csoportos biztosítások, ✓ csapatépítő összejövetelek, ✓ dress code-mentes munkahely, ✓ irodai kávé / tea. Jelentkezzen erre a pozícióra A toborzási folyamatot az eRecruiter rendszerben bonyolítjuk. Kattintson az alábbi gombra az űrlap kitöltéséhez. Ugrás a jelentkezési űrlapra",
        "cs": "Tvoje náplň práce ✓ aktivní získávání nových klientů v stavebním sektoru, ✓ analýza trhu průmyslových, skladových a komerčních investic, ✓ budování a udržování dlouhodobých vztahů s potenciálními klienty, ✓ identifikace nových obchodních příležitostí a získávání obchodních kontaktů, ✓ reprezentace firmy na veletrzích, konferencích a oborových akcích, ✓ úzká spolupráce s marketingovým oddělením v oblasti image a generování leadů, ✓ spolutvorba PR a obchodní strategie společně s obchodním ředitelem, ✓ příprava nabídek, prezentací a obchodních materiálů. Naše požadavky ✓ praxe na pozici s obdobným charakterem, ✓ znalost stavebního trhu, ✓ technické vzdělání, ✓ znalost trhu komerčních nemovitostí (průmyslové haly, sklady, komerční objekty), ✓ vysoce rozvinuté komunikační a vyjednávací schopnosti, ✓ proaktivita, samostatnost a schopnost budování obchodních vztahů, ✓ orientace na dosahování prodejních cílů, ✓ schopnost reprezentovat firmu při jednáních s klienty a během oborových akcí, ✓ řidičský průkaz skupiny B, ✓ ochota ke krátkodobým služebním cestám. Nabízíme ✓ stabilní zaměstnání na základě pracovní smlouvy nebo B2B, ✓ atraktivní ohodnocení odpovídající přijímaným úkolům (pevný základ mzdy), ✓ podporu zkušeného manažerského týmu, ✓ možnost rozvoje a práce na unikátních projektech pro přední a prestižní investory na polském trhu, ✓ certifikovaná školení a kurzy zvyšující kvalifikaci, ✓ služební vůz, ✓ možnost hybridní práce, ✓ soukromou zdravotní péči Medicover, ✓ skupinové pojištění WARTA, ✓ teambuildingové akce, ✓ žádný dress code, ✓ kávu / čaj v kanceláři. Ucházet se o tuto pozici Náborový proces vedeme v systému eRecruiter. Klikněte na níže uvedené tlačítko a vyplňte formulář. Přejít na přihlašovací formulář",
        "sk": "Vaša náplň práce ✓ aktívne získavanie nových klientov v stavebnom sektore, ✓ analýza trhu priemyselných, skladových a službových investícií, ✓ budovanie a udržiavanie dlhodobých vzťahov s potenciálnymi klientmi, ✓ identifikácia nových obchodných príležitostí a získavanie obchodných kontaktov, ✓ reprezentovanie firmy na veľtrhoch, konferenciách a odborových podujatiach, ✓ úzka spolupráca s marketingovým oddelením v oblasti imidžových aktivít a generovania leadov, ✓ spolutvorba PR a obchodnej stratégie spolu s Obchodným riaditeľom, ✓ príprava ponúk, prezentácií a obchodných materiálov. Naše požiadavky ✓ skúsenosť v práci na pozícii s podobným charakterom, ✓ znalosť stavebného trhu, ✓ technické vzdelanie, ✓ znalosť trhu komerčných nehnuteľností (priemyselné haly, sklady, službové objekty), ✓ vysoko rozvinuté komunikačné a vyjednávacie schopnosti, ✓ proaktivita, samostatnosť a schopnosť budovať obchodné vzťahy, ✓ orientácia na dosahovanie obchodných cieľov, ✓ schopnosť reprezentovať firmu v kontaktoch s klientmi a počas odborových podujatí, ✓ vodičský preukaz skupiny B, ✓ pripravenosť na krátkodobé služobné cesty. Čo ponúkame ✓ stabilné zamestnanie na základe pracovnej zmluvy alebo B2B, ✓ atraktívne ohodnotenie zodpovedajúce prijímaným úlohám (pevný základ mzdy), ✓ podporu skúseného manažmentu, ✓ možnosť rozvoja a prácu na unikátnych projektoch pre popredných a prestížnych Investorov na poľskom trhu, ✓ certifikované školenia a kurzy zvyšujúce kvalifikáciu, ✓ služobné auto, ✓ možnosť hybridnej práce, ✓ súkromné zdravotné poistenie Medicover, ✓ skupinové poistenie WARTA, ✓ integračné stretnutia, ✓ žiaden dress code, ✓ káva / čaj v kancelárii. Aplikujte na túto pozíciu Náborový proces realizujeme v systéme eRecruiter. Kliknite na tlačidlo nižšie a vyplňte formulár. Prejsť na prihláškový formulár"
    },
    "order": 0
},
    {
    "title": "Praktyka/Staż",
    "slug": "p2253",
    "text": "Twój zakres obowiązków ✓ wsparcie zespołu w codziennych zadaniach projektowych i realizacyjnych, ✓ pomoc w analizie dokumentacji technicznej i rysunków, ✓ udział w przygotowywaniu zestawień, przedmiarów i zapytań ofertowych, ✓ zapoznanie się z procesami budowlanymi i specyfiką pracy w generalnym wykonawstwie, ✓ współpraca z inżynierami i kierownikami przy bieżących projektach. Nasze wymagania ✓ status studenta lub absolwenta (preferowane kierunki: budownictwo, architektura, inżynieria środowiska lub pokrewne), ✓ chęć do nauki, zaangażowanie i proaktywne podejście do powierzonych zadań, ✓ podstawowa znajomość rysunku technicznego oraz pakietu MS Office i AutoCAD, ✓ umiejętność pracy w zespole i dobra organizacja czasu, ✓ dyspozycyjność w wymiarze minimum 3-4 dni w tygodniu. To oferujemy ✓ płatny staż lub praktykę studencką z możliwością dłuższego zatrudnienia po ich zakończeniu, ✓ elastyczne godziny pracy, które bez problemu pogodzisz z planem zajęć na uczelni, ✓ dedykowanego opiekuna, który podzieli się praktyczną wiedzą i doświadczeniem, ✓ zdobycie pierwszego doświadczenia przy dużych inwestycjach komercyjnych i przemysłowych, ✓ przyjazną atmosferę pracy i brak dress code’u, ✓ nielimitowaną kawę i herbatę w biurze. Proces rekrutacji prowadzimy w systemie eRecruiter. Kliknij poniższy przycisk, aby wypełnić formularz. Przejdź do formularza",
    "t_t": {
        "en": "Internship / Placement",
        "de": "Praktikum / Hospitation",
        "hu": "Gyakorlat / Szakmai gyakorlat",
        "cs": "Praxe/Stáž",
        "sk": "Prax/Stáž"
    },
    "t_x": {
        "en": "Your responsibilities ✓ supporting the team in day-to-day design and delivery tasks, ✓ assisting in the analysis of technical documentation and drawings, ✓ participating in the preparation of summaries, take-offs and tender enquiries, ✓ getting familiar with construction processes and the specifics of working in general contracting, ✓ cooperating with engineers and managers on current projects. Our requirements ✓ student or graduate status (preferred fields of study: civil engineering, architecture, environmental engineering or related), ✓ willingness to learn, commitment and a proactive approach to assigned tasks, ✓ basic knowledge of technical drawing and the MS Office suite and AutoCAD, ✓ ability to work in a team and good time management, ✓ availability of a minimum of 3-4 days per week. What we offer ✓ paid internship or student placement with the possibility of longer-term employment after completion, ✓ flexible working hours that can easily be combined with your university timetable, ✓ a dedicated mentor who will share practical knowledge and experience, ✓ gaining first experience on large commercial and industrial investments, ✓ a friendly working atmosphere and no dress code, ✓ unlimited coffee and tea in the office. Our recruitment process is conducted in the eRecruiter system. Click the button below to fill in the application form. Go to the application form",
        "de": "Ihre Aufgaben ✓ Unterstützung des Teams bei täglichen Projekt- und Ausführungsaufgaben, ✓ Mithilfe bei der Analyse technischer Dokumentation und Zeichnungen, ✓ Teilnahme an der Erstellung von Zusammenstellungen, Vormessungen und Angebotsanfragen, ✓ Kennenlernen der Bauprozesse und der Besonderheiten der Arbeit in der Generalunternehmerschaft, ✓ Zusammenarbeit mit Ingenieuren und Bauleitern bei laufenden Projekten. Unsere Anforderungen ✓ Status als Student oder Absolvent (vorzugsweise Fachrichtungen: Bauingenieurwesen, Architektur, Umweltingenieurwesen oder verwandte Bereiche), ✓ Lernbereitschaft, Engagement und proaktive Herangehensweise an übertragene Aufgaben, ✓ Grundkenntnisse im technischen Zeichnen sowie im MS-Office-Paket und AutoCAD, ✓ Teamfähigkeit und gute Zeitorganisation, ✓ Verfügbarkeit von mindestens 3–4 Tagen pro Woche. Wir bieten ✓ bezahltes Praktikum oder Studentenpraktikum mit Möglichkeit einer längeren Anstellung danach, ✓ flexible Arbeitszeiten, die sich problemlos mit dem Stundenplan an der Hochschule vereinbaren lassen, ✓ einen engagierten Mentor, der praktisches Wissen und Erfahrung teilt, ✓ erste Berufserfahrung bei großen kommerziellen und industriellen Investitionen, ✓ freundliche Arbeitsatmosphäre und kein Dresscode, ✓ unbegrenzt Kaffee und Tee im Büro. Den Einstellungsprozess führen wir im eRecruiter-System durch. Klicken Sie auf die Schaltfläche unten, um das Formular auszufüllen. Zum Bewerbungsformular",
        "hu": "Feladatkör ✓ a csapat támogatása a napi projekt- és megvalósítási feladatokban, ✓ segítségnyújtás a műszaki dokumentáció és rajzok elemzésében, ✓ részvétel kimutatások, mennyiségi felmérések és ajánlatkérések előkészítésében, ✓ megismerkedés az építési folyamatokkal és a generálkivitelezés sajátosságaival, ✓ együttműködés mérnökökkel és vezetőkkel a napi projektekben. Elvárásaink ✓ hallgatói vagy végzettségi státusz (előnyben részesített szakok: építészet, építőmérnöki, környezetmérnöki vagy kapcsolódó), ✓ tanulási vágy, elkötelezettség és proaktív hozzáállás a rábízott feladatokhoz, ✓ a műszaki rajz és az MS Office csomag, valamint az AutoCAD alapvető ismerete, ✓ csapatmunka-készség és jó időszervezés, ✓ legalább heti 3-4 nap rendelkezésre állás. Amit kínálunk ✓ fizetett szakmai gyakorlat vagy egyetemi gyakorlat, hosszabb távú foglalkoztatás lehetőségével, ✓ rugalmas munkaidő, amelyet probléma nélkül összeegyeztethet az egyetemi órarendjével, ✓ dedikált mentor, aki megosztja gyakorlati tudását és tapasztalatait, ✓ első tapasztalatszerzés nagy kereskedelmi és ipari beruházásokban, ✓ barátságos munkalégkör és dress code-mentes munkahely, ✓ korlátlan kávé és tea az irodában. A toborzási folyamatot az eRecruiter rendszerben bonyolítjuk. Kattintson az alábbi gombra az űrlap kitöltéséhez. Ugrás a jelentkezési űrlapra",
        "cs": "Tvoje náplň práce ✓ podpora týmu v každodenních projektových a realizačních úkolech, ✓ pomoc při analýze technické dokumentace a výkresů, ✓ účast na přípravě soupisek, výkazů výměr a poptávkových řízení, ✓ seznámení se se stavebními procesy a specifiky práce v generálním dodavatelství, ✓ spolupráce s inženýry a vedoucími na běžících projektech. Naše požadavky ✓ status studenta nebo absolventa (preferované obory: stavebnictví, architektura, environmentální inženýrství nebo příbuzné), ✓ chuť se učit, angažovanost a proaktivní přístup ke svěřeným úkolům, ✓ základní znalost technického kreslení a balíku MS Office a AutoCAD, ✓ schopnost týmové práce a dobrá organizace času, ✓ disponibilita v rozsahu minimálně 3-4 dnů v týdnu. Nabízíme ✓ placenou stáž nebo studentskou praxi s možností delšího zaměstnání po jejím skončení, ✓ flexibilní pracovní dobu, kterou bez problémů skloubíte s rozvrhem výuky, ✓ dedikovaného mentora, který se podělí o praktické znalosti a zkušenosti, ✓ získání první zkušenosti na velkých komerčních a průmyslových investicích, ✓ přátelskou pracovní atmosféru a žádný dress code, ✓ neomezenou kávu a čaj v kanceláři. Náborový proces vedeme v systému eRecruiter. Klikněte na níže uvedené tlačítko a vyplňte formulář. Přejít na přihlašovací formulář",
        "sk": "Vaša náplň práce ✓ podpora tímu pri každodenných projektových a realizačných úlohách, ✓ pomoc pri analýze technickej dokumentácie a výkresov, ✓ účasť na príprave súpisov, výkazov výmer a dopytov, ✓ zoznámenie sa so stavebnými procesmi a špecifikami práce pri generálnom vykonávateľstve, ✓ spolupráca s inžiniermi a vedúcimi pri bežných projektoch. Naše požiadavky ✓ status študenta alebo absolventa (preferované smery: stavebníctvo, architektúra, environmentálne inžinierstvo alebo príbuzné), ✓ chuť učiť sa, angažovanosť a proaktívny prístup k zvereným úlohám, ✓ základná znalosť technického kreslenia a balíka MS Office a AutoCAD, ✓ schopnosť pracovať v tíme a dobrá organizácia času, ✓ disponibilita v rozsahu minimálne 3-4 dni v týždni. Čo ponúkame ✓ platenú stáž alebo študentskú prax s možnosťou dlhodobejšieho zamestnania po ich skončení, ✓ flexibilný pracovný čas, ktorý bez problémov zladíte s rozvrhom na univerzite, ✓ venovaného mentora, ktorý sa podelí o praktické znalosti a skúsenosti, ✓ získanie prvej skúsenosti pri veľkých komerčných a priemyselných investíciách, ✓ priateľskú pracovnú atmosféru a žiaden dress code, ✓ neobmedzenú kávu a čaj v kancelárii. Náborový proces realizujeme v systéme eRecruiter. Kliknite na tlačidlo nižšie a vyplňte formulár. Prejsť na prihláškový formulár"
    },
    "order": 0
}
]

WORKERS = [
    {
    "name": "Tomasz Kalisz",
    "position": "Prezes Zarządu",
    "opis": "Jestem inżynierem z wykształcenia i liderem z 15-letnim doświadczeniem w realizacji wymagających projektów budowlanych w Polsce i za granicą, specjalizując się w budownictwie infrastrukturalnym i przemysłowym. W 2018 roku, wspólnie z Jackiem, założyłem MBT Modern Building Team – firmę skupiającą się na dostarczaniu niezawodnych rozwiązań w najbardziej skomplikowanych projektach. Relacje oparte na szczerości i przejrzystości stanowią dla mnie fundament skutecznej współpracy z inwestorami i zespołem.",
    "photo": "/static/img/mbt/Bez-nazwy---kopia-5aee5d92.png",
    "linkedin": "https://www.linkedin.com/in/tomasz-kalisz-28917386/",
    "t_p": {
        "en": "President of the Board",
        "de": "Projektleiter",
        "hu": "Vezérigazgató",
        "cs": "Předseda představenstva",
        "sk": "Predseda predstavenstva"
    },
    "t_o": {
        "en": "I am an engineer by training and a leader with 15 years of experience in delivering demanding construction projects in Poland and abroad, specialising in infrastructure and industrial construction. In 2018, together with Jacek, I founded MBT Modern Building Team – a company focused on delivering reliable solutions on the most complex projects. Relationships built on honesty and transparency are, for me, the foundation of effective cooperation with investors and teams.",
        "de": "Von den ersten Sandburgen bis hin zu groß angelegten Investitionen – das Bauwesen war schon immer Teil meiner Welt. Als Projektleiter verbinde ich eine technische Herangehensweise mit praktischer Erfahrung. Ich schätze es, wenn Arbeit Menschen zusammenbringt und sich der gemeinsame Einsatz in einem greifbaren, dauerhaften Ergebnis niederschlägt, das über Jahre Bestand hat.",
        "hu": "Képzettségem szerint mérnök vagyok, és 15 éves tapasztalattal rendelkezem az igényes építési projektek megvalósításában Lengyelországban és külföldön, az infrastrukturális és ipari építésre specializálódva. 2018-ban Jackkel közösen megalapítottam az MBT Modern Building Teamet – egy olyan céget, amely a legbonyolultabb projektekben megbízható megoldásokat kínál. A befektetőkkel és a csapattal való együttműködés alapját a számomra a tisztességre és átláthatóságra épülő kapcsolatok jelentik.",
        "cs": "Jsem inženýr vzděláním a lídr s 15letou zkušeností s realizací náročných stavebních projektů v Polsku i v zahraničí, specializující se na infrastrukturní a průmyslové stavitelství. V roce 2018 jsem společně s Jackem založil MBT Modern Building Team – společnost zaměřenou na poskytování spolehlivých řešení u těch nejsložitějších projektů. Vztahy založené na upřímnosti a transparentnosti jsou pro mě základem efektivní spolupráce s investory a týmem.",
        "sk": "Som inžinier vzdelaním a líder s 15-ročnými skúsenosťami v realizácii náročných stavebných projektov v Poľsku a v zahraničí, špecializujúci sa na infraštruktúrne a priemyselné staviteľstvo. V roku 2018 som spolu s Jackom založil MBT Modern Building Team – spoločnosť zameranú na poskytovanie spoľahlivých riešení v najzložitejších projektoch. Vzťahy založené na úprimnosti a transparentnosti sú pre mňa základom efektívnej spolupráce s investormi a tímom"
    },
    "order": 1
},
    {
    "name": "Jacek Lewandowski",
    "position": "Wiceprezes",
    "opis": "Od 2003 roku działam w branży budowlanej i mimo braku wykształcenia inżynierskiego, swobodnie poruszam się w jej realiach. Jestem handlowcem i negocjatorem z natury, zawsze znajduję sposób, by osiągnąć cel. Cenię relacje oparte na zaufaniu i wzajemnym szacunku. Wierzę, że każde doświadczenie w życiu ma sens, celebruję sukcesy i wyciągam wnioski z porażek.",
    "photo": "/static/img/mbt/Projekt-bez-nazwy-7-95f5eaf2.png",
    "linkedin": "https://www.linkedin.com/in/jacek-lewandowski-7a348b9b/",
    "t_p": {
        "en": "Vice-President",
        "de": "Vorstandsvorsitzender",
        "hu": "Alelnök",
        "cs": "Místopředseda",
        "sk": "Podpredseda"
    },
    "t_o": {
        "en": "I have been active in the construction industry since 2003 and, despite not holding an engineering degree, I navigate its realities with ease. I am a salesperson and a negotiator by nature, always finding a way to achieve the goal. I value relationships built on trust and mutual respect. I believe that every experience in life has a purpose – I celebrate successes and draw conclusions from failures.",
        "de": "Ich bin Ingenieur von Ausbildung und Führungskraft mit 15-jähriger Erfahrung in der Umsetzung anspruchsvoller Bauprojekte in Polen und im Ausland, spezialisiert auf Infrastruktur- und Industriebau. 2018 habe ich gemeinsam mit Jacek MBT Modern Building Team gegründet – ein Unternehmen, das sich auf die Bereitstellung zuverlässiger Lösungen in den komplexesten Projekten konzentriert. Beziehungen, die auf Ehrlichkeit und Transparenz basieren, sind für mich das Fundament einer erfolgreichen Zusammenarbeit mit Investoren und Team.",
        "hu": "2003 óta dolgozom az építőiparban, és bár nincs mérnöki végzettségem, magabiztosan mozgok a terület mindennapjaiban. Alapvetően kereskedő és tárgyaló vagyok, mindig megtalálom a módját a cél elérésének. A bizalmon és kölcsönös tiszteleten alapuló kapcsolatokat értékelem. Hiszek abban, hogy minden élettapasztalatnak van értelme, ünneplém a sikereket és levonom a tanulságot a kudarcokból.",
        "cs": "Od roku 2003 působím ve stavebním odvětví a i přes absenci inženýrského vzdělání se v něm volně pohybuji. Jsem obchodník a vyjednavač od přírody, vždy najdu způsob, jak dosáhnout cíle. Vážím si vztahů založených na důvěře a vzájemném respektu. Věřím, že každá životní zkušenost má smysl, slavím úspěchy a vyvozuji závěry z neúspěchů.",
        "sk": "Od roku 2003 pôsobím v stavebnom odvetví a aj napriek tomu, že nemám inžinierske vzdelanie, sa v ňom voľne pohybujem. Som obchodník a vyjednávač od prírody, vždy nájdem spôsob, ako dosiahnuť cieľ. Cením si vzťahy založené na dôvere a vzájomnom rešpekte. Verím, že každá životná skúsenosť má zmysel, oslavujem úspechy a vyvodzujem závery z neúspechov."
    },
    "order": 2
},
    {
    "name": "Amelia  Mzyk",
    "position": "Dyrektor Controllingu",
    "opis": "Jestem inżynierem budownictwa, od ponad 20 lat związana z finansami i controllingiem. \r\nW obecnej roli łącze analityczne myślenie z praktycznym podejściem do projektów.\r\nWierzę, że kluczem do sukcesu są ludzie, wspólne wartości i współpraca, aby osiągnąć założony cel.",
    "photo": "/static/img/mbt/o-nas-Amelia-Mzyk-scaled-e1769717176779-5c63eb5f.jpg",
    "linkedin": "https://www.linkedin.com/in/amelia-mzyk-91a98b71/",
    "t_p": {
        "en": "Deputy Director of the Delivery Department for Finance",
        "de": "Stellvertretende Direktorin der Ausführungsabteilung (Finanzen)",
        "hu": "Megvalósítási Osztály Igazgatóhelyettese – pénzügyi terület",
        "cs": "Zástupce ředitele realizačního oddělení pro finance",
        "sk": "Zástupkyňa riaditeľa realizačného oddelenia pre financie"
    },
    "t_o": {
        "en": "I am a civil engineer with over 20 years of experience connected with finance and controlling.\nIn my current role, I combine analytical thinking with a practical approach to projects.\nI believe that the key to success lies in people, shared values and cooperation in order to achieve the intended goal.\n",
        "de": "Ich bin Bauingenieurin und seit über 20 Jahren in den Bereichen Finanzen und Controlling tätig.\nIn meiner aktuellen Rolle verbinde ich analytisches Denken mit einem praxisorientierten Projektansatz.\nIch glaube, dass der Schlüssel zum Erfolg die Menschen sind, gemeinsame Werte und Zusammenarbeit, um das gesetzte Ziel zu erreichen.",
        "hu": "Építőmérnök vagyok, több mint 20 éve kapcsolódom a pénzügyekhez és a controllinghoz.\nJelenlegi szerepemben az analitikus gondolkodást a projektek gyakorlati megközelítésével ötvözöm.\nHiszem, hogy a siker kulcsa az emberek, a közös értékek és az együttműködés a kitűzött cél elérése érdekében.",
        "cs": "Jsem inženýrka stavebnictví, přes 20 let spojená s financemi a controllingem. \nV současné roli spojuji analytické myšlení s praktickým přístupem k projektům.\nVěřím, že klíčem k úspěchu jsou lidé, společné hodnoty a spolupráce při dosahování stanoveného cíle.\n",
        "sk": "Som stavebný inžinier, viac ako 20 rokov spätá s financiami a controllingom. \nV súčasnej úlohe spájam analytické myslenie s praktickým prístupom k projektom.\nVerím, že kľúčom k úspechu sú ľudia, spoločné hodnoty a spolupráca na dosiahnutí stanoveného cieľa.\n"
    },
    "order": 3
},
    {
    "name": "Jakub Walczak",
    "position": "Dyrektor Działu Realizacji",
    "opis": "Jestem inżynierem, który zdobył doświadczenie, przechodząc przez wszystkie szczeble kariery, aby teraz dzielić się nim z zespołem i stale się rozwijać. Każdy dzień to dla mnie okazja do pracy nad ambitnymi projektami, które stanowią prawdziwe wyzwanie.",
    "photo": "/static/img/mbt/Projekt-bez-nazwy-12-2a515545.png",
    "linkedin": "https://www.linkedin.com/in/jakub-walczak-ab5210274/",
    "t_p": {
        "en": "Director of the Delivery Department",
        "de": "Stellvertretender Vorstandsvorsitzender",
        "hu": "Megvalósítási Osztály Igazgatója",
        "cs": "Ředitel realizačního oddělení",
        "sk": "Riaditeľ realizačného oddelenia"
    },
    "t_o": {
        "en": "I am an engineer who has gained experience by progressing through every rung of the career ladder in order to share it with the team today and to keep developing. Every day is an opportunity for me to work on ambitious projects that are a real challenge.",
        "de": "Seit 2003 bin ich in der Baubranche tätig und bewege mich trotz fehlender Ingenierausbildung sicher in ihren Realitäten. Ich bin von Natur aus Kaufmann und Verhandlungsführer und finde immer einen Weg, das Ziel zu erreichen. Ich schätze Beziehungen, die auf Vertrauen und gegenseitigem Respekt basieren. Ich glaube, dass jede Lebenserfahrung sinnvoll ist, feiere Erfolge und ziehe Lehren aus Misserfolgen.",
        "hu": "Olyan mérnök vagyok, aki a karrier minden szintjét megjárta, hogy most megoszthassam tapasztalatait a csapattal és tovább fejlődhessek. Minden nap lehetőség számomra az ambiciózus, igazi kihívást jelentő projekteken való munkára.",
        "cs": "Jsem inženýr, který získal zkušenosti postupně přes všechny kariérní stupně, abych se o ně nyní mohl dělit s týmem a neustále se rozvíjet. Každý den je pro mě příležitostí pracovat na ambiciózních projektech, které představují skutečnou výzvu.",
        "sk": "Som inžinier, ktorý získal skúsenosti prechodom cez všetky kariérne stupne, aby sa o ne teraz delil s tímom a neustále sa rozvíjal. Každý deň je pre mňa príležitosťou pracovať na ambicióznych projektoch, ktoré predstavujú skutočnú výzvu."
    },
    "order": 4
},
    {
    "name": "Krzysztof Filipowski",
    "position": "Dyrektor ds. finansowych",
    "opis": "Jestem odpowiedzialny za finanse firmy, koncentrując się na jej stabilnym rozwoju. Moim celem jest maksymalizacja efektywności zarządzania zasobami finansowymi, by wspierać dalszy wzrost.",
    "photo": "/static/img/mbt/3-152bc7d6.png",
    "linkedin": "https://www.linkedin.com/company/modern-building-team/",
    "t_p": {
        "en": "Chief Financial Officer",
        "de": "Vertriebsdirektor",
        "hu": "Pénzügyi Igazgató",
        "cs": "Finanční ředitel",
        "sk": "Finančný riaditeľ"
    },
    "t_o": {
        "en": "I am responsible for the company's finances, focusing on its stable growth. My goal is to maximise the efficiency of financial resource management in order to support further growth.",
        "de": "Ich bin Vertriebsdirektor mit zehnjähriger Branchenerfahrung. Das Bauwesen ist meine Leidenschaft, und die Arbeit mit Menschen ist die Erfüllung meiner beruflichen Ambitionen und ein fantastisches Abenteuer.",
        "hu": "A vállalat pénzügyeiert felelek, és a stabil fejlődésére összpontosítok. Célom a pénzügyi erőforrások kezelésének hatékonyságának maximalizálása a további növekedés támogatása érdekében.",
        "cs": "Jsem zodpovědný za finance společnosti se zaměřením na její stabilní rozvoj. Mým cílem je maximalizace efektivity řízení finančních zdrojů pro podporu dalšího růstu.",
        "sk": "Som zodpovedný za financie spoločnosti, pričom sa sústredím na jej stabilný rozvoj. Mojou cieľom je maximalizácia efektívnosti riadenia finančných zdrojov na podporu ďalšieho rastu."
    },
    "order": 5
},
    {
    "name": "Marek Latoś",
    "position": "Dyrektor Oddziału Kraków",
    "opis": "Mam 20 lat doświadczenia w branży budowlanej, zbieram doświadczenie zarówno w sektorze przemysłowym, jak i w sektorze kubaturowym. Zarządzam inwestycjami prywatnymi i publicznymi, wykorzystując wiedzę techniczną i formalną.",
    "photo": "/static/img/mbt/Projekt-bez-nazwy-14-9b985d19.png",
    "linkedin": "https://www.linkedin.com/in/marek-lato%C5%9B-4aa93233b/",
    "t_p": {
        "en": "Dyrektor Oddziału Kraków",
        "de": "Leiter der Angebotsabteilung",
        "hu": "Project Manager",
        "cs": "Projektový manažer",
        "sk": "Projektový manažér"
    },
    "t_o": {
        "en": "I have 20 years of experience in the construction industry, gaining it in both the industrial and building sectors. I manage private and public investments, drawing on technical and formal expertise.",
        "de": "Ich leite das Angebots-Team und verbinde technisches Wissen mit Erfahrung in Bauprojekten. Ich erstelle präzise Angebote, die auf die Anforderungen der Kunden und die Marktbedingungen zugeschnitten sind.\n\n",
        "hu": "20 év tapasztalattal rendelkezem az építőiparban, tapasztalatot gyűjtöttem mind az ipari, mind a magasépítési szektorban. Magán- és közberuházásokat irányítok, a műszaki és formális tudás felhasználásával.",
        "cs": "Mám 20 let zkušeností ve stavebním odvětví, sbírám zkušenosti jak v průmyslovém, tak v objektovém sektoru. Řídím soukromé i veřejné investice s využitím technických a formálních znalostí.",
        "sk": "Mám 20 rokov skúseností v stavebnom odvetví, zbieram skúsenosti v priemyselnom aj objektovom sektore. Riadim súkromné a verejné investície s využitím technických a formálnych znalostí."
    },
    "order": 6
},
    {
    "name": "Katarzyna  Knabel",
    "position": "Kierownik ds. przygotowania produkcji",
    "opis": "Zarządzam zespołem Działu Przygotowania Produkcji, który ściśle współpracuje z Działem Realizacji projektów budowlanych realizowanych przez MBT.\r\nJako inżynier, łączę techniczne myślenie z dobrą organizacją i zdolnościami komunikacyjnymi. Jestem typem lidera, prowadzę swój zespół z pełnym wsparciem, dzieląc się swoim doświadczeniem. Jednocześnie sama stale się rozwijam. \r\nMawiają o mnie: „Sprawy niemożliwe załatwia od ręki, na cuda trzeba poczekać.”",
    "photo": "/static/img/mbt/O-nas-Katarzyna-Knabel-scaled-e1769718370116-2340d047.jpg",
    "linkedin": "https://www.linkedin.com/in/katarzyna-knabel-1286451ba/",
    "t_p": {
        "en": "Head of Production Preparation",
        "de": "Projektleiter",
        "hu": "Gyártás-előkészítési Vezető",
        "cs": "Vedoucí přípravy výroby",
        "sk": "Vedúca pre prípravu výroby"
    },
    "t_o": {
        "en": "I manage the Production Preparation Department team, which works closely with the Delivery Department on construction projects executed by MBT.\nAs an engineer, I combine technical thinking with strong organisational and communication skills. I am a hands-on type of leader – I lead my team with full support, sharing my experience. At the same time, I keep developing myself.\nPeople say about me: \"Impossible tasks she handles straight away; miracles take a little longer.\"\n",
        "de": "Ich bin Bauingenieur und seit 2015 in der Ausführung tätig. Ich habe alle Stufen durchlaufen – vom Bauingenieur bis zum Projektleiter – und Wohn- sowie Industrieobjekte realisiert, wie Produktionsstätten, Kläranlagen und Raffinerien. Bei meiner Arbeit lege ich Wert auf Qualität, Termintreue und die Sorgfalt im Detail.",
        "hu": "Az MBT által megvalósított építési projektek Megvalósítási Osztályával szorosan együttműködő Gyártás-előkészítési Osztály csapatát irányítom.\nMérnökként a műszaki gondolkodást ötvözöm a jó szervezéssel és a kommunikációs készségekkel. Támogató vezető típus vagyok, teljes támogatással irányítom csapatomat, megosztva tapasztalataimat. Egyúttal magam is folyamatosan fejlődöm.\nRólam azt mondják: „A lehetetlen ügyeket azonnal elintézi, a csodákra várni kell.”",
        "cs": "Vedu tým Oddělení přípravy výroby, který úzce spolupracuje s Oddělením realizace stavebních projektů realizovaných společností MBT.\nJako inženýr spojuji technické myšlení s dobrou organizací a komunikačními schopnostmi. Jsem typem lídra, svůj tým vedu s plnou podporou a dělím se o své zkušenosti. Zároveň se sama neustále rozvíjím. \nŘíkají o mně: „Nemožné věci vyřídí hned, na zázraky je třeba počkat.\"\n",
        "sk": "Riadim tím Oddelenia prípravy výroby, ktorý úzko spolupracuje s Oddelením realizácie stavebných projektov realizovaných MBT.\nAko inžinier spájam technické myslenie s dobrou organizáciou a komunikačnými schopnosťami. Som typ lídra, ktorý vedie svoj tím s plnou podporou a delí sa o svoje skúsenosti. Zároveň sa sama neustále rozvíjam. \nO mne hovoria: „Neriešiteľné veci vybaví hneď, na zázraky treba počkať.\"\n"
    },
    "order": 7
},
    {
    "name": "Piotr Burda",
    "position": "Kierownik Działu Ofertowego",
    "opis": "Zarządzam zespołem ofertowym, łącząc wiedzę techniczną z doświadczeniem w projektach budowlanych. Tworzę precyzyjne oferty, dopasowane do wymagań klienta i warunków rynkowych.",
    "photo": "/static/img/mbt/Projekt-bez-nazwy-2-ef2befd0.png",
    "linkedin": "https://www.linkedin.com/in/piotr-burda-14513a180/",
    "t_p": {
        "en": "Head of the Tender Department",
        "de": "Finanzdirektor",
        "hu": "Ajánlatkészítő Osztály Vezetője",
        "cs": "Vedoucí nabídkového oddělení",
        "sk": "Vedúci oddelenia ponúk"
    },
    "t_o": {
        "en": "I manage the tender team, combining technical knowledge with experience in construction projects. I create precise offers tailored to client requirements and market conditions.\n\n",
        "de": "Ich bin verantwortlich für die Finanzen des Unternehmens und konzentriere mich auf seine stabile Entwicklung. Mein Ziel ist es, die Effizienz des Finanzmanagements zu maximieren, um das weitere Wachstum zu unterstützen.",
        "hu": "Az ajánlatkészítő csapatot irányítom, ötvözve a műszaki tudást az építési projektekben szerzett tapasztalattal. Precíz, az ügyfél igényeihez és a piaci feltételekhez igazított ajánlatokat készítek.",
        "cs": "Vedu nabídkový tým a spojuji technické znalosti se zkušenostmi v oblasti stavebních projektů. Vytvářím přesné nabídky přizpůsobené požadavkům klienta a podmínkám trhu.\n\n",
        "sk": "Riadim ponukový tím, spájajúc technické znalosti so skúsenosťami v stavebných projektoch. Tvorím presné ponuky prispôsobené požiadavkám klienta a trhovým podmienkam.\n\n"
    },
    "order": 8
},
    {
    "name": "Dariusz  Kudełko",
    "position": "Kierownik Projektu",
    "opis": "Jestem inżynierem budownictwa związanym z wykonawstwem od 2015 roku. Przeszedłem wszystkie etapy – od Inżyniera Budowy po Kierownika Projektu, realizując obiekty mieszkaniowe i przemysłowe, takie jak zakłady produkcyjne, oczyszczalnie ścieków oraz rafinerie. W pracy stawiam na jakość, terminowość i dopracowanie każdego szczegółu.",
    "photo": "/static/img/mbt/O-nas-Dariusz-Kudelko-scaled-b05be7e3.jpeg",
    "linkedin": "https://www.linkedin.com/company/modern-building-team/",
    "t_p": {
        "en": "Project Manager",
        "de": "Project Manager",
        "hu": "Projektvezető",
        "cs": "Vedoucí projektu",
        "sk": "Vedúci projektu"
    },
    "t_o": {
        "en": "I am a civil engineer connected with contracting since 2015. I have worked my way up – from Site Engineer to Project Manager – delivering residential and industrial buildings such as production plants, wastewater treatment plants and refineries. In my work, I focus on quality, timeliness and perfecting every detail.",
        "de": "Ich habe 20 Jahre Erfahrung in der Baubranche und sammle Erfahrungen sowohl im Industrie- als auch im Hochbausektor. Ich manage private und öffentliche Investitionen und nutze dabei technisches und formelles Wissen.",
        "hu": "Építőmérnök vagyok, 2015 óta kötődöm a kivitelezéshez. Végigmentem minden szinten – az építésvezetőtől a projektvezetőig, lakó- és ipari létesítményeket, például gyárakat, szennyvíztisztítókat és finomítókat megvalósítva. Munkámban a minőségre, a pontosságra és minden részlet kidolgozására helyezem a hangsúlyt.",
        "cs": "Jsem inženýr stavebnictví spojený s realizací od roku 2015. Prošel jsem všemi fázemi – od stavbyvedoucího po vedoucího projektu, realizoval jsem obytné a průmyslové objekty, jako jsou výrobní závody, čistírny odpadních vod a rafinérie. V práci kladu důraz na kvalitu, dochvilnost a propracování každého detailu.",
        "sk": "Som stavebný inžinier spätý s realizáciou od roku 2015. Prešiel som všetkými etapami – od stavebného inžiniera po vedúceho projektu, pričom som realizoval rezidenčné a priemyselné objekty, ako výrobné závody, čističky odpadových vôd a rafinérie. V práci kladiem dôraz na kvalitu, včasnosť a dôkladnosť každého detailu."
    },
    "order": 10
},
    {
    "name": "Bartłomiej Potuczko",
    "position": "Project Manager",
    "opis": "Pracuję w budownictwie od ponad dekady, realizując projekty przemysłowe, drogowe i konserwatorskie. Szybko się adaptuję i wprowadzam nowatorskie rozwiązania.",
    "photo": "/static/img/mbt/Projekt-bez-nazwy-9-5d2bde70.png",
    "linkedin": "https://www.linkedin.com/company/modern-building-team/",
    "t_p": {
        "en": "Project Manager",
        "de": "Direktor der Ausführungsabteilung",
        "hu": "Project Manager",
        "cs": "Projektový manažer",
        "sk": "Projektový manažér"
    },
    "t_o": {
        "en": "I have been working in construction for over a decade, delivering industrial, road and heritage conservation projects. I adapt quickly and introduce innovative solutions.",
        "de": "Ich bin Ingenieur und habe Erfahrungen gesammelt, indem ich alle Karrierestufen durchlaufen habe, um dieses Wissen nun mit dem Team zu teilen und mich ständig weiterzuentwickeln. Jeder Tag ist für mich eine Gelegenheit, an ambitionierten Projekten zu arbeiten, die eine echte Herausforderung darstellen.",
        "hu": "Több mint egy évtizede dolgozom az építőiparban, ipari, közúti és műemléki projekteket megvalósítva. Gyorsan alkalmazkodom, és innovatív megoldásokat vezetek be.",
        "cs": "Pracuji ve stavebnictví přes deset let, realizuji průmyslové, dopravní a památkové projekty. Rychle se adaptuji a zavádím novátorská řešení.",
        "sk": "Pracujem v stavebníctve vyše desaťročie, realizujem priemyselné, dopravné a reštaurátorské projekty. Rýchlo sa adaptujem a zavádzam inovatívne riešenia."
    },
    "order": 11
},
    {
    "name": "Michał  Swoboda",
    "position": "Kierownik Projektu",
    "opis": "Od pierwszych konstrukcji z piasku po wielkoskalowe inwestycje – budownictwo zawsze było częścią mojego świata. Jako Kierownik Projektu łączę techniczne podejście z praktycznym doświadczeniem. Lubię, gdy praca łączy ludzi, a wspólny wysiłek przekłada się na realny, trwały efekt, który zostaje na lata.",
    "photo": "/static/img/mbt/O-nas-Michal-Swoboda-scaled-e1769718309917-1c973d48.jpg",
    "linkedin": "https://www.linkedin.com/in/micha%C5%82-swoboda-b52085159/",
    "t_p": {
        "en": "Project Manager",
        "de": "Project Manager",
        "hu": "Projektvezető",
        "cs": "Vedoucí projektu",
        "sk": "Vedúci projektu"
    },
    "t_o": {
        "en": "From my first sand constructions to large-scale investments – construction has always been part of my world. As a Project Manager, I combine a technical approach with hands-on experience. I enjoy work that brings people together, where the joint effort translates into a real, lasting result that stands the test of time.",
        "de": "Ich arbeite seit über einem Jahrzehnt im Bauwesen und realisiere Industrie-, Straßen- und Konservierungsprojekte. Ich passe mich schnell an und bringe innovative Lösungen ein.",
        "hu": "Az első homokváras építményektől a nagy léptékű beruházásokig – az építés mindig is a világom része volt. Projektvezetőként a műszaki megközelítést a gyakorlati tapasztalattal ötvözöm. Szeretem, amikor a munka összehozza az embereket, és a közös erőfeszítés valós, tartós, évekig megmaradó eredményt hoz.",
        "cs": "Od prvních konstrukcí z písku po velkorozměrové investice – stavitelství bylo vždy součástí mého světa. Jako vedoucí projektu spojuji technický přístup s praktickými zkušenostmi. Mám rád, když práce spojuje lidi a společné úsilí se promítá do reálného, trvalého výsledku, který zůstává na roky.",
        "sk": "Od prvých konštrukcií z piesku po veľké investície – stavebníctvo bolo vždy súčasťou môjho sveta. Ako Vedúci projektu spájam technický prístup s praktickými skúsenosťami. Mám rád, keď práca spája ľudí a spoločné úsilie sa premieta do reálneho, trvalého výsledku, ktorý zostáva na roky."
    },
    "order": 12
},
    {
    "name": "Karol Pinoczek",
    "position": "Manager ds. handlowych",
    "opis": "Jestem Dyrektorem Handlowym z  dziesięcioletnim doświadczeniem w branży. Budownictwo jest moją pasją, a praca z ludźmi spełnieniem zawodowych ambicji i fantastyczną przygodą.",
    "photo": "",
    "linkedin": "https://www.linkedin.com/in/karol-pinoczek-380157151/",
    "t_p": {
        "en": "Sales Director",
        "de": "Leiterin der Produktionsvorbereitung",
        "hu": "Kereskedelmi Igazgató",
        "cs": "Obchodní ředitel",
        "sk": "Obchodný riaditeľ"
    },
    "t_o": {
        "en": "I am a Sales Director with ten years of experience in the industry. Construction is my passion, and working with people is the fulfilment of my professional ambitions and a fantastic adventure.",
        "de": "Ich leite das Team der Abteilung Produktionsvorbereitung, das eng mit der Projektausführungsabteilung der von MBT realisierten Bauprojekte zusammenarbeitet.\nAls Ingenieurin verbinde ich technisches Denken mit guter Organisation und kommunikativen Fähigkeiten. Ich bin ein Führungstyp, der sein Team voll unterstützt und seine Erfahrung teilt. Gleichzeitig entwickle ich mich selbst ständig weiter.\nÜber mich sagt man: „Unmögliches erledige ich sofort, für Wunder braucht man etwas Geduld.\"\n",
        "hu": "Tízéves iparági tapasztalattal rendelkező Kereskedelmi Igazgató vagyok. Az építés a szenvedélyem, az emberekkel való munka pedig szakmai ambícióim beteljesítése és fantasztikus kaland.",
        "cs": "Jsem obchodní ředitel s desetiletou zkušeností v oboru. Stavitelství je mou vášní a práce s lidmi naplněním profesních ambicí a fantastickým dobrodružstvím.",
        "sk": "Som Obchodný riaditeľ s desaťročnými skúsenosťami v odvetví. Stavebníctvo je mojou vášňou a práca s ľuďmi naplnením pracovných ambícií a fantastickým dobrodružstvom."
    },
    "order": 13
}
]

SALES_REPS = [
    {
    "name": "Agnieszka Grzelak",
    "position": "Dział Handlowy",
    "email": "a.grzelak@mbt.pl",
    "phone": "881 202 233",
    "photo": "",
    "t_p": {},
    "order": 0
},
    {
    "name": "Karol Pinoczek",
    "position": "Dział Handlowy",
    "email": "k.pinoczek@mbt.pl",
    "phone": "881 202 784",
    "photo": "",
    "t_p": {},
    "order": 1
},
    {
    "name": "Marcin Kobryń",
    "position": "Dział Handlowy",
    "email": "m.kobryn@mbt.pl",
    "phone": "881 202 615",
    "photo": "",
    "t_p": {},
    "order": 2
},
    {
    "name": "Jarosław Wawrzyk",
    "position": "Dział Handlowy",
    "email": "j.wawrzyk@mbt.pl",
    "phone": "881 202 167",
    "photo": "",
    "t_p": {},
    "order": 3
}
]

REFERENCES = [
    {
    "firma": "Browar Zamkowy Sp. z o.o.",
    "osoba": "Mariusz Dudek",
    "stanowisko": "Prezes Zarządu",
    "tresc": "Powierzone prace zostały wykonane zgodnie ze sztuką budowlaną, w pełni profesjonalnie i w wyznaczonych harmonogramem terminach. Właściwie dobrana kadra oraz poziom jej zarządzania przyczynił się w znacznej mierze do sukcesu całego procesu inwestycyjnego. Rekomenduję firmę MBT Modern Building Team Sp. z o.o. jako rzetelną i w pełni przygotowaną do prowadzenia inwestycji budowlanych w formule Generalnego Wykonawstwa.",
    "t_o": {
        "en": "Mariusz Dudek",
        "de": "Robert Tomczyk",
        "hu": "Mariusz Dudek",
        "cs": "Mariusz Dudek",
        "sk": "Mariusz Dudek"
    },
    "t_s": {
        "en": "President of the Board",
        "de": "Vorsitzender",
        "hu": "Igazgatótanács Elnöke",
        "cs": "Předseda představenstva",
        "sk": "Predseda predstavenstva"
    },
    "t_r": {
        "en": "The entrusted works were carried out in accordance with the building craft, fully professionally and within the deadlines set by the schedule. A properly selected team and the level of its management contributed significantly to the success of the entire investment process. I recommend MBT Modern Building Team Sp. z o.o. as a reliable company fully prepared to carry out construction investments under the General Contracting formula.",
        "de": "Die übertragenen Arbeiten wurden fachgerecht, vollständig professionell und innerhalb der im Zeitplan festgelegten Fristen realisiert. Die sachgerecht ausgewählte Mannschaft und das Niveau ihrer Leitung haben in erheblichem Maße zum Erfolg des gesamten Investitionsprozesses beigetragen.\n\nIch empfehle das Unternehmen MBT Modern Building Team Sp. z o.o. als zuverlässigen und vollständig für die Durchführung von Bauinvestitionen in der Formel der Generalunternehmerschaft vorbereiteten Auftragnehmer.",
        "hu": "A rábízott munkák az építési szakmai szabályoknak megfelelően, teljes mértékben professzionálisan és az ütemezés szerinti határidőkre készültek el. A megfelelően összeállított csapat és annak irányítási színvonala jelentős mértékben hozzájárult a teljes beruházási folyamat sikeréhez. Az MBT Modern Building Team Sp. z o.o. társaságot megbízható, a generálkivitelezési formulában megvalósított építési beruházások vezetésére teljes mértékben felkészült vállalatként ajánljuk.",
        "cs": "Svěřené práce byly provedeny v souladu se stavebním řemeslem, plně profesionálně a ve stanovených termínech harmonogramu. Správně vybraný tým a úroveň jeho řízení se ve značné míře zasloužily o úspěch celého investičního procesu. Doporučujeme společnost MBT Modern Building Team Sp. z o.o. jako spolehlivou a plně připravenou k vedení stavebních investic ve formě generálního dodavatele.",
        "sk": "Zverené práce boli vykonané v súlade so stavebným umením, plne profesionálne a v stanovených harmonogramových termínoch. Správne zvolený personál a úroveň jeho riadenia sa výraznou mierou pričinili o úspech celého investičného procesu. Odporúčame spoločnosť MBT Modern Building Team Sp. z o.o. ako spoľahlivú a plne pripravenú na vedenie stavebných investícií vo formul generálneho dodávateľstva."
    },
    "order": 0
},
    {
    "firma": "Canpack",
    "osoba": "Rafał Starzyk",
    "stanowisko": "Investment Operations Specjalist",
    "tresc": "Powierzone prace zostały wykonane zgodnie z projektem, sztuką budowlaną, w wyznaczonych w umowie i aneksach do umowy terminach.",
    "t_o": {
        "en": "Rafał Starzyk",
        "de": "Piotr Kowalski",
        "hu": "Rafał Starzyk",
        "cs": "Rafał Starzyk",
        "sk": "Rafał Starzyk"
    },
    "t_s": {
        "en": "Investment Operations Specialist",
        "de": "Vorstandsvorsitzender",
        "hu": "Investment Operations Specialist",
        "cs": "Investment Operations Specialist",
        "sk": "Investment Operations Specialist"
    },
    "t_r": {
        "en": "The entrusted works were carried out in accordance with the design, the building craft and within the deadlines set out in the contract and its annexes.",
        "de": "Die übertragenen Arbeiten wurden fachgerecht, vollständig professionell und innerhalb der im Zeitplan festgelegten Fristen ausgeführt. Die sachgerecht ausgewählte Mannschaft und das Niveau ihrer Leitung haben in erheblichem Maße zum Erfolg des gesamten Investitionsprozesses beigetragen. Ich empfehle das Unternehmen MBT Modern Building Team Sp. z o.o. als zuverlässigen und vollständig für die Durchführung von Bauinvestitionen in der Formel der Generalunternehmerschaft vorbereiteten Auftragnehmer.",
        "hu": "A rábízott munkák a projektnek, az építési szakmai szabályoknak, valamint a szerződésben és annak mellékleteiben meghatározott határidőknek megfelelően készültek el.",
        "cs": "Svěřené práce byly provedeny v souladu s projektem, stavebním řemeslem a v termínech stanovených smlouvou a dodatky smlouvy.",
        "sk": "Zverené práce boli vykonané v súlade s projektom, stavebným umením, v termínoch stanovených v zmluve a dodatkoch k zmluve."
    },
    "order": 0
},
    {
    "firma": "EURONOVA",
    "osoba": "Piotr Kowalski",
    "stanowisko": "Prezes Zarządu",
    "tresc": "Powierzone prace zostały wykonane zgodnie ze sztuką budowlaną, w pełni profesjonalnie i w wyznaczonych harmonogramem terminach. Właściwie dobrana kadra oraz poziom jej zarządzania przyczynił się w znacznej mierze do sukcesu całego procesu inwestycyjnego. Rekomenduję firmę MBT Modern Building Team Sp. z o.o. jako rzetelną i w pełni przygotowaną do prowadzenia inwestycji budowlanych w formule Generalnego Wykonawstwa.",
    "t_o": {
        "en": "Piotr Kowalski",
        "de": "Michał Kopiec",
        "hu": "Piotr Kowalski",
        "cs": "Piotr Kowalski",
        "sk": "Piotr Kowalski"
    },
    "t_s": {
        "en": "President of the Board",
        "de": "Prokurist",
        "hu": "Igazgatótanács Elnöke",
        "cs": "Předseda představenstva",
        "sk": "Predseda predstavenstva"
    },
    "t_r": {
        "en": "The entrusted works were carried out in accordance with the building craft, fully professionally and within the deadlines set by the schedule. A properly selected team and the level of its management contributed significantly to the success of the entire investment process. I recommend MBT Modern Building Team Sp. z o.o. as a reliable company fully prepared to carry out construction investments under the General Contracting formula.",
        "de": "Wir bestätigen, dass das Unternehmen MBT Modern Building Team Sp. z o.o. die übertragenen Aufgaben professionell erfüllt hat und die Arbeiten im Rahmen des Projekts gemäß dem vereinbarten Terminplan ausgeführt wurden. Wir können das Unternehmen MBT Modern Building Team Sp. z o.o. als zuverlässigen Auftragnehmer für Bauinvestitionen in der Formel der Generalunternehmerschaft empfehlen.",
        "hu": "A rábízott munkák az építési szakmai szabályoknak megfelelően, teljes mértékben professzionálisan és az ütemezés szerinti határidőkre készültek el. A megfelelően összeállított csapat és annak irányítási színvonala jelentős mértékben hozzájárult a teljes beruházási folyamat sikeréhez. Az MBT Modern Building Team Sp. z o.o. társaságot megbízható, a generálkivitelezési formulában megvalósított építési beruházások vezetésére teljes mértékben felkészült vállalatként ajánljuk.",
        "cs": "Svěřené práce byly provedeny v souladu se stavebním řemeslem, plně profesionálně a ve stanovených termínech harmonogramu. Správně vybraný tým a úroveň jeho řízení se ve značné míře zasloužily o úspěch celého investičního procesu. Doporučujeme společnost MBT Modern Building Team Sp. z o.o. jako spolehlivou a plně připravenou k vedení stavebních investic ve formě generálního dodavatele.",
        "sk": "Zverené práce boli vykonané v súlade so stavebným umením, plne profesionálne a v stanovených harmonogramových termínoch. Správne zvolený personál a úroveň jeho riadenia sa výraznou mierou pričinili o úspech celého investičného procesu. Odporúčame spoločnosť MBT Modern Building Team Sp. z o.o. ako spoľahlivú a plne pripravenú na vedenie stavebných investícií vo formul generálneho dodávateľstva."
    },
    "order": 0
},
    {
    "firma": "Euro-Trade",
    "osoba": "Rafał Goliński",
    "stanowisko": "Pełnomocnik Spółki",
    "tresc": "Właściwie dobrana kadra oraz poziom jej zarządzania przyczynił się w znacznej mierze do sukcesu całego procesu inwestycyjnego. Rekomenduję firmę MBT Modern Building Team spółkę z ograniczoną odpowiedzialnością jako rzetelną i w pełni przygotowaną do prowadzenia inwestycji budowlanych w formule Generalnego Wykonawstwa.",
    "t_o": {
        "en": "Rafał Goliński",
        "de": "Piotr Skudlarski",
        "hu": "Rafał Goliński",
        "cs": "Rafał Goliński",
        "sk": "Rafał Goliński"
    },
    "t_s": {
        "en": "Company Proxy",
        "de": "Stellvertretender Vorstandsvorsitzender",
        "hu": "Társaság Meghatalmazottja",
        "cs": "Zmocněnec společnosti",
        "sk": "Splnomocnenec spoločnosti"
    },
    "t_r": {
        "en": "A properly selected team and the level of its management contributed significantly to the success of the entire investment process. I recommend MBT Modern Building Team spółka z ograniczoną odpowiedzialnością (limited liability company) as a reliable company fully prepared to carry out construction investments under the General Contracting formula.",
        "de": "Die übertragenen Arbeiten wurden fachgerecht, vollständig professionell und innerhalb der im Zeitplan festgelegten Fristen ausgeführt. Ich empfehle das Unternehmen MBT Modern Building Team Sp. z o.o. als zuverlässigen und vollständig für die Durchführung von Bauinvestitionen in der Formel der Generalunternehmerschaft vorbereiteten Auftragnehmer.",
        "hu": "A megfelelően összeállított csapat és annak irányítási színvonala jelentős mértékben hozzájárult a teljes beruházási folyamat sikeréhez. Az MBT Modern Building Team korlátolt felelősségű társaságot megbízható, a generálkivitelezési formulában megvalósított építési beruházások vezetésére teljes mértékben felkészült vállalatként ajánljuk.",
        "cs": "Správně vybraný tým a úroveň jeho řízení se ve značné míře zasloužily o úspěch celého investičního procesu. Doporučujeme společnost MBT Modern Building Team, společnost s ručením omezeným, jako spolehlivou a plně připravenou k vedení stavebních investic ve formě generálního dodavatele.",
        "sk": "Správne zvolený personál a úroveň jeho riadenia sa výraznou mierou pričinili o úspech celého investičného procesu. Odporúčame spoločnosť MBT Modern Building Team spoločnosť s ručením obmedzeným ako spoľahlivú a plne pripravenú na vedenie stavebných investícií vo formul generálneho dodávateľstva."
    },
    "order": 0
},
    {
    "firma": "HERZ Armatury i Systemy grzewcze Sp. z o.o.",
    "osoba": "Piotr Skudlarski",
    "stanowisko": "Wiceprezes Zarządu",
    "tresc": "Powierzone prace zostały wykonane zgodnie ze sztuką budowlaną, w pełni profesjonalnie i w wyznaczonych harmonogramem terminach. Rekomenduję firmę MBT Modern Building Team Sp. z o.o. jako rzetelną i w pełni przygotowaną do prowadzenia inwestycji budowlanych w formule Generalnego Wykonawstwa.",
    "t_o": {
        "en": "Piotr Skudlarski",
        "de": "Rafał Goliński",
        "hu": "Piotr Skudlarski",
        "cs": "Piotr Skudlarski",
        "sk": "Piotr Skudlarski"
    },
    "t_s": {
        "en": "Vice-President of the Board",
        "de": "Bevollmächtigter der Gesellschaft",
        "hu": "Igazgatótanács Alelnöke",
        "cs": "Místopředseda představenstva",
        "sk": "Podpredseda predstavenstva"
    },
    "t_r": {
        "en": "The entrusted works were carried out in accordance with the building craft, fully professionally and within the deadlines set by the schedule. I recommend MBT Modern Building Team Sp. z o.o. as a reliable company fully prepared to carry out construction investments under the General Contracting formula.",
        "de": "Die sachgerecht ausgewählte Mannschaft und das Niveau ihrer Leitung haben in erheblichem Maße zum Erfolg des gesamten Investitionsprozesses beigetragen. Ich empfehle das Unternehmen MBT Modern Building Team – eine Gesellschaft mit beschränkter Haftung – als zuverlässigen und vollständig für die Durchführung von Bauinvestitionen in der Formel der Generalunternehmerschaft vorbereiteten Auftragnehmer.",
        "hu": "A rábízott munkák az építési szakmai szabályoknak megfelelően, teljes mértékben professzionálisan és az ütemezés szerinti határidőkre készültek el. Az MBT Modern Building Team Sp. z o.o. társaságot megbízható, a generálkivitelezési formulában megvalósított építési beruházások vezetésére teljes mértékben felkészült vállalatként ajánljuk.",
        "cs": "Svěřené práce byly provedeny v souladu se stavebním řemeslem, plně profesionálně a ve stanovených termínech harmonogramu. Doporučujeme společnost MBT Modern Building Team Sp. z o.o. jako spolehlivou a plně připravenou k vedení stavebních investic ve formě generálního dodavatele.",
        "sk": "Zverené práce boli vykonané v súlade so stavebným umením, plne profesionálne a v stanovených harmonogramových termínoch. Odporúčame spoločnosť MBT Modern Building Team Sp. z o.o. ako spoľahlivú a plne pripravenú na vedenie stavebných investícií vo formul generálneho dodávateľstva."
    },
    "order": 0
},
    {
    "firma": "Sutco Polska",
    "osoba": "Michał Kopiec",
    "stanowisko": "Prokurent",
    "tresc": "Potwierdzamy, że firma MBT Modern Building Team Sp. z o.o wywiązała się z powierzonych zadań profesjonalnie, a prace w ramach projektu wykonane zostały zgodnie z ustalonym harmonogramem terminowym. Możemy polecić firmę MBT Modern Building Team Sp. z o.o jako rzetelnego wykonawcę inwestycji budowlanych w formule generalnego wykonawstwa.",
    "t_o": {
        "en": "Michał Kopiec",
        "de": "Mariusz Dudek",
        "hu": "Michał Kopiec",
        "cs": "Michał Kopiec",
        "sk": "Michał Kopiec"
    },
    "t_s": {
        "en": "Prokurist",
        "de": "Vorstandsvorsitzender",
        "hu": "Cégvezető (Prokurent)",
        "cs": "Prokurista",
        "sk": "Prokurista"
    },
    "t_r": {
        "en": "We confirm that MBT Modern Building Team Sp. z o.o. has performed the entrusted tasks in a professional manner, and the works under the project were carried out in accordance with the agreed time schedule. We can recommend MBT Modern Building Team Sp. z o.o. as a reliable contractor for construction investments under the general contracting formula.",
        "de": "Die übertragenen Arbeiten wurden fachgerecht, vollständig professionell und innerhalb der im Zeitplan festgelegten Fristen ausgeführt. Die sachgerecht ausgewählte Mannschaft und das Niveau ihrer Leitung haben in erheblichem Maße zum Erfolg des gesamten Investitionsprozesses beigetragen. Ich empfehle das Unternehmen MBT Modern Building Team Sp. z o.o. als zuverlässigen und vollständig für die Durchführung von Bauinvestitionen in der Formel der Generalunternehmerschaft vorbereiteten Auftragnehmer.",
        "hu": "Igazoljuk, hogy az MBT Modern Building Team Sp. z o.o. társaság a rábízott feladatokat professzionálisan teljesítette, és a projekt keretében végzett munkák a megállapodás szerinti határidő-ütemezésnek megfelelően készültek el. Az MBT Modern Building Team Sp. z o.o. társaságot megbízható, generálkivitelezési formulában megvalósított építési beruházások kivitelezőjeként ajánlhatjuk.",
        "cs": "Potvrzujeme, že společnost MBT Modern Building Team Sp. z o.o. splnila svěřené úkoly profesionálně a práce v rámci projektu byly provedeny v souladu se stanoveným časovým harmonogramem. Můžeme doporučit společnost MBT Modern Building Team Sp. z o.o. jako spolehlivého zhotovitele stavebních investic ve formě generálního dodavatele.",
        "sk": "Potvrdzujeme, že spoločnosť MBT Modern Building Team Sp. z o.o si zverené úlohy splnila profesionálne a práce v rámci projektu boli vykonané v súlade s dohodnutým časovým harmonogramom. Môžeme odporučiť spoločnosť MBT Modern Building Team Sp. z o.o ako spoľahlivého realizátora stavebných investícií vo formul generálneho dodávateľa."
    },
    "order": 0
},
    {
    "firma": "TOTO Hair Company",
    "osoba": "Robert Tomczyk",
    "stanowisko": "Prezes",
    "tresc": "Powierzone prace zostały zrealizowane zgodnie ze sztuką budowlaną, w pełni profesjonalnie i w wyznaczonych harmonogramem terminach. Właściwie dobrana kadra oraz poziom jej zarządzania przyczynił się w znacznej mierze do sukcesu całego procesu inwestycyjnego.\n\nRekomenduję firmę MBT Modern Building Team Sp. z o.o. jako rzetelną i w pełni przygotowaną do prowadzenia inwestycji budowlanych w formule Generalnego Wykonawstwa.",
    "t_o": {
        "en": "Robert Tomczyk",
        "de": "Rafał Starzyk",
        "hu": "Robert Tomczyk",
        "cs": "Robert Tomczyk",
        "sk": "Robert Tomczyk"
    },
    "t_s": {
        "en": "President",
        "de": "Investment Operations Specialist",
        "hu": "Elnök",
        "cs": "Předseda",
        "sk": "Predseda"
    },
    "t_r": {
        "en": "The entrusted works were carried out in accordance with the building craft, fully professionally and within the deadlines set by the schedule. A properly selected team and the level of its management contributed significantly to the success of the entire investment process.\n\nI recommend MBT Modern Building Team Sp. z o.o. as a reliable company fully prepared to carry out construction investments under the General Contracting formula.",
        "de": "Die übertragenen Arbeiten wurden gemäß dem Projekt, den Regeln der Baukunst sowie innerhalb der im Vertrag und in den Vertragsanlagen festgelegten Fristen ausgeführt.",
        "hu": "A rábízott munkák az építési szakmai szabályoknak megfelelően, teljes mértékben professzionálisan és az ütemezés szerinti határidőkre valósultak meg. A megfelelően összeállított csapat és annak irányítási színvonala jelentős mértékben hozzájárult a teljes beruházási folyamat sikeréhez.\n\nAz MBT Modern Building Team Sp. z o.o. társaságot megbízható, a generálkivitelezési formulában megvalósított építési beruházások vezetésére teljes mértékben felkészült vállalatként ajánlom.",
        "cs": "Svěřené práce byly realizovány v souladu se stavebním řemeslem, plně profesionálně a ve stanovených termínech harmonogramu. Správně vybraný tým a úroveň jeho řízení se ve značné míře zasloužily o úspěch celého investičního procesu.\n\nDoporučujeme společnost MBT Modern Building Team Sp. z o.o. jako spolehlivou a plně připravenou k vedení stavebních investic ve formě generálního dodavatele.",
        "sk": "Zverené práce boli zrealizované v súlade so stavebným umením, plne profesionálne a v stanovených harmonogramových termínoch. Správne zvolený personál a úroveň jeho riadenia sa výraznou mierou pričinili o úspech celého investičného procesu.\n\nOdporúčame spoločnosť MBT Modern Building Team Sp. z o.o. ako spoľahlivú a plne pripravenú na vedenie stavebných investícií vo formul generálneho dodávateľstva."
    },
    "order": 0
}
]

ARTICLES = [
    {
    "title": "✈️ Historyczny moment na Lotnisko Gliwice. Wmurowanie kamienia węgielnego pod inwestycję firmy Artus Aircraft!",
    "slug": "historyczny-moment-na-lotnisko-gliwice-wmurowanie-kamienia-wegielnego-pod-inwestycje-firmy-artus-aircraft",
    "excerpt": "",
    "text": "Dziś, 8 września, oficjalnie rozpoczęliśmy projekt w strefie GAPR. \r\nJako Generalny Wykonawca wznosimy zakład produkcyjny i hangar dla innowacyjnego polskiego producenta statków powietrznych.\r\nParametry inwestycji MBT:\r\n🔹 Hala produkcyjna (~2 100 m²): trwała konstrukcja z prefabrykatów żelbetowych.\r\n🔹 Biurowiec: konstrukcja tradycyjna, wysoki standard wykończenia dla kadry R&D.\r\n🔹 Infrastruktura: kompleksowe wykonanie sieci i zagospodarowania terenu.\r\nTo właśnie tutaj, w bezpośrednim sąsiedztwie lotniska, Inwestor będzie produkował ultranowoczesne, lekkie samoloty kompozytowe, rozwijane przez własny zespół badawczy.\r\nW wydarzeniu uczestniczyli m.in.: Prezydent Gliwice Katarzyna Kuczyńska-Budka prezydentka Gliwic, zarząd Artus wraz ze swoimi ekspertami od lotnictwa, Prezes GAPR a także przedstawiciele służb nadzorujących (PSP, PINB, Sanepid) oraz Inspektorzy Nadzoru.\r\nPrace na lotnisku ruszają – przed nami kolejna budowa bez komplikacji! 🏗️",
    "image": "https://media.mbt.pl/uploads/00c6b1dda4c3.webp",
    "t_t": {},
    "t_e": {},
    "t_x": {}
},
    {
    "title": "Trwają prace na budowie hali montażowo-magazynowej dla firmy @Instalacje Elektryczne Krzysztof Fiołka  w Raciborzu 🏗️",
    "slug": "trwaja-prace-na-budowie-hali-montazowo-magazynowej-dla-firmy-instalacje-elektryczne-krzysztof-fiolka-w-raciborzu",
    "excerpt": "",
    "text": "Jako Generalny Wykonawca realizujemy obiekt przemysłowy połączony z zapleczem socjalno-biurowym. Docelowo budynek posłuży do produkcji i prefabrykacji rozdzielni silnoprądowych.\r\nProjekt w liczbach i technologii:\r\n🔹 Powierzchnia: 3 634 m² (część produkcyjno-magazynowa) oraz 250,52 m² (część socjalno-biurowa).\r\n🔹 Odźwigowienie: Hala jest projektowana pod dwie suwnice o łącznym udźwigu 20 ton.\r\n🔹 Fundamentowanie: Posadowienie pośrednie na kolumnach betonowych.\r\n🔹 Konstrukcja hali: Stalowa konstrukcja ścian i dachu, obudowa z płyt warstwowych. Pokrycie dachu: blacha trapezowa, izolacja z wełny mineralnej i membrana PVC.\r\n🔹 Biurowiec: Konstrukcja mieszana (murowana, żelbetowe rdzenie i wieńce, prefabrykowane stropy z płyt kanałowych typu HC).\r\nNasz zakres obejmuje również wykonanie sieci, instalacji oraz zagospodarowanie terenu wokół obiektu.\r\nPlanujesz budowę zakładu produkcyjnego? Skontaktuj się z naszym zespołem.",
    "image": "https://media.mbt.pl/uploads/622258660799.webp",
    "t_t": {},
    "t_e": {},
    "t_x": {}
},
    {
    "title": "Trwają zaawansowane prace na budowie nowego salonu BYD Dąbrowscy w Bytomiu 🏗️",
    "slug": "trwaja-zaawansowane-prace-na-budowie-nowego-salonu-byd-dabrowscy-w-bytomiu",
    "excerpt": "",
    "text": "Jako Generalny Wykonawca realizujemy zaawansowany obiekt w sektorze automotive dla Grupy Dąbrowscy. W Bytomiu wznosimy kompleksowy salon samochodowy dealera marki BYD.\r\nZakres prowadzonych przez nas prac obejmuje:\r\n🔹 Reprezentacyjną strefę ekspozycyjną: Powstaje przestronny showroom zgodny z rygorystycznymi standardami marki, który zapewni klientom najwyższą jakość obsługi.\r\n🔹 Pełne zaplecze serwisowe: Wznosimy zaawansowaną technologicznie halę warsztatową. Tworzymy infrastrukturę w pełni przygotowaną do profesjonalnej diagnostyki, napraw oraz płynnej obsługi posprzedażowej.\r\nRealizacja inwestycji przebiega rzetelnie, zgodnie z założonym harmonogramem i inżynieryjnymi standardami MBT. Będziemy na bieżąco informować o kolejnych etapach prac z placu budowy.",
    "image": "https://media.mbt.pl/uploads/4406a21c6082.webp",
    "t_t": {},
    "t_e": {},
    "t_x": {}
},
    {
    "title": "Kolejny etap na budowie hali magazynowej dla firmy Wessper 🏗️",
    "slug": "kolejny-etap-na-budowie-hali-magazynowej-dla-firmy-wessper",
    "excerpt": "",
    "text": "Jako Generalny Wykonawca przechodzimy do kolejnej fazy realizacji. Na placu budowy właśnie rozpoczęliśmy montaż prefabrykowanych elementów konstrukcji żelbetowej. Zastosowanie gotowych prefabrykatów pozwala nam na rzetelny i precyzyjny montaż szkieletu budynku, optymalizując czas całego procesu.\r\nKluczowe parametry realizowanego obiektu:\r\n - Funkcja: Hala magazynowa (1 kondygnacja naziemna)\r\n- Powierzchnia użytkowa: 1227 m²\r\n- Wysokość zabudowy: 11,63 m\r\nPrace postępują zgodnie z założonym harmonogramem i naszymi standardami inżynieryjnymi. Będziemy na bieżąco informować o kolejnych postępach z placu budowy.",
    "image": "https://media.mbt.pl/uploads/dcd5a52e2d3b.webp",
    "t_t": {},
    "t_e": {},
    "t_x": {}
},
    {
    "title": "Solidna podstawa dla lidera branży TSL! 🏗️📍 Raben Gniewomierz",
    "slug": "solidna-podstawa-dla-lidera-branzy-tsl-raben-gniewomierz",
    "excerpt": "",
    "text": "Zaglądamy na plac budowy naszej najnowszej inwestycji realizowanej dla Grupy Raben. W Gniewomierzu praca wre – jesteśmy obecnie na kluczowym etapie wznoszenia struktur fundamentowych.\r\nBudowanie dla tak znaczącego gracza na rynku logistycznym wymaga nie tylko precyzji inżynieryjnej, ale także doskonałej koordynacji i dotrzymywania napiętych terminów. Jako Generalny Wykonawca dbamy o to, aby fundamenty pod ten nowoczesny obiekt logistyczny były wykonane zgodnie z najwyższymi standardami jakości i bezpieczeństwa.\r\nPlanujesz budowę nowoczesnej hali magazynowej lub produkcyjnej? Zaufaj ekspertom z Modern Building Team. Skontaktuj się z nami!",
    "image": "https://media.mbt.pl/uploads/765a3c15eec4.webp",
    "t_t": {},
    "t_e": {},
    "t_x": {}
},
    {
    "title": "HALO Kraków! Jesteśmy jeszcze bliżej Was! 🏗️ Nowy oddział MBT oficjalnie otwarty!",
    "slug": "halo-krakow-jestesmy-jeszcze-blizej-was-nowy-oddzial-mbt-oficjalnie-otwarty",
    "excerpt": "",
    "text": "Ostatnio mieliśmy ogromną przyjemność świętować otwarcie naszego nowego krakowskiego biura przy ul. Zawiłej 65 (bud. X, lok. 5). To dla nas przełomowy moment i niezwykle ważny krok w dynamicznym rozwoju firmy.\r\nDlaczego #Kraków? Jako Generalny Wykonawca realizujemy ogromną część wymagających inwestycji na obszarze południowo-wschodniej Polski. Chcemy być w centrum wydarzeń, bliżej naszych Inwestorów oraz bezpośrednio przy rozwijających się rynkach. Jest to pierwszy z naszych oddziałów terenowych, a już mamy na horyzoncie następne obszary w Polsce !\r\nTo był wyjątkowy dzień, podczas którego mieliśmy zaszczyt gościć przedstawicielkę Prezydenta Miasta Kraków, Panią Dominikę Walec. Była to doskonała okazja do spotkania w gronie naszych nieocenionych partnerów biznesowych, przyszłych inwestorów oraz firm, z którymi z sukcesami współpracowaliśmy.\r\nWczorajsze otwarcie przerodziło się w niesamowitą platformę do wymiany doświadczeń i kuluarowych rozmów o wielkich i ambitnych inwestycjach w regionie.\r\nSerdecznie zapraszamy na kawę i rozmowy biznesowe do naszego nowego oddziału – w szczególności Inwestorów z południowo-wschodniej Polski, którzy planują realizację obiektów przemysłowych, produkcyjnych czy magazynowych.\r\nWpadnijcie na Zawiłą. Zbudujmy razem miejsce na Twój biznes!",
    "image": "https://media.mbt.pl/uploads/6c2d5f891c4d.webp",
    "t_t": {},
    "t_e": {},
    "t_x": {}
},
    {
    "title": "Optymalizacja i kontrola robót ziemnych w procesie inwestycyjnym. Wykorzystanie technologii 3D i UAV przez MBT",
    "slug": "optymalizacja-robot-ziemnych-uav-3d",
    "excerpt": "Wprowadzenie &nbsp;Roboty ziemne stanowią inicjalny i jeden z najbardziej krytycznych etapów każdej inwestycji kubaturowej. Błędy w szacowaniu objętości mas ziemnych na etapie przygotowawczym prowadzą do znacznych odchyl",
    "text": "Wprowadzenie &nbsp;Roboty ziemne stanowią inicjalny i jeden z najbardziej krytycznych etapów każdej inwestycji kubaturowej. Błędy w szacowaniu objętości mas ziemnych na etapie przygotowawczym prowadzą do znacznych odchyleń w budżecie inwestycyjnym. Z tego względu firma MBT (Modern Building Team) z powodzeniem wykorzystuje zaawansowane technologie geodezyjne i informatyczne. Wdrożenie precyzyjnych procedur pomiarowych pozwala na zminimalizowanie ryzyka błędu oraz optymalne zabezpieczenie interesów finansowych Inwestora. Inwentaryzacja terenu i pozyskiwanie danych przestrzennych &nbsp;Proces weryfikacji ilościowej robót ziemnych w MBT rozpoczyna się od szczegółowej inwentaryzacji geodezyjnej stanu istniejącego. Podstawą działań jest stabilizacja osnowy geodezyjnej oraz wykonanie precyzyjnych pomiarów za pomocą satelitarnych systemów pozycjonowania (GNSS/GPS). W celu uzyskania maksymalnej gęstości danych pomiarowych wykorzystujemy bezzałogowe statki powietrzne (UAV). Fotogrametria niskiego pułapu umożliwia wygenerowanie dokładnej chmury punktów, która odzwierciedla rzeźbę terenu ze znacznie wyższą rozdzielczością niż tradycyjne pomiary siatkowe. Przetwarzanie danych i cyfrowe modelowanie terenu (DTM) &nbsp;Surowe dane pozyskane podczas nalotów fotogrametrycznych podlegają obróbce w specjalistycznym oprogramowaniu, takim jak DJI Terra. Wygenerowana chmura punktów jest następnie eksportowana do środowiska inżynieryjnego Trimble Business Center. Na tym etapie specjaliści MBT tworzą numeryczny model terenu (DTM) stanu istniejącego. Następnie model ten jest nakładany na projekt zagospodarowania terenu (PZT) oraz projekt architektoniczno-budowlany opracowany w środowisku CAD. Przestrzenne nałożenie na siebie tych dwóch składowych umożliwia weryfikację rzędnych projektowanych względem rzędnych rzeczywistych. Bilans mas ziemnych i optymalizacja kosztów &nbsp;Kluczowym wynikiem opisanego procesu jest precyzyjny bilans mas ziemnych. Oprogramowanie generuje dokładne przekroje oraz oblicza rzeczywistą objętość wykopów i nasypów z dokładnością do ułamków metrów sześciennych. Posiadanie tak precyzyjnych danych przed rozpoczęciem fizycznych prac na budowie pozwala MBT na: Optymalizację logistyki: Dokładne zaplanowanie ilości niezbędnych jednostek transportowych do wywozu urobku lub przywozu materiału zasypowego. Minimalizację kosztów: Identyfikację możliwości zbilansowania mas ziemnych w obrębie samej działki inwestycyjnej (wykorzystanie materiału z wykopu do makroniwelacji w innym sektorze). Transparentność finansową: Przedstawienie Inwestorowi jednoznacznych, bezspornych danych ilościowych, które stanowią podstawę do rozliczeń z podwykonawcami. Podsumowanie &nbsp;Wykorzystanie technologii skaningu przestrzennego, pomiarów satelitarnych oraz oprogramowania inżynieryjnego stanowi istotny element operacyjny MBT. Takie podejście gwarantuje pełną kontrolę nad zakresem robót ziemnych, terminowością ich wykonania oraz budżetem, zapewniając Inwestorowi bezpieczeństwo na najwcześniejszym etapie realizacji projektu.",
    "image": "",
    "t_t": {
        "en": "Optimisation and control of earthworks in the investment process. The use of 3D and UAV technology by MBT",
        "de": "Express-Bau der Produktionshalle ATT in Kokotów – Geschwindigkeitsrekord und unübertroffene Qualität dank sorgfältiger Planung und Bodenanalyse",
        "hu": "Földmunkák optimalizálása és ellenőrzése a beruházási folyamatban. 3D- és UAV-technológia alkalmazása az MBT-nél",
        "cs": "Optimalizace a kontrola zemních prací v investičním procesu. Využití 3D a UAV technologií společností MBT",
        "sk": "Optimalizácia a kontrola zemných prác v investičnom procese. Využitie 3D technológie a UAV spoločnosťou MBT"
    },
    "t_e": {
        "en": "Introduction &nbsp;Earthworks constitute the initial and one of the most critical stages of any building investment. Mistakes in estimating the volume of earth masses at the preparatory stage lead to significant deviations in the investment budget. For this reason, MBT (Modern Building Team) successfully uses advanced surveying and IT technologies. The implementation of precise measurement procedures allows the risk of error to be minimised and the financial interests of the Investor to be optimally safeguarded.",
        "de": "Mit Freude geben wir den Baustart der modernen Produktionshalle ATT in Kokotów bekannt – einer Investition, die für uns ein weiterer Beweis dafür ist, dass präzise Planung und sorgfältige Erkundung der Bodenverhältnisse die Grundlagen für den Erfolg jedes Bauvorhabens sind.",
        "hu": "Bevezetés A földmunkák minden terepi beruházás kezdeti és egyik legkritikusabb szakaszát jelentik. Az előkészítő fázisban elkövetett hibák a földmennyiségek becslésében jelentős eltérésekhez vezetnek a beruházási költségvetésben.",
        "cs": "Úvod &nbsp;Zemní práce představují počáteční a jednu z nejkritičtějších fází každé objemové investice. Chyby v odhadu objemu zemních hmot v přípravné fázi vedou k výrazným odchyl",
        "sk": "Úvod &nbsp;Zemné práce tvoria počiatočnú a jednu z najkritickejších etáp každej objemovej investície. Chyby pri odhadovaní objemov zemných hmôt v prípravnej fáze vedú k značným odchýlkam v investičnom rozpočte."
    },
    "t_x": {
        "en": "Introduction &nbsp;Earthworks constitute the initial and one of the most critical stages of any building investment. Mistakes in estimating the volume of earth masses at the preparatory stage lead to significant deviations in the investment budget. For this reason, MBT (Modern Building Team) successfully uses advanced surveying and IT technologies. The implementation of precise measurement procedures allows the risk of error to be minimised and the financial interests of the Investor to be optimally safeguarded. Site inventory and acquisition of spatial data &nbsp;The quantitative verification process of earthworks at MBT begins with a detailed geodetic inventory of the existing state. The basis for activities is the stabilisation of the survey control network and the execution of precise measurements using satellite positioning systems (GNSS/GPS). In order to obtain the maximum density of measurement data, we use unmanned aerial vehicles (UAVs). Low-altitude photogrammetry enables the generation of an accurate point cloud that reflects the terrain shape with significantly higher resolution than traditional grid surveys. Data processing and digital terrain modelling (DTM) &nbsp;The raw data acquired during photogrammetric flights is processed in specialist software, such as DJI Terra. The generated point cloud is then exported to the Trimble Business Center engineering environment. At this stage, MBT specialists create a digital terrain model (DTM) of the existing state. This model is then overlaid on the site development plan (PZT) and the architectural-construction design prepared in a CAD environment. The spatial overlay of these two components enables the verification of the designed elevations against the actual elevations. Earth mass balance and cost optimisation &nbsp;The key outcome of the described process is a precise earth mass balance. The software generates accurate cross-sections and",
        "de": "Mit Freude geben wir den Baustart der modernen Produktionshalle ATT in Kokotów bekannt – einer Investition, die für uns ein weiterer Beweis dafür ist, dass präzise Planung und sorgfältige Erkundung der Bodenverhältnisse die Grundlagen für den Erfolg jedes Bauvorhabens sind. Planung als Schlüsselphase jeder Bauinvestition Unser Ansatz beruht auf der Überzeugung, dass wir jede Bauphase umso effizienter und sicherer umsetzen, je besser wir sie im Voraus planen. Eine detaillierte Erkundung und Analyse der Baugrund- und Wasserverhältnisse ermöglicht es uns, alle potenziellen Schwierigkeiten zu erkennen, die sich auf die Stabilität und Dauerhaftigkeit des Bauwerks auswirken könnten. Dies ist besonders wichtig bei großen Industrieinvestitionen, in denen selbst minimale Fehler erhebliche Konsequenzen haben können. Überprüfung der Untersuchungen aus der Ausschreibungsphase und Geländeanalyse Einer der Schlüsselmomente unserer Arbeit ist die Überprüfung der Baugrunduntersuchungen, die in der Ausschreibungsphase durchgeführt wurden, da die tatsächlichen Bedingungen von den vorläufigen Annahmen abweichen können. Nur eine genaue Baugrundprüfung, die nach dem Betreten der Baustelle durchgeführt wird, ermöglicht eine passgenaue Auswahl der Technologie, die eine optimale Lösung für die Fundamente gewährleistet. Ein solcher Ansatz ist besonders wichtig bei Investitionen mit großer Fläche, wie der Produktionshalle ATT, da eine fehlerhafte Einschätzung der Bodenverhältnisse die Stabilität der gesamten Konstruktion beeinträchtigen und in der Nutzungsphase des Objekts Kosten verursachen kann. Technologieauswahl und Baugrundverstärkung – solide Grundlage für eine langlebige Konstruktion Unsere Analysen haben gezeigt, dass das für den Bau vorgesehene Gelände eine Verstärkung erfordert, was den Einsatz von Spezialgeräten wie einer Pfahlramme ermöglicht. Dadurch sichern wir bereits in der Fundamentierungsphase der Konstruktion Stabilität und Widerstandsfähigkeit gegenüber Nutzlasten. Die korrekte Auswahl der Fundamentgründungstechnologie bildet die Grundlage, auf der die gesamte Gebäudekonstruktion aufbaut. Der Einsatz fortschrittlicher Gründungsmethoden ermöglicht es uns, die Dauerhaftigkeit und Stabilität der Konstruktion über Jahrzehnte hinweg zu gewährleisten, was im Einklang mit unserer Strategie steht, Objekte zu errichten, die den Erwartungen der Investoren über viele Jahre hinweg gerecht werden. Zusammenfassung Der Bau der Produktionshalle ATT in Kokotów ist ein perfektes Beispiel dafür, dass erfolgreiche Investitionen auf einer Kombination aus modernsten Technologien, ingenieurtechnischem Know-how und individueller Herangehensweise an die spezifischen Anforderungen jedes Projekts basieren, die unseren Kunden die Gewissheit einer soliden und sicheren Konstruktion bieten.",
        "hu": "Bevezetés  A földmunkák minden terepi beruházás kezdeti és egyik legkritikusabb szakaszát jelentik. Az előkészítő fázisban a földmennyiségek becslésében elkövetett hibák jelentős eltérésekhez vezetnek a beruházási költségvetésben. Ezért az MBT (Modern Building Team) sikeresen alkalmaz fejlett geodéziai és informatikai technológiákat. A precíz mérési eljárások bevezetése lehetővé teszi a hibák kockázatának minimalizálását és a Befektető pénzügyi érdekeinek optimális védelmét. A terület felmérése és a térbeli adatok beszerzése  A földmunkák mennyiségi ellenőrzésének folyamata az MBT-nél a meglévő állapot részletes geodéziai felmérésével kezdődik. A tevékenység alapja a geodéziai alappont-hálózat stabilizálása, valamint a műholdas helymeghatározó rendszerekkel (GNSS/GPS) végzett precíz mérések. A mérési adatok maximális sűrűsége érdekében pilóta nélküli légi járműveket (UAV) használunk. Az alacsonyan repülő fotogrammetria lehetővé teszi egy pontos pontfelhő létrehozását, amely a hagyományos hálós méréseknél lényegesen nagyobb felbontással tükrözi a terepfelszínt. Adatfeldolgozás és digitális terepmodell (DTM)  A fotogrammetriai repülések során szerzett nyers adatok feldolgozásra kerülnek speciális szoftverekben, mint például a DJI Terra. Az előállított pontfelhőt ezután a Trimble Business Center mérnöki környezetbe exportáljuk. Ebben a szakaszban az MBT szakemberei elkészítik a meglévő állapot digitális terepmodelljét (DTM). Ezt a modellt ezután a területrendezési tervre (PZT) és a CAD környezetben készült építészeti-műszaki tervekre illesztjük. Ezen két összetevő térbeli egymásra vetítése lehetővé teszi a tervezett szinteknek a valós szintekhez viszonyított ellenőrzését. Földmennyiség-mérleg és költségoptimalizálás  A leírt folyamat kulcsfontosságú eredménye a pontos földmennyiség-mérleg. A szoftver pontos keresztmetszeteket generál, ami lehetővé teszi az egyes szakaszokon a feleslegek és hiányok azonosítását.",
        "cs": "Úvod &nbsp;Zemní práce představují počáteční a jednu z nejkritičtějších fází každé objemové investice. Chyby v odhadu objemu zemních hmot v přípravné fázi vedou k výrazným odchylkám v investičním rozpočtu. Z tohoto důvodu společnost MBT (Modern Building Team) úspěšně využívá pokročilé geodetické a IT technologie. Zavedení přesných měřicích postupů umožňuje minimalizovat riziko chyby a optimálně chránit finanční zájmy investora. Inventarizace terénu a získávání prostorových dat &nbsp;Proces kvantitativního ověření zemních prací v MBT začíná podrobnou geodetickou inventarizací stávajícího stavu. Základem činností je stabilizace geodetické základny a provedení přesných měření pomocí satelitních pozičních systémů (GNSS/GPS). Pro dosažení maximální hustoty měřicích dat využíváme bezpilotní letouny (UAV). Letecká fotogrammetrie z nízké výšky umožňuje vygenerovat přesné mračno bodů, které odráží reliéf terénu s podstatně vyšším rozlišením než tradiční síťová měření. Zpracování dat a digitální modelování terénu (DTM) &nbsp;Surová data pořízená při fotogrammetrických letech jsou zpracována ve specializovaném softwaru, jako je DJI Terra. Vygenerované mračno bodů je následně exportováno do inženýrského prostředí Trimble Business Center. V této fázi specialisté MBT vytvářejí numerický model terénu (DTM) stávajícího stavu. Poté je tento model naložen na projekt úpravy pozemku (PZT) a architektonicko-stavební projekt zpracovaný v prostředí CAD. Prostorové naložení těchto dvou složek na sebe umožňuje ověření projektovaných výšek vůči skutečným výškám. Bilance zemních hmot a optimalizace nákladů &nbsp;Klíčovým výsledkem popsaného procesu je přesná bilance zemních hmot. Software generuje přesné průřezy",
        "sk": "Úvod &nbsp;Zemné práce tvoria počiatočnú a jednu z najkritickejších etáp každej objemovej investície. Chyby pri odhadovaní objemov zemných hmôt v prípravnej fáze vedú k značným odchýlkam v investičnom rozpočte. Z tohto dôvodu spoločnosť MBT (Modern Building Team) úspešne využíva pokročilé geodetické a informačné technológie. Zavedenie precíznych meracích postupov umožňuje minimalizovať riziko chyby a optimálne zabezpečiť finančné záujmy Investora. Inventarizácia terénu a získavanie priestorových dát &nbsp;Proces kvantitatívnej verifikácie zemných prác v MBT sa začína podrobnou geodetickou inventarizáciou súčasného stavu. Základom činností je stabilizácia geodetického bodového poľa a vykonanie precíznych meraní pomocou satelitných polohových systémov (GNSS/GPS). Na dosiahnutie maximálnej hustoty meracích dát využívame bezpilotné lietajúce prostriedky (UAV). Nízkoletová fotogrametria umožňuje vygenerovať presnú bodovú mraku, ktorá odráža tvar terénu s výrazne vyšším rozlíšením ako tradičné sieťové merania. Spracovanie dát a digitálne modelovanie terénu (DTM) &nbsp;Surové dáta získané počas fotogrametrických letov sú spracované v špecializovanom softvéri, ako je DJI Terra. Vygenerovaná bodová mračna je následne exportovaná do inžinierskeho prostredia Trimble Business Center. V tejto fáze špecialisti MBT vytvárajú numerický model terénu (DTM) súčasného stavu. Následne sa tento model nanáša na projekt úpravy terénu (PZT) a architektonicko-stavebný projekt spracovaný v CAD prostredí. Priestorové prekrytie týchto dvoch zložiek umožňuje overenie projektovaných výšok oproti skutočným výškam. Bilancia zemných hmôt a optimalizácia nákladov &nbsp;Kľúčovým výstupom opísaného procesu je presná bilancia zemných hmôt. Softvér generuje presné..."
    }
},
    {
    "title": "Koszt budowy hali przemysłowej w 2026 roku. Czy ceny wreszcie wyhamowały? Raport Inwestora.",
    "slug": "koszt-budowy-hali-przemyslowej-w-2026-roku-czy-ceny-wreszcie-wyhamowaly-raport-inwestora",
    "excerpt": "Początek roku to moment, w którym każdy Inwestor – od dyrektora logistyki po właściciela firmy produkcyjnej – zadaje sobie jedno pytanie: \"Czy to dobry moment na budowę?\". Po burzliwym okresie inflacji, rok 2026 przynosi",
    "text": "Początek roku to moment, w którym każdy Inwestor – od dyrektora logistyki po właściciela firmy produkcyjnej – zadaje sobie jedno pytanie: \"Czy to dobry moment na budowę?\". Po burzliwym okresie inflacji, rok 2026 przynosi na rynku budowlanym nowe otwarcie. Jako Generalny Wykonawca widzimy wyraźny trend: to nie jest rok \"tanich budów\", to rok \"mądrych budów\". Ile realnie kosztuje postawienie hali w Polsce w 2026 roku i gdzie szukać oszczędności, które nie zagrażają jakości? Oto analiza ekspertów MBT Modern Building Team. 1. Stal, beton i ludzie – co steruje ceną w 2026? Jeszcze dwa lata temu wyceny ofertowe były ważne przez 24 godziny. Dziś rynek surowców wchodzi w fazę stabilizacji, ale zmienia się struktura kosztów: Materiały (Stal/Beton): Ceny stali konstrukcyjnej ustabilizowały się, choć pozostają na wysokim poziomie. Nie widzimy już jednak drastycznych skoków z miesiąca na miesiąc, co pozwala na bezpieczniejsze planowanie budżetów w systemie ryczałtowym (Lump Sum). Robocizna i Energia: To tutaj w 2026 roku widać największą presję. Wzrost płacy minimalnej oraz kosztów energii sprawia, że proces budowlany drożeje. Wniosek MBT: Jeśli liczysz na spadek cen materiałów – możesz się przeliczyć. Oszczędności trzeba szukać w optymalizacji projektu , a nie w czekaniu na \"lepsze czasy\". 2. Ukryty zabójca budżetu: Geotechnika Najczęstszy błąd Inwestorów w 2025 roku? Zakup \"taniej działki\", która okazywała się \"inwestycyjnym bagnem\". W MBT wyceniamy dziesiątki zapytań miesięcznie i widzimy prostą zależność: im tańszy grunt w lokalizacji miejskiej (Last Mile), tym droższa inżynieria podziemna. Tradycyjna wymiana gruntu przy obecnych cenach paliwa i transportu to finansowe samobójstwo. Rozwiązanie MBT: W projektach realizowanych m.in. na Śląsku czy w Warszawie, stosujemy zaawansowane metody wzmocnienia podłoża (np. kolumny betonowe, stabilizacja spoiwami). Dzięki temu potrafimy zredukować koszty posadowienia nawet o 15-20% względem tradycyjnych metod. Rada Eksperta: Nigdy nie podpisuj aktu notarialnego na działkę bez wykonania badań geotechnicznych i konsultacji z Generalnym Wykonawcą. To, co zaoszczędzisz na metrze kwadratowym ziemi, możesz wydać podwójnie na beton w fundamentach. 3. System \"Zaprojektuj i Wybuduj\" – polisa na niepewność W 2026 roku model tradycyjny (osobno Projektant, osobno Wykonawca) staje się ryzykowny. Dlaczego? Bo projekt zrobiony w styczniu, w czerwcu może być już nieopłacalny do realizacji ze względu na dostępność materiałów. System \"Design &amp; Build\" (Zaprojektuj i Wybuduj) , w którym specjalizuje się MBT, pozwala na: Value Engineering: Nasi inżynierowie i kosztorysanci pracują razem od pierwszego dnia. Jeśli stal drożeje – przeprojektowujemy ustrój na żelbetowy lub hybrydowy. Gwarancję Ceny: Przejmując odpowiedzialność za projekt, bierzemy na siebie ryzyko błędów w dokumentacji. Inwestor otrzymuje cenę ryczałtową i śpi spokojnie. 4. Nie buduj \"po taniości\", buduj tanio w eksploatacji (OPEX) Koszt budowy (CAPEX) to tylko wierzchołek góry lodowej. Prawdziwe koszty zaczynają się po odbiorze kluczy. W 2026 roku standardem stają się hale przygotowane pod certyfikację BREEAM i wyposażone w inteligentne systemy zarządzania energią. W MBT nie pytamy tylko \"jaką dużą halę chcesz?\". Pytamy: \"ile chcesz płacić za jej ogrzanie?\". Lepsza izolacja dachu, świetliki optymalizujące dostęp światła dziennego czy przygotowanie dachu pod fotowoltaikę – to inwestycje, które zwracają się w 3-5 lat. Podsumowanie: Jak bezpiecznie zaplanować budżet? Budowa hali w 2026 roku wymaga partnera, a nie tylko wykonawcy. Wymaga firmy, która rozumie geotechnikę, umie żonglować technologiami i dowiezie termin bez wymówek. Planujesz inwestycję? Nie zgaduj kosztów. Skontaktuj się z działem handlowym MBT. Przygotujemy dla Ciebie Wstępną Analizę Inwestycyjną , która pokaże realne koszty i potencjalne ryzyka Twojej budowy.",
    "image": "/static/img/mbt/hala-1024x672-eb7144c9.jpg",
    "t_t": {
        "en": "Cost of building an industrial hall in 2026. Have prices finally stabilised? An Investor's Report.",
        "de": "Grünes Licht für Ihre Investition. Wie MBT Bauprojekte im strengen BREEAM-Standard realisiert?",
        "hu": "Ipari csarnok építési költsége 2026-ban. Végre megálltak az árak? Befektetői jelentés.",
        "cs": "Náklady na výstavbu průmyslové haly v roce 2026. Konečně se ceny zastavily? Investorova zpráva.",
        "sk": "Náklady na výstavbu priemyselnej haly v roku 2026. Konečne sa ceny zastavili? Správa pre Investora."
    },
    "t_e": {
        "en": "The beginning of the year is the moment when every Investor – from a logistics director to the owner of a production company – asks themselves one question: \"Is this a good time to build?\". After a turbulent period of inflation, the year 2026 brings",
        "de": "Noch vor einem Jahrzehnt galen Umweltzertifikate im Bauwesen als teures Image-Add-on für die größten Konzerne. Heute sind sie Marktstandard. Die ESG-Berichtspflichten, der Druck seitens der finanzierenden Fonds und die Erwartungen bewusster Mieter haben dafür gesorgt, dass „grünes Bauen\" einfach hartes Business ist. Wir bei MBT Modern Building Team verstehen das bestens.",
        "hu": "Az év eleje az az időszak, amikor minden Befektető – a logisztikai igazgatótól a termelőcég tulajdonosáig – felteszi magának a kérdést: „Most jó alkalom az építkezésre?”. A viharos inflációs időszak után 2026 új fejezetet nyit az építőipari piacon.",
        "cs": "Začátek roku je okamžikem, kdy si každý Investor – od ředitele logistiky po majitele výrobní firmy – klade jednu otázku: \"Je to správný okamžik pro stavbu?\". Po bouřlivém inflačním období přináší rok 2026",
        "sk": "Začiatok roka je moment, v ktorom si každý Investor – od riaditeľa logistiky po majiteľa výrobnej firmy – kladie jednu otázku: \"Je to správny moment na výstavbu?\". Po búrlivom období inflácie prináša rok 2026"
    },
    "t_x": {
        "en": "The beginning of the year is the moment when every Investor – from a logistics director to the owner of a production company – asks themselves one question: \"Is this a good time to build?\". After a turbulent period of inflation, the year 2026 brings a new opening to the construction market. As General Contractor, we see a clear trend: this is not a year of \"cheap builds\", it is a year of \"smart builds\". How much does it really cost to put up a hall in Poland in 2026 and where can savings be found that do not jeopardise quality? Here is an analysis by MBT Modern Building Team experts. 1. Steel, concrete and people – what drives price in 2026? Just two years ago, offer valuations were valid for 24 hours. Today the raw materials market is entering a phase of stabilisation, but the cost structure is changing: Materials (Steel/Concrete): The prices of structural steel have stabilised, although they remain at a high level. We no longer see drastic month-on-month jumps, which allows for safer budget planning under a lump-sum system (Lump Sum). Labour and energy: This is where the greatest pressure is visible in 2026. The rise in the minimum wage and energy costs make the construction process more expensive. MBT's conclusion: If you are counting on a fall in material prices, you may be miscounting. Savings must be sought in project optimisation, rather than in waiting for \"better times\". 2. The hidden budget killer: Geotechnics The most common mistake made by Investors in 2025? Buying \"cheap land\" which turned out to be an \"investment swamp\". At MBT, we price dozens of enquiries every month and see a simple correlation: the cheaper the land in an urban (Last Mile) location, the more expensive the underground engineering. Traditional soil replacement at current fuel and transport prices is financial suicide. MBT's solution: In projects delivered, among others, in Silesia and Warsaw, we apply advanced ground improvement methods (e.g. concrete columns, binder stabilisation). Thanks to this, we are able to reduce foundation costs by as much as 15–20% compared to traditional methods....",
        "de": "Noch vor einem Jahrzehnt galen Umweltzertifikate im Bauwesen als teures Image-Add-on für die größten Konzerne. Heute sind sie Marktstandard. Die ESG-Berichtspflichten, der Druck seitens der finanzierenden Fonds und die Erwartungen bewusster Mieter haben dafür gesorgt, dass „grünes Bauen\" einfach hartes Business ist. Wir bei MBT Modern Building Team verstehen das bestens. Wir verfügen über dokumentierte Erfahrung und eingeführte Verfahren, die es uns als Generalunternehmer ermöglichen, den Investor reibungslos durch den strengen BREEAM-Zertifizierungsprozess zu führen. &nbsp;BREEAM ist nicht nur Photovoltaik auf dem Dach. Es ist eine Bauphilosophie &nbsp;Für viele Investoren beschränkt sich nachhaltiges Bauen auf Photovoltaik und Wärmepumpen. Tatsächlich ist BREEAM (Building Research Establishment Environmental Assessment Method) eines der anspruchsvollsten, multikriteriellen Bewertungssysteme für Gebäude weltweit. Bewertet wird nicht nur das fertige Objekt, sondern in großem Umfang auch der Prozess seiner Entstehung. Und genau hier wird die Rolle eines qualifizierten Generalunternehmers wie MBT entscheidend. Selbst das beste „grüne\" Gebäude erhält keine hohe Bewertung (z. B. Excellent oder Very Good), wenn der Auftragnehmer in der Bauphase die entsprechenden Standards nicht sicherstellt. &nbsp;Die Rolle von MBT auf der Baustelle. Wie gewinnen wir Punkte für Ihre Investition? &nbsp;Die Realisierung eines Objekts für die BREEAM-Zertifizierung erfordert von uns als Generalunternehmer eiserne Disziplin, präzise Planung und fortschrittliches Berichtswesen. Worauf konzentrieren wir uns konkret? Abfallmanagement (Waste Management): &nbsp;Auf unseren Baustellen im BREEAM-Standard landet nichts zufällig in einem Container. Wir setzen strenge Abfallwirtschaftspläne um und stellen sicher, dass ein maximaler Anteil von Schutt, Stahl, Holz oder Kunststoff dem Recycling zugeführt wird und nicht auf die Deponie. Bewusste Lieferkette: &nbsp;Das Zertifikat verlangt die Verwendung von Materialien mit dokumentierter Herkunft und Umweltverträglichkeit. Wir kontrollieren unsere Lieferanten, prüfen Produktdatenblätter und EPDs (Environmental Product Declarations) und stellen so die vollständige Rückverfolgbarkeit der verwendeten Materialien sicher. Energieeffizienz und Monitoring: &nbsp;Wir setzen fortschrittliche HLK- und Elektroinstallationen um, die auf die Minimierung des Energieverbrauchs während des Betriebs ausgelegt sind. Die Wirksamkeit dieser Lösungen wird durch Monitoringsysteme nachgewiesen, die Daten für die Zertifizierung liefern. Wasser- und Abwassermanagement: &nbsp;Wir planen und realisieren Sanitärinstallationen sowie Regenwassernutzungs- und -rückhaltesysteme, um den Frischwasserverbrauch zu reduzieren. Auch auf der Baustelle selbst setzen wir Wasserzähler und Wasserspartechniken ein. Standort und Transport: &nbsp;Wir organisieren die Baustellenlogistik so, dass Emissionen und Belastungen der Anwohner minimiert werden. Unsere Bauleiter überwachen die Einhaltung der Verfahren auf jeder Etappe. &nbsp;BREEAM – ein Mehrwert für Ihren ESG-Bericht &nbsp;Die BREEAM-Zertifizierung eines von MBT realisierten Objekts ist nicht nur ein dekoratives Element. Sie ist ein konkretes Argument bei ESG-Audits, ein Hebel zur Senkung der Betriebskosten und ein Signal an Mieter und Geschäftspartner, dass Ihr Gebäude den höchsten Nachhaltigkeitsstandards entspricht. &nbsp;Lassen Sie uns Ihr Projekt nach BREEAM-Anforderungen realisieren. &nbsp;Kontaktieren Sie unser Beratungsteam!",
        "hu": "Az év eleje az az időszak, amikor minden Befektető – a logisztikai igazgatótól a termelőcég tulajdonosáig – felteszi magának a kérdést: „Most jó alkalom az építkezésre?”. A viharos inflációs időszak után 2026 új fejezetet nyit az építőipari piacon. Fővállalkozóként egyértelmű tendenciát látunk: ez nem a „olcsó építkezések” éve, hanem az „okos építkezések” éve. Mennyibe kerül valójában egy csarnok felállítása Lengyelországban 2026-ban, és hol találhatók olyan megtakarítások, amelyek nem veszélyeztetik a minőséget? Íme az MBT Modern Building Team szakértőinek elemzése. 1. Acél, beton és emberek – mi hajtja az árakat 2026-ban? Még két évvel ezelőtt az ajánlati árak 24 órán át voltak érvényesek. Ma a nyersanyagpiac stabilizációs szakaszba lép, de a költségszerkezet átalakul: Anyagok (Acél/Beton): a szerkezeti acél ára stabilizálódott, bár magas szinten maradt. Már nem látunk viszont havi szinten drasztikus ugrásokat, ami biztonságosabb költségvetés-tervezést tesz lehetővé átalánydíjas (Lump Sum) rendszerben. Munkaerő és energia: itt látható 2026-ban a legnagyobb nyomás. A minimálbér és az energiaköltségek emelkedése az építési folyamat drágulását okozza. Az MBT következtetése: ha anyagárak csökkenésére számítasz, tévedhetsz. A megtakarítást a projekt optimalizálásában kell keresni, nem pedig a „jobb időkre” várva. 2. A költségvetés rejtett gyilkosa: geotechnika A Befektetők leggyakoribb hibája 2025-ben? „Olcsó telek” vásárlása, amely „befektetési mocsárnak” bizonyult. Az MBT-nél havonta több tucat megkeresést értékelünk, és egyértelmű összefüggést látunk: minél olcsóbb a földterület városi (Last Mile) elhelyezkedésben, annál drágább a földalatti mérnöki munka. A hagyományos talajcsere a jelenlegi üzemanyag- és szállítási árak mellett anyagi öngyilkosság. Az MBT megoldása: a többek között Sziléziában és Varsóban megvalósított projektekben fejlett talajmegerősítési módszereket alkalmazunk (pl. beton oszlopok, kötőanyaggal történő stabilizálás). Ennek köszönhetően az alapozási költségeket a hagyományos módszerekhez képest akár 15-20%-kal is csökkenteni tudjuk. Szakértői tanács: Soha ne spórolj a talajon",
        "cs": "Začátek roku je okamžikem, kdy si každý Investor – od ředitele logistiky po majitele výrobní firmy – klade jednu otázku: \"Je to správný okamžik pro stavbu?\". Po bouřlivém inflačním období přináší rok 2026 na stavebním trhu nový začátek. Jako Generální dodavatel vidíme jasný trend: není to rok „levných staveb\", je to rok \"chytrých staveb\". Kolik reálně stojí postavit halu v Polsku v roce 2026 a kde hledat úspory, které neohrozí kvalitu? Přinášíme analýzu expertů MBT Modern Building Team. 1. Ocel, beton a lidé – co řídí ceny v roce 2026? Ještě před dvěma lety byly nabídkové kalkulace platné 24 hodin. Dnes trh surovin vstupuje do fáze stabilizace, ale mění se struktura nákladů: Materiály (ocel/beton): Ceny konstrukční oceli se stabilizovaly, i když zůstávají na vysoké úrovni. Nevidíme však již dramatické skoky z měsíce na měsíc, což umožňuje bezpečnější plánování rozpočtů v paušálním systému (Lump Sum). Práce a energie: Právě zde je v roce 2026 vidět největší tlak. Růst minimální mzdy a nákladů na energii způsobuje, že stavební proces zdražuje. Závěr MBT: Pokud počítáte s poklesem cen materiálů – můžete se přepočítat. Úspory je třeba hledat v optimalizaci projektu , a ne v čekání na \"lepší časy\". 2. Skrytý zabiják rozpočtu: Geotechnika Nejčastější chyba investorů v roce 2025? Nákup \"levného pozemku\", který se ukázal jako \"investiční bažina\". V MBT oceňujeme desítky poptávek měsíčně a vidíme jednoduchou závislost: čím levnější pozemek v městské lokalitě (Last Mile), tím dražší podzemní inženýrství. Tradiční výměna zeminy při současných cenách pohonných hmot a dopravy je finanční sebevražda. Řešení MBT: V projektech realizovaných mj. ve Slezsku či ve Varšavě používáme pokročilé metody zesílení podloží (např. betonové sloupy, stabilizace pojivy). Díky tomu dokážeme snížit náklady na založení až o 15–20 % oproti tradičním metodám. Rada experta: Nikdy nepo",
        "sk": "Začiatok roka je moment, v ktorom si každý Investor – od riaditeľa logistiky po majiteľa výrobnej firmy – kladie jednu otázku: „Je to správny moment na výstavbu?\". Po búrlivom období inflácie prináša rok 2026 na stavebnom trhu nový začiatok. Ako Generálny dodávateľ vidíme jasný trend: nie je to rok „lacných stavieb\", je to rok „múdrych stavieb\". Koľko reálne stojí postaviť halu v Poľsku v roku 2026 a kde hľadať úspory, ktoré neohrozujú kvalitu? Tu je analýza expertov MBT Modern Building Team. 1. Oceľ, betón a ľudia – čo riadi ceny v 2026? Ešte pred dvomi rokmi boli cenové ponuky platné 24 hodín. Dnes trh so surovinami vstupuje do fázy stabilizácie, ale mení sa štruktúra nákladov: Materiály (Oceľ/Betón): Ceny konštrukčnej ocele sa stabilizovali, hoci zostávajú na vysokej úrovni. Už nevidíme drastické skoky z mesiaca na mesiac, čo umožňuje bezpečnejšie plánovanie rozpočtov v paušálnom systéme (Lump Sum). Práca a Energia: Tu je v roku 2026 viditeľný najväčší tlak. Rast minimálnej mzdy a nákladov na energiu spôsobuje, že stavebný proces zdražuje. Záver MBT: Ak počítate s poklesom cien materiálov – môžete sa prepočítať. Úspory treba hľadať v optimalizácii projektu, a nie v čakaní na „lepšie časy\". 2. Skrytý zabijak rozpočtu: Geotechnika Najčastejšia chyba Investorov v roku 2025? Kúpa „lacného pozemku\", ktorý sa ukázal ako „investičné močiar\". V MBT oceňujeme desaťky dopytov mesačne a vidíme jednoduchú závislosť: čím lacnejší pozemok v mestskej lokalite (Last Mile), tým drahšia podzemná inžinierska infraštruktúra. Tradičná výmena zeminy pri súčasných cenách paliva a dopravy je finančná samovražda. Riešenie MBT: V projektoch realizovaných okrem iného na Sliezsku či vo Varšave používame pokročilé metódy spevnenia podložia (napr. betónové kolóny, stabilizácia spojivami). Vďaka tomu dokážeme znížiť náklady na založenie až o 15-20% v porovnaní s tradičnými metódami...."
    }
},
    {
    "title": "Zielone światło dla Twojej inwestycji. Jak MBT realizuje budowy w rygorystycznym standardzie BREEAM?",
    "slug": "generalny-wykonawca-breeam",
    "excerpt": "eszcze dekadę temu certyfikaty ekologiczne w budownictwie były traktowane jako drogi dodatek wizerunkowy dla największych korporacji. Dziś to rynkowy standard. Wymogi raportowania ESG, naciski ze strony funduszy finansuj",
    "text": "Jeszcze dekadę temu certyfikaty ekologiczne w budownictwie były traktowane jako drogi dodatek wizerunkowy dla największych korporacji. Dziś to rynkowy standard. Wymogi raportowania ESG, naciski ze strony funduszy finansujących inwestycje oraz oczekiwania świadomych najemców sprawiły, że \"zielone budownictwo\" to po prostu twardy biznes. W MBT Modern Building Team doskonale to rozumiemy. Posiadamy udokumentowane doświadczenie i wdrożone procedury, które pozwalają nam jako Generalnemu Wykonawcy sprawnie przeprowadzić Inwestora przez rygorystyczny proces certyfikacji BREEAM. &nbsp;BREEAM to nie tylko panele na dachu. To filozofia budowania &nbsp;Wielu Inwestorom zrównoważone budownictwo kojarzy się wyłącznie z fotowoltaiką i pompami ciepła. Tymczasem BREEAM (Building Research Establishment Environmental Assessment Method) to jeden z najbardziej wymagających, wielokryterialnych systemów oceny budynków na świecie. Ocenie podlega nie tylko sam gotowy obiekt, ale w ogromnej mierze&nbsp; proces jego powstawania . I to właśnie tutaj kluczowa staje się rola wykwalifikowanego Generalnego Wykonawcy, takiego jak MBT. Nawet najlepiej zaprojektowany, \"zielony\" budynek nie uzyska wysokiej oceny (np. na poziomie&nbsp; Excellent &nbsp;czy&nbsp; Very Good ), jeśli na etapie budowy wykonawca nie dopilnuje odpowiednich standardów. &nbsp;Rola MBT na placu budowy. Jak zdobywamy punkty dla Twojej inwestycji? &nbsp;Realizacja obiektu pod certyfikację BREEAM wymaga od nas, jako Generalnego Wykonawcy, żelaznej dyscypliny, precyzyjnego planowania i zaawansowanego raportowania. Na czym dokładnie się skupiamy? Zarządzanie odpadami (Waste Management): &nbsp;Na naszych budowach w standardzie BREEAM nic nie trafia przypadkowo do jednego kontenera. Wdrażamy rygorystyczne plany gospodarki odpadami, dbając o to, by maksymalny procent gruzu, stali, drewna czy plastiku trafił do recyklingu, a nie na wysypisko. Świadomy łańcuch dostaw: &nbsp;Certyfikat wymaga stosowania materiałów o udokumentowanym, niskim śladzie węglowym. W MBT pilnujemy, by dostarczane na budowę drewno posiadało certyfikaty FSC, a wbudowywane materiały (beton, stal, izolacje) miały odpowiednie deklaracje środowiskowe (EPD). Preferujemy też lokalnych dostawców, by ograniczyć emisję z transportu. Ochrona środowiska na placu budowy: &nbsp;Monitorujemy i minimalizujemy zużycie wody oraz energii elektrycznej podczas samych prac budowlanych. Zabezpieczamy lokalną florę i faunę, zapobiegamy zanieczyszczeniu wód gruntowych i dbamy o to, by nasz plac budowy nie był uciążliwy dla sąsiadów (redukcja hałasu i zapylenia). Jakość powietrza (Indoor Air Quality): &nbsp;Dbamy o to, by używane przez nas farby, kleje i uszczelniacze charakteryzowały się niską emisją lotnych związków organicznych (LZO/VOC), co przekłada się na zdrowie przyszłych użytkowników budynku. &nbsp;Współpraca z Asesorem to nasz chleb powszedni &nbsp;Zdobycie certyfikatu to gra zespołowa. W MBT nie traktujemy wizyt Asesora BREEAM jako uciążliwej kontroli, ale jako partnerską współpracę. Nasi Kierownicy Budów i Inżynierowie doskonale znają wymogi dokumentacyjne. Kompletujemy karty materiałowe, wykonujemy raporty fotograficzne z kluczowych etapów (tzw.&nbsp; evidence ) i na bieżąco dostarczamy dane niezbędne do uzyskania punktów certyfikacyjnych. Zdejmujemy ten obowiązek z barków Inwestora. &nbsp;Dlaczego warto budować w BREEAM z MBT? &nbsp;Wybór Generalnego Wykonawcy, który \"uczy się\" certyfikacji dopiero na Twoim obiekcie, to ogromne ryzyko utraty punktów i wydłużenia procesu. Stawiając na MBT, zyskujesz partnera, dla którego segregacja odpadów, kontrola łańcucha dostaw i zielona inżynieria to standard operacyjny. Budynki certyfikowane w BREEAM to wyższa wartość rynkowa nieruchomości, niższe koszty eksploatacji (OPEX) i magnes na prestiżowych najemców. Chcesz, aby Twoja nowa hala produkcyjna, magazyn czy park handlowy spełniały najwyższe standardy ESG?&nbsp;&nbsp; Porozmawiajmy o tym, jak MBT może zrealizować Twój projekt zgodnie z wymogami BREEAM. &nbsp;Skontaktuj się z naszym zespołem doradczym!",
    "image": "/static/img/mbt/breem-e659b8f2.jpg",
    "t_t": {
        "en": "Green light for your investment. How does MBT deliver construction to the rigorous BREEAM standard?",
        "de": "Baukosten einer Industriehalle im Jahr 2026. Sind die Preise endlich zum Stillstand gekommen? Investorenbericht.",
        "hu": "Zöld jelzés a befektetésednek. Hogyan valósít meg az MBT BREEAM szigorú szabványú építkezéseket?",
        "cs": "Zelená vlajka pro Vaši investici. Jak MBT realizuje stavby v přísném standardu BREEAM?",
        "sk": "Zelené svetlo pre vašu investíciu. Ako MBT realizuje stavby v prísnom štandarde BREEAM?"
    },
    "t_e": {
        "en": "ust a decade ago, green building certificates were treated as an expensive image-making add-on for the largest corporations. Today it is a market standard. The requirements of ESG reporting, pressure from funds financing investments and the expectations of conscious tenants have turned \"green construction\" into simply hard business.",
        "de": "Der Jahresbeginn ist der Moment, in dem sich jeder Investor – vom Logistikdirektor bis zum Eigentümer eines Produktionsunternehmens – eine Frage stellt: „Ist dies der richtige Zeitpunkt für einen Bau?\" Nach einer turbulenten Inflationsphase bringt das Jahr 2026 eine neue Eröffnung auf dem Baumarkt. Als Generalunternehmer sehen wir einen klaren Trend: Dies ist kein Jahr der „billigen Bauten\", sondern der „klugen Bauten\".",
        "hu": "Még egy évtizeddel ezelőtt a környezetvédelmi tanúsítványok az építőiparban a legnagyobb vállalatok számára drága imázs-kiegészítőnek számítottak. Ma már piaci szabványt jelentenek. Az ESG jelentéstételi követelmények, a finanszírozó alapok nyomása, valamint a tudatos bérlők elvárásai miatt a „zöld építés” egyszerűen kemény üzlet.",
        "cs": "e před deseti lety byly ekologické certifikáty ve stavebnictví vnímány jako drahý imageový doplněk pro největší korporace. Dnes jsou tržním standardem. Požadavky ESG reportování, tlak ze strany",
        "sk": "Ešte pred desiatimi rokmi boli ekologické certifikáty v stavebníctve vnímané ako drahý imidžový doplnok pre najväčšie korporácie. Dnes sú trhovým štandardom. Požiadavky ESG reportovania, tlak zo strany financujúcich fondov"
    },
    "t_x": {
        "en": "Just a decade ago, green building certificates were treated as an expensive image-making add-on for the largest corporations. Today it is a market standard. The requirements of ESG reporting, pressure from funds financing investments and the expectations of conscious tenants have turned \"green construction\" into simply hard business. At MBT Modern Building Team we understand this perfectly. We have documented experience and implemented procedures that allow us, as a General Contractor, to efficiently guide the Investor through the rigorous BREEAM certification process. &nbsp;BREEAM is not only panels on the roof. It is a philosophy of building &nbsp;For many Investors, sustainable construction is associated exclusively with photovoltaics and heat pumps. Meanwhile, BREEAM (Building Research Establishment Environmental Assessment Method) is one of the most demanding, multi-criteria building assessment systems in the world. The assessment covers not only the finished building itself, but to a large extent&nbsp; the process of its creation . And this is precisely where the role of a qualified General Contractor such as MBT becomes crucial. Even the best-designed, \"green\" building will not obtain a high rating (e.g. at the Excellent &nbsp;or Very Good level), if at the construction stage the contractor fails to ensure appropriate standards. &nbsp;MBT's role on the construction site. How do we earn points for your investment? &nbsp;Delivering a building under BREEAM certification requires us, as General Contractor, to demonstrate iron discipline, precise planning and advanced reporting. What exactly do we focus on? Waste management: &nbsp;On our BREEAM-standard construction sites, nothing ends up in a single container by accident. We implement rigorous waste management plans, ensuring that the maximum percentage of rubble, steel, wood or plastic is sent for recycling rather than to landfill. Conscious supply chain: &nbsp;The certificate requires the use of materials with documented, low",
        "de": "Der Jahresbeginn ist der Moment, in dem sich jeder Investor – vom Logistikdirektor bis zum Eigentümer eines Produktionsunternehmens – eine Frage stellt: „Ist dies der richtige Zeitpunkt für einen Bau?\" Nach einer turbulenten Inflationsphase bringt das Jahr 2026 eine neue Eröffnung auf dem Baumarkt. Als Generalunternehmer sehen wir einen klaren Trend: Dies ist kein Jahr der „billigen Bauten\", sondern der „klugen Bauten\". Was kostet es wirklich, eine Halle in Polen im Jahr 2026 zu errichten, und wo lassen sich Einsparungen finden, ohne die Qualität zu gefährden? Hier ist die Analyse der Experten von MBT Modern Building Team. 1. Stahl, Beton und Menschen – was steuert den Preis im Jahr 2026? Noch vor zwei Jahren waren Angebotskalkulationen 24 Stunden lang gültig. Heute tritt der Rohstoffmarkt in eine Stabilisierungsphase ein, aber die Kostenstruktur verändert sich: Materialien (Stahl/Beton): Die Preise für Konstruktionsstahl haben sich stabilisiert, bleiben jedoch auf hohem Niveau. Wir sehen jedoch keine drastischen Sprünge von Monat zu Monat mehr, was eine sicherere Budgetplanung im Pauschalpreissystem (Lump Sum) ermöglicht. Lohnkosten und Energie: Hier ist 2026 der größte Druck spürbar. Der Anstieg des Mindestlohns und der Energiekosten verteuert den Bauprozess. Fazit von MBT: Wer auf fallende Materialpreise hofft, irrt sich möglicherweise. Einsparungen muss man in der Projektoptimierung suchen, nicht im Warten auf „bessere Zeiten\". 2. Der versteckte Budgetkiller: Geotechnik Der häufigste Fehler von Investoren im Jahr 2025? Der Kauf eines „billigen Grundstücks\", das sich als „Investitionssumpf\" entpuppte. Bei MBT kalkulieren wir monatlich Dutzende Anfragen und sehen einen einfachen Zusammenhang: Je günstiger das Grundstück in städtischer Lage (Last Mile), desto teurer die Tiefbau-Ingenieurleistungen. Der herkömmliche Bodenaustausch ist bei den aktuellen Kraftstoff- und Transportpreisen ein finanzieller Selbstmord. MBT-Lösung: In Projekten u. a. in Schlesien oder in Warschau setzen wir fortschrittliche Methoden der Baugrundverstärkung ein (z. B. Betonsäulen, Bindemittelstabilisierung). Dadurch können wir die Gründungskosten im Vergleich zu herkömmlichen Methoden um 15–20 % senken. 3. DesignBuild – Geschwindigkeit als Kostenfaktor Das Modell „Planen und Bauen\" (DesignBuild) ist die Antwort auf die Budgetrealität 2026. Warum? Weil es das größte Risiko aus dem Prozess eliminiert – die Schnittstelle zwischen Planer und Auftragnehmer. Anstatt mit widersprüchlichen Dokumenten, Mehrkostenforderungen und Verzögerungen zu kämpfen, erhält der Investor einen einzigen Vertragspartner, der für die Einhaltung des Budgets, des Zeitplans und der Qualität verantwortlich ist. MBT-Modell: Wir führen das Projekt vom Konzept bis zur Schlüsselübergabe. Sie erhalten ein festes Preisangebot (Lump Sum) und die Gewissheit, dass es keine „bösen Überraschungen\" auf der Baustelle geben wird. 4. Wo befindet sich der Mehrwert – und wo ist der Preis „zu niedrig\"? Bei der Bewertung von Angeboten achten Investoren am häufigsten auf den Endpreis. Wir bei MBT wissen jedoch, dass die Kosten einer Industriehalle nur die halbe Miete sind. Die andere Hälfte sind: Betriebskosten (Energie, Wartung), Flexibilität (Möglichkeit zur Anpassung der Halle an veränderte Bedürfnisse), Sicherheit (Brandschutz, Konstruktionsstabilität), Zertifizierungen (BREEAM, ESG-Reporting). Ein billigeres Angebot ohne diese Elemente kann sich nach 5 Jahren Betrieb als deutlich teurer erweisen. &nbsp;Zusammenfassung &nbsp;2026 ist kein Jahr, in dem man auf sinkende Preise warten sollte. Es ist ein Jahr, in dem intelligente Investoren auf folgende Elemente setzen: Gründungsoptimierung (Geotechnik zuerst), DesignBuild-Modelle (Risikoeliminierung), BREEAM-Zertifizierung (ESG-Wert), Festpreisangebote (Lump Sum) und Partnerschaft mit einem erfahrenen Generalunternehmer. Bei MBT Modern Building Team laden wir Sie ein, eine Vorläufige Investitionsanalyse zu erstellen, die die tatsächlichen Kosten und potenziellen Risiken Ihres Bauvorhabens aufzeigt.",
        "hu": "Még egy évtizeddel ezelőtt a környezetvédelmi tanúsítványok az építőiparban a legnagyobb vállalatok számára drága imázs-kiegészítőnek számítottak. Ma már piaci szabványt jelentenek. Az ESG jelentéstételi követelmények, a finanszírozó alapok nyomása, valamint a tudatos bérlők elvárásai miatt a „zöld építés” egyszerűen kemény üzlet. Az MBT Modern Building Teambennél ezt tökéletesen megértjük. Dokumentált tapasztalattal és bevezetett eljárásokkal rendelkezünk, amelyek lehetővé teszik, hogy Fővállalkozóként zökkenőmentesen végigvezessük a Befektetőt a BREEAM tanúsítás szigorú folyamatán. A BREEAM nem csak tetőn lévő paneleket jelent. Ez egy építési filozófia Sok Befektető számára a fenntartható építés kizárólag a fotovoltaikus rendszereket és hőszivattyúkat jelenti. Eközben a BREEAM (Building Research Establishment Environmental Assessment Method) a világ egyik legigényesebb, többkritériumos épületértékelési rendszere. Az értékelés nemcsak magára a kész épületre, hanem nagymértékben annak keletkezési folyamatára is kiterjed. És pontosan itt válik kulcsfontosságúvá egy szakképzett Fővállalkozó, mint az MBT, szerepe. Még a legjobban megtervezett, „zöld” épület sem fog magas minősítést elérni (pl. Excellent vagy Very Good szinten), ha a kivitelező az építkezés szakaszában nem biztosítja a megfelelő szabványokat. Az MBT szerepe az építkezésen. Hogyan szerzünk pontokat az Ön befektetésének? A BREEAM tanúsítású létesítmény megvalósítása tőlünk, mint Fővállalkozótól, vasfegyelmet, precíz tervezést és fejlett jelentéstételt követel. Mire összpontosítunk pontosan? Hulladékgazdálkodás (Waste Management): A BREEAM szabványú építkezéseinken semmi nem kerül véletlenszerűen egyetlen konténerbe. Szigorú hulladékgazdálkodási terveket vezetünk be, gondoskodva arról, hogy a törmelék, acél, fa vagy műanyag maximális arányban újrahasznosításra kerüljön, ne pedig lerakókba. Tudatos ellátási lánc: A tanúsítvány olyan anyagok alkalmazását írja elő, amelyek dokumentáltan alacsony",
        "cs": "Ještě před deseti lety byly ekologické certifikáty ve stavebnictví vnímány jako drahý imageový doplněk pro největší korporace. Dnes jsou tržním standardem. Požadavky ESG reportování, tlak ze strany investičních fondů a očekávání uvědomělých nájemců způsobily, že „zelené stavitelství\" je jednoduše tvrdý byznys. V MBT Modern Building Team to dokonale chápeme. Máme doložené zkušenosti a zavedené postupy, které nám jako Generálnímu dodavateli umožňují efektivně provést investora přísným procesem certifikace BREEAM. &nbsp;BREEAM nejsou jen panely na střeše. Je to filozofie stavění &nbsp;Mnoha investorům se udržitelné stavitelství pojí výhradně s fotovoltaikou a tepelnými čerpadly. Přitom BREEAM (Building Research Establishment Environmental Assessment Method) je jedním z nejnáročnějších vícekriteriálních systémů hodnocení budov na světě. Hodnocen je nejen samotný hotový objekt, ale do značné míry&nbsp; proces jeho vzniku . A právě zde se klíčovou stává role kvalifikovaného Generálního dodavatele, jakým je MBT. I ta nejlépe navržená „zelená\" budova nezíská vysoké hodnocení (např. na úrovni&nbsp; Excellent &nbsp;či&nbsp; Very Good ), pokud zhotovitel ve fázi výstavby nedodrží odpovídající standardy. &nbsp;Role MBT na stavbě. Jak získáváme body pro Vaši investici? &nbsp;Realizace objektu pro certifikaci BREEAM vyžaduje od nás jako Generálního dodavatele železnou disciplínu, precizní plánování a pokročilé reportování. Na čem přesně se soustředíme? Hospodaření s odpady (Waste Management): &nbsp;Na našich stavbách ve standardu BREEAM se nic nedostane náhodně do jednoho kontejneru. Zavádíme přísné plány odpadového hospodářství a dbáme na to, aby maximální podíl suťi, oceli, dřeva či plastu směřoval do recyklace, a ne na skládku. Vědomý dodavatelský řetězec: &nbsp;Certifikát vyžaduje použití materiálů s doloženým",
        "sk": "Ešte pred desiatimi rokmi boli ekologické certifikáty v stavebníctve vnímané ako drahý imidžový doplnok pre najväčšie korporácie. Dnes sú trhovým štandardom. Požiadavky ESG reportovania, tlak zo strany financujúcich fondov a očakávania uvedomelých nájomcov spôsobili, že „zelené stavebníctvo\" je jednoducho tvrdý biznis. V MBT Modern Building Team to dokonale chápeme. Máme zdokumentované skúsenosti a zavedené postupy, ktoré nám ako Generálnemu dodávateľovi umožňujú efektívne previesť Investora náročným procesom certifikácie BREEAM. &nbsp;BREEAM nie sú len panely na streche. Je to filozofia stavania &nbsp;Mnohým Investorom sa udržateľné stavebníctvo spája výlučne s fotovoltikou a tepelnými čerpadlami. Medzitým BREEAM (Building Research Establishment Environmental Assessment Method) je jeden z najnáročnejších, multikriteriálnych systémov hodnotenia budov na svete. Hodnotený je nielen samotný hotový objekt, ale vo veľkej miere aj proces jeho vzniku. A práve tu sa stáva kľúčovou úloha kvalifikovaného Generálneho dodávateľa, akým je MBT. Aj najlepšie navrhnutá „zelená\" budova nezíska vysoké hodnotenie (napr. na úrovni Excellent alebo Very Good), ak počas výstavby dodávateľ nedodrží príslušné štandardy. &nbsp;Úloha MBT na stavenisku. Ako získavame body pre vašu investíciu? &nbsp;Realizácia objektu pre certifikáciu BREEAM vyžaduje od nás ako Generálneho dodávateľa železnú disciplínu, precízne plánovanie a pokročilé reportovanie. Na čom sa konkrétne zameriavame? Manažment odpadov (Waste Management): &nbsp;Na našich stavbách v štandarde BREEAM nič nekončí náhodne v jednom kontajneri. Zavádzame prísne plány hospodárenia s odpadmi, dbáme na to, aby maximálne percento stavebnej sutiny, ocele, dreva či plastu putovalo do recyklácie a nie na skládku. Uvedomelý dodávateľský reťazec: &nbsp;Certifikát vyžaduje používanie materiálov s..."
    }
},
    {
    "title": "Ekspresowa budowa hali produkcyjnej ATT w Kokotowie – rekord prędkości i niezrównana jakość dzięki odpowiedniemu planowaniu i analizie gruntowej",
    "slug": "ekspresowa-budowa-hali-produkcyjnej-att-w-kokotowie-rekord-predkosci-i-niezrownana-jakosc-dzieki-odpowiedniemu-planowaniu-i-analizie-gruntowej",
    "excerpt": "Z satysfakcją informujemy o rozpoczęciu budowy nowoczesnej hali produkcyjnej ATT w Kokotowie – inwestycji, która stanowi dla nas kolejny dowód na to, że precyzyjne planowanie i rzetelne rozpoznanie warunków gruntowych są",
    "text": "Z satysfakcją informujemy o rozpoczęciu budowy nowoczesnej hali produkcyjnej ATT w Kokotowie – inwestycji, która stanowi dla nas kolejny dowód na to, że precyzyjne planowanie i rzetelne rozpoznanie warunków gruntowych są fundamentami sukcesu każdej budowy. Planowanie jako kluczowy etap każdej inwestycji budowlanej Nasze podejście opiera się na przekonaniu, że im lepiej rozplanujemy każdy etap budowy, tym bardziej efektywnie i bezpiecznie przebiegnie jej realizacja. Szczegółowe rozpoznanie i analiza warunków gruntowo-wodnych pozwalają nam na wykrycie wszelkich potencjalnych trudności, które mogą wpłynąć na stabilność i trwałość budowli. Jest to szczególnie istotne w dużych inwestycjach przemysłowych, gdzie nawet minimalne błędy mogą mieć znaczące konsekwencje. Weryfikacja badań z etapu przetargu i analiza terenu Jednym z kluczowych momentów naszej pracy jest weryfikacja badań gruntowych, wykonanych na etapie przetargu, gdyż rzeczywiste warunki mogą różnić się od wstępnych założeń. Tylko dokładne sprawdzenie gruntu, przeprowadzone po wejściu na plac budowy, pozwala odpowiednio dopasować technologię, która zagwarantuje optymalne rozwiązanie dla fundamentów. Takie podejście jest szczególnie istotne w przypadku inwestycji o dużej powierzchni, jak hala produkcyjna ATT, ponieważ błędne oszacowanie warunków gruntowych może wpłynąć na stabilność całej konstrukcji i generować koszty na etapie użytkowania obiektu. Dobór technologii i wzmocnienie podłoża – solidna podstawa dla długowiecznej konstrukcji Nasze analizy wykazały, że teren przeznaczony pod budowę wymaga wzmocnienia, co umożliwia zastosowanie specjalistycznego sprzętu, takiego jak palownica. Dzięki temu już na etapie fundamentowania zapewniamy konstrukcji stabilność i odporność na obciążenia użytkowe. Prawidłowy dobór technologii posadowienia fundamentów jest podstawą, na której opiera się cała konstrukcja budynku. Zastosowanie zaawansowanych metod fundamentowania pozwala nam zagwarantować trwałość i bezpieczeństwo hali ATT, eliminując potencjalne zagrożenia konstrukcyjne w przyszłości. Kolejne etapy – żelbet, sieci zewnętrzne i prefabrykaty Po odpowiednim przygotowaniu fundamentów przechodzimy do robót żelbetowych i montażu sieci zewnętrznych. Równocześnie przystępujemy do etapu prefabrykacji i montażu głównej konstrukcji, dachu i obudowy hali. Przemyślana kolejność prac oraz precyzyjne wykonanie każdego z etapów są możliwe dzięki dokładnemu zaplanowaniu i analizie technicznej, a także przygotowaniu zespołu do wdrożenia najnowszych rozwiązań technologicznych. Wysokie standardy jakości i bezpieczeństwa – nasza obietnica dla inwestorów Nasz zespół ekspertów czuwa nad każdym etapem realizacji, dbając o to, by każdy szczegół odpowiadał najwyższym standardom jakości i bezpieczeństwa. Jako liderzy w branży budowlanej kładziemy nacisk na zapewnienie, że projektowane i realizowane przez nas rozwiązania są bezpieczne i długotrwałe. Każdy etap inwestycji jest nadzorowany z najwyższą starannością, co przekłada się na jakość całej konstrukcji. Wyjątkowy projekt, zaawansowana technologia i precyzyjne planowanie – z dumą podejmujemy każde wyzwanie Budowa hali produkcyjnej ATT to przykład inwestycji, w której najważniejsze są nie tylko tempo realizacji, ale także jakość każdego etapu. Dzięki doświadczeniu i dokładnemu rozpoznaniu terenu budowy, możemy dostosować najlepsze technologie do specyficznych wymagań projektu, zapewniając naszym klientom pewność solidnej i bezpiecznej konstrukcji.",
    "image": "",
    "t_t": {
        "en": "Express construction of the ATT production hall in Kokotów – a record of speed and unmatched quality thanks to proper planning and soil analysis",
        "de": "Optimierung und Kontrolle von Erdarbeiten im Investitionsprozess. Einsatz der 3D- und UAV-Technologie durch MBT",
        "hu": "Expressz ATT termelőcsarnok-építés Kokotówban – sebességi rekord és páratlan minőség a megfelelő tervezésnek és talajvizsgálatnak köszönhetően",
        "cs": "Expresní výstavba výrobní haly ATT v Kokotowě – rekord rychlosti a bezkonkurenční kvalita díky správnému plánování a geologické analýze",
        "sk": "Expresná výstavba výrobnej haly ATT v Kokotowe – rekord rýchlosti a nekompromisná kvalita vďaka správnemu plánovaniu a analýze zeminy"
    },
    "t_e": {
        "en": "We are pleased to announce the start of construction of the modern ATT production hall in Kokotów – an investment that is, for us, further proof that precise planning and reliable recognition of soil conditions are",
        "de": "Einleitung &nbsp;Erdarbeiten sind die initiale und eine der kritischsten Phasen jeder Hochbauinvestition. Fehler bei der Schätzung der Erdmassen in der Vorbereitungsphase führen zu erheblichen Abweichungen im Investitionsbudget. Aus diesem Grund setzt das Unternehmen MBT (Modern Building Team) erfolgreich fortschrittliche Vermessungs- und Informationstechnologien ein. Die Einführung präziser Messverfahren ermöglicht es, das Fehlerrisiko zu minimieren und die finanziellen Interessen des Investors optimal zu sichern.",
        "hu": "Örömmel jelentjük be a kokotówi modern ATT termelőcsarnok építésének megkezdését – ez a beruházás ismét bizonyítja számunkra, hogy a precíz tervezés és a talajviszonyok alapos feltárása minden építkezés sikerének alapja.",
        "cs": "S potěšením oznamujeme zahájení výstavby moderní výrobní haly ATT v Kokotowě – investice, která je pro nás dalším důkazem, že precizní plánování a spolehlivé posouzení geologických podmínek",
        "sk": "S radosťou oznamujeme začatie výstavby modernej výrobnej haly ATT v Kokotowe – investície, ktorá je pre nás ďalším dôkazom, že precízne plánovanie a dôkladné preskúmanie pôdnych podmienok sú základmi"
    },
    "t_x": {
        "en": "We are pleased to announce the start of construction of the modern ATT production hall in Kokotów – an investment that is, for us, further proof that precise planning and reliable recognition of soil conditions are the foundations of success for any construction project. Planning as the key stage of every construction investment Our approach is based on the conviction that the better we plan every stage of construction, the more efficiently and safely its execution will proceed. Detailed recognition and analysis of soil and water conditions allow us to identify all potential difficulties that may affect the stability and durability of the building. This is particularly important in large industrial investments, where even minimal mistakes can have significant consequences. Verification of surveys from the tender stage and analysis of the site One of the key moments of our work is the verification of soil surveys carried out at the tender stage, as actual conditions may differ from the initial assumptions. Only a thorough inspection of the soil, carried out after arriving at the construction site, makes it possible to tailor the technology that will guarantee the optimal solution for the foundations. Such an approach is particularly important in the case of investments with a large footprint, such as the ATT production hall, because an erroneous estimation of soil conditions may affect the stability of the entire structure and generate costs during the use of the building. Selection of technology and subsoil reinforcement – a solid base for a long-lasting structure Our analyses showed that the site designated for construction requires reinforcement, which enables the use of specialist equipment, such as a piling rig. Thanks to this, already at the foundation stage, we provide the structure with stability and resistance to operational loads. The correct selection of foundation technology is the basis on which the entire structure of the building rests. The use of advanced foundation methods allows us to guarantee the durability and safety of th",
        "de": "Einleitung &nbsp;Erdarbeiten sind die initiale und eine der kritischsten Phasen jeder Hochbauinvestition. Fehler bei der Schätzung der Erdmassen in der Vorbereitungsphase führen zu erheblichen Abweichungen im Investitionsbudget. Aus diesem Grund setzt das Unternehmen MBT (Modern Building Team) erfolgreich fortschrittliche Vermessungs- und Informationstechnologien ein. Die Einführung präziser Messverfahren ermöglicht es, das Fehlerrisiko zu minimieren und die finanziellen Interessen des Investors optimal zu sichern. Geländeaufnahme und Gewinnung räumlicher Daten &nbsp;Der Prozess der quantitativen Überprüfung von Erdarbeiten beginnt bei MBT mit einer detaillierten geodätischen Bestandsaufnahme. Grundlage der Arbeiten ist die Stabilisierung des Vermessungsnetzes sowie die Durchführung präziser Messungen mittels satellitengestützter Positionierungssysteme (GNSS/GPS). Um eine maximale Dichte der Messdaten zu erreichen, setzen wir unbemannte Luftfahrzeuge (UAV) ein. Die niedrigfliegende Photogrammetrie ermöglicht die Erzeugung einer präzisen Punktwolke, die das Geländerelief mit deutlich höherer Auflösung abbildet als herkömmliche Rastermessungen. Datenverarbeitung und digitales Geländemodell (DTM) &nbsp;Die bei den photogrammetrischen Befliegungen gewonnenen Rohdaten werden in Spezialsoftware wie DJI Terra verarbeitet. Die erzeugte Punktwolke wird anschließend in die Ingenieurumgebung Trimble Business Center exportiert. In dieser Phase erstellen die Spezialisten von MBT ein digitales Geländemodell (DTM) des Ist-Zustands. Anschließend wird dieses Modell mit dem Geländegestaltungsprojekt (PZT) sowie dem in CAD erstellten Architektur- und Bauprojekt überlagert. Die räumliche Überlagerung dieser beiden Komponenten ermöglicht die Überprüfung der projektierten Höhen gegenüber den tatsächlichen Höhen. Erdmassenbilanz und Kostenoptimierung &nbsp;Das zentrale Ergebnis dieses Prozesses ist eine präzise Erdmassenbilanz. Die Software generiert genaue Volumina sowohl für Aushub als auch für Aufschüttung. Die Genauigkeit dieser Berechnungen hat direkte Auswirkungen auf das gesamte Investitionsbudget – sowohl in Bezug auf die Erdbewegung selbst als auch auf nachfolgende Arbeiten, die von der Geländeform abhängen. Zusammenfassung &nbsp;Der vorgestellte Ansatz ist Ausdruck der MBT-Philosophie: Der Einsatz modernster Technologien in Kombination mit ingenieurtechnischer Erfahrung bildet ein kohärentes System, das dem Investor Sicherheit und Budgetkontrolle bereits in der frühesten Phase der Projektrealisierung gewährleistet.",
        "hu": "Örömmel jelentjük be a kokotówi modern ATT termelőcsarnok építésének megkezdését – ez a beruházás ismét bizonyítja számunkra, hogy a precíz tervezés és a talajviszonyok alapos feltárása minden építkezés sikerének alapja. A tervezés, mint kulcsfontosságú szakasz Minden építési beruházásban Megközelítésünk azon a meggyőződésen alapul, hogy minél jobban megtervezünk minden építési szakaszt, annál hatékonyabban és biztonságosabban zajlik annak megvalósítása. A talaj- és vízviszonyok részletes feltárása és elemzése lehetővé teszi számunkra, hogy felismerjük azokat a lehetséges nehézségeket, amelyek befolyásolhatják az építmény stabilitását és tartósságát. Ez különösen fontos a nagy ipari beruházásoknál, ahol még a legkisebb hibáknak is jelentős következményei lehetnek. A közbeszerzési szakaszban végzett vizsgálatok ellenőrzése és a terület elemzése Munkánk egyik kulcsfontosságú pillanata a közbeszerzés szakaszában elvégzett talajvizsgálatok ellenőrzése, mivel a tényleges feltételek eltérhetnek az előzetes feltevésektől. Csak a talaj pontos, az építkezésre való belépés után elvégzett vizsgálata teszi lehetővé az alapozási technológia megfelelő kiválasztását, amely optimális megoldást garantál. Ez a megközelítés különösen fontos a nagy alapterületű beruházásoknál, mint amilyen az ATT termelőcsarnok, mivel a talajviszonyok hibás becslése befolyásolhatja a teljes szerkezet stabilitását, és a létesítmény használati szakaszában költségeket generálhat. A technológia kiválasztása és az altalaj megerősítése – szilárd alap a tartós szerkezethez Elemzéseink kimutatták, hogy az építésre szánt terület megerősítést igényel, ami lehetővé teszi speciális berendezések, például cölöpverő alkalmazását. Ennek köszönhetően már az alapozás szakaszában biztosítjuk a szerkezet stabilitását és a használati terhelésekkel szembeni ellenállását. Az alapozási technológia helyes megválasztása az az alap, amelyre az épület teljes szerkezete épül. A fejlett alapozási módszerek alkalmazása lehetővé teszi számunkra, hogy garantáljuk az épület tartósságát és biztonságát",
        "cs": "S potěšením oznamujeme zahájení výstavby moderní výrobní haly ATT v Kokotowě – investice, která je pro nás dalším důkazem, že precizní plánování a spolehlivé posouzení geologických podmínek jsou základem úspěchu každé stavby. Plánování jako klíčová fáze každé stavební investice Náš přístup vychází z přesvědčení, že čím lépe naplánujeme každou fázi stavby, tím efektivněji a bezpečněji proběhne její realizace. Podrobné posouzení a analýza geologicko-hydrogeologických podmínek nám umožňují odhalit veškeré potenciální obtíže, které mohou ovlivnit stabilitu a trvanlivost stavby. To je zvláště důležité u velkých průmyslových investic, kde i minimální chyby mohou mít závažné důsledky. Ověření průzkumů z fáze výběrového řízení a analýza terénu Jedním z klíčových momentů naší práce je ověření geologických průzkumů provedených ve fázi výběrového řízení, neboť skutečné podmínky se mohou lišit od předběžných předpokladů. Pouze důkladná kontrola zeminy provedená po vstupu na staveniště umožňuje vhodně přizpůsobit technologii, která zaručí optimální řešení základů. Takový přístup je zvláště důležitý u investic s velkou plochou, jako je výrobní hala ATT, protože chybný odhad geologických podmínek může ovlivnit stabilitu celé konstrukce a generovat náklady ve fázi užívání objektu. Volba technologie a zesílení podloží – solidní základ pro dlouhověkou konstrukci Naše analýzy prokázaly, že terén určený k výstavbě vyžaduje zesílení, což umožňuje použití specializovaného vybavení, jako je pilotovací souprava. Díky tomu již ve fázi založení zajišťujeme konstrukci stabilitu a odolnost vůči provoznímu zatížení. Správná volba technologie založení základů je základem, na kterém spočívá celá konstrukce budovy. Použití pokročilých metod zakládání nám umožňuje zaručit trvanlivost a bezpečnost",
        "sk": "S radosťou oznamujeme začatie výstavby modernej výrobnej haly ATT v Kokotowe – investície, ktorá je pre nás ďalším dôkazom, že precízne plánovanie a dôkladné preskúmanie pôdnych podmienok sú základmi úspechu každej stavby. Plánovanie ako kľúčová etapa každej stavebnej investície Naše prístupy sa opiera o presvedčení, že čím lepšie naplánujeme každú etapu výstavby, tým efektívnejšie a bezpečnejšie bude jej realizácia prebiehať. Podrobné preskúmanie a analýza pôdno-vodných podmienok nám umožňujú odhaliť všetky potenciálne ťažkosti, ktoré môžu ovplyvniť stabilitu a trvanlivosť stavby. Toto je obzvlášť dôležité pri veľkých priemyselných investíciách, kde aj minimálne chyby môžu mať závažné dôsledky. Overenie prieskumov z fázy tendra a analýza terénu Jedným z kľúčových momentov našej práce je overenie pôdnych prieskumov vykonaných vo fáze tendra, pretože skutočné podmienky sa môžu líšiť od počiatočných predpokladov. Len dôkladná kontrola zeminy vykonaná po vstupe na stavenisko umožňuje prispôsobiť technológiu, ktorá zaručí optimálne riešenie pre základy. Takýto prístup je obzvlášť dôležitý pri investíciách s veľkou plochou, ako je výrobná hala ATT, pretože chybný odhad pôdnych podmienok môže ovplyvniť stabilitu celej konštrukcie a generovať náklady vo fáze užívania objektu. Výber technológie a spevnenie podložia – solídny základ pre dlhotrvajúcu konštrukciu Naše analýzy ukázali, že terén určený na výstavbu vyžaduje spevnenie, čo umožňuje použitie špecializovanej techniky, ako je baranidlo pilót. Vďaka tomu už vo fáze zakladania zabezpečujeme konštrukcii stabilitu a odolnosť voči úžitkovým zaťaženiam. Správny výber technológie zakladania základov je základom, na ktorom spočíva celá konštrukcia budovy. Použitie pokročilých metód zakladania nám umožňuje zaručiť trvanlivosť a b..."
    }
}
]

SECTORS = [
    {
    "title": "Hale przemysłowe i produkcyjne",
    "slug": "",
    "view_name": "#gw-wycena",
    "opis": "Obiekty dostosowane do rygorystycznych wymogów technologicznych, w tym hale z suwnicami i zaawansowanym parkiem maszynowym.",
    "icon": "ri-building-2-line",
    "image": "https://media.mbt.pl/uploads/a8d6d2908191.webp",
    "order": 0,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Konstrukcje stalowe",
    "slug": "konstrukcje-stalowe",
    "view_name": "sectorDetail",
    "opis": "Produkcja, dostawa i montaż nowoczesnych konstrukcji stalowych pod wszelkiego rodzaju obiekty wielkopowierzchniowe.",
    "icon": "ri-tools-line",
    "image": "https://media.mbt.pl/uploads/cfe86a26e478.webp",
    "order": 1,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Konstrukcje żelbetowe",
    "slug": "konstrukcje-zelbetowe",
    "view_name": "sectorDetail",
    "opis": "Realizacja trwałych i ognioodpornych konstrukcji żelbetowych, od fundamentów po skomplikowane stropy i słupy nośne.",
    "icon": "ri-building-4-line",
    "image": "https://media.mbt.pl/uploads/5c4261182884.webp",
    "order": 2,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Biurowce",
    "slug": "biurowce",
    "view_name": "sectorDetail",
    "opis": "Nowoczesne obiekty biurowe oraz prace fit-out, dostosowane do najwyższych standardów ergonomii i certyfikacji BREEAM.",
    "icon": "ri-briefcase-4-line",
    "image": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/151dd278be86.webp",
    "order": 3,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Parki handlowe",
    "slug": "parki-handlowe",
    "view_name": "sectorDetail",
    "opis": "Nowoczesne parki handlowe i obiekty retail. Dbamy o wielofunkcyjność (multi-use) i nowoczesny design elewacji.",
    "icon": "ri-shopping-bag-3-line",
    "image": "https://media.mbt.pl/uploads/eba049e8204f.webp",
    "order": 4,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Magazyny",
    "slug": "",
    "view_name": "haleMagazynowe",
    "opis": "Przestrzenie magazynowe wysokiego składowania, dopasowane do specyfiki łańcucha dostaw i wymogów pożarowych.",
    "icon": "ri-archive-line",
    "image": "https://media.mbt.pl/uploads/133184963a8c.webp",
    "order": 5,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Obiekty Self storage",
    "slug": "obiekty-self-storage",
    "view_name": "sectorDetail",
    "opis": "Nowoczesne obiekty magazynowe z kontrolowanym dostępem, zróżnicowanymi boksami i wysokimi standardami bezpieczeństwa.",
    "icon": "ri-box-3-line",
    "image": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/ed67bb1b2b03.webp",
    "order": 6,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Obiekty użyteczności publicznej",
    "slug": "obiekty-uzytecznosci-publicznej",
    "view_name": "sectorDetail",
    "opis": "Budynki użyteczności publicznej realizowane zgodnie z najwyższymi standardami dostępności i bezpieczeństwa.",
    "icon": "ri-government-line",
    "image": "/static/img/mbt/ZREALIZOWANE-ATT-5-scaled-b27ef1aa.jpg",
    "order": 7,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Obiekty medyczne (szpitale)",
    "slug": "obiekty-medyczne-szpitale",
    "view_name": "sectorDetail",
    "opis": "Specjalistyczne placówki ochrony zdrowia, szpitale i przychodnie budowane z myślą o pacjentach i personelu.",
    "icon": "ri-hospital-line",
    "image": "https://media.mbt.pl/uploads/f43899b152f8.webp",
    "order": 8,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Mieszkaniówka",
    "slug": "mieszkaniowka",
    "view_name": "sectorDetail",
    "opis": "Inwestycje deweloperskie i budynki wielorodzinne o wysokim standardzie wykończenia.",
    "icon": "ri-home-8-line",
    "image": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/4b52bd6eff86.webp",
    "order": 9,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Salony samochodowe i Automotive",
    "slug": "salony-samochodowe",
    "view_name": "sectorDetail",
    "opis": "Nowoczesne salony sprzedaży i autoryzowane stacje obsługi pojazdów spełniające normy producentów.",
    "icon": "ri-car-line",
    "image": "https://media.mbt.pl/uploads/a3fc2bc72cbe.webp",
    "order": 10,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Chłodnie i mroźnie (branża spożywcza)",
    "slug": "chlodnie-mroznie",
    "view_name": "sectorDetail",
    "opis": "Obiekty z kontrolowaną temperaturą i rygorystycznymi normami sanitarnymi.",
    "icon": "ri-temp-cold-line",
    "image": "https://media.mbt.pl/uploads/4e0ab68864c3.webp",
    "order": 11,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Obiekty e-commerce",
    "slug": "obiekty-e-commerce",
    "view_name": "sectorDetail",
    "opis": "Nowoczesne przestrzenie logistyczne dostosowane do szybkiej obsługi zamówień (sortownie, centra dystrybucyjne).",
    "icon": "ri-shopping-cart-2-line",
    "image": "https://media.mbt.pl/uploads/6c56aa2fb100.webp",
    "order": 12,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Centra R&D i Laboratoria",
    "slug": "centra-badawczo-rozwojowe",
    "view_name": "sectorDetail",
    "opis": "Zaawansowane technologicznie obiekty badawcze wymagające precyzyjnych instalacji i warunków.",
    "icon": "ri-test-tube-line",
    "image": "https://media.mbt.pl/uploads/a2862c2e44c5.webp",
    "order": 13,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Data Center / Serwerownie",
    "slug": "data-center",
    "view_name": "sectorDetail",
    "opis": "Bezpieczne i wydajne energetycznie obiekty dla infrastruktury IT o podwyższonym standardzie zasilania.",
    "icon": "ri-server-line",
    "image": "https://media.mbt.pl/uploads/e832f1a38f9f.webp",
    "order": 14,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Hale sportowe i widowiskowe",
    "slug": "hale-sportowe",
    "view_name": "sectorDetail",
    "opis": "Wielofunkcyjne obiekty sportowe, areny i hale zaprojektowane z myślą o masowych wydarzeniach.",
    "icon": "ri-basketball-line",
    "image": "https://media.mbt.pl/uploads/d2c5e6b809e6.webp",
    "order": 15,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Obiekty branży militarnej",
    "slug": "obiekty-militarne",
    "view_name": "sectorDetail",
    "opis": "Obiekty o podwyższonym rygorze bezpieczeństwa i specjalistycznych wymaganiach konstrukcyjnych.",
    "icon": "ri-shield-cross-line",
    "image": "https://media.mbt.pl/uploads/46a252afa9c0.webp",
    "order": 16,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Zakłady recyklingu i gospodarka odpadami",
    "slug": "zaklady-recyklingu",
    "view_name": "sectorDetail",
    "opis": "Ekologiczne zakłady przetwarzania odpadów i nowoczesne instalacje ochrony środowiska.",
    "icon": "ri-recycle-line",
    "image": "https://media.mbt.pl/uploads/1648f91ebdc2.webp",
    "order": 17,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Centra handlowe",
    "slug": "centra-handlowe",
    "view_name": "sectorDetail",
    "opis": "Przestrzenie komercyjne łączące funkcje handlowe, rozrywkowe i usługowe w atrakcyjnej formie.",
    "icon": "ri-shopping-bag-line",
    "image": "https://media.mbt.pl/uploads/8815bdaf26e7.webp",
    "order": 18,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Markety",
    "slug": "markety",
    "view_name": "sectorDetail",
    "opis": "Funkcjonalne obiekty handlowe o optymalnym układzie komunikacyjnym dla wygody klientów.",
    "icon": "ri-store-2-line",
    "image": "/static/img/mbt/ZREALIZOWANE-ATT-5-scaled-b27ef1aa.jpg",
    "order": 19,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Markety budowlane",
    "slug": "markety-budowlane",
    "view_name": "sectorDetail",
    "opis": "Wielkopowierzchniowe obiekty handlowe dostosowane konstrukcyjnie do asortymentu budowlanego.",
    "icon": "ri-tools-line",
    "image": "/static/img/mbt/ZREALIZOWANE-ATT-6-scaled-e17253f9.jpg",
    "order": 20,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Sklepy stacjonarne",
    "slug": "sklepy-stacjonarne",
    "view_name": "sectorDetail",
    "opis": "Atrakcyjne wizualnie lokale i pawilony handlowe dla różnorodnych branż.",
    "icon": "ri-store-3-line",
    "image": "https://media.mbt.pl/uploads/b6991aad2996.webp",
    "order": 21,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Galerie handlowe",
    "slug": "galerie-handlowe",
    "view_name": "sectorDetail",
    "opis": "Prestiżowe obiekty handlowe o unikalnej architekturze i wysokim standardzie wykończenia.",
    "icon": "ri-building-3-line",
    "image": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/151dd278be86.webp",
    "order": 22,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Hipermarkety",
    "slug": "hipermarkety",
    "view_name": "sectorDetail",
    "opis": "Duże obiekty handlowe z zaawansowaną infrastrukturą towarzyszącą i przestronnymi parkingami.",
    "icon": "ri-shopping-basket-line",
    "image": "https://media.mbt.pl/uploads/33a95c4212a6.webp",
    "order": 23,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Nieruchomości komercyjne",
    "slug": "nieruchomosci-komercyjne",
    "view_name": "sectorDetail",
    "opis": "Inwestycje w nieruchomości przeznaczone pod wynajem oraz różnorodną działalność biznesową.",
    "icon": "ri-building-4-line",
    "image": "/static/img/mbt/3-2-scaled-38947c85.jpg",
    "order": 24,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Powierzchnie usługowo-handlowe",
    "slug": "powierzchnie-uslugowo-handlowe",
    "view_name": "sectorDetail",
    "opis": "Nowoczesne lokale usługowe i handlowe elastycznie dostosowane do potrzeb przyszłych najemców.",
    "icon": "ri-storefront-line",
    "image": "https://media.mbt.pl/uploads/ddb053ae7834.webp",
    "order": 25,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Fabryki",
    "slug": "fabryki",
    "view_name": "sectorDetail",
    "opis": "Zaawansowane zakłady przemysłowe i złożone linie produkcyjne dla różnych sektorów gospodarki.",
    "icon": "ri-factory-line",
    "image": "/static/img/mbt/hala-1024x672-eb7144c9.jpg",
    "order": 26,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Wytwórnie",
    "slug": "wytwornie",
    "view_name": "sectorDetail",
    "opis": "Specjalistyczne obiekty produkcyjne dopasowane do unikalnych procesów technologicznych.",
    "icon": "ri-flask-line",
    "image": "https://media.mbt.pl/uploads/ac71356f53de.webp",
    "order": 27,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Place składowe",
    "slug": "place-skladowe",
    "view_name": "sectorDetail",
    "opis": "Profesjonalnie utwardzone i odpowiednio przygotowane tereny pod bezpieczne składowanie materiałów.",
    "icon": "ri-map-pin-line",
    "image": "https://media.mbt.pl/uploads/9ac4af006f93.webp",
    "order": 28,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Centra Biznesowe",
    "slug": "centra-biznesowe",
    "view_name": "sectorDetail",
    "opis": "Kompleksy biurowe i prestiżowe przestrzenie do prowadzenia działalności korporacyjnej.",
    "icon": "ri-briefcase-line",
    "image": "/static/img/mbt/ZREALIZOWANE-ATT-3-scaled-b0f20287.jpg",
    "order": 29,
    "t_t": {},
    "t_o": {}
},
    {
    "title": "Magazyny automatyczne",
    "slug": "magazyny-automatyczne",
    "view_name": "sectorDetail",
    "opis": "Nowoczesne przestrzenie magazynowe projektowane specjalnie pod zautomatyzowane systemy logistyczne.",
    "icon": "ri-robot-line",
    "image": "https://media.mbt.pl/uploads/04bfb07ae41b.webp",
    "order": 30,
    "t_t": {},
    "t_o": {}
}
]

AWARDS = [
    {
    "name": "Gazele Biznesu",
    "image": "/static/img/mbt/award-gazele.png",
    "order": 1
},
    {
    "name": "Rzetelna Firma",
    "image": "/static/img/mbt/award-rzetelna.svg",
    "order": 2
},
    {
    "name": "Diamenty Forbesa",
    "image": "/static/img/mbt/award-forbes.svg",
    "order": 3
}
]

PHOTOS = {
    "home_hero_bg": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/e7c67178548f.webp",
    "home_att8": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/42b91ab7c950.webp",
    "home_o_nas_2": "/static/img/mbt/o-nas-2.jpg",
    "home_o_nas_zespol": "https://media.mbt.pl/uploads/c4f9f468d740.webp",
    "home_realizacja": "/static/img/mbt/realizacja-eurosleeve.jpg",
    "home_bg_why": "/static/img/bg/why-bg3-1.png",
    "home_bg_cta": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/c4c3b74ce689.webp",
    "home_bg_contact": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/34754bbfa84c.webp",
    "home_client_group": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/65f5ac2e1b40.webp",
    "home_testi_2": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/aaa9406ed7a3.webp",
    "work_gallery": [
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/caa74380050b.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/6f43bfc3bf1c.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/d9df34622f41.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/2e72cf285aaf.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/7a1b37c27156.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/d016fd735e56.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/cc59a6d9b5d5.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/91a266765989.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/2b0eecc96d45.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/427662a1bd15.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/ee5d542c1a17.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/5df613347b32.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/4cec556f3753.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/f491e80d2a25.webp",
        "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/609ba634da28.webp"
    ],
    "about_1": "/static/img/mbt/o-nas-1.jpg",
    "service_1": "/static/img/mbt/Eurosleeve-10-scaled-fd8f7247.jpg",
    "service_2": "/static/img/mbt/IMG_20220722_102326-scaled-1-fdde92f8.jpg",
    "gw_hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/edc93501919b.webp",
    "gw_1": "/static/img/mbt/ZREALIZOWANE-ATT-1-scaled-f12dacac.jpg",
    "gw_2": "/static/img/mbt/ZREALIZOWANE-ATT-3-scaled-b0f20287.jpg",
    "gw_3": "https://media.mbt.pl/uploads/a8d6d2908191.webp",
    "gw_4": "/static/img/mbt/ZREALIZOWANE-ATT-5-scaled-b27ef1aa.jpg",
    "gw_5": "/static/img/mbt/ZREALIZOWANE-ATT-6-scaled-e17253f9.jpg",
    "gw_6": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/4b52bd6eff86.webp",
    "gw_7": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/151dd278be86.webp",
    "gw_8": "/static/img/mbt/Huber-6-scaled-b00b8b23.jpg",
    "gw_9": "/static/img/mbt/3-2-scaled-38947c85.jpg",
    "gw_10": "/static/img/mbt/breem-e659b8f2.jpg",
    "gw_11": "/static/img/mbt/hala-1024x672-eb7144c9.jpg",
    "gw_12": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/205539665175.webp",
    "bg_header": "/static/img/bg/header-1-bg.png",
    "bg_footer": "/static/img/bg/footer-bg1-1.png",
    "bg_breadcrumb": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/374e7a5adfbf.webp",
    "hale_przemyslowe_hero": "https://media.mbt.pl/uploads/41003d4cca6e.webp",
    "hale_przemyslowe_1": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/a07b2f5a2585.webp",
    "hale_przemyslowe_2": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/36d1642694e1.webp",
    "hale_magazynowe_hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/cde95e4141b2.webp",
    "hale_magazynowe_1": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/6f70f8a65c1f.webp",
    "obiekty_komercyjne_hero": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/570767cfd0e4.webp",
    "obiekty_komercyjne_1": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/80628a4cba4c.webp",
    "obiekty_komercyjne_2": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/uploads/c6103a286635.webp",
    "general_contracting_1": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/0b5b6f5c26b1.webp",
    "general_contracting_2": "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/ed67bb1b2b03.webp"
}
