"""Modele Django dla strony MBT.

Dane edytujesz w panelu admina (/admin). Widoki czytają je przez ORM
(MBTApp/mbt_orm.py) z fallbackiem do mbt_data.py, więc kontrakt danych
(dict) jest zachowany — szablony działają bez zmian.
"""
from django.db import models


class Project(models.Model):
    """Realizacja (hala, magazyn, biurowiec...).

    Wielojęzyczność: atrybuty tekstowe (title, opis, czas, status, formula) mają
    pomocnicze pola JSON z mapą język→tekst, np. {"pl":"BTS Park","en":"BTS Park",...}.
    Szablon pobiera właściwy wariant przez gettext + fallback na polski.
    """

    TYPE_CHOICES = [
        ('realizacja-zrealizow', 'Zrealizowane'),
        ('realizacja-w-trakcie', 'W trakcie realizacji'),
    ]

    title = models.CharField('Tytuł (PL)', max_length=200)
    slug = models.SlugField('Slug (adres URL)', max_length=200, unique=True)
    type = models.CharField('Typ', max_length=40, choices=TYPE_CHOICES, default='realizacja-zrealizow')
    status = models.CharField('Status (PL)', max_length=80, default='Zrealizowane')
    czas = models.CharField('Czas realizacji (PL)', max_length=120, blank=True)
    formula = models.CharField('Formuła (PL)', max_length=120, blank=True)
    opis = models.TextField('Opis (specyfikacja) PL', blank=True)
    logo = models.CharField('Logo firmy (URL)', max_length=500, blank=True)
    hero = models.CharField('Zdjęcie główne (URL)', max_length=500, blank=True)
    gallery = models.JSONField('Galeria (lista URL-i)', default=list, blank=True)
    latitude = models.FloatField('Szerokość geogr. (Latitude)', null=True, blank=True, help_text='Np. 52.2297 dla Warszawy')
    longitude = models.FloatField('Długość geogr. (Longitude)', null=True, blank=True, help_text='Np. 21.0122 dla Warszawy')
    order = models.PositiveIntegerField('Kolejność', default=0)

    # Wielojęzyczność (JSON: {lang: text}). Puste = fallback na PL.
    t_title = models.JSONField('Tytuł — tłumaczenia', default=dict, blank=True,
                               help_text='JSON np. {"en":"...","de":"...","cs":"...","sk":"...","hu":"..."}')
    t_status = models.JSONField('Status — tłumaczenia', default=dict, blank=True)
    t_czas = models.JSONField('Czas realizacji — tłumaczenia', default=dict, blank=True)
    t_formula = models.JSONField('Formuła — tłumaczenia', default=dict, blank=True)
    t_opis = models.JSONField('Opis — tłumaczenia', default=dict, blank=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Realizacja'
        verbose_name_plural = 'Realizacje'

    def __str__(self):
        return self.title


class Job(models.Model):
    """Oferta pracy w dziale Kariera."""

    title = models.CharField('Stanowisko (PL)', max_length=200)
    slug = models.SlugField('Slug (adres URL)', max_length=200, unique=True)
    text = models.TextField('Treść oferty (PL)')
    order = models.PositiveIntegerField('Kolejność', default=0)

    # Wielojęzyczność (JSON: {lang: text}). Puste = fallback na PL.
    t_title = models.JSONField('Stanowisko — tłumaczenia', default=dict, blank=True,
                               help_text='JSON np. {"en":"...","de":"...","cs":"...","sk":"...","hu":"..."}')
    t_text = models.JSONField('Treść oferty — tłumaczenia', default=dict, blank=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Oferta pracy'
        verbose_name_plural = 'Oferty pracy'

    def __str__(self):
        return self.title


class Worker(models.Model):
    """Pracownik — sekcja Zespół."""

    name = models.CharField('Imię i nazwisko', max_length=200)
    position = models.CharField('Stanowisko (PL)', max_length=200)
    opis = models.TextField('Opis (PL)', blank=True)
    photo = models.CharField('Zdjęcie (URL)', max_length=500, blank=True)
    linkedin = models.URLField('LinkedIn (URL)', blank=True)
    order = models.PositiveIntegerField('Kolejność', default=0)

    # Wielojęzyczność (JSON: {lang: text}). Puste = fallback na PL.
    t_position = models.JSONField('Stanowisko — tłumaczenia', default=dict, blank=True,
                                  help_text='JSON np. {"en":"...","de":"...","cs":"...","sk":"...","hu":"..."}')
    t_opis = models.JSONField('Opis — tłumaczenia', default=dict, blank=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Pracownik'
        verbose_name_plural = 'Pracownicy'

    def __str__(self):
        return self.name


class Reference(models.Model):
    """Opinia klienta — sekcja Opinie."""

    firma = models.CharField('Firma', max_length=200)
    tresc = models.TextField('Treść opinii (PL)')
    osoba = models.CharField('Osoba (PL)', max_length=200, blank=True)
    stanowisko = models.CharField('Stanowisko (PL)', max_length=200, blank=True)
    order = models.PositiveIntegerField('Kolejność', default=0)

    # Wielojęzyczność (JSON: {lang: text}). Puste = fallback na PL.
    t_tresc = models.JSONField('Treść opinii — tłumaczenia', default=dict, blank=True,
                               help_text='JSON np. {"en":"...","de":"...","cs":"...","sk":"...","hu":"..."}')
    t_osoba = models.JSONField('Osoba — tłumaczenia', default=dict, blank=True)
    t_stanowisko = models.JSONField('Stanowisko — tłumaczenia', default=dict, blank=True)

    class Meta:
        ordering = ['order', 'firma']
        verbose_name = 'Opinia klienta'
        verbose_name_plural = 'Opinie klientów'

    def __str__(self):
        return self.firma


class Article(models.Model):
    """Artykuł na blogu."""

    title = models.CharField('Tytuł (PL)', max_length=300)
    slug = models.SlugField('Slug (adres URL)', max_length=300, unique=True)
    excerpt = models.CharField('Skrót (podgląd) PL', max_length=400, blank=True)
    text = models.TextField('Treść artykułu (PL)')
    image = models.CharField('Zdjęcie główne (URL)', max_length=500, blank=True)
    gallery = models.JSONField('Galeria (lista URL-i)', default=list, blank=True)
    published = models.BooleanField('Opublikowany', default=True)
    created = models.DateTimeField('Data dodania', auto_now_add=True)
    order = models.PositiveIntegerField('Kolejność', default=0)

    # Wielojęzyczność (JSON: {lang: text}). Puste = fallback na PL.
    t_title = models.JSONField('Tytuł — tłumaczenia', default=dict, blank=True,
                               help_text='JSON np. {"en":"...","de":"...","cs":"...","sk":"...","hu":"..."}')
    t_excerpt = models.JSONField('Skrót — tłumaczenia', default=dict, blank=True)
    t_text = models.JSONField('Treść artykułu — tłumaczenia', default=dict, blank=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Artykuł'
        verbose_name_plural = 'Artykuły'

    def __str__(self):
        return self.title


class SiteConfig(models.Model):
    """Dane firmy (telefon, adresy, liczniki, social) — jeden rekord."""

    phone = models.CharField('Telefon', max_length=40, default='+48 881 444 333')
    phone_href = models.CharField('Telefon (href)', max_length=40, default='+48881444333')
    email = models.EmailField('E-mail', default='biuro@mbt.pl')
    hours = models.CharField('Godziny (krótko)', max_length=60, default='Pon - Pt / 8:00 - 16:00')
    hours_long = models.CharField('Godziny (długo)', max_length=60, default='Pon-Pt: 8:00 do 16:00')

    office_zabrze = models.CharField('Biuro Zabrze', max_length=200, default='Roosevelta 81, 41-800 Zabrze')
    office_katowice = models.CharField('Siedziba Katowice', max_length=200, default='Jankego 176/1A, 40-663 Katowice')
    office_krakow = models.CharField('Oddział Kraków', max_length=200, default='Zawiła 65, bud. X lok. 5, 30-390 Kraków')

    # Zdjęcia biur na stronie /kontakt/ (URL lub ścieżka statyczna)
    office_zabrze_photo = models.CharField('Zdjęcie biura Zabrze (URL)', max_length=500, blank=True,
                                           default='/static/img/mbt/o-nas-1.jpg')
    office_katowice_photo = models.CharField('Zdjęcie siedziby Katowice (URL)', max_length=500, blank=True,
                                             default='/static/img/mbt/o-nas-zespol.jpg')
    office_krakow_photo = models.CharField('Zdjęcie oddziału Kraków (URL)', max_length=500, blank=True,
                                           default='/static/img/mbt/o-nas-2.jpg')
    # 4. lokalizacja: "Twój plac budowy" (Twoja inwestycja)
    office_site_label = models.CharField('Plac budowy: nagłówek', max_length=120, blank=True,
                                         default='Twój plac budowy')
    office_site_adres = models.CharField('Plac budowy: adres', max_length=200, blank=True,
                                         default='Adres Twojej inwestycji')
    office_site_photo = models.CharField('Zdjęcie placu budowy (URL) - stare', max_length=500, blank=True,
                                         default='/static/img/mbt/DSC03738-scaled-c238f3f3.jpeg')
    office_site_gallery = models.JSONField('Galeria placu budowy (lista URL-i)', default=list, blank=True)

    nip = models.CharField('NIP', max_length=20, default='9542788822')
    regon = models.CharField('REGON', max_length=20, default='369557780')
    krs = models.CharField('KRS', max_length=20, default='0000720424')
    founded = models.CharField('Rok założenia', max_length=10, default='2005')
    tagline = models.CharField('Slogan', max_length=300, default='Z pasją budujemy Wasze biznesy. Jeden team – pełna realizacja. Od projektu aż po dach!')
    about_short = models.TextField('Opis firmy (stopka)', default='MBT Modern Building Team — generalny wykonawca hal magazynowych, produkcyjnych i usługowych. Terminowa budowa obiektów przemysłowych pod klucz.')

    # Tłumaczenia t_* (JSON {lang: text}) — używane gdy DB dostępne
    t_tagline = models.JSONField('Slogan — tłumaczenia', default=dict, blank=True,
                                help_text='JSON {pl: "...", en: "...", de: "...", cs: "...", sk: "...", hu: "..."}')
    t_about_short = models.JSONField('Opis firmy — tłumaczenia', default=dict, blank=True)
    t_counter_years_label = models.JSONField('Licznik "lata" — tłumaczenia', default=dict, blank=True)
    t_counter_projects_label = models.JSONField('Licznik "inwestycje" — tłumaczenia', default=dict, blank=True)
    t_counter_ontime_label = models.JSONField('Licznik "terminowość" — tłumaczenia', default=dict, blank=True)
    t_counter_brands_label = models.JSONField('Licznik "marki" — tłumaczenia', default=dict, blank=True)
    t_hours = models.JSONField('Godziny — tłumaczenia', default=dict, blank=True)
    t_hours_long = models.JSONField('Godziny długie — tłumaczenia', default=dict, blank=True)
    t_office_zabrze = models.JSONField('Biuro Zabrze — tłumaczenia', default=dict, blank=True)
    t_office_katowice = models.JSONField('Siedziba Katowice — tłumaczenia', default=dict, blank=True)
    t_office_krakow = models.JSONField('Oddział Kraków — tłumaczenia', default=dict, blank=True)

    counter_years = models.CharField('Licznik: lata', max_length=10, default='100%')
    counter_years_label = models.CharField('Licznik: lata (etykieta)', max_length=80, default='Zaangażowania')
    counter_projects = models.CharField('Licznik: inwestycje', max_length=10, default='100')
    counter_projects_label = models.CharField('Licznik: inwestycje (etykieta)', max_length=80, default='Zrealizowanych inwestycji')
    counter_ontime = models.CharField('Licznik: terminowość', max_length=10, default='100')
    counter_ontime_suffix = models.CharField('Licznik: terminowość (sufiks)', max_length=10, default='%')
    counter_ontime_label = models.CharField('Licznik: terminowość (etykieta)', max_length=80, default='Terminowości')
    counter_brands = models.CharField('Licznik: marki', max_length=10, default='16')
    counter_brands_label = models.CharField('Licznik: marki (etykieta)', max_length=80, default='Zaufanych marek')

    # Hero (Strona główna)
    hero_subtitle = models.CharField('Podtytuł hero', max_length=200, default='Z pasją budujemy Wasze biznesy')
    hero_title1 = models.CharField('Tytuł hero 1', max_length=200, default='Twój Generalny')
    hero_title2 = models.CharField('Tytuł hero 2', max_length=200, default='Wykonawca')
    hero_text = models.TextField('Tekst hero', default='Jeden team – pełna realizacja. <strong>Od projektu aż po dach!</strong> Budujemy hale magazynowe, produkcyjne i usługowe pod klucz.')

    t_hero_subtitle = models.JSONField('Podtytuł hero — tłum.', default=dict, blank=True)
    t_hero_title1 = models.JSONField('Tytuł hero 1 — tłum.', default=dict, blank=True)
    t_hero_title2 = models.JSONField('Tytuł hero 2 — tłum.', default=dict, blank=True)
    t_hero_text = models.JSONField('Tekst hero — tłum.', default=dict, blank=True)

    social_linkedin = models.URLField('LinkedIn', blank=True)
    social_youtube = models.URLField('YouTube', blank=True)
    social_facebook = models.URLField('Facebook', blank=True)
    social_instagram = models.URLField('Instagram', blank=True)

    # Film w tle strony głównej (hero) — URL wgranego pliku wideo
    hero_video = models.CharField('Film w tle (strona główna)', max_length=500, blank=True,
                                  help_text='Wgraj film MP4 (bez dźwięku, odtwarzany w pętli) — pojawi się zamiast zdjęcia w sekcji hero na stronie głównej.')

    class Meta:
        verbose_name = 'Dane firmy'
        verbose_name_plural = 'Dane firmy'

    def __str__(self):
        return 'Dane firmy (edytuj)'


def default_work_gallery():
    return [
        '/static/img/mbt/DSC03626-scaled-6f5bda4e.jpeg',
        '/static/img/mbt/DSC03726-scaled-04284a3e.jpeg',
        '/static/img/mbt/DSC03730-scaled-ee7d1094.jpeg',
        '/static/img/mbt/DSC03738-scaled-c238f3f3.jpeg',
        '/static/img/mbt/DSC03980-scaled-ea8b4933.jpeg',
        '/static/img/mbt/DJI_0174-scaled-5106e265.jpeg',
        '/static/img/mbt/DJI_0181-1-scaled-b366f7fb.jpeg',
        '/static/img/mbt/DJI_3-03272d0f.jpg',
    ]

class SitePhotos(models.Model):
    """Fotografie strony — każda podmienialna z poziomu admina (upload na R2).

    Jedno pole = jedno miejsce na stronie/podstronie. Puste pole = brak
    podmiany (używana domyślna ścieżka statyczna). Wzorzec jak SiteConfig.
    """

    home_hero_bg = models.CharField('Hero — tło/poszerzenie strony głównej', max_length=500, blank=True, default='/static/img/hero/hero_bg_3_1.png')
    home_att8 = models.CharField('Oferta — zdjęcie zakładki Generalne Wykonawstwo', max_length=500, blank=True, default='/static/img/mbt/ZREALIZOWANE-ATT-8-c1d848dd.jpg')
    home_o_nas_2 = models.CharField('Dlaczego MBT — zdjęcie sekcji (o-nas-2)', max_length=500, blank=True, default='/static/img/mbt/o-nas-2.jpg')
    home_o_nas_zespol = models.CharField('Sekcja zespołu — tło/grupa (o-nas-zespol)', max_length=500, blank=True, default='/static/img/mbt/o-nas-zespol.jpg')
    home_realizacja = models.CharField('Realizacje na stronie głównej — karta (eurosleeve)', max_length=500, blank=True, default='/static/img/mbt/realizacja-eurosleeve.jpg')
    home_bg_why = models.CharField('Tło sekcji Oferta (why-bg3-1)', max_length=500, blank=True, default='/static/img/bg/why-bg3-1.png')
    home_bg_cta = models.CharField('Tło sekcji CTA „Wyceń projekt" (cta-bg3-1)', max_length=500, blank=True, default='/static/img/bg/cta-bg3-1.png')
    home_bg_contact = models.CharField('Tło sekcji kontakt/aktualności (contact-bg3-1)', max_length=500, blank=True, default='/static/img/bg/contact-bg3-1.png')
    home_client_group = models.CharField('Opinie klientów — zdjęcie grupy (client_group_1-2)', max_length=500, blank=True, default='/static/img/normal/client_group_1-2.png')
    home_testi_2 = models.CharField('Opinie klientów — zdjęcie (testi_2_2)', max_length=500, blank=True, default='/static/img/testimonial/testi_2_2.png')
    work_gallery = models.JSONField('Galeria pracy', default=default_work_gallery, blank=True)
    about_1 = models.CharField('O nas — zdjęcie główne (o-nas-1)', max_length=500, blank=True, default='/static/img/mbt/o-nas-1.jpg')
    service_1 = models.CharField('Oferta — zdjęcie 1 (Eurosleeve)', max_length=500, blank=True, default='/static/img/mbt/Eurosleeve-10-scaled-fd8f7247.jpg')
    service_2 = models.CharField('Oferta — zdjęcie 2 (budowa)', max_length=500, blank=True, default='/static/img/mbt/IMG_20220722_102326-scaled-1-fdde92f8.jpg')
    gw_hero = models.CharField('GW — tło hero (ATT-8)', max_length=500, blank=True, default='/static/img/mbt/ZREALIZOWANE-ATT-8-c1d848dd.jpg')
    gw_1 = models.CharField('GW — zdjęcie 1 (ATT-1)', max_length=500, blank=True, default='/static/img/mbt/ZREALIZOWANE-ATT-1-scaled-f12dacac.jpg')
    gw_2 = models.CharField('GW — zdjęcie 2 (ATT-3)', max_length=500, blank=True, default='/static/img/mbt/ZREALIZOWANE-ATT-3-scaled-b0f20287.jpg')
    gw_3 = models.CharField('GW — zdjęcie 3 (ATT-4)', max_length=500, blank=True, default='/static/img/mbt/ZREALIZOWANE-ATT-4-scaled-ffc91418.jpg')
    gw_4 = models.CharField('GW — zdjęcie 4 (ATT-5)', max_length=500, blank=True, default='/static/img/mbt/ZREALIZOWANE-ATT-5-scaled-b27ef1aa.jpg')
    gw_5 = models.CharField('GW — zdjęcie 5 (ATT-6)', max_length=500, blank=True, default='/static/img/mbt/ZREALIZOWANE-ATT-6-scaled-e17253f9.jpg')
    gw_6 = models.CharField('GW — zdjęcie 6 (Fronton-1)', max_length=500, blank=True, default='/static/img/mbt/Fronton-1-scaled-42981731.jpg')
    gw_7 = models.CharField('GW — zdjęcie 7 (Fronton-2)', max_length=500, blank=True, default='/static/img/mbt/Fronton-2-scaled-de057284.jpg')
    gw_8 = models.CharField('GW — zdjęcie 8 (Huber)', max_length=500, blank=True, default='/static/img/mbt/Huber-6-scaled-b00b8b23.jpg')
    gw_9 = models.CharField('GW — zdjęcie 9 (3-2)', max_length=500, blank=True, default='/static/img/mbt/3-2-scaled-38947c85.jpg')
    gw_10 = models.CharField('GW — zdjęcie 10 (BREEAM)', max_length=500, blank=True, default='/static/img/mbt/breem-e659b8f2.jpg')
    gw_11 = models.CharField('GW — zdjęcie 11 (hala)', max_length=500, blank=True, default='/static/img/mbt/hala-1024x672-eb7144c9.jpg')
    gw_12 = models.CharField('GW — zdjęcie 12 (Stokado)', max_length=500, blank=True, default='/static/img/mbt/realizacja-stokado.jpg')
    bg_header = models.CharField('Tło nagłówka (header-1-bg)', max_length=500, blank=True, default='/static/img/bg/header-1-bg.png')
    bg_footer = models.CharField('Tło stopki (footer-bg1-1)', max_length=500, blank=True, default='/static/img/bg/footer-bg1-1.png')
    bg_breadcrumb = models.CharField('Tło breadcrumb / podstron (breadcrumb-bg)', max_length=500, blank=True, default='/static/img/bg/breadcrumb-bg.png')

    # Podstrony Ofertowe (Landing Pages)
    hale_przemyslowe_hero = models.CharField('Hale Przem. — hero', max_length=500, blank=True, default='https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/29cd5ab28014.jpg')
    hale_przemyslowe_1 = models.CharField('Hale Przem. — zdjęcie 1', max_length=500, blank=True, default='https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/261907cbff38.jpg')
    hale_przemyslowe_2 = models.CharField('Hale Przem. — zdjęcie 2 (ESG)', max_length=500, blank=True, default='https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/bdabf42fbc92.jpg')

    hale_magazynowe_hero = models.CharField('Hale Magaz. — hero', max_length=500, blank=True, default='https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/0b5b6f5c26b1.webp')
    hale_magazynowe_1 = models.CharField('Hale Magaz. — zdjęcie 1', max_length=500, blank=True, default='https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/bdabf42fbc92.jpg')

    obiekty_komercyjne_hero = models.CharField('Obiekty Komercyjne — hero', max_length=500, blank=True, default='https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/bdabf42fbc92.jpg')
    obiekty_komercyjne_1 = models.CharField('Obiekty Komercyjne — zdjęcie 1', max_length=500, blank=True, default='https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/261907cbff38.jpg')
    obiekty_komercyjne_2 = models.CharField('Obiekty Komercyjne — zdjęcie 2 (wnętrza)', max_length=500, blank=True, default='https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/ed67bb1b2b03.webp')

    general_contracting_1 = models.CharField('Generalne Wykonawstwo — magazyny', max_length=500, blank=True, default='https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/0b5b6f5c26b1.webp')
    general_contracting_2 = models.CharField('Generalne Wykonawstwo — self storage', max_length=500, blank=True, default='https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev/media/uploads/ed67bb1b2b03.webp')

    class Meta:
        verbose_name = 'Zdjęcia strony'
        verbose_name_plural = 'Zdjęcia strony'

    def __str__(self):
        return 'Zdjęcia strony (edytuj)'


# ============================================================
# Oznakowanie budowy — szablony banerów
# ============================================================

class BannerTemplate(models.Model):
    """Szablon banera (np. 2m×1m) — użytkownik wgrywa plik PNG/JPG z projektem,
    określa miejsce na logo. System nakłada logo kierownika na szablon."""

    SIZE_CHOICES = [
        ('200x100', '2 m × 1 m (banner standard)'),
        ('250x100', '2,5 m × 1 m'),
        ('300x100', '3 m × 1 m'),
        ('400x100', '4 m × 1 m'),
        ('400x200', '4 m × 2 m'),
        ('250x150_bhp', 'Baner BHP (2,5 m × 1,5 m)'),
        ('bioz', 'Tablica BIOZ'),
        ('informacyjna', 'Tablica informacyjna'),
        ('200x100_apology', 'Baner „Przepraszamy za utrudnienia" (2 m × 1 m)'),
        ('300x100_apology', 'Baner „Przepraszamy za utrudnienia" (3 m × 1 m)'),
        ('600x200_billboard', 'Billboard (6 m × 2 m)'),
        ('znak_wjazd_logo', 'Znak: Wjazd na budowę (z logiem)'),
        ('znak_wjazd_bez', 'Znak: Wjazd na budowę (bez loga)'),
        ('znak_biuro_logo', 'Znak: Biuro budowy (z logiem)'),
        ('znak_biuro_bez', 'Znak: Biuro budowy (bez loga)'),
        ('znak_kierunek_prawo', 'Znak kierunkowy: Prawo'),
        ('znak_kierunek_lewo', 'Znak kierunkowy: Lewo'),
        ('znak_kierunek_prosto', 'Znak kierunkowy: Prosto / Bez strzałek'),
    ]

    slug = models.SlugField('Slug', max_length=80, unique=True,
                            help_text='Identyfikator URL — np. "banner-2m", "apology"')
    title = models.CharField('Nazwa', max_length=120,
                             help_text='Np. „Banner 2 m × 1 m", „Przepraszamy za utrudnienia"')
    size = models.CharField('Rozmiar', max_length=20, choices=SIZE_CHOICES)
    template_image = models.FileField(
        'Plik szablonu (PNG/JPG)',
        upload_to='oznakowanie/szablony/',
        help_text='Szablon bez logo (dla personalizowanych) lub gotowy plik (dla ogólnych)',
    )
    is_personalized = models.BooleanField(
        'Czy personalizowany?', default=False,
        help_text='Zaznacz, jeśli to baner 2x1 lub 3x1 z miejscem na logo'
    )
    description = models.TextField('Opis (dla kierownika)', blank=True)
    is_active = models.BooleanField('Aktywny', default=True)
    order = models.PositiveSmallIntegerField('Kolejność', default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # tłumaczenia
    t_title = models.JSONField('Nazwa — tłumaczenia', default=dict, blank=True,
                               help_text='JSON {pl: "...", en: "...", de: "...", cs: "...", sk: "...", hu: "..."}')
    t_description = models.JSONField('Opis — tłumaczenia', default=dict, blank=True)

    class Meta:
        verbose_name = 'Szablon banera'
        verbose_name_plural = 'Szablony banerów'
        ordering = ['order', 'id']

    def __str__(self):
        return self.title


class BannerDownload(models.Model):
    """Log pobrania banera przez kierownika."""

    user = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='banner_downloads',
        verbose_name='Kierownik',
    )
    user_email = models.EmailField('Email (kopia)', max_length=200,
                                   help_text='Kopia email — zostaje nawet po usunięciu usera')
    template = models.ForeignKey(
        BannerTemplate,
        on_delete=models.SET_NULL,
        null=True,
        related_name='downloads',
        verbose_name='Szablon',
    )
    template_title_snapshot = models.CharField('Nazwa szablonu (kopia)', max_length=200)
    downloaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Data pobrania')
    ip_address = models.GenericIPAddressField('IP', null=True, blank=True)
    user_agent = models.CharField('User Agent', max_length=500, blank=True)

    class Meta:
        verbose_name = 'Pobranie banera'
        verbose_name_plural = 'Pobrania banerów'
        ordering = ['-downloaded_at']

    def __str__(self):
        return f'{self.user_email} → {self.template_title_snapshot} @ {self.downloaded_at:%Y-%m-%d %H:%M}'


class UserProfile(models.Model):
    """Profil użytkownika — flaga wymuszenia zmiany hasła przy pierwszym logowaniu."""

    user = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Użytkownik',
    )
    must_change_password = models.BooleanField(
        'Wymuś zmianę hasła przy pierwszym logowaniu',
        default=True,
    )
    is_kierownik = models.BooleanField(
        'Kierownik budowy (dostęp do /oznakowanie-budowy/)',
        default=False,
    )
    last_password_change = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Profil użytkownika'
        verbose_name_plural = 'Profile użytkowników'

    def __str__(self):
        return f'Profil: {self.user.username}'


class SalesRepresentative(models.Model):
    """Handlowiec — sekcja kontakt i strona główna."""

    name = models.CharField('Imię i nazwisko', max_length=200)
    position = models.CharField('Stanowisko / Dział (PL)', max_length=200, default='Dział Handlowy')
    email = models.EmailField('E-mail')
    phone = models.CharField('Telefon', max_length=50, blank=True)
    photo = models.CharField('Zdjęcie (URL)', max_length=500, blank=True)
    order = models.PositiveIntegerField('Kolejność', default=0)

    # Wielojęzyczność (JSON: {lang: text}). Puste = fallback na PL.
    t_position = models.JSONField('Stanowisko — tłumaczenia', default=dict, blank=True,
                                  help_text='JSON np. {"en":"...","de":"...","cs":"...","sk":"...","hu":"..."}')

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Handlowiec'
        verbose_name_plural = 'Handlowcy'

    def __str__(self):
        return self.name

class Award(models.Model):
    """Nagrody / Wyróżnienia / Partnerstwa — strona główna i o nas."""
    name = models.CharField('Nazwa', max_length=200)
    image = models.CharField('Logotyp (URL)', max_length=500, blank=True)
    order = models.PositiveIntegerField('Kolejność', default=0)
    is_active = models.BooleanField('Aktywne', default=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Wyróżnienie / Partnerstwo'
        verbose_name_plural = 'Wyróżnienia i Partnerstwa'

    def __str__(self):
        return self.name


class Sector(models.Model):
    """Sektor B2B (np. Hale przemysłowe) — sekcja Nasze specjalizacje na stronie GW."""

    title = models.CharField('Nazwa sektora (PL)', max_length=200)
    slug = models.CharField('Slug (dla URL)', max_length=200, help_text='np. konstrukcje-stalowe', blank=True)
    view_name = models.CharField('Nazwa widoku', max_length=100, default='sectorDetail', help_text='np. sectorDetail, halePrzemyslowe')
    opis = models.TextField('Opis (PL)')
    icon = models.CharField('Ikona (klasa RemixIcon)', max_length=100, default='ri-building-2-line')
    image = models.CharField('Zdjęcie (URL)', max_length=500, blank=True)
    order = models.PositiveIntegerField('Kolejność', default=0)

    # Wielojęzyczność
    t_title = models.JSONField('Nazwa — tłumaczenia', default=dict, blank=True)
    t_opis = models.JSONField('Opis — tłumaczenia', default=dict, blank=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Sektor B2B'
        verbose_name_plural = 'Sektory B2B (Nasze Specjalizacje)'

    def __str__(self):
        return self.title
