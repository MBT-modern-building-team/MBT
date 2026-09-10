# Utworzono lokalnie (Django)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBTApp', '0006_sitephotos'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='t_excerpt',
            field=models.JSONField(blank=True, default=dict, verbose_name='Skrót — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='article',
            name='t_text',
            field=models.JSONField(blank=True, default=dict, verbose_name='Treść artykułu — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='article',
            name='t_title',
            field=models.JSONField(blank=True, default=dict, help_text='JSON np. {"en":"...","de":"...","cs":"...","sk":"...","hu":"..."}', verbose_name='Tytuł — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='job',
            name='t_text',
            field=models.JSONField(blank=True, default=dict, verbose_name='Treść oferty — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='job',
            name='t_title',
            field=models.JSONField(blank=True, default=dict, help_text='JSON np. {"en":"...","de":"...","cs":"...","sk":"...","hu":"..."}', verbose_name='Stanowisko — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='project',
            name='t_czas',
            field=models.JSONField(blank=True, default=dict, verbose_name='Czas realizacji — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='project',
            name='t_formula',
            field=models.JSONField(blank=True, default=dict, verbose_name='Formuła — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='project',
            name='t_opis',
            field=models.JSONField(blank=True, default=dict, verbose_name='Opis — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='project',
            name='t_status',
            field=models.JSONField(blank=True, default=dict, verbose_name='Status — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='project',
            name='t_title',
            field=models.JSONField(blank=True, default=dict, help_text='JSON np. {"en":"...","de":"...","cs":"...","sk":"...","hu":"..."}', verbose_name='Tytuł — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='reference',
            name='t_osoba',
            field=models.JSONField(blank=True, default=dict, verbose_name='Osoba — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='reference',
            name='t_stanowisko',
            field=models.JSONField(blank=True, default=dict, verbose_name='Stanowisko — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='reference',
            name='t_tresc',
            field=models.JSONField(blank=True, default=dict, help_text='JSON np. {"en":"...","de":"...","cs":"...","sk":"...","hu":"..."}', verbose_name='Treść opinii — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='worker',
            name='t_opis',
            field=models.JSONField(blank=True, default=dict, verbose_name='Opis — tłumaczenia'),
        ),
        migrations.AddField(
            model_name='worker',
            name='t_position',
            field=models.JSONField(blank=True, default=dict, help_text='JSON np. {"en":"...","de":"...","cs":"...","sk":"...","hu":"..."}', verbose_name='Stanowisko — tłumaczenia'),
        ),
        migrations.AlterField(
            model_name='article',
            name='excerpt',
            field=models.CharField(blank=True, max_length=400, verbose_name='Skrót (podgląd) PL'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(verbose_name='Treść artykułu (PL)'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Tytuł (PL)'),
        ),
        migrations.AlterField(
            model_name='job',
            name='text',
            field=models.TextField(verbose_name='Treść oferty (PL)'),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Stanowisko (PL)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='czas',
            field=models.CharField(blank=True, max_length=120, verbose_name='Czas realizacji (PL)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='formula',
            field=models.CharField(blank=True, max_length=120, verbose_name='Formuła (PL)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='opis',
            field=models.TextField(blank=True, verbose_name='Opis (specyfikacja) PL'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(default='Zrealizowane', max_length=80, verbose_name='Status (PL)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Tytuł (PL)'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='osoba',
            field=models.CharField(blank=True, max_length=200, verbose_name='Osoba (PL)'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='stanowisko',
            field=models.CharField(blank=True, max_length=200, verbose_name='Stanowisko (PL)'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='tresc',
            field=models.TextField(verbose_name='Treść opinii (PL)'),
        ),
        migrations.AlterField(
            model_name='sitephotos',
            name='gw_12',
            field=models.CharField(blank=True, default='/static/img/mbt/realizacja-stokado.jpg', max_length=500, verbose_name='GW — zdjęcie 12 (Stokado)'),
        ),
        migrations.AlterField(
            model_name='sitephotos',
            name='gw_hero',
            field=models.CharField(blank=True, default='/static/img/mbt/ZREALIZOWANE-ATT-8-c1d848dd.jpg', max_length=500, verbose_name='GW — tło hero (ATT-8)'),
        ),
        migrations.AlterField(
            model_name='sitephotos',
            name='home_att8',
            field=models.CharField(blank=True, default='/static/img/mbt/ZREALIZOWANE-ATT-8-c1d848dd.jpg', max_length=500, verbose_name='Oferta — zdjęcie zakładki Generalne Wykonawstwo'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='opis',
            field=models.TextField(blank=True, verbose_name='Opis (PL)'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='position',
            field=models.CharField(max_length=200, verbose_name='Stanowisko (PL)'),
        ),
    ]
