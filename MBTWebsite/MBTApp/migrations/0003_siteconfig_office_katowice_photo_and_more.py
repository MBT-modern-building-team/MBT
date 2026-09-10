# Utworzono lokalnie (Django)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBTApp', '0002_worker_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='office_katowice_photo',
            field=models.CharField(blank=True, default='/static/img/mbt/o-nas-zespol.jpg', max_length=500, verbose_name='Zdjęcie siedziby Katowice (URL)'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='office_krakow_photo',
            field=models.CharField(blank=True, default='/static/img/mbt/o-nas-2.jpg', max_length=500, verbose_name='Zdjęcie oddziału Kraków (URL)'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='office_zabrze_photo',
            field=models.CharField(blank=True, default='/static/img/mbt/o-nas-1.jpg', max_length=500, verbose_name='Zdjęcie biura Zabrze (URL)'),
        ),
    ]
