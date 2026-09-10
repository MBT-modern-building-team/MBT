# Utworzono lokalnie (Django)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBTApp', '0004_siteconfig_office_site_adres_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='hero_video',
            field=models.CharField(blank=True, help_text='Wgraj film MP4 (bez dźwięku, odtwarzany w pętli) — pojawi się zamiast zdjęcia w sekcji hero na stronie głównej.', max_length=500, verbose_name='Film w tle (strona główna)'),
        ),
        migrations.AlterField(
            model_name='siteconfig',
            name='phone_href',
            field=models.CharField(default='+488****0465', max_length=40, verbose_name='Telefon (href)'),
        ),
    ]
