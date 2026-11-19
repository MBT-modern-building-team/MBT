"""Testy panelu CMS: każda strona admina się renderuje, tłumaczenia zapisują się poprawnie."""
import json

from django.contrib import admin
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from MBTApp import models
from MBTApp.forms import TranslationsWidget


class TranslationsWidgetTests(TestCase):
    def test_roundtrip_keeps_only_filled_and_unknown_keys(self):
        w = TranslationsWidget()
        data = {'t__en': ' Hello ', 't__de': '', 't__extra': json.dumps({'fr': 'Bonjour'})}
        self.assertEqual(json.loads(w.value_from_datadict(data, {}, 't')), {'fr': 'Bonjour', 'en': 'Hello'})

    def test_context_reads_dict_and_json(self):
        w = TranslationsWidget()
        for value in ({'en': 'A'}, '{"en": "A"}'):
            ctx = w.get_context('t', value, {'id': 'id_t'})
            langs = {lang['code']: lang['value'] for lang in ctx['widget']['langs']}
            self.assertEqual(langs['en'], 'A')
            self.assertEqual(ctx['widget']['filled'], 1)

    def test_bad_json_is_empty(self):
        ctx = TranslationsWidget().get_context('t', 'not json', {})
        self.assertEqual(ctx['widget']['filled'], 0)


class AdminPagesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_superuser('cms_test', 'cms@example.com', None)
        cls.project = models.Project.objects.create(
            title='Hala testowa', slug='hala-testowa', t_title={'en': 'Test hall'},
        )

    def setUp(self):
        self.client.force_login(self.user)

    def test_index_groups(self):
        r = self.client.get(reverse('admin:index'))
        self.assertEqual(r.status_code, 200)
        names = [app['name'] for app in r.context['app_list']]
        self.assertIn('Treści strony', names)
        self.assertIn('Dane firmy i zdjęcia', names)

    def test_all_changelists_and_add_forms_render(self):
        for model, model_admin in admin.site._registry.items():
            info = (model._meta.app_label, model._meta.model_name)
            r = self.client.get(reverse('admin:%s_%s_changelist' % info), follow=True)
            self.assertEqual(r.status_code, 200, model.__name__)
            if model_admin.has_add_permission(r.wsgi_request):
                r = self.client.get(reverse('admin:%s_%s_add' % info))
                self.assertEqual(r.status_code, 200, model.__name__)

    def test_siteconfig_shows_translations(self):
        r = self.client.get(reverse('admin:MBTApp_siteconfig_changelist'), follow=True)
        self.assertContains(r, 'name="t_hero_title1__en"')

    def test_project_translations_save(self):
        url = reverse('admin:MBTApp_project_change', args=[self.project.pk])
        r = self.client.get(url)
        self.assertContains(r, 'value="Test hall"')
        form = r.context['adminform'].form
        data = {}
        for name, field in form.fields.items():
            if name.startswith('t_') or name in ('_multipart',):
                continue
            val = form.initial.get(name, field.initial)
            if name == 'gallery':
                val = json.dumps(val or [])
            data[name] = '' if val is None else val
        data.update({'t_title__en': 'New hall', 't_title__de': 'Neue Halle', '_save': 'Zapisz'})
        r = self.client.post(url, data)
        self.assertEqual(r.status_code, 302, getattr(r, 'context', None) and r.context['adminform'].form.errors)
        self.project.refresh_from_db()
        self.assertEqual(self.project.t_title, {'en': 'New hall', 'de': 'Neue Halle'})
