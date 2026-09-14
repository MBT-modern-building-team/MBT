import sys, os, json, re
sys.path.insert(0, ".")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MBT.settings")
import django; django.setup()

from MBTApp.mbt_data import SECTORS
from MBTApp.storage import _upload_to_r2, _compress_image
from django.conf import settings

replacements = {}

for s in SECTORS:
    url = s.get('image')
    if url and url.startswith('/media/'):
        local_path = os.path.join(settings.BASE_DIR, url.lstrip('/'))
        if os.path.exists(local_path):
            print(f"Uploading {local_path}...")
            with open(local_path, 'rb') as f:
                ext = os.path.splitext(local_path)[1].lower()
                data, content_type = _compress_image(f)
                new_filename = os.path.splitext(os.path.basename(local_path))[0] + '.webp'
                
                subpath = url[len('/media/'):]
                r2_key = os.path.dirname(subpath) + '/' + new_filename if os.path.dirname(subpath) else 'uploads/' + new_filename
                r2_key = r2_key.strip('/')
                
                r2_url = _upload_to_r2(r2_key, data, content_type)
                print(f"  -> {r2_url}")
                replacements[url] = r2_url
        else:
            print(f"Missing local file: {local_path}")

print("Replacements:", replacements)

if replacements:
    with open("MBTApp/mbt_data.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(f'"{old}"', f'"{new}"')
        content = content.replace(f"'{old}'", f"'{new}'")
        
    with open("MBTApp/mbt_data.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("mbt_data.py updated!")
