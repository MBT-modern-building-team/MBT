import sys
import re

with open('Construz/scripts/gen_mbt_data.py', 'r') as f:
    content = f.read()

# Add Award to imports
content = content.replace(
    'Article, Job, Project, Reference, SiteConfig, SitePhotos, Worker, SalesRepresentative',
    'Article, Job, Project, Reference, SiteConfig, SitePhotos, Worker, SalesRepresentative, Award'
)

# Add awards generation
awards_section = """
    # --- AWARDS ---
    awards = []
    for a in Award.objects.filter(is_active=True).order_by('order', 'name'):
        awards.append({
            'name': a.name,
            'image': a.image,
            'order': a.order,
        })

    # --- PHOTOS"""
content = content.replace('    # --- PHOTOS', awards_section)

# Export AWARDS
export_section = """+ _section('ARTICLES', arts) + '\\n'
        + _section('AWARDS', awards) + '\\n'
        + f'PHOTOS = {_dump(photos)}\\n'"""
content = re.sub(r"\+ _section\('ARTICLES', arts\) \+ '\\n'\s*\+ f'PHOTOS = \{_dump\(photos\)\}\\n'", export_section, content)

# Print count
print_section = """print(f'  ARTICLES   : {len(arts)}')
    print(f'  AWARDS     : {len(awards)}')"""
content = content.replace("print(f'  ARTICLES   : {len(arts)}')", print_section)

with open('Construz/scripts/gen_mbt_data.py', 'w') as f:
    f.write(content)
