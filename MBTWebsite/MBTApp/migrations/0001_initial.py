# Utworzono lokalnie (Django)

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Tytuł')),
                ('slug', models.SlugField(max_length=300, unique=True, verbose_name='Slug (adres URL)')),
                ('excerpt', models.CharField(blank=True, max_length=400, verbose_name='Skrót (podgląd)')),
                ('text', models.TextField(verbose_name='Treść artykułu')),
                ('image', models.CharField(blank=True, max_length=500, verbose_name='Zdjęcie (URL)')),
                ('published', models.BooleanField(default=True, verbose_name='Opublikowany')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Kolejność')),
            ],
            options={
                'verbose_name': 'Artykuł',
                'verbose_name_plural': 'Artykuły',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Stanowisko')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug (adres URL)')),
                ('text', models.TextField(verbose_name='Treść oferty')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Kolejność')),
            ],
            options={
                'verbose_name': 'Oferta pracy',
                'verbose_name_plural': 'Oferty pracy',
                'ordering': ['order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Tytuł')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug (adres URL)')),
                ('type', models.CharField(choices=[('realizacja-zrealizow', 'Zrealizowane'), ('realizacja-w-trakcie', 'W trakcie realizacji')], default='realizacja-zrealizow', max_length=40, verbose_name='Typ')),
                ('status', models.CharField(default='Zrealizowane', max_length=80, verbose_name='Status (tekst)')),
                ('czas', models.CharField(blank=True, max_length=120, verbose_name='Czas realizacji')),
                ('formula', models.CharField(blank=True, max_length=120, verbose_name='Formuła')),
                ('opis', models.TextField(blank=True, verbose_name='Opis (specyfikacja)')),
                ('logo', models.CharField(blank=True, max_length=500, verbose_name='Logo firmy (URL)')),
                ('hero', models.CharField(blank=True, max_length=500, verbose_name='Zdjęcie główne (URL)')),
                ('gallery', models.JSONField(blank=True, default=list, verbose_name='Galeria (lista URL-i)')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Kolejność')),
            ],
            options={
                'verbose_name': 'Realizacja',
                'verbose_name_plural': 'Realizacje',
                'ordering': ['order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firma', models.CharField(max_length=200, verbose_name='Firma')),
                ('tresc', models.TextField(verbose_name='Treść opinii')),
                ('osoba', models.CharField(blank=True, max_length=200, verbose_name='Osoba')),
                ('stanowisko', models.CharField(blank=True, max_length=200, verbose_name='Stanowisko')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Kolejność')),
            ],
            options={
                'verbose_name': 'Opinia klienta',
                'verbose_name_plural': 'Opinie klientów',
                'ordering': ['order', 'firma'],
            },
        ),
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='+48 881 444 333', max_length=40, verbose_name='Telefon')),
                ('phone_href', models.CharField(default='+48881444333', max_length=40, verbose_name='Telefon (href)')),
                ('email', models.EmailField(default='biuro@mbt.pl', max_length=254, verbose_name='E-mail')),
                ('hours', models.CharField(default='Pon - Pt / 8:00 - 16:00', max_length=60, verbose_name='Godziny (krótko)')),
                ('hours_long', models.CharField(default='Pon-Pt: 8:00 do 16:00', max_length=60, verbose_name='Godziny (długo)')),
                ('office_zabrze', models.CharField(default='Roosevelta 81, 41-800 Zabrze', max_length=200, verbose_name='Biuro Zabrze')),
                ('office_katowice', models.CharField(default='Jankego 176/1A, 40-663 Katowice', max_length=200, verbose_name='Siedziba Katowice')),
                ('office_krakow', models.CharField(default='Zawiła 65, bud. X lok. 5, 30-390 Kraków', max_length=200, verbose_name='Oddział Kraków')),
                ('nip', models.CharField(default='9542788822', max_length=20, verbose_name='NIP')),
                ('regon', models.CharField(default='369557780', max_length=20, verbose_name='REGON')),
                ('krs', models.CharField(default='0000720424', max_length=20, verbose_name='KRS')),
                ('founded', models.CharField(default='2005', max_length=10, verbose_name='Rok założenia')),
                ('tagline', models.CharField(default='Z pasją budujemy Wasze biznesy. Jeden team – pełna realizacja. Od projektu aż po dach!', max_length=300, verbose_name='Slogan')),
                ('about_short', models.TextField(default='MBT Modern Building Team — generalny wykonawca hal magazynowych, produkcyjnych i usługowych. Terminowa budowa obiektów przemysłowych pod klucz.', verbose_name='Opis firmy (stopka)')),
                ('counter_years', models.CharField(default='20', max_length=10, verbose_name='Licznik: lata')),
                ('counter_years_label', models.CharField(default='Zaangażowania', max_length=80, verbose_name='Licznik: lata (etykieta)')),
                ('counter_projects', models.CharField(default='100', max_length=10, verbose_name='Licznik: inwestycje')),
                ('counter_projects_label', models.CharField(default='Zrealizowanych inwestycji', max_length=80, verbose_name='Licznik: inwestycje (etykieta)')),
                ('counter_ontime', models.CharField(default='100', max_length=10, verbose_name='Licznik: terminowość')),
                ('counter_ontime_suffix', models.CharField(default='%', max_length=10, verbose_name='Licznik: terminowość (sufiks)')),
                ('counter_ontime_label', models.CharField(default='Terminowości', max_length=80, verbose_name='Licznik: terminowość (etykieta)')),
                ('counter_brands', models.CharField(default='16', max_length=10, verbose_name='Licznik: marki')),
                ('counter_brands_label', models.CharField(default='Zaufanych marek', max_length=80, verbose_name='Licznik: marki (etykieta)')),
                ('social_linkedin', models.URLField(blank=True, verbose_name='LinkedIn')),
                ('social_youtube', models.URLField(blank=True, verbose_name='YouTube')),
                ('social_facebook', models.URLField(blank=True, verbose_name='Facebook')),
            ],
            options={
                'verbose_name': 'Dane firmy',
                'verbose_name_plural': 'Dane firmy',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Imię i nazwisko')),
                ('position', models.CharField(max_length=200, verbose_name='Stanowisko')),
                ('opis', models.TextField(blank=True, verbose_name='Opis')),
                ('photo', models.CharField(blank=True, max_length=500, verbose_name='Zdjęcie (URL)')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Kolejność')),
            ],
            options={
                'verbose_name': 'Pracownik',
                'verbose_name_plural': 'Pracownicy',
                'ordering': ['order', 'name'],
            },
        ),
    ]
