import os
import sys
import django

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'MBTWebsite'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MBT.settings')
django.setup()

from django.conf import settings
from MBTApp.models import Project, Worker, SalesRepresentative, SitePhotos, SiteConfig, Award, Article, BannerTemplate, Sector
from MBTApp.storage import _r2_configured, _upload_to_r2, _compress_image
import boto3

if not _r2_configured():
    print("R2 NOT CONFIGURED IN ENV! Check Construz/.env.")
    sys.exit(1)

def fix_url(url, is_file_field=False):
    # If the URL is already absolute or doesn't start with /media/ (and is not a file field), skip
    if not url:
        return url
        
    if is_file_field:
        # FileField values are relative to MEDIA_ROOT, e.g. "oznakowanie/szablony/file.png"
        if url.startswith('http'):
            return url
        local_path = os.path.join(settings.MEDIA_ROOT, url)
    else:
        if not url.startswith('/media/'):
            return url
        # CharField with '/media/uploads/...'
        local_path = os.path.join(settings.BASE_DIR, url.lstrip('/'))
        
    if not os.path.exists(local_path):
        print(f"  [!] Missing local file: {local_path} (URL: {url})")
        return url
        
    print(f"  [*] Uploading {local_path} to R2...")
    try:
        with open(local_path, 'rb') as f:
            ext = os.path.splitext(local_path)[1].lower()
            if ext in ['.svg', '.pdf', '.mp4', '.webm']:
                data = f.read()
                content_type = 'image/svg+xml' if ext == '.svg' else 'application/pdf' if ext == '.pdf' else f'video/{ext.strip(".")}'
                new_filename = os.path.basename(local_path)
            else:
                data, content_type = _compress_image(f)
                new_filename = os.path.splitext(os.path.basename(local_path))[0] + '.webp'
            
            # Keep directory structure for R2 key
            # Usually we use 'uploads/new_filename' but if it's 'awards/award-1.png' we could use 'awards/award-1.png'
            # Let's extract the subfolder from the original URL
            # e.g., /media/awards/award-1.png -> awards/award-1.webp
            if url.startswith('/media/'):
                subpath = url[len('/media/'):]
                r2_key = os.path.dirname(subpath) + '/' + new_filename if os.path.dirname(subpath) else 'uploads/' + new_filename
            elif is_file_field:
                r2_key = os.path.dirname(url) + '/' + new_filename if os.path.dirname(url) else 'uploads/' + new_filename
            else:
                r2_key = 'uploads/' + new_filename
                
            r2_key = r2_key.strip('/')
            
            r2_url = _upload_to_r2(r2_key, data, content_type)
            print(f"      -> Uploaded to {r2_url}")
            return r2_url
    except Exception as e:
        print(f"  [X] Error uploading {local_path}: {e}")
        return url

print("--- Migrating Projects ---")
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

print("--- Migrating Workers ---")
for w in Worker.objects.all():
    if w.photo and w.photo.startswith('/media/'):
        w.photo = fix_url(w.photo)
        w.save()

print("--- Migrating SalesRepresentatives ---")
for s in SalesRepresentative.objects.all():
    if s.photo and s.photo.startswith('/media/'):
        s.photo = fix_url(s.photo)
        s.save()

print("--- Migrating SitePhotos ---")
for sp in SitePhotos.objects.all():
    changed = False
    for field in SitePhotos._meta.fields:
        if field.name == 'id': continue
        val = getattr(sp, field.name, '')
        if isinstance(val, str) and val.startswith('/media/'):
            setattr(sp, field.name, fix_url(val))
            changed = True
    if changed:
        sp.save()
        
print("--- Migrating SiteConfig ---")
for sc in SiteConfig.objects.all():
    changed = False
    for field in ['office_zabrze_photo', 'office_katowice_photo', 'office_krakow_photo', 'office_site_photo', 'hero_video']:
        val = getattr(sc, field, '')
        if val and val.startswith('/media/'):
            setattr(sc, field, fix_url(val))
            changed = True
    if changed:
        sc.save()

print("--- Migrating Awards ---")
for a in Award.objects.all():
    if a.image and a.image.startswith('/media/'):
        a.image = fix_url(a.image)
        a.save()

print("--- Migrating Articles ---")
for art in Article.objects.all():
    if art.image and art.image.startswith('/media/'):
        art.image = fix_url(art.image)
        art.save()
        
print("--- Migrating BannerTemplates ---")
for bt in BannerTemplate.objects.all():
    if bt.template_image and not str(bt.template_image.name).startswith('http'):
        new_url = fix_url(bt.template_image.name, is_file_field=True)
        if new_url != bt.template_image.name:
            bt.template_image.name = new_url
            bt.save()

print("--- Migrating Sectors ---")
for s in Sector.objects.all():
    if s.image and s.image.startswith('/media/'):
        s.image = fix_url(s.image)
        s.save()

print("--- Done migrating media to R2! ---")
print("Regenerating mbt_data.py...")
from MBTApp.signals import regenerate_mbt_data
regenerate_mbt_data()
print("Success!")
