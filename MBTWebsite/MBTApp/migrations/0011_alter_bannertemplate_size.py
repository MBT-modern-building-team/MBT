# Utworzono lokalnie (Django)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBTApp', '0010_remove_bannertemplate_logo_max_height_percent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannertemplate',
            name='size',
            field=models.CharField(choices=[('200x100', '2 m × 1 m (banner standard)'), ('250x100', '2,5 m × 1 m'), ('300x100', '3 m × 1 m'), ('400x100', '4 m × 1 m'), ('400x200', '4 m × 2 m'), ('250x150_bhp', 'Baner BHP (2,5 m × 1,5 m)'), ('bioz', 'Tablica BIOZ'), ('informacyjna', 'Tablica informacyjna'), ('200x100_apology', 'Baner „Przepraszamy za utrudnienia"')], max_length=20, verbose_name='Rozmiar'),
        ),
    ]
