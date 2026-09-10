import sys

with open('Construz/MBTApp/mbt_orm.py', 'r') as f:
    content = f.read()

old_get_awards = """def get_awards():
    if _db_ready():
        return [{'name': a.name, 'image': a.image.url if a.image else ''} for a in Award.objects.filter(is_active=True)]
    return []"""

new_get_awards = """def get_awards():
    if _db_ready():
        return [{'name': a.name, 'image': a.image if a.image else ''} for a in Award.objects.filter(is_active=True)]
    
    # Fallback to mbt_data on Vercel
    awards = []
    for a in getattr(mbt_data, 'AWARDS', []):
        awards.append(a)
    return awards"""

content = content.replace(old_get_awards, new_get_awards)

with open('Construz/MBTApp/mbt_orm.py', 'w') as f:
    f.write(content)
