path = 'Construz/MBTApp/oznakowanieViews.py'
with open(path, 'r') as f:
    code = f.read()

import re

# Find the logo_file section in _download_view
pattern = r"    logo_bytes = logo_file\.read\(\)\n    base = apply_logo_to_template\(template, logo_bytes\).*?return FileResponse\(buf, as_attachment=True, filename=filename\)"

new_code = '''    logo_bytes = logo_file.read()
    result, is_pdf = apply_logo_to_template(template, logo_bytes)

    if not result:
        messages.error(request, 'Błąd podczas generowania banera. Sprawdź czy format logo jest poprawny (PNG/JPG).')
        return redirect(reverse('oznakowanie_panel'))

    BannerDownload.objects.create(
        user=request.user,
        user_email=request.user.email or request.user.username,
        template=template,
        template_title_snapshot=template.title,
        ip_address=request.META.get('REMOTE_ADDR'),
        user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
    )

    if is_pdf:
        filename = f'baner_{slug}_{datetime.now():%Y%m%d_%H%M%S}.pdf'
        result.seek(0)
        return FileResponse(result, as_attachment=True, filename=filename)
    else:
        buf = BytesIO()
        result.convert('RGB').save(buf, 'PNG', dpi=(300, 300))
        buf.seek(0)
        filename = f'baner_{slug}_{datetime.now():%Y%m%d_%H%M%S}.png'
        return FileResponse(buf, as_attachment=True, filename=filename)'''

code = re.sub(pattern, new_code, code, flags=re.DOTALL)

with open(path, 'w') as f:
    f.write(code)
