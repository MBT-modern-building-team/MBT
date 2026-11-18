"""Czytelne slugi zamiast technicznych (SEO). Stare adresy przekierowuje
SeoRedirectMiddleware (301) — patrz LEGACY_PROJECT_SLUGS / LEGACY_JOB_SLUGS."""
from django.db import migrations

PROJECT_RENAMES = {'VESUVIUS': 'vesuvius-skawina', 'p1704': 'epco-bytom'}
JOB_RENAMES = {'p2253': 'praktyka-staz'}


def _rename(model, renames, reverse=False):
    for old, new in renames.items():
        if reverse:
            old, new = new, old
        if model.objects.filter(slug=new).exists():
            continue
        model.objects.filter(slug=old).update(slug=new)


def forwards(apps, schema_editor):
    _rename(apps.get_model('MBTApp', 'Project'), PROJECT_RENAMES)
    _rename(apps.get_model('MBTApp', 'Job'), JOB_RENAMES)


def backwards(apps, schema_editor):
    _rename(apps.get_model('MBTApp', 'Project'), PROJECT_RENAMES, reverse=True)
    _rename(apps.get_model('MBTApp', 'Job'), JOB_RENAMES, reverse=True)


class Migration(migrations.Migration):
    dependencies = [('MBTApp', '0027_sitephotos_defaults')]
    operations = [migrations.RunPython(forwards, backwards)]
