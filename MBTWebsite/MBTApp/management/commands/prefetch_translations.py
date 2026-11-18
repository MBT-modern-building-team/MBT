"""Buduje MBTApp/translation_cache.json — gotowe tłumaczenia maszynowe.

Na produkcji `auto_translate.translate()` nie łączy się z internetem (żeby nie
spowalniać stron). Ta komenda renderuje wszystkie strony z sitemapy we
wszystkich językach z włączonym tłumaczeniem online i zapisuje wyniki do pliku
JSON, który trzeba zacommitować.

Użycie (lokalnie, po dodaniu/zmianie treści w CMS):
    python manage.py prefetch_translations
    python manage.py prefetch_translations --lang en --lang de
"""
import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.test import Client
from django.test.utils import override_settings

from MBTApp import auto_translate as at


class Command(BaseCommand):
    help = 'Pobiera tłumaczenia maszynowe dla wszystkich stron i zapisuje translation_cache.json.'

    def add_arguments(self, parser):
        parser.add_argument('--lang', action='append', help='Kod języka (domyślnie wszystkie poza pl).')

    def handle(self, *args, **options):
        # Python z python.org na macOS nie ma certyfikatów CA — użyj certifi, jeśli jest.
        try:
            import certifi
            os.environ.setdefault('SSL_CERT_FILE', certifi.where())
        except ImportError:
            pass

        langs = options['lang'] or [code for code, _ in settings.LANGUAGES if code != 'pl']
        paths = self._collect_paths()

        existing = {}
        if os.path.exists(at.BUNDLED_CACHE_PATH):
            with open(at.BUNDLED_CACHE_PATH, encoding='utf-8') as f:
                existing = json.load(f)

        recorder = {}
        at._online_state.recorder = recorder
        client = Client()
        errors = 0
        try:
            with at.online_translation(), override_settings(SECURE_SSL_REDIRECT=False):
                for lang in langs:
                    for path in paths:
                        url = f'/{lang}{path}'
                        resp = client.get(url, HTTP_HOST='localhost', secure=True)
                        if resp.status_code >= 400:
                            errors += 1
                            self.stderr.write(f'{resp.status_code} {url}')
                    self.stdout.write(f'{lang}: gotowe ({len(paths)} stron)')
        finally:
            at._online_state.recorder = None

        merged = {**existing, **recorder}
        with open(at.BUNDLED_CACHE_PATH, 'w', encoding='utf-8') as f:
            json.dump(merged, f, ensure_ascii=False, indent=0, sort_keys=True)
        self.stdout.write(self.style.SUCCESS(
            f'Zapisano {len(merged)} tłumaczeń (nowych: {len(set(recorder) - set(existing))}, błędów stron: {errors}) '
            f'-> {at.BUNDLED_CACHE_PATH}'
        ))

    def _collect_paths(self):
        """Ścieżki PL (bez prefiksu języka) ze wszystkich sitemap."""
        from django.utils import translation
        from MBT.urls import sitemaps

        paths = set()
        with translation.override('pl'):
            for sm_cls in sitemaps.values():
                sm = sm_cls()
                for item in sm.items():
                    paths.add(sm.location(item))
        return sorted(paths)
