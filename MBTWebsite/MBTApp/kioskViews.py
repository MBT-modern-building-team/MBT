"""Widok Kiosku Dotykowego (mbt.pl/kiosk).

Zaprojektowany specjalnie dla 32-calowego monitora dotykowego 4K LG (webOS).
Udostępnia pełne portfolio MBT Modern Building Team, model 'Zaprojektuj i wybuduj',
interaktywny suwak Przed/Po, referencje oraz pełnowymiarowy Pitch Deck prezentacyjny.
"""
import json
from django.shortcuts import render
from MBTApp import mbt_orm


def _get_presentation_slides(site):
    """Zwraca usystematyzowaną, 10-slajdową prezentację MBT."""
    return [
        {
            'id': 1,
            'title': 'Jeden team – pełna realizacja',
            'subtitle': 'Od projektu aż po dach! Twój Generalny Wykonawca hal przemysłowych i magazynowych.',
            'tag': 'WPROWADZENIE',
            'badge': 'Diamenty Forbesa 2026 💎',
            'bg_image': '/static/img/mbt/o-nas-1.jpg',
            'points': [
                'Kompleksowe generalne wykonawstwo inwestycji kubaturowych w całej Polsce',
                'Specjalizacja w formule „Zaprojektuj i wybuduj” (Design & Build)',
                'Ponad 20 lat doświadczenia inżynierskiego i 100% terminowości',
                'Własna wyspecjalizowana kadra kierownicza i inżynieryjna',
            ],
            'stat_number': '100+',
            'stat_label': 'Zrealizowanych obiektów',
        },
        {
            'id': 2,
            'title': 'Diamenty Forbesa 2026',
            'subtitle': 'Potwierdzenie stabilności finansowej, dynamiki rozwoju i inżynierskiej rzetelności.',
            'tag': 'STABILNOŚĆ & ZAUFANIE',
            'badge': 'Laureat Rankingu Forbes',
            'bg_image': '/static/img/mbt/artykul-diamenty-forbesa-2026.webp',
            'points': [
                'Wycena oparta o rzetelną szwajcarską metodę analityków Dun & Bradstreet',
                'Pełne bezpieczeństwo kapitałowe dla Inwestorów i instytucji finansujących',
                'Stabilne zaplecze finansowe i ubezpieczeniowe kontraktów wielomilionowych',
                'Wyróżnienia: Gazele Biznesu, Złoty Laur RIG Katowice, Rzetelna Firma',
            ],
            'stat_number': '100%',
            'stat_label': 'Wiarygodności finansowej',
        },
        {
            'id': 3,
            'title': 'Model „Zaprojektuj i wybuduj” (Design & Build)',
            'subtitle': 'Jeden partner, jedna odpowiedzialność – eliminacja sporów między projektantem a wykonawcą.',
            'tag': 'METODOLOGIA',
            'badge': 'Optymalizacja Inwestycji',
            'bg_image': '/static/img/mbt/design-build-2026.jpg',
            'points': [
                'Brak bufora i konfliktów: Inwestor ma jednego partnera od koncepcji po odbiór',
                'Gwarancja budżetu: Koszty są znane i gwarantowane już na etapie koncepcji',
                'Koordynacja administracyjna: Uzyskujemy decyzje środowiskowe, WZ, PnB i PnU',
                'Płynne przekazanie do eksploatacji z pełną dokumentacją powykonawczą',
            ],
            'stat_number': '-25%',
            'stat_label': 'Mniej formalności po stronie Inwestora',
        },
        {
            'id': 4,
            'title': 'Value Engineering: Inżynieria Wartości',
            'subtitle': 'Oszczędności powstają przy desce kreślarskiej, a nie kosztem jakości na budowie.',
            'tag': 'OPTYMALIZACJA KOSZTÓW',
            'badge': 'Oszczędność Budżetu',
            'bg_image': '/static/img/mbt/ZREALIZOWANE-ATT-4-scaled-ffc91418.jpg',
            'points': [
                'Optymalizacja konstrukcji stalowej i żelbetowej: eliminacja przewymiarowania',
                'Dobór posadowienia: precyzyjna kalkulacja między palowaniem a wymianą gruntu',
                'Efektywność energetyczna: rozwiązania ograniczające późniejsze koszty eksploatacji (OPEX)',
                'Certyfikacja BREEAM / LEED w standardzie na życzenie Inwestora',
            ],
            'stat_number': '15-20%',
            'stat_label': 'Średniej redukcji kosztów konstrukcji',
        },
        {
            'id': 5,
            'title': 'Fast-Tracking: Czas to Pieniądz',
            'subtitle': 'Nakładanie się etapów projektowych i budowlanych skraca czas realizacji o miesiące.',
            'tag': 'HARMONOGRAM',
            'badge': 'Szybki Zwrot z Inwestycji',
            'bg_image': '/static/img/mbt/DSC03738-scaled-c238f3f3.jpeg',
            'points': [
                'Równoległość procesów: Prace ziemne i fundamentowe ruszają w trakcie dopinania detali branżowych',
                'Wcześniejsze zamawianie konstrukcji stalowej bezpośrednio u sprawdzonych wytwórców',
                'Cotygodniowe raportowanie z drona i bieżący monitoring kamery online z placu budowy',
                'Oddanie do użytkowania przed umownym terminem to szybszy przychód dla Twojego biznesu',
            ],
            'stat_number': '3-5 m-cy',
            'stat_label': 'Szybsze oddanie hali do użytku',
        },
        {
            'id': 6,
            'title': 'Specjalizacje Budowlane MBT',
            'subtitle': 'Kompleksowe obiekty kubaturowe dopasowane do specyfiki procesów technologicznych.',
            'tag': 'OFERTA',
            'badge': 'Wszechstronność',
            'bg_image': '/static/img/mbt/realizacja-eurosleeve.jpg',
            'points': [
                'Hale magazynowe i centra logistyczne (wysokie składowanie, posadzki bezspoinowe)',
                'Zaawansowane hale produkcyjne (suwnice, instalacje technologiczne, sprężone powietrze)',
                'Chłodnie, mroźnie i zakłady przetwórstwa spożywczego (rygorystyczne normy sanitarne)',
                'Parki handlowe, salony wystawiennicze oraz nowoczesne biurowce klasy A',
            ],
            'stat_number': '100%',
            'stat_label': 'Standardu wykonania pod klucz',
        },
        {
            'id': 7,
            'title': 'ESG, Zielone Budownictwo i BREEAM',
            'subtitle': 'Inwestycje przyszłości: niskoemisyjność, samowystarczalność energetyczna i trwałość.',
            'tag': 'ZRÓWNOWAŻONY ROZWÓJ',
            'badge': 'Certyfikacja BREEAM',
            'bg_image': '/static/img/mbt/breem-e659b8f2.jpg',
            'points': [
                'Konstrukcje dachowe przygotowane pod pełne obciążenie instalacjami PV (fotowoltaika)',
                'Zaawansowane pompy ciepła, rekuperacja i odzysk ciepła z procesów technologicznych',
                'Retencja wód opadowych, zbiorniki bezodpływowe i zielone strefy buforowe',
                'Ułatwiona ścieżka zielonego finansowania (Green Bonds / preferencyjne kredyty bankowe)',
            ],
            'stat_number': 'A+',
            'stat_label': 'Klasa efektywności energetycznej',
        },
        {
            'id': 8,
            'title': 'Kultura BHP i Nadzór Inżynierski',
            'subtitle': 'Zero kompromisów w bezpieczeństwie. Budowa prowadzona według najwyższych norm europejskich.',
            'tag': 'BEZPIECZEŃSTWO',
            'badge': 'Standard MBT Safe',
            'bg_image': '/static/img/mbt/mbt_baner_bhp.png',
            'points': [
                'Dedykowany Koordynator BHP na każdym placu budowy MBT',
                'Stały nadzór uprawnionych Kierowników Budów i Inspektorów Nadzoru Inwestorskiego',
                'Elektroniczny obieg dokumentacji i dziennik budowy dostępny dla Inwestora online 24/7',
                'Własne standardy oznakowania budowy i rygorystyczny dobór certyfikowanych podwykonawców',
            ],
            'stat_number': 'Zero',
            'stat_label': 'Wypadków na budowach',
        },
        {
            'id': 9,
            'title': 'Zaufali nam liderzy rynku',
            'subtitle': 'Wieloletnie relacje i kolejne realizacje powierzane MBT przez stałych partnerów.',
            'tag': 'REFERENCJE',
            'badge': 'Partnerzy Biznesowi',
            'bg_image': '/static/img/mbt/ZREALIZOWANE-ATT-8-c1d848dd.jpg',
            'points': [
                'Kompania Piwowarska, Canpack, Browar Zamkowy, Huber+Suhner, Less Mess Storage',
                'Euro-Trade, DL Invest Group, Epco, Herz, Toto Hair Company, Sutco Polska',
                'Wysoki wskaźnik repeat business: ponad 70% Inwestorów wraca do nas z kolejnymi etapami',
                'Pisane referencje zarządów potwierdzające terminowość i kulturę inżynierską',
            ],
            'stat_number': '70%+',
            'stat_label': 'Inwestycji od powracających Klientów',
        },
        {
            'id': 10,
            'title': 'Rozpocznijmy współpracę',
            'subtitle': 'Przeanalizujemy Twoją działkę, zrobimy wstępną koncepcję i wycenimy inwestycję w 7 dni.',
            'tag': 'KONTAKT & START',
            'badge': 'Twój Partner w Biznesie',
            'bg_image': '/static/img/mbt/o-nas-zespol.jpg',
            'points': [
                'Bezpłatna wstępna analiza chłonności terenu i warunków gruntowo-wodnych',
                'Opracowanie szacunkowego budżetu i harmonogramu w wariancie Design & Build',
                'Biura w Katowicach, Zabrzu i Krakowie – działamy na terenie całego kraju',
                'Zeskanuj kod QR na ekranie, aby pobrać bezpośredni kontakt do Dyrekcji MBT',
            ],
            'stat_number': '7 dni',
            'stat_label': 'Czas na wstępną koncepcję hali',
        },
    ]


