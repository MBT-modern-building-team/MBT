"""Middleware — panel admina, przekierowania SEO 301 oraz wielojęzyczność."""
from django.conf import settings
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import redirect


BOT_USER_AGENTS = (
    'googlebot',
    'bingbot',
    'slurp',
    'duckduckbot',
    'baiduspider',
    'yandexbot',
    'sogou',
    'exabot',
    'facebot',
    'ia_archiver',
    'google-inspectiontool',
    'chrome-lighthouse',
    'applebot',
)

LEGACY_PAGE_MAPPINGS = {
    'privacy-policy': 'polityka-prywatnosci',
    'privacy': 'polityka-prywatnosci',
    'about-us': 'o-nas',
    'about': 'o-nas',
    'offer': 'oferta',
    'contact': 'kontakt',
    'contact-us': 'kontakt',
    'careers': 'kariera',
}

LEGACY_PROJECT_SLUGS = {
    'herz-wieliczka-2': 'herz-wieliczka',
    'pumar-siemianowice': 'pumar',
    'inpost-legnica': 'in-post-w-legnicy',
    'in-post-legnica': 'in-post-w-legnicy',
    'browar-lech-in-poznan': 'kompania-piwowarska',
    'lech-browary-wielkopolski': 'kompania-piwowarska',
    'stokado-self-storage-cracow': 'stokado-self-storage-krakow',
    'canpack-bss-excellence-centre-brzesk': 'canpack-bss-lab-brzesk',
}

_SLUG_CACHE = None


def _get_known_slugs():
    global _SLUG_CACHE
    if _SLUG_CACHE is not None:
        return _SLUG_CACHE
    try:
        from MBTApp import mbt_data
        articles = {a.get('slug') for a in getattr(mbt_data, 'ARTICLES', []) if a.get('slug')}
        projects = {p.get('slug') for p in getattr(mbt_data, 'PROJECTS', []) if p.get('slug')}
        jobs = {j.get('slug') for j in getattr(mbt_data, 'JOBS', []) if j.get('slug')}
        _SLUG_CACHE = (articles, projects, jobs)
        return _SLUG_CACHE
    except Exception:
        return (set(), set(), set())


class SeoRedirectMiddleware:
    """Zarządza przekierowaniami 301 pod kątem Google Search Console i SEO."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0].lower()

        # 1. Wymuszenie domeny głównej bez www (www.mbt.pl -> mbt.pl)
        if host == 'www.mbt.pl':
            clean_url = f"https://mbt.pl{request.get_full_path()}"
            return HttpResponsePermanentRedirect(clean_url)

        # 2. Czyszczenie starych parametrów WordPressa (?p=2033 itp.)
        if 'p' in request.GET and request.GET.get('p', '').isdigit():
            return HttpResponsePermanentRedirect(f"https://mbt.pl{request.path}")

        path = request.path
        # Normalizacja ścieżki
        stripped = path.strip('/')
        parts = stripped.split('/') if stripped else []

        if parts:
            # Rozpoznanie prefiksu językowego (np. en, de, cs, sk, hu, uk, pl)
            lang_codes = {code for code, _ in getattr(settings, 'LANGUAGES', [])}
            lang_codes.add('pl')

            lang_prefix = ''
            content_parts = parts
            if parts[0] in lang_codes:
                if parts[0] != 'pl':
                    lang_prefix = f"/{parts[0]}"
                content_parts = parts[1:]

            # Jeśli URL kończy się na /feed/ lub /feed (stare kanały RSS z WordPressa)
            if content_parts and content_parts[-1] == 'feed':
                target_parts = content_parts[:-1]
                if target_parts:
                    last_slug = target_parts[-1]
                    articles, projects, _ = _get_known_slugs()
                    if last_slug in articles:
                        return HttpResponsePermanentRedirect(f"{lang_prefix}/blog/{last_slug}/")
                    elif last_slug in projects:
                        return HttpResponsePermanentRedirect(f"{lang_prefix}/realizacja/{last_slug}/")
                return HttpResponsePermanentRedirect(f"{lang_prefix}/blog/")

            # Mapowanie starych angielskich ścieżek WordPressa (np. /en/about-us/)
            if len(content_parts) == 1 and content_parts[0] in LEGACY_PAGE_MAPPINGS:
                target_slug = LEGACY_PAGE_MAPPINGS[content_parts[0]]
                return HttpResponsePermanentRedirect(f"{lang_prefix}/{target_slug}/")

            # Mapowanie /realizacja-w-trakcie/ i zmienionych slugów realizacji
            if content_parts and content_parts[0] in ('realizacja-w-trakcie', 'realizacja'):
                if len(content_parts) > 1:
                    proj_slug = content_parts[1]
                    new_slug = LEGACY_PROJECT_SLUGS.get(proj_slug.lower(), proj_slug)
                    if content_parts[0] == 'realizacja-w-trakcie' or new_slug != proj_slug:
                        return HttpResponsePermanentRedirect(f"{lang_prefix}/realizacja/{new_slug}/")
                elif content_parts[0] == 'realizacja-w-trakcie':
                    return HttpResponsePermanentRedirect(f"{lang_prefix}/realizacje/")

            if content_parts and content_parts[0] == 'realizacje-w-trakcie':
                return HttpResponsePermanentRedirect(f"{lang_prefix}/realizacje/")

            # Artykuły/projekty wywołane bezpośrednio pod rootem (bez /blog/ lub /realizacja/)
            if len(content_parts) == 1:
                single_slug = content_parts[0]
                if single_slug.lower() in LEGACY_PROJECT_SLUGS:
                    return HttpResponsePermanentRedirect(f"{lang_prefix}/realizacja/{LEGACY_PROJECT_SLUGS[single_slug.lower()]}/")

                articles, projects, jobs = _get_known_slugs()
                if single_slug in articles:
                    return HttpResponsePermanentRedirect(f"{lang_prefix}/blog/{single_slug}/")
                elif single_slug in projects:
                    return HttpResponsePermanentRedirect(f"{lang_prefix}/realizacja/{single_slug}/")
                elif single_slug in jobs:
                    return HttpResponsePermanentRedirect(f"{lang_prefix}/kariera/{single_slug}/")

        return self.get_response(request)


class AdminSubdomainMiddleware:
    """Zezwala na logowanie do panelu admina na domenie głównej (mbt.pl, www.mbt.pl) oraz subdomenach."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)


class AutoLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Nigdy nie wymuszaj języka robotom wyszukiwarek na podstawie geolokalizacji IP
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        if any(bot in user_agent for bot in BOT_USER_AGENTS):
            return self.get_response(request)

        has_lang_cookie = settings.LANGUAGE_COOKIE_NAME in request.COOKIES
        
        set_lang = None
        if not has_lang_cookie:
            country = request.META.get('HTTP_X_VERCEL_IP_COUNTRY', '').upper()
            if not country:
                country = request.META.get('HTTP_CF_IPCOUNTRY', '').upper()
                
            if country == 'UA':
                set_lang = 'uk'
            elif country in ('GB', 'US', 'CA', 'AU', 'IE'):
                set_lang = 'en'
            elif country == 'DE':
                set_lang = 'de'
            elif country == 'CZ':
                set_lang = 'cs'
            elif country == 'SK':
                set_lang = 'sk'
            elif country == 'HU':
                set_lang = 'hu'

        if set_lang:
            request.COOKIES[settings.LANGUAGE_COOKIE_NAME] = set_lang

        response = self.get_response(request)

        if set_lang:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, set_lang)

        return response
