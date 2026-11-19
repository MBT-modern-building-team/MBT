"""Realizacje dodawane/usuwane razem z podstroną „Potencjał i referencje”.

Stałe w osobnym module (bez importów), żeby mbt_orm i portfolio mogły z nich korzystać bez cyklu.
Nakładka w mbt_orm pokazuje NEW_SLUGS (z mbt_data.PROJECTS) dopóki rekordu nie ma w CMS/bazie
(`manage.py sync_portfolio_projects` zapisuje je do CMS) i ukrywa REMOVED_SLUGS.
"""
import os


def page_is_public():
    """Czy podstrona /potencjal-i-referencje/ jest widoczna dla wszystkich.

    Domyślnie NIE (404 dla odwiedzających, brak w sitemapie). Włączenie: zmienna środowiskowa
    PORTFOLIO_PAGE_PUBLIC=1 (np. w Vercel). Poza tym widoczna wyłącznie lokalnie (DEBUG);
    na produkcji nie widzi jej nikt, także zalogowany personel.
    """
    return os.getenv('PORTFOLIO_PAGE_PUBLIC', '').strip().lower() in ('1', 'true', 'yes', 'on')


NEW_SLUGS = [
    'eurostyl-chelmek',
    'artus-aircraft',
    'centrum-sportow-rakietowych-ue-wroclaw',
    'stokado-gdansk',
    'kbh-akord-siemianowice-slaskie',
    'brembo-poland-dabrowa-gornicza',
    'invest-tdj-estate-zabrze-zielona-dolina-4',
]
REMOVED_SLUGS = ['venus-brzegi']
