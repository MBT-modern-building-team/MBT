# Utworzono lokalnie (Django)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBTApp', '0013_salesrepresentative'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesrepresentative',
            name='phone',
            field=models.CharField(blank=True, max_length=50, verbose_name='Telefon'),
        ),
    ]
