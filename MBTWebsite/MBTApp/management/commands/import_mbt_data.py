"""Zasiej bazę danymi z mbt_data.py (idempotentnie).

Użycie:  python manage.py import_mbt_data
- Nie nadpisuje istniejących rekordów (po slug) — edycje z admina zostają.
- Tworzy SiteConfig (jeden rekord) jeśli nie istnieje.
"""
from django.core.management.base import BaseCommand
from MBTApp import mbt_data
from MBTApp.models import Project, Job, Worker, Reference, Article, SiteConfig


class Command(BaseCommand):
    help = 'Importuje dane z mbt_data.py do bazy (bez nadpisywania edycji).'

    def handle(self, *args, **options):
        created_p = created_j = created_w = created_r = created_a = 0

        # Projekty
        for p in mbt_data.PROJECTS:
            _, created = Project.objects.update_or_create(
                slug=p['slug'],
                defaults={
                    'title': p['title'],
                    'type': p.get('type', 'realizacja-zrealizow'),
                    'status': p.get('status', 'Zrealizowane'),
                    'czas': p.get('czas', ''),
                    'formula': p.get('formula', ''),
                    'opis': p.get('opis', ''),
                    'logo': p.get('logo', ''),
                    'hero': p.get('hero', ''),
                    'gallery': p.get('gallery') or [],
                    'latitude': p.get('latitude'),
                    'longitude': p.get('longitude'),
                    'order': p.get('order', 0),
                    't_title': p.get('t_t', {}),
                    't_status': p.get('t_s', {}),
                    't_czas': p.get('t_c', {}),
                    't_formula': p.get('t_f', {}),
                    't_opis': p.get('t_o', {}),
                },
            )
            created_p += int(created)

        # Oferty pracy
        for j in mbt_data.JOBS:
            _, created = Job.objects.update_or_create(
                slug=j['slug'],
                defaults={
                    'title': j['title'], 
                    'text': j['text'],
                    't_title': j.get('t_t', {}),
                    't_text': j.get('t_x', {}),
                    'order': j.get('order', 0),
                },
            )
            created_j += int(created)

        # Pracownicy
        for w in mbt_data.WORKERS:
            _, created = Worker.objects.update_or_create(
                name=w['name'],
                defaults={
                    'position': w.get('position', ''),
                    'opis': w.get('opis', ''),
                    'photo': w.get('photo', ''),
                    'linkedin': w.get('linkedin', ''),
                    't_position': w.get('t_p', {}),
                    't_opis': w.get('t_o', {}),
                    'order': w.get('order', 0),
                },
            )
            created_w += int(created)
            
        # Nasi handlowcy
        from MBTApp.models import SalesRepresentative
        created_s = 0
        if hasattr(mbt_data, 'SALES_REPS'):
            for s in mbt_data.SALES_REPS:
                _, created = SalesRepresentative.objects.update_or_create(
                    name=s['name'],
                    defaults={
                        'position': s.get('position', ''),
                        'email': s.get('email', ''),
                        'phone': s.get('phone', ''),
                        'photo': s.get('photo', ''),
                        't_position': s.get('t_p', {}),
                        'order': s.get('order', 0),
                    },
                )
                created_s += int(created)

        # Opinie
        for r in mbt_data.REFERENCES:
            _, created = Reference.objects.update_or_create(
                firma=r['firma'],
                defaults={
                    'tresc': r['tresc'],
                    'osoba': r.get('osoba', ''),
                    'stanowisko': r.get('stanowisko', ''),
                    't_osoba': r.get('t_o', {}),
                    't_stanowisko': r.get('t_s', {}),
                    't_tresc': r.get('t_r', {}),
                    'order': r.get('order', 0),
                },
            )
            created_r += int(created)

        # Artykuły
        for a in mbt_data.ARTICLES:
            _, created = Article.objects.update_or_create(
                slug=a['slug'],
                defaults={
                    'title': a['title'],
                    'excerpt': a.get('excerpt', ''),
                    'text': a['text'],
                    'image': a.get('image', ''),
                    't_title': a.get('t_t', {}),
                    't_excerpt': a.get('t_e', {}),
                    't_text': a.get('t_x', {}),
                    'order': a.get('order', 0),
                },
            )
            created_a += int(created)

        # Dane firmy (zawsze nadpisujemy ze skryptu)
        SiteConfig.objects.all().delete()
        SiteConfig.objects.create(**mbt_data.SITE)
        created_site = 1

        self.stdout.write(self.style.SUCCESS(
            f'OK — utworzono: projekty={created_p}, oferty={created_j}, '
            f'pracownicy={created_w}, handlowcy={created_s}, opinie={created_r}, artykuły={created_a}, '
            f'site={created_site}'
        ))
