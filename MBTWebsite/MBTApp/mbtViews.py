from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from MBTApp import mbt_orm

PER_PAGE = 9  # 9 inwestycji na stronę — równa siatka 3x3 bez pustych pól


def _project_paras(project):
    """Podziel opis projektu na akapity.

    Opis uzupełniony z podstrony Potencjał i referencje ma na początku dwie linie (typ obiektu
    i parametry) — zostają w całości. Starą specyfikację (jeden blok) dzielimy po słowach kluczowych.
    """
    import re
    opis = (project.get('opis') or '').strip()
    if not opis:
        return []
    lines = [ln.strip() for ln in opis.splitlines() if ln.strip()]
    head, rest = (lines[:2], ' '.join(lines[2:])) if len(lines) >= 2 else ([], opis)
    parts = re.split(r'(?=(?:Specyfikacja|Powierzchnia|Certyfikacja|Układ budynku|Infrastruktura|Konstrukcja|Elewacja|Zagospodarowanie|Inwestor|Lokalizacja))', rest)
    return head + [p.strip() for p in parts if p.strip()]


def _card(project):
    """Kopia projektu z krótkim opisem do karty na liście (typ obiektu + początek parametrów)."""
    paras = _project_paras(project)
    text = paras[1] if len(paras) > 1 else ''
    if len(text) > 170:
        text = text[:170].rsplit(' ', 1)[0].rstrip(',;:') + '…'
    return dict(project, card_type=paras[0] if paras else '', card_text=text)


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
    page_obj.object_list = [_card(p) for p in page_obj.object_list]
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
    
    meta_desc = (project.get('opis') or project.get('text') or '').strip()
    if meta_desc:
        import re
        meta_desc = re.sub(r'\s+', ' ', meta_desc)[:160].strip()
    else:
        meta_desc = _("Inwestycja %(title)s zrealizowana przez generalnego wykonawcę MBT Modern Building Team.") % {'title': project.get('title')}
        
    data = {
        'title': project['title'],
        'meta_description': meta_desc,
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
    
    meta_desc = _("Oferta pracy: %(title)s w MBT Modern Building Team. Sprawdź wymagania i dołącz do naszego zespołu inżynierów.") % {'title': job['title']}
    data = {
        'title': job['title'],
        'meta_description': meta_desc,
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

def rodo(request):
    data = {
        'title': _('RODO'),
        'subTitle': _('RODO'),
    }
    return render(request, 'pages/rodo.html', data)