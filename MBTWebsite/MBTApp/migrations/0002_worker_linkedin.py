# Utworzono lokalnie (Django)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBTApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='linkedin',
            field=models.URLField(blank=True, verbose_name='LinkedIn (URL)'),
        ),
    ]
