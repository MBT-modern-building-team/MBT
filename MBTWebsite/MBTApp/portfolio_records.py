"""Realizacje dodawane/usuwane razem z podstroną „Potencjał i referencje”.

Stałe w osobnym module (bez importów), żeby mbt_orm i portfolio mogły z nich korzystać bez cyklu.
Nakładka w mbt_orm pokazuje NEW_SLUGS (z mbt_data.PROJECTS) dopóki rekordu nie ma w CMS/bazie
(`manage.py sync_portfolio_projects` zapisuje je do CMS) i ukrywa REMOVED_SLUGS.
"""
NEW_SLUGS = [
    'eurostyl-chelmek',
    'stokado-gdansk',
    'kbh-akord-siemianowice-slaskie',
    'brembo-poland-dabrowa-gornicza',
    'invest-tdj-estate-zabrze-zielona-dolina-4',
]
REMOVED_SLUGS = ['venus-brzegi']
