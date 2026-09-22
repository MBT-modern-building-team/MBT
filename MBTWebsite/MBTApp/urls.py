from django.contrib import admin
from django.urls import path
from MBTApp import homeViews
from MBTApp import newsViews
from MBTApp import oznakowanieViews
from MBTApp import pagesViews
from MBTApp import serviceViews
from MBTApp import mbtViews

urlpatterns = [

    # Strona główna
    path('', homeViews.home, name='index'),

    # O nas / Oferta / Kontakt
    path('o-nas/', homeViews.about, name='about'),
    path('oferta/', serviceViews.service, name='service'),
    path('generalne-wykonawstwo/', serviceViews.generalContracting, name='generalContracting'),
    path('hale-przemyslowe/', serviceViews.halePrzemyslowe, name='halePrzemyslowe'),
    path('hale-magazynowe/', serviceViews.haleMagazynowe, name='haleMagazynowe'),
    path('obiekty-komercyjne/', serviceViews.obiektyKomercyjne, name='obiektyKomercyjne'),
    path('sektor/<slug:slug>/', serviceViews.sectorDetail, name='sectorDetail'),
    path('kontakt/', homeViews.contact, name='contact'),
    path('szukaj/', homeViews.search, name='search'),
    path('mapa-witryny/', homeViews.sitemap_html, name='sitemap_html'),
    path('ankieta-wizerunek/', serviceViews.ankieta_wizerunek, name='ankieta_wizerunek'),
    path('uroczysosc-rozpoczencia-inwestycji/', serviceViews.uroczystosc, name='uroczystosc'),
    path('uroczystosc-rozpoczecia-inwestycji/', serviceViews.uroczystosc, name='uroczystosc_correct'),

    # Blog / Artykuły
    path('blog/', newsViews.blog, name='blog'),
    path('blog/<slug:slug>/', newsViews.articleDetail, name='articleDetail'),

    # Realizacje (paginacja 1..4)
    path('realizacje/', mbtViews.realizacje, name='project'),
    path('realizacje/strona/<int:page>/', mbtViews.realizacje, name='projectPage'),
    path('realizacja/<slug:slug>/', mbtViews.realizacjaDetail, name='realizacjaDetail'),

    # Kariera
    path('kariera/', mbtViews.career, name='career'),
    path('kariera/<slug:slug>/', mbtViews.careerDetail, name='careerDetail'),

    # Polityka prywatności
    path('polityka-prywatnosci/', mbtViews.privacy, name='privacy'),

    # Oznakowanie budowy (panel kierownika)
    path('admin-budowa/', oznakowanieViews._panel_view, name='oznakowanie_public'),
    path('admin-budowa/login/', oznakowanieViews._login_view, name='oznakowanie_login'),
    path('admin-budowa/logout/', oznakowanieViews._logout_view, name='oznakowanie_logout'),
    path('admin-budowa/panel/', oznakowanieViews._panel_view, name='oznakowanie_panel'),
    path('admin-budowa/zmien-haslo/', oznakowanieViews._change_password_view, name='oznakowanie_change_password'),
    path('admin-budowa/zapomnialem-hasla/', oznakowanieViews._forgot_password_view, name='oznakowanie_forgot'),
    path('admin-budowa/podglad/<slug:slug>/', oznakowanieViews._preview_view, name='oznakowanie_preview'),
    path('admin-budowa/pobierz/<slug:slug>/', oznakowanieViews._download_view, name='oznakowanie_download'),
    path('admin-budowa/tablice/<str:board_type>/podglad/', oznakowanieViews._board_preview_view, name='board_preview'),
    path('admin-budowa/tablice/<str:board_type>/pobierz/', oznakowanieViews._board_download_view, name='board_download'),
]

from django.conf import settings
if settings.DEBUG:
    from django.shortcuts import render
    def test_404_view(request):
        return render(request, '404.html')
    urlpatterns.append(
        path('404/', test_404_view)
    )
