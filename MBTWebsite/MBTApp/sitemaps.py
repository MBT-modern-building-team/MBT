from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from MBTApp.models import Article, Project, Job, Sector


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'
    i18n = True
    alternates = True

    def items(self):
        return [
            'index', 'about', 'service', 'generalContracting',
            'halePrzemyslowe', 'haleMagazynowe', 'obiektyKomercyjne',
            'contact', 'blog', 'project', 'career', 'privacy'
        ]

    def location(self, item):
        return reverse(item)


class SectorSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7
    i18n = True
    alternates = True

    def items(self):
        try:
            db_sectors = [s.slug for s in Sector.objects.exclude(slug='') if s.view_name == 'sectorDetail']
            if db_sectors:
                return db_sectors
        except Exception:
            pass
        return [
            'biurowce', 'centra-badawczo-rozwojowe', 'centra-biznesowe', 'centra-handlowe',
            'chlodnie-mroznie', 'data-center', 'fabryki', 'galerie-handlowe',
            'hale-sportowe', 'hipermarkety', 'konstrukcje-stalowe', 'konstrukcje-zelbetowe',
            'magazyny-automatyczne', 'markety-budowlane', 'markety', 'mieszkaniowka',
            'nieruchomosci-komercyjne', 'obiekty-e-commerce', 'obiekty-medyczne-szpitale',
            'obiekty-militarne', 'obiekty-self-storage', 'obiekty-uzytecznosci-publicznej',
            'parki-handlowe', 'place-skladowe', 'powierzchnie-uslugowo-handlowe',
            'salony-samochodowe', 'sklepy-stacjonarne', 'wytwornie', 'zaklady-recyklingu'
        ]

    def location(self, item):
        return reverse('sectorDetail', args=[item])


class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7
    i18n = True
    alternates = True

    def items(self):
        try:
            items = list(Article.objects.filter(published=True))
            if items:
                return items
        except Exception:
            pass
        from MBTApp import mbt_data
        return [{'slug': a['slug'], 'created': None} for a in getattr(mbt_data, 'ARTICLES', []) if a.get('slug')]

    def lastmod(self, obj):
        if hasattr(obj, 'created'):
            return obj.created
        return None

    def location(self, obj):
        slug = obj.slug if hasattr(obj, 'slug') else obj.get('slug')
        return reverse('articleDetail', args=[slug])


class ProjectSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7
    i18n = True
    alternates = True

    def items(self):
        try:
            items = list(Project.objects.all())
            if items:
                return items
        except Exception:
            pass
        from MBTApp import mbt_data
        return [{'slug': p['slug']} for p in getattr(mbt_data, 'PROJECTS', []) if p.get('slug')]

    def location(self, obj):
        slug = obj.slug if hasattr(obj, 'slug') else obj.get('slug')
        return reverse('realizacjaDetail', args=[slug])


class JobSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6
    i18n = True
    alternates = True

    def items(self):
        try:
            items = list(Job.objects.all())
            if items:
                return items
        except Exception:
            pass
        from MBTApp import mbt_data
        return [{'slug': j['slug']} for j in getattr(mbt_data, 'JOBS', []) if j.get('slug')]

    def location(self, obj):
        slug = obj.slug if hasattr(obj, 'slug') else obj.get('slug')
        return reverse('careerDetail', args=[slug])
