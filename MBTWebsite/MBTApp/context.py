"""Context processor — wstrzykuje dane SITE i ARTICLES do wszystkich szablonów.

Dzięki temu w każdym szablonie możesz użyć {{ site.phone }}, {{ site.email }},
{% for a in articles %} itd. Dane pochodzą z bazy (admin), z fallbackiem
do mbt_data.py gdy baza jest pusta. Wszystkie dane tekstowe są tłumaczone
na bieżący język (request.LANGUAGE_CODE).
"""
from MBTApp import mbt_orm
from MBTApp.i18n_views import _translate_url_safe


# Strony, których nie chcemy w wynikach wyszukiwania (wyszukiwarka, ankiety,
# wydarzenia, panel oznakowania, kiosk, brandbook).
NOINDEX_URL_NAMES = {
    'search', 'ankieta_wizerunek', 'uroczystosc', 'uroczystosc_correct',
    'kiosk', 'brandbook', 'rodo_upper',
}
NOINDEX_URL_PREFIXES = ('oznakowanie_', 'board_')


def site_context(request):
    lang = getattr(request, 'LANGUAGE_CODE', 'pl')
    match = getattr(request, 'resolver_match', None)
    url_name = getattr(match, 'url_name', None) or ''
    return {
        'site': mbt_orm.get_site(lang),
        'articles': mbt_orm.get_articles(lang),
        'photos': mbt_orm.get_photos(),
        'is_home': url_name == 'index',
        'seo_noindex': url_name in NOINDEX_URL_NAMES or url_name.startswith(NOINDEX_URL_PREFIXES),
    }


def translate_url(request):
    """Context processor: udostępnia {{ translate_urls }} oraz {{ site_languages }} w szablonach.

    Dict { 'pl': '/oferta/', 'en': '/en/oferta/', ... } — niezawodne tłumaczenia bieżącego
    URL-a na każdy język (nawet przy braku prefiksu w domyślnym języku PL).
    """
    clean_path = request.path
    from django.conf import settings as _settings
    lang_list = []
    out = {}
    for code, name in _settings.LANGUAGES:
        try:
            url = _translate_url_safe(clean_path, code)
        except Exception:
            url = clean_path
        out[code] = url
        lang_list.append({
            'code': code,
            'name': name,
            'url': url,
        })
    return {
        'translate_urls': out,
        'site_languages': lang_list,
    }