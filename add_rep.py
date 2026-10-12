import os
import sys
import django

sys.path.append(os.path.join(os.getcwd(), 'MBTWebsite'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MBT.settings')
django.setup()

from MBTApp.models import SalesRepresentative

rep, created = SalesRepresentative.objects.get_or_create(
    email='l.liszka@mbt.pl',
    defaults={
        'name': 'Łukasz Liszka',
        'position': 'Manager ds. handlowych/Business Development Manager',
        'phone': '881 202 306',
        'photo': '',
        'order': 4,
    }
)
if not created:
    rep.name = 'Łukasz Liszka'
    rep.position = 'Manager ds. handlowych/Business Development Manager'
    rep.phone = '881 202 306'
    rep.save()
    print("Updated Łukasz Liszka in DB.")
else:
    print("Added Łukasz Liszka to DB.")