def kiosk_view(request):
    """Główny widok Kiosku Dotykowego MBT."""
    lang = 'pl'
    projects = mbt_orm.get_projects(lang=lang)
    site = mbt_orm.get_site(lang=lang)
    references = mbt_orm.get_references(lang=lang)
    awards = mbt_orm.get_awards()
    workers = mbt_orm.get_workers(lang=lang)
    sales_reps = mbt_orm.get_sales_reps(lang=lang)
    sectors = mbt_orm.get_sectors(lang=lang)

    # Przygotowanie bezpiecznej reprezentacji JSON projektów pod szybki modal
    clean_projects = []
    for p in projects:
        clean_projects.append({
            'title': p.get('title', ''),
            'slug': p.get('slug', ''),
            'type': p.get('type', ''),
            'status': p.get('status', ''),
            'czas': p.get('czas', ''),
            'formula': p.get('formula', ''),
            'opis': p.get('opis', ''),
            'hero': p.get('hero', ''),
            'logo': p.get('logo', ''),
            'gallery': p.get('gallery', []) or [],
        })

    projects_json = json.dumps(clean_projects, ensure_ascii=False)

    # Slajdy do pełnoekranowej prezentacji MBT
    presentation_slides = _get_presentation_slides(site)

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
        'workers': workers,
        'sales_reps': sales_reps,
        'sectors': sectors,
        'trusted_brands': trusted_brands,
        'presentation_slides': presentation_slides,
        'before_after': before_after,
    }

    return render(request, 'pages/kiosk.html', context)
