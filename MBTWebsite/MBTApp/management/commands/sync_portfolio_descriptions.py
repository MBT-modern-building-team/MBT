"""Dopisuje opisy z portfolio_mbt.json (typ obiektu + parametry) do rekordów /realizacje/ w bazie.

Użycie (poza cold startem, na wybranej bazie):
    python manage.py sync_portfolio_descriptions --dry-run
    python manage.py sync_portfolio_descriptions

Operacja jest idempotentna: gdy parametry są już w opisie, rekord się nie zmienia.
Tłumaczenia (t_opis) zostają bez zmian — brak wpisu = fallback na polski opis.
"""
from django.core.management.base import BaseCommand

from MBTApp import portfolio
from MBTApp.models import Project


class Command(BaseCommand):
    help = 'Dopisuje opisy z portfolio_mbt.json do realizacji (Project.opis).'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true', help='Tylko pokaż, co by się zmieniło.')

    def handle(self, *args, **options):
        dry = options['dry_run']
        changed = missing = 0
        for r in portfolio._raw()['realizacje']:
            slugs = portfolio.EXISTING_SLUGS.get(r['nr'])
            if not slugs:
                continue
            slugs = (slugs,) if isinstance(slugs, str) else slugs
            p = Project.objects.filter(slug__in=slugs).first()
            if not p:
                missing += 1
                self.stderr.write(f'brak rekordu w bazie: {slugs}')
                continue
            new = portfolio.project_description(r, p.opis)
            if new == (p.opis or '').strip():
                continue
            changed += 1
            self.stdout.write(f'{"[dry] " if dry else ""}{p.slug}: opis zaktualizowany')
            if not dry:
                p.opis = new
                p.save(update_fields=['opis'])
        self.stdout.write(self.style.SUCCESS(f'Zmienione: {changed}, bez rekordu w bazie: {missing}'))
