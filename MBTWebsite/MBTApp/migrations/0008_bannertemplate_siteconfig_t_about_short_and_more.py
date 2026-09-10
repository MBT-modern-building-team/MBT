# Utworzono lokalnie (Django)

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBTApp', '0007_article_t_excerpt_article_t_text_article_t_title_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text='Identyfikator URL — np. "banner-2m", "apology"', max_length=80, unique=True, verbose_name='Slug')),
                ('title', models.CharField(help_text='Np. „Banner 2 m × 1 m", „Przepraszamy za utrudnienia"', max_length=120, verbose_name='Nazwa')),
                ('size', models.CharField(choices=[('200x100', '2 m × 1 m (banner standard)'), ('250x100', '2,5 m × 1 m'), ('300x100', '3 m × 1 m'), ('400x100', '4 m × 1 m'), ('200x100_apology', 'Baner „Przepraszamy za utrudnienia"')], max_length=20, verbose_name='Rozmiar')),
                ('template_image', models.FileField(help_text='Szablon bez logo — zostanie na nim nałożone logo kierownika', upload_to='oznakowanie/szablony/', verbose_name='Plik szablonu (PNG/JPG)')),
                ('logo_position', models.CharField(choices=[('center', 'Środek'), ('left-bottom', 'Lewy dolny róg'), ('right-bottom', 'Prawy dolny róg'), ('left-top', 'Lewy górny róg'), ('right-top', 'Prawy górny róg')], default='left-bottom', max_length=20, verbose_name='Pozycja logo')),
                ('logo_max_width_percent', models.PositiveSmallIntegerField(default=20, help_text='Np. 20 = logo do 20% szerokości banera', verbose_name='Maks. szerokość logo (% szerokości szablonu)')),
                ('logo_max_height_percent', models.PositiveSmallIntegerField(default=20, help_text='Np. 20 = logo do 20% wysokości banera', verbose_name='Maks. wysokość logo (% wysokości szablonu)')),
                ('logo_padding_percent', models.PositiveSmallIntegerField(default=5, help_text='Odstęp logo od krawędzi banera w pozycji bezwzględnej', verbose_name='Padding od krawędzi (%)')),
                ('description', models.TextField(blank=True, verbose_name='Opis (dla kierownika)')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktywny')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Kolejność')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('t_title', models.JSONField(blank=True, default=dict, help_text='JSON {pl: "...", en: "...", de: "...", cs: "...", sk: "...", hu: "..."}', verbose_name='Nazwa — tłumaczenia')),
                ('t_description', models.JSONField(blank=True, default=dict, verbose_name='Opis — tłumaczenia')),
            ],
            options={
                'verbose_name': 'Szablon banera',
                'verbose_name_plural': 'Szablony banerów',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='t_about_short',
            field=models.JSONField(blank=True, default=dict, verbose_name='Opis firmy — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='t_counter_brands_label',
            field=models.JSONField(blank=True, default=dict, verbose_name='Licznik "marki" — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='t_counter_ontime_label',
            field=models.JSONField(blank=True, default=dict, verbose_name='Licznik "terminowość" — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='t_counter_projects_label',
            field=models.JSONField(blank=True, default=dict, verbose_name='Licznik "inwestycje" — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='t_counter_years_label',
            field=models.JSONField(blank=True, default=dict, verbose_name='Licznik "lata" — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='t_hours',
            field=models.JSONField(blank=True, default=dict, verbose_name='Godziny — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='t_hours_long',
            field=models.JSONField(blank=True, default=dict, verbose_name='Godziny długie — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='t_office_katowice',
            field=models.JSONField(blank=True, default=dict, verbose_name='Siedziba Katowice — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='t_office_krakow',
            field=models.JSONField(blank=True, default=dict, verbose_name='Oddział Kraków — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='t_office_zabrze',
            field=models.JSONField(blank=True, default=dict, verbose_name='Biuro Zabrze — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='t_tagline',
            field=models.JSONField(blank=True, default=dict, help_text='JSON {pl: "...", en: "...", de: "...", cs: "...", sk: "...", hu: "..."}', verbose_name='Slogan — tłumaczenia'),
        ),
        migrations.CreateModel(
            name='BannerDownload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(help_text='Kopia email — zostaje nawet po usunięciu usera', max_length=200, verbose_name='Email (kopia)')),
                ('template_title_snapshot', models.CharField(max_length=200, verbose_name='Nazwa szablonu (kopia)')),
                ('downloaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Data pobrania')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP')),
                ('user_agent', models.CharField(blank=True, max_length=500, verbose_name='User Agent')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='banner_downloads', to=settings.AUTH_USER_MODEL, verbose_name='Kierownik')),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='downloads', to='MBTApp.bannertemplate', verbose_name='Szablon')),
            ],
            options={
                'verbose_name': 'Pobranie banera',
                'verbose_name_plural': 'Pobrania banerów',
                'ordering': ['-downloaded_at'],
            },
        ),
    ]
