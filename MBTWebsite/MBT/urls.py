"""URL configuration for MBT project.

Strona jest wielojęzyczna (pl/en/cs/sk/de/hu). URL-e stron dostają prefiks
językowy przez i18n_patterns: / = pl (domyślny), /en/ = English, /cs/ = Čeština
itd. Admin oraz media pozostają poza prefiksem językowym.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import RedirectView
import os

def robots_txt_view(request):
    content = "User-agent: *\nAllow: /\nSitemap: https://mbt.pl/sitemap.xml\nDisallow: /admin/\nDisallow: /admin-budowa/\n"
    return HttpResponse(content, content_type="text/plain; charset=utf-8")

from django.contrib.sitemaps.views import sitemap
from MBTApp.sitemaps import StaticViewSitemap, ArticleSitemap, ProjectSitemap, JobSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'articles': ArticleSitemap,
    'projects': ProjectSitemap,
    'jobs': JobSitemap,
}

def media_redirect_view(request, path_str):
    if settings.DEBUG:
        local_path = os.path.join(settings.MEDIA_ROOT, path_str)
        if os.path.exists(local_path):
            from django.http import FileResponse
            return FileResponse(open(local_path, 'rb'))

    # Remove 'uploads/' if it's already at the beginning of path_str
    if path_str.startswith('uploads/'):
        path_str = path_str[len('uploads/'):]
        
    base, ext = os.path.splitext(path_str)
    if ext.lower() in ['.jpg', '.jpeg', '.png']:
        ext = '.webp'
    new_filename = base + ext
    r2_public = os.getenv('R2_PUBLIC_URL', 'https://pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev')
    
    # Check if it was an awards file, which might not be in 'uploads' directory on R2
    if 'awards/' in new_filename:
        # e.g., 'awards/award-1.png'
        return redirect(f"{r2_public.rstrip('/')}/media/{new_filename}", permanent=True)
        
    # Default to uploads folder on R2
    return redirect(f"{r2_public.rstrip('/')}/uploads/{os.path.basename(new_filename)}", permanent=True)

urlpatterns = [
    path('robots.txt', robots_txt_view),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('media/<path:path_str>', media_redirect_view),
    path('admin/', admin.site.urls),
    # Przekierowanie z /pl/ na / (ponieważ polski jest domyślnym językiem bez prefiksu)
    path('pl/', RedirectView.as_view(url='/', permanent=True)),
    path('pl/<path:rest>', RedirectView.as_view(url='/%(rest)s', permanent=True)),
    # Przełącznik języka (name='set_language' dopasowuje {% url 'set_language' %})
    # umieszczony poza i18n_patterns, żeby przełącznik działał w każdym języku
    # i zachowywał bieżący URL (parametr next).
    # Używamy własnego widoku z MBTApp.i18n_views, bo wbudowany set_language
    # Django nie tłumaczy URL-i prawidłowo gdy next ma inny prefiks niż aktywny
    # język (np. /de/ → pl) — PREFIX_DEFAULT_LANGUAGE=False powoduje, że cache
    # translacji nie ma wpisu dla prefiksu 'pl', więc translate_url() zwraca
    # oryginalny URL i redirect zostaje na /de/.
    path('i18n/setlang/', include('MBTApp.i18n_urls')),
]

# Strony publiczne — z prefiksem językowym (/en/, /cs/, /sk/, /de/, /hu/; / = pl)
urlpatterns += i18n_patterns(
    path('', include('MBTApp.urls')),
    prefix_default_language=settings.PREFIX_DEFAULT_LANGUAGE,
)

# Serwowanie uploadowanych plików (MEDIA) — tylko lokalnie (DEBUG).
# Na Vercel upload trafia do Vercel Blob (pełny URL), więc to zbędne.
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom error handlers
handler404 = 'MBTApp.error_handlers.handler404'
handler500 = 'MBTApp.error_handlers.handler500'
