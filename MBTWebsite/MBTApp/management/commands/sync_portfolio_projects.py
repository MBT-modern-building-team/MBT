"""Tworzy brakujące realizacje (tylko logo klienta) i usuwa realizacje wycofane z serwisu.

Źródło: portfolio_mbt.json + stałe NEW_RECORDS / REMOVED_SLUGS w MBTApp/portfolio.py.

Użycie (poza cold startem, na wybranej bazie):
    python manage.py sync_portfolio_projects --dry-run
    python manage.py sync_portfolio_projects

Idempotentne: istniejące rekordy nie są zmieniane, usunięte nie wracają.
Opisy istniejących realizacji uzupełnia osobno `sync_portfolio_descriptions`.
"""
import re

from django.core.management.base import BaseCommand
from django.db.models import Max

from MBTApp import portfolio
from MBTApp.models import Project


class Command(BaseCommand):
    help = 'Tworzy brakujące realizacje z logo i usuwa wycofane (Venus).'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true', help='Tylko pokaż, co by się zmieniło.')
        parser.add_argument('--fixes-only', action='store_true',
                            help='Tylko poprawki pisowni, nazw i slugów (bez tworzenia i usuwania realizacji).')

    def handle(self, *args, **options):
        dry = options['dry_run']
        tag = '[dry] ' if dry else ''
        data = {r['nr']: r for r in portfolio._raw()['realizacje']}
        order = (Project.objects.aggregate(m=Max('order'))['m'] or 0) + 1
        created = deleted = 0

        fixes_only = options['fixes_only']
        for nr, logo in ({} if fixes_only else portfolio.NEW_RECORDS).items():
            r = data[nr]
            slugs = portfolio.EXISTING_SLUGS[nr]
            slug = slugs if isinstance(slugs, str) else slugs[0]
            if Project.objects.filter(slug=slug).exists():
                continue
            created += 1
            self.stdout.write(f'{tag}nowa realizacja: {slug} ({r["nazwa"]})')
            if not dry:
                Project.objects.create(
                    title=r['nazwa'], slug=slug,
                    type='realizacja-w-trakcie' if nr in portfolio.IN_PROGRESS_NEW else 'realizacja-zrealizow',
                    status='W trakcie realizacji' if nr in portfolio.IN_PROGRESS_NEW else 'Zrealizowane',
                    formula=r.get('formula') or '', opis=portfolio.project_description(r),
                    logo=logo, hero=logo, gallery=[], order=order,
                )
                order += 1

        for slug, title in portfolio.TITLE_FIXES.items():
            qs = Project.objects.filter(slug=slug).exclude(title=title)
            if qs.exists():
                self.stdout.write(f'{tag}nazwa: {slug} -> {title}')
                if not dry:
                    qs.update(title=title)

        # Poprawki pisowni w tekstach realizacji (tytuł, opis, tłumaczenia) oraz slugów.
        fixes = [(re.compile(a), b) for a, b in portfolio.TEXT_FIXES]

        def fix(text):
            for rx, rep in fixes:
                text = rx.sub(rep, text)
            return text

        for old, new in portfolio.SLUG_FIXES.items():
            qs = Project.objects.filter(slug=old)
            if qs.exists() and not Project.objects.filter(slug=new).exists():
                self.stdout.write(f'{tag}slug: {old} -> {new}')
                if not dry:
                    qs.update(slug=new)
        text_fields = ('title', 'opis', 'czas', 'formula', 'status')
        dict_fields = ('t_title', 't_opis', 't_czas', 't_formula', 't_status')
        for p in Project.objects.all():
            changed = []
            for f in text_fields:
                val = getattr(p, f) or ''
                new = fix(val)
                if new != val:
                    changed.append(f)
                    setattr(p, f, new)
            for f in dict_fields:
                d = getattr(p, f) or {}
                nd = {k: fix(v) if isinstance(v, str) else v for k, v in d.items()}
                if nd != d:
                    changed.append(f)
                    setattr(p, f, nd)
            if changed:
                self.stdout.write(f'{tag}pisownia: {p.slug} ({", ".join(changed)})')
                if not dry:
                    p.save(update_fields=changed)

        for slug in ([] if fixes_only else portfolio.REMOVED_SLUGS):
            qs = Project.objects.filter(slug=slug)
            if qs.exists():
                deleted += qs.count()
                self.stdout.write(f'{tag}usunięta realizacja: {slug}')
                if not dry:
                    qs.delete()

        self.stdout.write(self.style.SUCCESS(f'Utworzone: {created}, usunięte: {deleted}'))
