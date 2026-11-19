from django.db import migrations, models

L = '/static/img/mbt/logos/'
M = '/static/img/mbt/'
BRANDS = [
    ('BYD', L + 'byd.svg'),
    ('Raben', L + 'raben.svg'),
    ('UE Wrocław', L + 'ue-wroclaw.svg'),
    ('Stokado', L + 'stokado-self-storage.webp'),
    ('Less Mess Storage', M + 'trusted-us-less-mess-storage.svg'),
    ('Ponar', L + 'ponar.png'),
    ('Kompania Piwowarska', M + 'trusted-us-kompania-piwowarska.svg'),
    ('Brembo', L + 'brembo-logo.svg'),
    ('Bater', M + 'trusted-us-bater.svg'),
    ('Browar Zamkowy', M + 'trusted-us-browar-zamkowy.svg'),
    ('Canpack', M + 'trusted-us-canpack.svg'),
    ('DL Invest Group', M + 'trusted-us-dl-invest-group.svg'),
    ('Epco', M + 'trusted-us-epco.svg'),
    ('Euro-Trade', M + 'trusted-us-euro-trade.svg'),
    ('Euronova', M + 'trusted-us-euronova.svg'),
    ('Herz', M + 'trusted-us-herz.svg'),
    ('Huber+Suhner', M + 'trusted-us-huber-suhner.svg'),
    ('Pumar', M + 'trusted-us-pumar.svg'),
    ('Stainless Steel Engineering', M + 'trusted-us-stainless-steel-engineering.svg'),
    ('Sutco Polska', M + 'trusted-us-sutco-polska.svg'),
    ('TOTO', M + 'trusted-us-toto.svg'),
]


def seed(apps, schema_editor):
    TrustedBrand = apps.get_model('MBTApp', 'TrustedBrand')
    for i, (name, image) in enumerate(BRANDS, start=1):
        TrustedBrand.objects.get_or_create(name=name, defaults={'image': image, 'order': i * 10})


class Migration(migrations.Migration):
    dependencies = [('MBTApp', '0028_rename_legacy_slugs')]

    operations = [
        migrations.CreateModel(
            name='TrustedBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nazwa')),
                ('image', models.CharField(blank=True, max_length=500, verbose_name='Logotyp (URL)')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Kolejność')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktywne')),
            ],
            options={
                'verbose_name': 'Marka (Zaufali nam)',
                'verbose_name_plural': 'Zaufali nam (logotypy)',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.RunPython(seed, migrations.RunPython.noop),
    ]
