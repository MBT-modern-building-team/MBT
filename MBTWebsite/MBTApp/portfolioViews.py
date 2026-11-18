import json

from django.shortcuts import render
from django.urls import NoReverseMatch, reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

from MBTApp import mbt_orm, portfolio

SITE_URL = 'https://mbt.pl'


def _json_ld(request, ctx, lang):
    p = ctx['p']
    c = p['contact']
    hq = next((o for o in p['offices'] if o.get('typ') == 'Centrala'), p['offices'][0])
    page_url = SITE_URL + request.path
    org = {
        '@context': 'https://schema.org',
        '@type': 'GeneralContractor',
        'name': p['company_name'],
        'url': c.get('www') or SITE_URL,
        'foundingDate': str(p['since']),
        'telephone': c.get('telefon'),
        'email': c.get('email'),
        'address': {
            '@type': 'PostalAddress',
            'streetAddress': hq.get('adres'),
            'addressLocality': hq.get('miasto'),
            'addressCountry': 'PL',
        },
        'knowsAbout': p['specializations'],
    }
    crumbs = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'MBT', 'item': SITE_URL + reverse('index')},
            {'@type': 'ListItem', 'position': 2, 'name': p['texts']['hero_kicker'], 'item': page_url},
        ],
    }
    # Bezpieczne osadzenie w <script>: bez sekwencji </ i znaków rozbijających parser HTML.
    dump = lambda o: json.dumps(o, ensure_ascii=False).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    return mark_safe(dump(org)), mark_safe(dump(crumbs))


def potencjal(request):
    lang = request.LANGUAGE_CODE
    ctx = portfolio.build_context(lang)
    try:
        pdf_url = reverse('portfolioPdf')
    except NoReverseMatch:
        pdf_url = ''  # generator Karty Wykonawcy PDF jeszcze nie podpięty (etap 2)
    ld_org, ld_crumbs = _json_ld(request, ctx, lang)
    ctx.update({
        'title': _('Potencjał i referencje'),
        'meta_title': _('Potencjał i referencje – %(n)s realizacji, kadra, struktura | MBT Modern Building Team') % {'n': ctx['p']['total']},
        'meta_description': _('Portfolio prekwalifikacyjne MBT: kapitał spółki, struktura organizacyjna, kadra, technologie oraz %(n)s realizacji w %(s)s sektorach. Generalne Wykonawstwo i Zaprojektuj i Wybuduj.') % {'n': ctx['p']['total'], 's': len(ctx['p']['sectors'])},
        'pdf_url': pdf_url,
        'sales_reps': mbt_orm.get_sales_reps(lang),
        'json_ld_org': ld_org,
        'json_ld_breadcrumbs': ld_crumbs,
        'site': mbt_orm.get_site(lang),
        'breadcrumb': True,  # własny hero zamiast globalnego breadcrumb-a
    })
    return render(request, 'pages/potencjal.html', ctx)
