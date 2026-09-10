import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MBT.settings')
django.setup()

from MBTApp.models import GeneralSettings, OfferSettings, Award, Realization, ContactPerson

OLD_DOMAIN = "https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev"
# Zmień to na swoją nową domenę, np. "https://media.mbt.pl"
NEW_DOMAIN = "https://media.mbt.pl"

def replace_domain(field_value):
    if field_value and isinstance(field_value, str) and OLD_DOMAIN in field_value:
        return field_value.replace(OLD_DOMAIN, NEW_DOMAIN)
    return field_value

print("Aktualizacja domeny R2 w bazie danych...")

# Aktualizacja GeneralSettings
for gs in GeneralSettings.objects.all():
    changed = False
    for field in ['hale_przemyslowe_hero', 'hale_przemyslowe_1', 'hale_przemyslowe_2', 
                  'hale_magazynowe_hero', 'hale_magazynowe_1',
                  'obiekty_komercyjne_hero', 'obiekty_komercyjne_1', 'obiekty_komercyjne_2',
                  'general_contracting_1', 'general_contracting_2',
                  'award_header_image', 'realization_header_image']:
        if hasattr(gs, field):
            old_val = getattr(gs, field)
            new_val = replace_domain(old_val)
            if old_val != new_val:
                setattr(gs, field, new_val)
                changed = True
    
    if changed:
        gs.save()
        print(f"Zaktualizowano GeneralSettings (ID: {gs.id})")

# Aktualizacja Realizacji
for r in Realization.objects.all():
    changed = False
    for field in ['image_1', 'image_2', 'image_3', 'image_4']:
        if hasattr(r, field):
            old_val = getattr(r, field)
            new_val = replace_domain(old_val)
            if old_val != new_val:
                setattr(r, field, new_val)
                changed = True
    if changed:
        r.save()
        print(f"Zaktualizowano Realization: {r.title}")
        
# Aktualizacja Nagrod
for a in Award.objects.all():
    changed = False
    if hasattr(a, 'image'):
        old_val = getattr(a, 'image')
        new_val = replace_domain(old_val)
        if old_val != new_val:
            setattr(a, 'image', new_val)
            changed = True
    if changed:
        a.save()
        print(f"Zaktualizowano Award: {a.title}")

print("Zrobione!")
