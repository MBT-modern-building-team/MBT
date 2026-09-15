import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MBT.settings')
django.setup()

from MBTApp.models import SiteConfig
config = SiteConfig.objects.first()
if config:
    config.founded = "wielu lat"
    config.save()
    print("Founded updated to 'wielu lat'")
