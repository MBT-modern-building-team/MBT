import os
import re
from unittest import mock

from django.conf import settings
from django.test import TestCase, override_settings


@override_settings(SECURE_SSL_REDIRECT=False, ALLOWED_HOSTS=['*'])
class PortfolioPageTests(TestCase):
    def setUp(self):
        patcher = mock.patch.dict(os.environ, {'PORTFOLIO_PAGE_PUBLIC': '1'})
        patcher.start()
        self.addCleanup(patcher.stop)
    """Podstrona /potencjal-i-referencje/ — treść z portfolio_mbt.json."""

    def _get(self, lang='pl'):
        path = '/potencjal-i-referencje/' if lang == 'pl' else f'/{lang}/potencjal-i-referencje/'
        return self.client.get(path, HTTP_HOST='localhost')

    def test_status_200_in_every_language(self):
        for code, _name in settings.LANGUAGES:
            with self.subTest(lang=code):
                self.assertEqual(self._get(code).status_code, 200)

    def test_project_cards_come_from_cms(self):
        from MBTApp import mbt_orm
        expected = len(mbt_orm.get_projects('pl'))
        html = self._get().content.decode()
        self.assertEqual(html.count('class="pot-proj-name"'), expected)
        self.assertNotIn('pot-proj-nr', html)  # numeracja kart usunięta

    def test_removed_content_not_present(self):
        for code, _name in settings.LANGUAGES:
            html = self._get(code).content.decode()
            body = re.sub(r'<(script|svg).*?</\1>', '', html, flags=re.S)
            for bad in ('MESKO', 'obronn', 'Zbrojeni', 'Łaziska', 'Na rynku od', 'Ponar Silesia', 'Venus', 'CDR Żory', 'Remondis', 'siedziba własna', 'Przemysłowa farma fotowoltaiczna'):
                self.assertNotIn(bad, body, f'{bad} w {code}')
        html = self._get().content.decode()
        self.assertIn('Ponar Wadowice', html)
        self.assertNotIn('Modlniczka', html)
        self.assertIn('Dolnośląska Izba Gospodarcza', html)

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

    def test_in_progress_badge_and_registry_data(self):
        html = self._get().content.decode()
        self.assertGreaterEqual(html.count('class="pot-badge"'), 10)  # wszystkie karty z logo (w trakcie realizacji)
        for label, value in (('NIP', '9542788822'), ('REGON', '369557780'), ('KRS', '0000720424')):
            self.assertRegex(html, r'<th scope="row">%s</th><td>%s</td>' % (label, value))
        for year, val in (('2023', '33,5 mln zł'), ('2024', '83,9 mln zł'), ('2025', '130,2 mln zł')):
            self.assertRegex(html, r'<th scope="row">Przychody %s</th><td>%s</td>' % (year, val))
        self.assertNotIn('Suma gwarancyjna OC', html)  # brak danych — pole ukryte
        self.assertNotIn('Liczba osób', html)  # kolumna ukryta, brak danych

    def test_single_h1(self):
        html = self._get().content.decode()
        self.assertEqual(html.count('<h1'), 1)

    def test_pdf_link_only_when_route_exists(self):
        html = self._get().content.decode()
        self.assertEqual('pobierz-pdf' in html, False)  # trasa PDF = etap 2 (nie istnieje w repo)

    def test_realizacje_added_and_removed(self):
        self.assertEqual(self.client.get('/realizacja/venus-brzegi/', HTTP_HOST='localhost').status_code, 404)
        for slug in ('eurostyl-chelmek', 'stokado-gdansk', 'artus-aircraft', 'centrum-sportow-rakietowych-ue-wroclaw', 'kbh-akord-siemianowice-slaskie',
                     'brembo-poland-dabrowa-gornicza', 'invest-tdj-estate-zabrze-zielona-dolina-4'):
            resp = self.client.get(f'/realizacja/{slug}/', HTTP_HOST='localhost')
            self.assertEqual(resp.status_code, 200, slug)
        html = self._get().content.decode()
        self.assertIn('/realizacja/eurostyl-chelmek/', html)
        self.assertIn('/static/img/mbt/logos/brembo.png', html)

    def test_pdf_mode_slides_16x9(self):
        from MBTApp import mbt_orm
        for code, _name in settings.LANGUAGES:
            path = '/potencjal-i-referencje/' if code == 'pl' else f'/{code}/potencjal-i-referencje/'
            resp = self.client.get(path + '?pdf=1', HTTP_HOST='localhost')
            self.assertEqual(resp.status_code, 200, code)
            html = resp.content.decode()
            self.assertIn('size:1600px 900px', html)
            self.assertEqual(html.count('class="proj"'), len(mbt_orm.get_projects(code)), code)
            text = re.sub(r'<(script|style).*?</\1>', '', html, flags=re.S)
            for bad in ('[DO UZUPE', '[DO T', 'None', 'MESKO', 'Venus'):
                self.assertNotIn(bad, re.sub(r'<[^>]+>', ' ', text), f'{bad} w {code}')


@override_settings(SECURE_SSL_REDIRECT=False, ALLOWED_HOSTS=['*'], DEBUG=False)
class PortfolioPageHiddenTests(TestCase):
    """Dopóki PORTFOLIO_PAGE_PUBLIC nie jest włączone, strona jest niewidoczna dla odwiedzających."""

    def setUp(self):
        patcher = mock.patch.dict(os.environ)
        patcher.start()
        os.environ.pop('PORTFOLIO_PAGE_PUBLIC', None)
        self.addCleanup(patcher.stop)

    def test_hidden_for_visitors_and_sitemap(self):
        for path in ('/potencjal-i-referencje/', '/en/potencjal-i-referencje/'):
            self.assertEqual(self.client.get(path, HTTP_HOST='localhost').status_code, 404, path)
        sitemap = self.client.get('/sitemap.xml', HTTP_HOST='localhost').content.decode()
        self.assertNotIn('potencjal-i-referencje', sitemap)

    def test_hidden_for_staff_too_in_production(self):
        from django.contrib.auth import get_user_model
        user = get_user_model().objects.create_user('staff', password='x', is_staff=True)
        self.client.force_login(user)
        for path in ('/potencjal-i-referencje/', '/potencjal-i-referencje/?pdf=1', '/potencjal-i-referencje/img/?u=%2Fstatic%2Fimg%2Fmbt%2Flogos%2Fbrembo.png'):
            self.assertEqual(self.client.get(path, HTTP_HOST='localhost').status_code, 404, path)

    @override_settings(DEBUG=True)
    def test_visible_locally_with_noindex(self):
        resp = self.client.get('/potencjal-i-referencje/', HTTP_HOST='localhost')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('noindex', resp['X-Robots-Tag'])
