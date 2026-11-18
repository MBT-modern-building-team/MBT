"""Tagi SEO: dane strukturalne JSON-LD (schema.org) i pomocnicze filtry.

Użycie w szablonie:
    {% load seo_tags %}
    {% organization_jsonld %}
    {% article_jsonld article %}
"""
import json

from django import template
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

register = template.Library()

SITE_URL = 'https://mbt.pl'
LOGO_URL = f'{SITE_URL}/static/img/favicons/favicon.png'

OG_LOCALES = {
    'pl': 'pl_PL', 'en': 'en_GB', 'cs': 'cs_CZ', 'sk': 'sk_SK',
    'de': 'de_DE', 'hu': 'hu_HU', 'uk': 'uk_UA',
}


def _script(data):
    # Escapowanie '<', '>' i '&' chroni przed zamknięciem </script> treścią z CMS.
    payload = json.dumps(data, ensure_ascii=False)
    payload = payload.replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    return mark_safe(f'<script type="application/ld+json">{payload}</script>')


def _absolute(url):
    if not url:
        return ''
    url = str(url)
    if url.startswith(('http://', 'https://')):
        return url
    return SITE_URL + ('' if url.startswith('/') else '/') + url


def _address(raw):
    """'Jankego 176/1A, 40-663 Katowice' -> PostalAddress."""
    if not raw:
        return None
    street, _, rest = str(raw).partition(',')
    rest = rest.strip()
    postal, _, city = rest.partition(' ')
    return {
        '@type': 'PostalAddress',
        'streetAddress': street.strip(),
        'postalCode': postal.strip(),
        'addressLocality': city.strip() or rest,
        'addressCountry': 'PL',
    }


@register.filter
def absolute_url(url):
    return _absolute(url)


@register.filter
def og_locale(lang):
    return OG_LOCALES.get(lang or 'pl', 'pl_PL')


@register.simple_tag(takes_context=True)
def organization_jsonld(context):
    site = context.get('site') or {}
    get = site.get if isinstance(site, dict) else (lambda k, d=None: getattr(site, k, d))
    same_as = [u for u in (get('social_linkedin'), get('social_facebook'),
                           get('social_instagram'), get('social_youtube')) if u]
    org = {
        '@type': 'GeneralContractor',
        '@id': f'{SITE_URL}/#organization',
        'name': 'MBT Modern Building Team',
        'url': f'{SITE_URL}/',
        'logo': LOGO_URL,
        'image': LOGO_URL,
        'telephone': get('phone') or None,
        'email': get('email') or None,
        'foundingDate': get('founded') or None,
        'taxID': get('nip') or None,
        'address': _address(get('office_katowice')),
        'areaServed': 'PL',
        'sameAs': same_as or None,
    }
    branches = [b for b in (_address(get('office_zabrze')), _address(get('office_krakow'))) if b]
    if branches:
        org['department'] = [
            {'@type': 'GeneralContractor', 'name': 'MBT Modern Building Team', 'address': b}
            for b in branches
        ]
    data = {
        '@context': 'https://schema.org',
        '@graph': [
            {k: v for k, v in org.items() if v},
            {
                '@type': 'WebSite',
                '@id': f'{SITE_URL}/#website',
                'url': f'{SITE_URL}/',
                'name': 'MBT Modern Building Team',
                'inLanguage': context.get('LANGUAGE_CODE') or 'pl',
                'publisher': {'@id': f'{SITE_URL}/#organization'},
            },
        ],
    }
    return _script(data)


@register.simple_tag(takes_context=True)
def article_jsonld(context, article):
    if not article:
        return ''
    request = context.get('request')
    url = SITE_URL + (request.path if request else '')
    description = strip_tags(article.get('excerpt') or '')[:300].strip()
    data = {
        '@context': 'https://schema.org',
        '@type': 'BlogPosting',
        'headline': strip_tags(article.get('title') or '')[:110],
        'description': description or None,
        'image': _absolute(article.get('image')) or None,
        'url': url,
        'mainEntityOfPage': url,
        'inLanguage': context.get('LANGUAGE_CODE') or 'pl',
        'author': {'@type': 'Organization', 'name': 'MBT Modern Building Team', 'url': f'{SITE_URL}/'},
        'publisher': {
            '@type': 'Organization',
            'name': 'MBT Modern Building Team',
            'logo': {'@type': 'ImageObject', 'url': LOGO_URL},
        },
    }
    created = article.get('created')
    if created:
        data['datePublished'] = created.isoformat()
    return _script({k: v for k, v in data.items() if v})
