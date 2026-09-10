# Utworzono lokalnie (Django)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBTApp', '0011_alter_bannertemplate_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='latitude',
            field=models.FloatField(blank=True, help_text='Np. 52.2297 dla Warszawy', null=True, verbose_name='Szerokość geogr. (Latitude)'),
        ),
        migrations.AddField(
            model_name='project',
            name='longitude',
            field=models.FloatField(blank=True, help_text='Np. 21.0122 dla Warszawy', null=True, verbose_name='Długość geogr. (Longitude)'),
        ),
    ]
