# Utworzono lokalnie (Django)

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBTApp', '0008_bannertemplate_siteconfig_t_about_short_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('must_change_password', models.BooleanField(default=True, verbose_name='Wymuś zmianę hasła przy pierwszym logowaniu')),
                ('is_kierownik', models.BooleanField(default=False, verbose_name='Kierownik budowy (dostęp do /oznakowanie-budowy/)')),
                ('last_password_change', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
            options={
                'verbose_name': 'Profil użytkownika',
                'verbose_name_plural': 'Profile użytkowników',
            },
        ),
    ]
