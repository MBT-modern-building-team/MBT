from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from MBTApp import mbt_orm


def home(request):
    """Strona główna — home/index.html."""
    lang = request.LANGUAGE_CODE
    projects = mbt_orm.get_projects(lang)
    data = {
        'workers': mbt_orm.get_workers(lang),
        'articles': mbt_orm.get_articles(lang),
        'projects': projects,
        'references': mbt_orm.get_references(lang),
        'sales_reps': mbt_orm.get_sales_reps(lang),
        'awards': mbt_orm.get_awards(),
    }
    return render(request, "home/index.html", data)


def about(request):
    context = {
        'title': _('O nas'),
        'subTitle': _('O nas'),
        'workers': mbt_orm.get_workers(request.LANGUAGE_CODE),
        'references': mbt_orm.get_references(request.LANGUAGE_CODE),
        'awards': mbt_orm.get_awards(),
    }
    return render(request, 'home/about.html', context)


def contact(request):
    data = {
        'title': _('Kontakt'),
        'subTitle': _('Kontakt'),
        'sales_reps': mbt_orm.get_sales_reps(request.LANGUAGE_CODE),
    }
    return render(request, 'home/contact.html', data)

def search(request):
    query = request.GET.get('q', '').strip().lower()
    lang = request.LANGUAGE_CODE
    
    context = {
        'title': _('Wyniki wyszukiwania'),
        'subTitle': _('Szukaj'),
        'query': query,
        'projects': [],
        'articles': [],
        'jobs': [],
    }
    
    if query:
        all_projects = mbt_orm.get_projects(lang)
        for p in all_projects:
            if query in (p.get('title') or '').lower() or query in (p.get('opis') or '').lower():
                context['projects'].append(p)
                
        all_articles = mbt_orm.get_articles(lang)
        for a in all_articles:
            if query in (a.get('title') or '').lower() or query in (a.get('text') or '').lower() or query in (a.get('excerpt_plain') or '').lower():
                context['articles'].append(a)
                
        all_jobs = mbt_orm.get_jobs(lang)
        for j in all_jobs:
            if query in (j.get('title') or '').lower() or query in (j.get('text') or '').lower():
                context['jobs'].append(j)
                
    return render(request, 'home/search_results.html', context)


def sitemap_html(request):
    lang = request.LANGUAGE_CODE
    context = {
        'title': _('Mapa witryny'),
        'subTitle': _('Mapa witryny'),
        'projects': mbt_orm.get_projects(lang),
        'articles': mbt_orm.get_articles(lang),
        'jobs': mbt_orm.get_jobs(lang),
    }
    return render(request, 'home/sitemap.html', context)