import os
import sys
import django

sys.path.append(os.path.join(os.path.dirname(__file__), 'Construz'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Construz.settings')
django.setup()

from MBTApp.models import Project
from django.utils.text import slugify

# Create Raben
raben, created = Project.objects.get_or_create(
    title="Raben",
    defaults={
        'slug': slugify("Raben"),
        'latitude': 51.177,
        'longitude': 16.237,
        'type': 'realizacja-zakonczona'
    }
)
if not created:
    raben.latitude = 51.177
    raben.longitude = 16.237
    raben.save()

# Create Less Mess Gdańsk
less_mess, created = Project.objects.get_or_create(
    title="Less Mess Gdańsk",
    defaults={
        'slug': slugify("Less Mess Gdańsk"),
        'latitude': 54.3445279, # Wziąłem dokładne koordynaty z KML (Less Mess Jasień Gdańsk)
        'longitude': 18.5456996,
        'type': 'realizacja-zakonczona'
    }
)
if not created:
    less_mess.latitude = 54.3445279
    less_mess.longitude = 18.5456996
    less_mess.save()

# Update ToTo
try:
    toto = Project.objects.get(id=11)
    toto.latitude = 49.914
    toto.longitude = 19.897
    toto.save()
except:
    pass

# Update Stokado Targowek
try:
    stokado = Project.objects.get(id=34)
    stokado.latitude = 52.2917104
    stokado.longitude = 21.0761354
    stokado.save()
except:
    pass

# Update BYD
try:
    byd = Project.objects.get(id=37)
    byd.latitude = 50.36019
    byd.longitude = 18.90364
    byd.save()
except:
    pass

print("Added missing projects and updated coords!")
