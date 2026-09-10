from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from MBTApp import mbt_orm

PER_PAGE = 9  # 9 inwestycji na stronę — równa siatka 3x3 bez pustych pól


def _project_paras(project):
    """Podziel opis projektu na akapity (specyfikacja z XML jest jednym blokiem)."""
    opis = (project.get('opis') or '').strip()
    if not opis:
        return []
    # rozbij po 'Specyfikacja', 'Powierzchnia', 'Certyfikacja' itd.
    import re
    parts = re.split(r'(?=(?:Specyfikacja|Powierzchnia|Certyfikacja|Układ budynku|Infrastruktura|Konstrukcja|Elewacja|Zagospodarowanie|Inwestor|Lokalizacja))', opis)
    return [p.strip() for p in parts if p.strip()]


def _enrich(project):
    p = dict(project)
    p['opis_paras'] = _project_paras(p)
    return p


def realizacje(request, page=1):
    """Lista realizacji z paginacją 1..4 (jak mbt.pl/realizacje)."""
    lang = request.LANGUAGE_CODE
    projects = mbt_orm.get_projects(lang)
    
    current_filter = request.GET.get('filter', 'all')
    if current_filter == 'completed':
        projects = [p for p in projects if p.get('type') == 'realizacja-zrealizow']
    elif current_filter == 'in-progress':
        projects = [p for p in projects if p.get('type') != 'realizacja-zrealizow']

    paginator = Paginator(projects, PER_PAGE)
    page_obj = paginator.get_page(page)
    data = {
        'title': _('Nasze realizacje'),
        'subTitle': _('Realizacje'),
        'page_obj': page_obj,
        'projects': page_obj.object_list,
        'is_paginated': paginator.num_pages > 1,
        'current_filter': current_filter,
    }
    return render(request, 'pages/project.html', data)


def realizacjaDetail(request, slug):
    lang = request.LANGUAGE_CODE
    project = mbt_orm.get_project_by_slug(slug, lang)
    if project is None:
        raise Http404(_("Realizacja nie istnieje"))
    project = _enrich(project)
    data = {
        'title': project['title'],
        'subTitle': _('Realizacje'),
        'project': project,
        'breadcrumb': True,
    }
    return render(request, 'pages/projectDetails.html', data)


def career(request):
    lang = request.LANGUAGE_CODE
    data = {
        'title': _('Kariera'),
        'subTitle': _('Kariera'),
        'jobs': mbt_orm.get_jobs(lang),
        'workers': mbt_orm.get_workers(lang),
    }
    return render(request, 'pages/career.html', data)


def careerDetail(request, slug):
    lang = request.LANGUAGE_CODE
    job = mbt_orm.get_job_by_slug(slug, lang)
    if job is None:
        raise Http404(_("Oferta nie istnieje"))
    job = dict(job)
    import re
    raw = job.get('text', '')
    parts = re.split(r'(?=(?:Twój zakres|Twoje zadania|Nasze wymagania|Oferujemy|Mile widziane|Wymagamy|Zakres obowiązków))', raw)
    lines = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if re.match(r'^(?:Twój zakres|Twoje zadania|Nasze wymagania|Oferujemy|Mile widziane|Wymagamy|Zakres obowiązków)', part):
            lines.append(part)
        else:
            items = [i.strip() for i in re.split(r'✓', part) if i.strip()]
            if len(items) > 1:
                lines.append(items[0])
                lines.extend([f'✓ {i}' for i in items[1:]])
            else:
                lines.append(part)
    job['lines'] = lines
    data = {
        'title': job['title'],
        'subTitle': _('Kariera'),
        'job': job,
        'jobs': mbt_orm.get_jobs(lang),
    }
    return render(request, 'pages/careerDetails.html', data)


def privacy(request):
    data = {
        'title': _('Polityka prywatności'),
        'subTitle': _('Polityka prywatności'),
    }
    return render(request, 'pages/privacy.html', data)