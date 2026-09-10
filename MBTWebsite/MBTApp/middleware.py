"""Middleware — panel admina tylko przez subdomenę admin.*.

Jeśli ktoś wejdzie na /admin/ z głównej domeny (np. twoja-strona.vercel.app),
zostanie przekierowany na https://admin.<ta-sama-domena>/admin/.
Dzięki temu panel jest dostępny wyłącznie pod subdomeną admin.,
co utrudnia jego odnalezienie (security through obscurity — hasło i tak
wymagane, ale to dodatkowa warstwa).

W trybie DEBUG (lokalny dev) przekierowanie jest wyłączone, żeby admin
działał na localhost.
"""
from django.conf import settings
from django.shortcuts import redirect


class AdminSubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        host = (request.get_host() or '').lower()

        is_admin_path = path.startswith('/admin/') or path == '/admin'
        already_on_subdomain = host.startswith('admin.') or host.startswith('localhost') or host.startswith('127.0.0.1')

        if (
            not settings.DEBUG
            and is_admin_path
            and not already_on_subdomain
            and host
        ):
            return redirect(f'https://admin.{host}{path}')

        return self.get_response(request)

class AutoLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
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
