import re

from django.conf import settings
from django.test import TestCase, override_settings


@override_settings(SECURE_SSL_REDIRECT=False, ALLOWED_HOSTS=['*'])
class PortfolioPageTests(TestCase):
    """Podstrona /potencjal-i-referencje/ — treść z portfolio_mbt.json."""

    def _get(self, lang='pl'):
        path = '/potencjal-i-referencje/' if lang == 'pl' else f'/{lang}/potencjal-i-referencje/'
        return self.client.get(path, HTTP_HOST='localhost')

    def test_status_200_in_every_language(self):
        for code, _name in settings.LANGUAGES:
            with self.subTest(lang=code):
                self.assertEqual(self._get(code).status_code, 200)

    def test_54_unique_project_cards(self):
        html = self._get().content.decode()
        nrs = re.findall(r'class="pot-proj-nr">(\d+)<', html)
        self.assertEqual(sorted(map(int, nrs)), list(range(1, 55)))
        self.assertEqual(len(set(nrs)), 54)

    def test_no_placeholders_or_null_leak(self):
        for code, _name in settings.LANGUAGES:
            html = self._get(code).content.decode()
            body = re.sub(r'<script.*?</script>', '', html, flags=re.S)
            for bad in ('[DO UZUPE', '[DO T', 'DO WERYFIKACJI'):
                self.assertNotIn(bad, body, f'{bad} w {code}')
            text = re.sub(r'<[^>]+>', ' ', body)
            self.assertNotRegex(text, r'\bNone\b')
            self.assertNotRegex(text, r'\bnull\b')

    def test_capital_amounts_exact(self):
        html = self._get().content.decode()
        for s in ('750 000,00 zł', '15 975 953,90 zł', '16 725 953,90 zł'):
            self.assertIn(s, html)

    def test_stokado_bemowo_hides_unverified_areas(self):
        html = self._get().content.decode()
        body = re.sub(r'<(script|svg).*?</\1>', '', html, flags=re.S)  # współrzędne SVG mapy to nie metraże
        self.assertNotRegex(body, r'9[ \u00a0]?142')
        self.assertNotRegex(body, r'6[ \u00a0]?818')

    def test_in_progress_badge_and_hidden_null_fields(self):
        html = self._get().content.decode()
        self.assertEqual(html.count('class="pot-badge"'), 2)
        for label in ('KRS', 'NIP', 'REGON', 'Przychody netto', 'Suma gwarancyjna OC'):
            self.assertNotIn(f'<th scope="row">{label}', html)
        self.assertNotIn('Liczba osób', html)  # kolumna ukryta, brak danych

    def test_single_h1(self):
        html = self._get().content.decode()
        self.assertEqual(html.count('<h1'), 1)

    def test_pdf_link_only_when_route_exists(self):
        html = self._get().content.decode()
        self.assertEqual('pobierz-pdf' in html, False)  # trasa PDF = etap 2 (nie istnieje w repo)
