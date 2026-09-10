# Utworzono lokalnie (Django)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBTApp', '0012_project_latitude_project_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesRepresentative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Imię i nazwisko')),
                ('position', models.CharField(default='Dział Handlowy', max_length=200, verbose_name='Stanowisko / Dział (PL)')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('photo', models.CharField(blank=True, max_length=500, verbose_name='Zdjęcie (URL)')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Kolejność')),
                ('t_position', models.JSONField(blank=True, default=dict, help_text='JSON np. {"en":"...","de":"...","cs":"...","sk":"...","hu":"..."}', verbose_name='Stanowisko — tłumaczenia')),
            ],
            options={
                'verbose_name': 'Handlowiec',
                'verbose_name_plural': 'Handlowcy',
                'ordering': ['order', 'name'],
            },
        ),
    ]
