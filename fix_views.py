import re

path = 'Construz/MBTApp/oznakowanieViews.py'
with open(path, 'r') as f:
    code = f.read()

# 1. Remove _upload_logo_view
code = re.sub(r'def _upload_logo_view\(request, slug\):.*?return JsonResponse\(\{\'ok\': True\}\)\n', '', code, flags=re.DOTALL)

# 2. Modify _preview_view
preview_old = '''def _preview_view(request, slug):
    """Generuje podgląd banera (PNG) z nałożonym logo — zwraca obrazek."""
    from django.http import FileResponse, HttpResponseForbidden
    from io import BytesIO

    template = BannerTemplate.objects.filter(slug=slug, is_active=True).first()
    if not template:
        return HttpResponseForbidden('Szablon nie istnieje.')

    if not template.is_personalized:
        return FileResponse(template.template_image.open('rb'))

    logo_data = request.session.get(f'logo_{slug}')
    if not logo_data:
        # bez logo — zwróć sam szablon
        return FileResponse(template.template_image.open('rb'))

    logo_bytes = bytes.fromhex(logo_data['data'])
    base = apply_logo_to_template(template, logo_bytes)
    if not base:
        return FileResponse(template.template_image.open('rb'))

    buf = BytesIO()
    base.convert('RGB').save(buf, 'PNG', dpi=(300, 300))
    buf.seek(0)
    return FileResponse(buf, as_attachment=False, filename=f'preview_{slug}.png')'''

preview_new = '''def _preview_view(request, slug):
    """Generuje podgląd banera z nałożonym logo — zwraca obrazek."""
    from django.http import FileResponse, HttpResponseForbidden, HttpResponseBadRequest
    from io import BytesIO

    template = BannerTemplate.objects.filter(slug=slug, is_active=True).first()
    if not template:
        return HttpResponseForbidden('Szablon nie istnieje.')

    if not template.is_personalized:
        return FileResponse(template.template_image.open('rb'))

    logo_file = request.FILES.get('logo')
    if not logo_file:
        return HttpResponseBadRequest('Brak logo w żądaniu.')

    logo_bytes = logo_file.read()
    base = apply_logo_to_template(template, logo_bytes)
    if not base:
        return HttpResponseBadRequest('Błąd przetwarzania logo.')

    buf = BytesIO()
    # Generujemy mniejszy i szybszy plik JPEG do podglądu, max 1200px szerokości
    max_w = 1200
    if base.width > max_w:
        ratio = max_w / base.width
        new_h = int(base.height * ratio)
        from PIL import Image
        base = base.resize((max_w, new_h), Image.LANCZOS)

    base.convert('RGB').save(buf, 'JPEG', quality=85)
    buf.seek(0)
    return FileResponse(buf, content_type='image/jpeg')'''
code = code.replace(preview_old, preview_new)


# 3. Modify _download_view
download_old = '''def _download_view(request, slug):
    """Pobiera gotowy baner (PNG, 300 DPI) z nałożonym logo (lub oryginalny, jeśli niepersonalizowany)."""
    from django.http import FileResponse, HttpResponseForbidden
    from django.shortcuts import redirect
    from django.urls import reverse
    from django.contrib import messages
    from datetime import datetime
    from io import BytesIO
    import os

    template = BannerTemplate.objects.filter(slug=slug, is_active=True).first()
    if not template:
        return HttpResponseForbidden('Szablon nie istnieje.')

    if not template.is_personalized:
        # Direct download for general banners
        BannerDownload.objects.create(
            user=request.user,
            user_email=request.user.email or request.user.username,
            template=template,
            template_title_snapshot=template.title,
            ip_address=request.META.get('REMOTE_ADDR'),
            user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
        )
        # return original file
        filename = f'baner_{slug}.pdf' if template.template_image.name.lower().endswith('.pdf') else f'baner_{slug}.png'
        return FileResponse(template.template_image.open('rb'), as_attachment=True, filename=filename)

    logo_data = request.session.get(f'logo_{slug}')
    if not logo_data:
        messages.warning(request, 'Najpierw wgraj logo, aby pobrać baner.')
        return redirect(reverse('oznakowanie_panel'))

    logo_bytes = bytes.fromhex(logo_data['data'])
    base = apply_logo_to_template(template, logo_bytes)

    if not base:
        messages.error(request, 'Błąd podczas generowania banera.')
        return redirect(reverse('oznakowanie_panel'))

    buf = BytesIO()
    base.convert('RGB').save(buf, 'PNG', dpi=(300, 300))
    buf.seek(0)

    BannerDownload.objects.create(
        user=request.user,
        user_email=request.user.email or request.user.username,
        template=template,
        template_title_snapshot=template.title,
        ip_address=request.META.get('REMOTE_ADDR'),
        user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
    )

    filename = f'baner_{slug}_{datetime.now():%Y%m%d_%H%M%S}.png'
    return FileResponse(buf, as_attachment=True, filename=filename)'''

download_new = '''def _download_view(request, slug):
    """Pobiera gotowy baner (PNG, 300 DPI) z nałożonym logo (lub oryginalny, jeśli niepersonalizowany)."""
    from django.http import FileResponse, HttpResponseForbidden
    from django.shortcuts import redirect
    from django.urls import reverse
    from django.contrib import messages
    from datetime import datetime
    from io import BytesIO
    import os

    template = BannerTemplate.objects.filter(slug=slug, is_active=True).first()
    if not template:
        return HttpResponseForbidden('Szablon nie istnieje.')

    if not template.is_personalized:
        # Direct download for general banners
        BannerDownload.objects.create(
            user=request.user,
            user_email=request.user.email or request.user.username,
            template=template,
            template_title_snapshot=template.title,
            ip_address=request.META.get('REMOTE_ADDR'),
            user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
        )
        # return original file
        filename = f'baner_{slug}.pdf' if template.template_image.name.lower().endswith('.pdf') else f'baner_{slug}.png'
        return FileResponse(template.template_image.open('rb'), as_attachment=True, filename=filename)

    logo_file = request.FILES.get('logo')
    if not logo_file:
        messages.warning(request, 'Wybierz logo przed pobraniem.')
        return redirect(reverse('oznakowanie_panel'))

    logo_bytes = logo_file.read()
    base = apply_logo_to_template(template, logo_bytes)

    if not base:
        messages.error(request, 'Błąd podczas generowania banera. Sprawdź format pliku logo.')
        return redirect(reverse('oznakowanie_panel'))

    buf = BytesIO()
    base.convert('RGB').save(buf, 'PNG', dpi=(300, 300))
    buf.seek(0)

    BannerDownload.objects.create(
        user=request.user,
        user_email=request.user.email or request.user.username,
        template=template,
        template_title_snapshot=template.title,
        ip_address=request.META.get('REMOTE_ADDR'),
        user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
    )

    filename = f'baner_{slug}_{datetime.now():%Y%m%d_%H%M%S}.png'
    return FileResponse(buf, as_attachment=True, filename=filename)'''

code = code.replace(download_old, download_new)

with open(path, 'w') as f:
    f.write(code)
