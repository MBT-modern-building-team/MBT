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

from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def uroczystosc(request):
    lang = request.LANGUAGE_CODE
    
    if request.method == 'POST':
        company = request.POST.get('company', '')
        contact_person = request.POST.get('contact_person', '')
        contact_info = request.POST.get('contact_info', '')
        location = request.POST.get('location', '')
        
        event_types = request.POST.getlist('event_type[]')
        event_type_other = request.POST.get('event_type_other', '')
        if 'Inne' in event_types and event_type_other:
            event_types.remove('Inne')
            event_types.append(f'Inne: {event_type_other}')
        
        event_date = request.POST.get('event_date', '')
        guests_count = request.POST.get('guests_count', '')
        seating = request.POST.get('seating', '')
        weather = request.POST.getlist('weather[]')
        
        investor_zone = request.POST.get('investor_zone', '')
        investor_tables = request.POST.get('investor_tables', '')
        if investor_zone == 'Tak' and investor_tables:
            investor_zone = f"Tak, {investor_tables} stołów"
            
        branding = request.POST.getlist('branding[]')
        media = request.POST.get('media', '')
        catering = request.POST.getlist('catering[]')
        audio = request.POST.getlist('audio[]')
        comments = request.POST.get('comments', '')
        
        subject = f"Nowe zapytanie o organizację uroczystości budowlanej: {company}"
        message_body = f"""
Formularz Organizacji Uroczystości Budowlanej – MBT

CZĘŚĆ 1: INFORMACJE PODSTAWOWE
Firma (Inwestor): {company}
Osoba kontaktowa: {contact_person}
Dane kontaktowe: {contact_info}
Lokalizacja: {location}

CZĘŚĆ 2: CHARAKTERYSTYKA WYDARZENIA
Rodzaj uroczystości: {', '.join(event_types)}
Data i godzina: {event_date}
Liczba uczestników: {guests_count}

CZĘŚĆ 3: LOGISTYKA, INFRASTRUKTURA I KOMFORT
Układ widowni: {seating}
Zabezpieczenie przed pogodą: {', '.join(weather)}
Strefa Inwestora: {investor_zone}

CZĘŚĆ 4: OPRAWA WIZUALNA, PR I MULTIMEDIA
Branding wydarzenia: {', '.join(branding)}
Obsługa medialna: {media}

CZĘŚĆ 5: USŁUGI DODATKOWE
Catering: {', '.join(catering)}
Oprawa dźwiękowa: {', '.join(audio)}

Uwagi dodatkowe:
{comments}
"""
        try:
            recipient = settings.SITE_EMAIL if hasattr(settings, 'SITE_EMAIL') else 'biuro@mbt.pl'
            send_mail(
                subject,
                message_body,
                settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'no-reply@mbt.pl',
                [recipient],
                fail_silently=False,
            )
            messages.success(request, _("Dziękujemy! Twój formularz został pomyślnie wysłany. Skontaktujemy się z Tobą wkrótce."))
        except Exception as e:
            messages.error(request, _(f"Wystąpił błąd podczas wysyłania formularza. Spróbuj ponownie lub skontaktuj się z nami bezpośrednio. (Szczegóły: {e})"))

    data = {
        'title': _('Uroczystość Rozpoczęcia Inwestycji'),
        'subTitle': _('Oferta'),
        'site': mbt_orm.get_site(lang),
        'breadcrumb': True,
    }
    return render(request, "service/uroczystosc.html", data)
