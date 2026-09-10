import os
import django
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Construz'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MBT.settings')
django.setup()

from MBTApp.models import Award

for a in Award.objects.all():
    if a.image and not a.image.startswith('/media/') and not a.image.startswith('http'):
        a.image = f'/media/{a.image}'
        a.save()
        print(f"Fixed {a.name} -> {a.image}")
