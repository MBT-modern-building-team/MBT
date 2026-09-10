import os
import re

directory = 'Construz/MBTApp/templates'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = [
        (r'<img\s+src="/static/img/mbt/trusted-us-([^"]+)\.svg"\s+alt="([^"]+)">', 
         r'<img src="/static/img/mbt/trusted-us-\1.svg" alt="\2" width="150" height="80" loading="lazy">'),
         
        (r'<img\s+src="/static/img/icon/quote3\.svg"\s+alt="([^"]+)">',
         r'<img src="/static/img/icon/quote3.svg" alt="\1" width="40" height="40" loading="lazy">'),

        (r'<img\s+src="/static/img/mbt/mapa-polska-hq\.png"\s+alt="Mapa Polski"\s+style="([^"]+)">',
         r'<img src="/static/img/mbt/mapa-polska-hq.png" alt="Mapa Polski" style="\1" width="608" height="553" loading="lazy">'),

        (r'<img\s+src="/static/img/icon/about-checklsit-icon1-1\.svg"\s+alt="([^"]+)">',
         r'<img src="/static/img/icon/about-checklsit-icon1-1.svg" alt="\1" width="20" height="20" loading="lazy">'),
         
        (r'<img\s+src="/static/img/mbt/o-nas-zespol\.jpg"\s+width="800"\s+height="533"\s+alt="([^"]+)"\s+loading="lazy"\s+decoding="async">',
         r'<img src="/static/img/mbt/o-nas-zespol.webp" width="687" height="459" alt="\1" loading="lazy" decoding="async">'),
         
        (r'<img\s+src="/static/img/mbt/o-nas-2\.jpg"\s+width="800"\s+height="507"\s+alt="([^"]+)"\s+loading="lazy"\s+decoding="async">',
         r'<img src="/static/img/mbt/o-nas-2.webp" width="687" height="436" alt="\1" loading="lazy" decoding="async">'),
         
        (r'<a\s+href="([^"]+)"\s+class="btn-with-icon">(\s*)ZOBACZ PEŁEN OPIS(\s*)</a>',
         r'<a href="\1" class="btn-with-icon" aria-label="Zobacz pełen opis realizacji \1">\2ZOBACZ PEŁEN OPIS\3</a>')
    ]
    
    new_content = content
    for pattern, repl in replacements:
        new_content = re.sub(pattern, repl, new_content)
        
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))
