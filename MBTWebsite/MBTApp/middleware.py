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
    'toto-golgoczow': 'toto-glogoczow',
    'vesuvius': 'vesuvius-skawina',
    'p1704': 'epco-bytom',
}

LEGACY_JOB_SLUGS = {
    'p2253': 'praktyka-staz',
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

            if len(content_parts) > 1 and content_parts[0] == 'kariera':
                new_job = LEGACY_JOB_SLUGS.get(content_parts[1].lower())
                if new_job:
                    return HttpResponsePermanentRedirect(f"{lang_prefix}/kariera/{new_job}/")

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
    """Zarządza subdomeną admin.* — wejście na stronę główną subdomeny przekierowuje do panelu /admin/."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = (request.get_host() or '').split(':')[0].lower()
        path = request.path

        # Jeśli ktoś wejdzie na subdomenę admin.* na stronę główną (/), przekieruj od razu do /admin/
        if host.startswith('admin.') and path in ('/', ''):
            return redirect('/admin/')

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


class PublicPageCacheMiddleware:
    """Pozwala CDN Vercela cache'ować publiczne strony HTML (s-maxage).

    Bez tego każde wejście uruchamia funkcję Pythona (zimny start = kilka sekund).
    Cache'ujemy TYLKO odpowiedzi, które są identyczne dla wszystkich odwiedzających:
      * GET/HEAD, status 200, brak własnego Cache-Control z widoku,
      * brak Set-Cookie w odpowiedzi i brak użytego tokenu CSRF (formularze),
      * żądanie bez ciasteczka sesji (zalogowani admini dostają świeżą stronę),
      * ścieżki spoza panelu/API/wyszukiwarki.
    Zmiany z CMS są widoczne najpóźniej po PUBLIC_PAGE_CACHE_SECONDS.

    Musi być PIERWSZYM middleware na liście (widzi odpowiedź po wszystkich innych).
    """

    EXCLUDED_PREFIXES = (
        '/admin', '/admin-budowa', '/api/', '/i18n/', '/kiosk', '/media/',
        '/szukaj', '/ankieta-wizerunek', '/uroczys',
    )

    def __init__(self, get_response):
        self.get_response = get_response
        self.seconds = int(getattr(settings, 'PUBLIC_PAGE_CACHE_SECONDS', 600))

    def _excluded_path(self, path):
        stripped = path
        lang_codes = {code for code, _ in getattr(settings, 'LANGUAGES', [])}
        parts = path.split('/', 2)
        if len(parts) > 2 and parts[1] in lang_codes:
            stripped = '/' + parts[2]
        return stripped.startswith(self.EXCLUDED_PREFIXES) or '/admin-budowa' in path

    def __call__(self, request):
        response = self.get_response(request)
        if (
            self.seconds <= 0
            or settings.DEBUG
            or request.method not in ('GET', 'HEAD')
            or response.status_code != 200
            or response.has_header('Cache-Control')
            or response.cookies
            or request.META.get('CSRF_COOKIE_NEEDS_UPDATE')
            or settings.SESSION_COOKIE_NAME in request.COOKIES
            or self._excluded_path(request.path)
            or not response.get('Content-Type', '').startswith(('text/html', 'application/xml', 'text/plain'))
        ):
            return response
        response['Cache-Control'] = (
            f'public, max-age=0, s-maxage={self.seconds}, stale-while-revalidate=86400'
        )
        return response
