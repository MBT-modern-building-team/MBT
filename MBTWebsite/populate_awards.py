import os
import sys
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MBT.settings')
django.setup()

from MBTApp.models import Award

if Award.objects.count() == 0:
    for i, (name, filename) in enumerate([
        ('Diamenty Forbesa', 'award-1.png'),
        ('Gazele Biznesu', 'award-2.png'),
        ('Rzetelna Firma', 'award-3.png')
    ]):
        filepath = os.path.join('MBTApp', 'static', 'img', 'mbt', filename)
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                award = Award(name=name, order=i)
                award.image.save(filename, File(f), save=True)
            print(f'Added {name}')
