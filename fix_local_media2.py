import os
import django
import sys
from django.conf import settings

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Construz'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MBT.settings')
django.setup()

from MBTApp.models import Project, Worker, SalesRepresentative, SitePhotos, SiteConfig
from MBTApp.storage import _r2_configured, _upload_to_r2, _compress_image
import boto3

if not _r2_configured():
    sys.exit(1)

def fix_url(url):
    if not isinstance(url, str) or not url.startswith('/media/'):
        return url
        
    local_path = os.path.join(settings.BASE_DIR, url.lstrip('/'))
    if not os.path.exists(local_path):
        return url
        
    try:
        with open(local_path, 'rb') as f:
            if url.endswith('.svg'):
                data = f.read()
                content_type = 'image/svg+xml'
                new_filename = os.path.basename(local_path)
            else:
                data, content_type = _compress_image(f)
                new_filename = os.path.splitext(os.path.basename(local_path))[0] + '.webp'
                
            r2_url = _upload_to_r2(f'uploads/{new_filename}', data, content_type)
            print(f"Uploaded {os.path.basename(local_path)} to {r2_url}")
            return r2_url
    except Exception as e:
        print(f"Error {local_path}: {e}")
        return url

for sp in SitePhotos.objects.all():
    changed = False
    for field in SitePhotos._meta.fields:
        if field.name == 'id': continue
        val = getattr(sp, field.name, '')
        if isinstance(val, str) and val.startswith('/media/'):
            setattr(sp, field.name, fix_url(val))
            changed = True
        elif isinstance(val, list):
            new_val = []
            for item in val:
                if isinstance(item, str) and item.startswith('/media/'):
                    new_val.append(fix_url(item))
                    changed = True
                else:
                    new_val.append(item)
            setattr(sp, field.name, new_val)
    if changed:
        sp.save()
        
for sc in SiteConfig.objects.all():
    changed = False
    for field in ['office_zabrze_photo', 'office_katowice_photo', 'office_krakow_photo', 'office_site_photo']:
        val = getattr(sc, field, '')
        if isinstance(val, str) and val.startswith('/media/'):
            setattr(sc, field, fix_url(val))
            changed = True
    if changed:
        sc.save()

print("Regenerating mbt_data.py...")
from MBTApp.signals import regenerate_mbt_data
regenerate_mbt_data()
