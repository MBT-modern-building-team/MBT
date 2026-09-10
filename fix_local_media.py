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
    print("R2 NOT CONFIGURED")
    sys.exit(1)

def fix_url(url):
    if not url or not url.startswith('/media/'):
        return url
        
    local_path = os.path.join(settings.BASE_DIR, url.lstrip('/'))
    if not os.path.exists(local_path):
        print(f"Missing local file: {local_path}")
        return url
        
    print(f"Uploading {local_path} to R2...")
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
            print(f"Uploaded to {r2_url}")
            return r2_url
    except Exception as e:
        print(f"Error uploading {local_path}: {e}")
        return url

# Fix Projects
for p in Project.objects.all():
    changed = False
    if p.hero and p.hero.startswith('/media/'):
        p.hero = fix_url(p.hero)
        changed = True
    if p.logo and p.logo.startswith('/media/'):
        p.logo = fix_url(p.logo)
        changed = True
    new_gallery = []
    if p.gallery:
        for g in p.gallery:
            if g.startswith('/media/'):
                new_gallery.append(fix_url(g))
                changed = True
            else:
                new_gallery.append(g)
        p.gallery = new_gallery
    if changed:
        p.save()

# Fix Workers
for w in Worker.objects.all():
    if w.photo and w.photo.startswith('/media/'):
        w.photo = fix_url(w.photo)
        w.save()

# Fix SalesReps
for s in SalesRepresentative.objects.all():
    if s.photo and s.photo.startswith('/media/'):
        s.photo = fix_url(s.photo)
        s.save()

# Fix SitePhotos
for sp in SitePhotos.objects.all():
    changed = False
    for field in SitePhotos._meta.fields:
        if field.name == 'id': continue
        val = getattr(sp, field.name, '')
        if val and val.startswith('/media/'):
            setattr(sp, field.name, fix_url(val))
            changed = True
    if changed:
        sp.save()
        
# Fix SiteConfig
for sc in SiteConfig.objects.all():
    changed = False
    for field in ['office_zabrze_photo', 'office_katowice_photo', 'office_krakow_photo', 'office_site_photo']:
        val = getattr(sc, field, '')
        if val and val.startswith('/media/'):
            setattr(sc, field, fix_url(val))
            changed = True
    if changed:
        sc.save()

print("Done fixing media URLs. Now regenerating mbt_data.py...")
from MBTApp.signals import regenerate_mbt_data
regenerate_mbt_data()
