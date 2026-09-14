from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from MBTApp.models import Article, Project, Job

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


class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7
    i18n = True
    alternates = True

    def items(self):
        return Article.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.created

    def location(self, obj):
        return reverse('articleDetail', args=[obj.slug])


class ProjectSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7
    i18n = True
    alternates = True

    def items(self):
        return Project.objects.all()

    def location(self, obj):
        return reverse('realizacjaDetail', args=[obj.slug])


class JobSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6
    i18n = True
    alternates = True

    def items(self):
        return Job.objects.all()

    def location(self, obj):
        return reverse('careerDetail', args=[obj.slug])
