# Utworzono lokalnie (Django)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBTApp', '0003_siteconfig_office_katowice_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='office_site_adres',
            field=models.CharField(blank=True, default='Adres Twojej inwestycji', max_length=200, verbose_name='Plac budowy: adres'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='office_site_label',
            field=models.CharField(blank=True, default='Twój plac budowy', max_length=120, verbose_name='Plac budowy: nagłówek'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='office_site_photo',
            field=models.CharField(blank=True, default='/static/img/mbt/DSC03738-scaled-c238f3f3.jpeg', max_length=500, verbose_name='Zdjęcie placu budowy (URL)'),
        ),
    ]
