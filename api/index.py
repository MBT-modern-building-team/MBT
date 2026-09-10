"""Vercel Serverless Function — wejście dla Django (MBT).

Ten plik MUSI być w katalogu `api/` na ROOT repo (Vercel widzi tylko
ścieżki od roota repo — stąd `api/index.py`, a nie `Construz/api/index.py`).

Adapter: serverless-wsgi 3.x. Dodajemy katalog projektu Django do sys.path,
bo Vercel uruchamia funkcję z roota repo (Construz/ nie jest w sys.path).

Przy starcie (cold start) wykonujemy:
  1. migrate        — tworzy/aktualizuje tabele (Postgres na Vercel)
  2. import_mbt_data — zasiewa bazę danymi z mbt_data.py, jeśli pusta
  3. superuser       — tworzy admina z env (DJANGO_SUPERUSER_EMAIL/PASSWORD),
                      jeśli podano i użytkownik nie istnieje
"""
import os
import sys

# Katalog projektu Django (MBTWebsite/ — tam gdzie MBT/ i MBTApp/)
DJANGO_PROJECT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'MBTWebsite')
DJANGO_PROJECT_DIR = os.path.normpath(DJANGO_PROJECT_DIR)
if DJANGO_PROJECT_DIR not in sys.path:
    sys.path.insert(0, DJANGO_PROJECT_DIR)


def _bootstrap():
    """Migracje + seed + superuser — tylko raz na cold start."""
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MBT.settings')
    django.setup()

    from django.core.management import call_command
    try:
        call_command('migrate', interactive=False, verbosity=0)
    except Exception:
        pass  # np. brak bazy — strona i tak działa z mbt_data.py

    try:
        call_command('import_mbt_data', verbosity=0)
    except Exception:
        pass

    username = os.getenv('DJANGO_SUPERUSER_USERNAME') or os.getenv('DJANGO_SUPERUSER_EMAIL')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
    if username and password:
        try:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username, email='', password=password)
        except Exception:
            pass


def _create_superuser():
    """Tworzy admina na cold-start bez odpalania wolnych migracji."""
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MBT.settings')
    django.setup()

    # Zmienne z Vercel, domyślnie 'm.dziubek@mbt.pl' i 'Mbt2024!@' jeśli brak
    username = os.getenv('DJANGO_SUPERUSER_USERNAME') or os.getenv('DJANGO_SUPERUSER_EMAIL') or 'm.dziubek@mbt.pl'
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD') or 'Mbt2026!@'
    
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email=username, password=password)
        else:
            # Wymuś aktualizację hasła w razie problemów z logowaniem
            u = User.objects.get(username=username)
            u.set_password(password)
            u.save()
    except Exception as e:
        print("Nie udalo sie utworzyc superusera (moze brak tabel w bazie?):", e)

_create_superuser()

from MBT.wsgi import application

# Vercel Serverless Functions wymagają obiektu WSGI o nazwie `app`
app = application
