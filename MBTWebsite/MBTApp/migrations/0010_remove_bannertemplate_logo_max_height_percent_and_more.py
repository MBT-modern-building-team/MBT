# Utworzono lokalnie (Django)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBTApp', '0009_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bannertemplate',
            name='logo_max_height_percent',
        ),
        migrations.RemoveField(
            model_name='bannertemplate',
            name='logo_max_width_percent',
        ),
        migrations.RemoveField(
            model_name='bannertemplate',
            name='logo_padding_percent',
        ),
        migrations.RemoveField(
            model_name='bannertemplate',
            name='logo_position',
        ),
        migrations.AddField(
            model_name='bannertemplate',
            name='is_personalized',
            field=models.BooleanField(default=False, help_text='Zaznacz, jeśli to baner 2x1 lub 3x1 z miejscem na logo', verbose_name='Czy personalizowany?'),
        ),
        migrations.AlterField(
            model_name='bannertemplate',
            name='template_image',
            field=models.FileField(help_text='Szablon bez logo (dla personalizowanych) lub gotowy plik (dla ogólnych)', upload_to='oznakowanie/szablony/', verbose_name='Plik szablonu (PNG/JPG)'),
        ),
    ]
