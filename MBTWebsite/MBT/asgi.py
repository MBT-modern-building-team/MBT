"""
ASGI config for MBT project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import sys

# Vercel (auto-detection) uruchamia ten plik z roota repo (/var/task),
# gdzie pakiet MBT/ jest w podkatalogu Construz/ — dodajemy go do sys.path,
# żeby 'MBT.settings' był importowalny niezależnie od katalogu startowego.
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MBT.settings')

from django.core.asgi import get_asgi_application

application = get_asgi_application()
