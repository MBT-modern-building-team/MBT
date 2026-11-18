"""Vercel Serverless Function — wejście dla Django (MBT).

Ten plik MUSI być w katalogu `api/` na ROOT repo (Vercel widzi tylko
ścieżki od roota repo — stąd `api/index.py`, a nie `Construz/api/index.py`).

Adapter: serverless-wsgi 3.x. Dodajemy katalog projektu Django do sys.path,
bo Vercel uruchamia funkcję z roota repo (Construz/ nie jest w sys.path).

"""
import os
import sys

# Katalog projektu Django (MBTWebsite/ — tam gdzie MBT/ i MBTApp/)
DJANGO_PROJECT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'MBTWebsite')
DJANGO_PROJECT_DIR = os.path.normpath(DJANGO_PROJECT_DIR)
if DJANGO_PROJECT_DIR not in sys.path:
    sys.path.insert(0, DJANGO_PROJECT_DIR)


# Migracje, seed danych i tworzenie superusera NIE są wykonywane przy starcie
# funkcji (spowalniało to cold start). Uruchamiaj je ręcznie:
#   python manage.py migrate
#   python manage.py import_mbt_data
#   python manage.py createsuperuser
# Hasła NIGDY nie mogą być zapisane w kodzie.

# UWAGA: Usunięto wywołanie _bootstrap() z poziomu modułu!
# Vercel Serverless Functions restartują się bardzo często (cold starts).
# Uruchamianie migracji (migrate) i siewu danych (import_mbt_data) 
# przy każdym starcie modułu drastycznie spowalniało ładowanie strony (nawet o kilka sekund).
# Migracje powinny być uruchamiane z konsoli lub poprzez dedykowany endpoint administracyjny.

from MBT.wsgi import application

# Vercel Serverless Functions wymagają obiektu WSGI o nazwie `app`
app = application
