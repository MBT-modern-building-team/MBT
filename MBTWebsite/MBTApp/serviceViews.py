from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from MBTApp import mbt_orm


def service(request):
    lang = request.LANGUAGE_CODE
    projects = mbt_orm.get_projects(lang)
    completed = [p for p in projects if p.get('type') == 'realizacja-zrealizow'][:6]
    data = {
        'title': _('Oferta'),
        'subTitle': _('Oferta'),
        'completed': completed,
        'site': mbt_orm.get_site(lang),
        'breadcrumb': True,
    }
    return render(request, "service/service.html", data)


def generalContracting(request):
    """Landing: Generalne Wykonawstwo (Google Ads) — pełna sprzedażowa podstrona."""
    lang = request.LANGUAGE_CODE
    projects = mbt_orm.get_projects(lang)
    completed = [p for p in projects if p.get('type') == 'realizacja-zrealizow'][:6]
    articles = mbt_orm.get_articles(lang)[:3]
    data = {
        'title': _('Generalne Wykonawstwo'),
        'subTitle': _('Oferta'),
        'completed': completed,
        'articles': articles,
        'sectors': mbt_orm.get_sectors(lang),
        'sales_reps': mbt_orm.get_sales_reps(lang),
        'site': mbt_orm.get_site(lang),
        'breadcrumb': True,
    }
    return render(request, "service/generalContracting.html", data)


def halePrzemyslowe(request):
    lang = request.LANGUAGE_CODE
    projects = mbt_orm.get_projects(lang)
    completed = [p for p in projects if p.get('type') == 'realizacja-zrealizow'][:3]
    data = {
        'title': _('Hale Przemysłowe'),
        'subTitle': _('Oferta'),
        'completed': completed,
        'site': mbt_orm.get_site(lang),
        'breadcrumb': True,
    }
    return render(request, "service/hale_przemyslowe.html", data)


def haleMagazynowe(request):
    lang = request.LANGUAGE_CODE
    projects = mbt_orm.get_projects(lang)
    completed = [p for p in projects if p.get('type') == 'realizacja-zrealizow'][:3]
    data = {
        'title': _('Hale Magazynowe'),
        'subTitle': _('Oferta'),
        'completed': completed,
        'site': mbt_orm.get_site(lang),
        'breadcrumb': True,
    }
    return render(request, "service/hale_magazynowe.html", data)


def obiektyKomercyjne(request):
    lang = request.LANGUAGE_CODE
    projects = mbt_orm.get_projects(lang)
    completed = [p for p in projects if p.get('type') == 'realizacja-zrealizow'][:3]
    data = {
        'title': _('Obiekty Komercyjne'),
        'subTitle': _('Oferta'),
        'completed': completed,
        'site': mbt_orm.get_site(lang),
        'breadcrumb': True,
    }
    return render(request, "service/obiekty_komercyjne.html", data)


def sectorDetail(request, slug):
    lang = request.LANGUAGE_CODE
    projects = mbt_orm.get_projects(lang)
    completed = [p for p in projects if p.get('type') == 'realizacja-zrealizow'][:3]
    
    # Próba załadowania szablonu dedykowanego dla danego sektora
    template_name = f"service/sectors/{slug}.html"
    
    # Generujemy czytelny tytuł ze sluga np. 'konstrukcje-stalowe' -> 'Konstrukcje stalowe'
    readable_title = slug.replace('-', ' ').capitalize()
    
    data = {
        'title': readable_title,
        'subTitle': _('Oferta'),
        'completed': completed,
        'site': mbt_orm.get_site(lang),
        'breadcrumb': True,
    }
    
    from django.template.exceptions import TemplateDoesNotExist
    try:
        return render(request, template_name, data)
    except TemplateDoesNotExist:
        from django.http import Http404
        raise Http404(f"Template {template_name} not found")
