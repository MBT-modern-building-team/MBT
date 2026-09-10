"""
Custom set_language view that properly translates URLs when switching languages.

Django's built-in set_language uses translate_url() which fails to translate
URLs that don't match the currently active language (e.g. '/de/' when
active is 'pl' — Django returns the original URL because PREFIX_DEFAULT_LANGUAGE=False
means there's no '/pl/' cache entry, and the pl-default fallback isn't matched).

This view works around it by:
  1. Stripping the language prefix from next_url before resolving (so /de/o-nas/
     becomes /o-nas/, which IS in urlpatterns under any active language).
  2. Reversing the URL in the target language (with override()), giving the
     correctly-prefixed URL — or '/' for pl thanks to PREFIX_DEFAULT_LANGUAGE=False.
"""
from urllib.parse import urlsplit, urlunsplit, unquote

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import resolve, reverse, NoReverseMatch
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.translation import check_for_language, override as lang_override


# Stała nazwy klucza sesji w Django 5+ (w starszych wersjach była w translation)
LANGUAGE_SESSION_KEY = 'django_language'

# Zestaw dostępnych kodów języków — z settings.LANGUAGES (lista (code, name))
LANG_CODES = {code for code, _ in getattr(settings, 'LANGUAGES', [])}


def set_language(request):
    """
    Custom version of django.views.i18n.set_language that correctly translates
    next_url even when next_url's language prefix differs from the active
    language (the case where Django's translate_url() fails).
    """
    next_url = request.POST.get('next', request.GET.get('next'))
    if (
        (next_url or request.accepts('text/html'))
        and not url_has_allowed_host_and_scheme(
            url=next_url,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure(),
        )
    ):
        next_url = request.META.get('HTTP_REFERER')
        if not url_has_allowed_host_and_scheme(
            url=next_url,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure(),
        ):
            next_url = '/'

    response = HttpResponseRedirect(next_url) if next_url else HttpResponse(status=204)

    if request.method == 'POST':
        # Accept both 'language' (Django standard) and 'django_language' (legacy)
        lang_code = (
            request.POST.get('language')
            or request.POST.get(settings.LANGUAGE_COOKIE_NAME)
            or request.POST.get('django_language')
        )

        if lang_code and check_for_language(lang_code):
            # Translate next_url using custom logic
            if next_url:
                translated = _translate_url_safe(next_url, lang_code)
                if translated != next_url:
                    response = HttpResponseRedirect(translated)

            if hasattr(request, 'session'):
                try:
                    request.session[LANGUAGE_SESSION_KEY] = lang_code
                except Exception:
                    pass

            response.set_cookie(
                settings.LANGUAGE_COOKIE_NAME,
                lang_code,
                max_age=settings.LANGUAGE_COOKIE_AGE,
                path=settings.LANGUAGE_COOKIE_PATH,
                domain=settings.LANGUAGE_COOKIE_DOMAIN,
                secure=settings.LANGUAGE_COOKIE_SECURE,
                httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
                samesite=settings.LANGUAGE_COOKIE_SAMESITE,
            )

    return response


def _strip_lang_prefix(path):
    """
    Jeśli path zaczyna się od /xx/ gdzie xx to znany kod języka (np. /de/, /en/),
    zwraca (path_bez_prefiksu_z_trailing_slash, kod_języka_z_url).
    W przeciwnym razie (path, None).

    Np. /de/o-nas/ → ('/o-nas/', 'de'), /de/ → ('/', 'de'), /oferta/ → ('/oferta/', None).
    """
    parts = path.split('/', 2)  # ['', 'xx', 'reszta...']
    if len(parts) >= 3 and parts[1] in LANG_CODES:
        url_lang = parts[1]
        rest = parts[2]
        # Path z prefiksem '/xx/' + 'reszta' = '/' + 'xx' + '/' + 'reszta'
        # Bez prefiksu: '/' + 'reszta', gdzie 'reszta' może być pusty string (dla '/xx/')
        stripped = '/' + rest if rest else '/'
        return stripped, url_lang
    return path, None


def _translate_url_safe(url, lang_code):
    """
    Niezawodna translacja URL-a dla set_language.

    Strategia:
      1. Spróbuj Django's translate_url (fast path; działa gdy URL ma prefiks
         aktywnego języka lub gdy active == target i prefiks nie jest wymagany).
      2. Jeśli zwróci oryginalny URL (failure), zdejmij prefiks językowy ręcznie
         (/de/o-nas/ → /o-nas/), rozwiąż view przez resolve(), odwróć w
         docelowym języku przez reverse() z override(lang_code).
    """
    from django.urls import translate_url

    # Fast path — Django's translate_url radzi sobie w typowych przypadkach.
    result = translate_url(url, lang_code)
    if result != url:
        return result

    # Fallback: ręczne zdjęcie prefiksu + resolve + reverse.
    parsed = urlsplit(url)
    path = unquote(parsed.path)
    stripped_path, _url_lang = _strip_lang_prefix(path)

    try:
        match = resolve(stripped_path)
    except Exception:
        # Nie udało się rozwiązać — zostawiamy URL jak jest (Django i tak
        # ustawił cookie, użytkownik zobaczy stronę w nowym języku po refreshu).
        return url

    to_be_reversed = (
        f'{match.namespace}:{match.url_name}'
        if match.namespace else match.url_name
    )

    with lang_override(lang_code):
        try:
            new_url = reverse(to_be_reversed, args=match.args, kwargs=match.kwargs)
        except NoReverseMatch:
            return url

    return urlunsplit((parsed.scheme, parsed.netloc, new_url, parsed.query, parsed.fragment))