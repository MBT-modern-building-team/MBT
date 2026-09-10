import re

path = 'Construz/MBTApp/oznakowanieViews.py'
with open(path, 'r') as f:
    code = f.read()

new_func = '''def apply_logo_to_template(template, logo_bytes):
    import os
    from io import BytesIO
    
    tmpl_path = template.template_image.path
    if not os.path.exists(tmpl_path):
        return None, False
        
    is_pdf = tmpl_path.lower().endswith('.pdf')
    
    if is_pdf:
        try:
            from pypdf import PdfReader, PdfWriter
            from reportlab.pdfgen import canvas
            from reportlab.lib.utils import ImageReader
            
            reader = PdfReader(tmpl_path)
            if not reader.pages:
                return None, False
            page = reader.pages[0]
            
            pdf_width = float(page.mediabox.width)
            pdf_height = float(page.mediabox.height)

            if template.size == '200x100':
                cm_w, cm_h = 200.0, 100.0
                target_x_cm, target_y_cm = 122.49, 8.41
                target_w_cm, target_h_cm = 42.31, 39.51
            elif template.size == '300x100':
                cm_w, cm_h = 300.0, 100.0
                target_x_cm, target_y_cm = 172.49, 3.43
                target_w_cm, target_h_cm = 42.31, 39.51
            else:
                cm_w, cm_h = 200.0, 100.0
                target_x_cm, target_y_cm = 0, 0
                target_w_cm, target_h_cm = 40, 40

            pts_per_cm_x = pdf_width / cm_w
            pts_per_cm_y = pdf_height / cm_h

            logo_x = target_x_cm * pts_per_cm_x
            logo_y = pdf_height - (target_y_cm * pts_per_cm_y) - (target_h_cm * pts_per_cm_y)
            logo_w = target_w_cm * pts_per_cm_x
            logo_h = target_h_cm * pts_per_cm_y

            overlay_buf = BytesIO()
            c = canvas.Canvas(overlay_buf, pagesize=(pdf_width, pdf_height))
            
            # handle transparent PNG properly
            try:
                from PIL import Image
                logo_pil = Image.open(BytesIO(logo_bytes))
                if logo_pil.mode != 'RGBA':
                    logo_pil = logo_pil.convert('RGBA')
                # Save to a temporary buffer as PNG
                temp_logo = BytesIO()
                logo_pil.save(temp_logo, format='PNG')
                temp_logo.seek(0)
                logo_img = ImageReader(temp_logo)
            except Exception:
                # fallback
                logo_img = ImageReader(BytesIO(logo_bytes))
                
            c.drawImage(logo_img, logo_x, logo_y, width=logo_w, height=logo_h, mask='auto')
            c.save()
            overlay_buf.seek(0)

            overlay_reader = PdfReader(overlay_buf)
            overlay_page = overlay_reader.pages[0]
            page.merge_page(overlay_page)

            writer = PdfWriter()
            writer.add_page(page)
            
            output_buf = BytesIO()
            writer.write(output_buf)
            output_buf.seek(0)
            
            return output_buf, True
        except Exception as e:
            print(f"PDF overlay error: {e}")
            return None, False
    else:
        # Puste fallbacki dla obrazków (stary flow)
        try:
            from PIL import Image
            base = Image.open(tmpl_path).convert('RGBA')
            
            logo = Image.open(BytesIO(logo_bytes))
            if logo.mode != 'RGBA':
                logo = logo.convert('RGBA')

            bw, bh = base.size
            if template.size == '200x100':
                cm_w, cm_h = 200.0, 100.0
                target_x_cm, target_y_cm = 122.49, 8.41
                target_w_cm, target_h_cm = 42.31, 39.51
            elif template.size == '300x100':
                cm_w, cm_h = 300.0, 100.0
                target_x_cm, target_y_cm = 172.49, 3.43
                target_w_cm, target_h_cm = 42.31, 39.51
            else:
                cm_w, cm_h = 200.0, 100.0
                target_x_cm, target_y_cm = 0, 0
                target_w_cm, target_h_cm = 40, 40

            px_per_cm_x = bw / cm_w
            px_per_cm_y = bh / cm_h

            box_x = int(target_x_cm * px_per_cm_x)
            box_y = int(target_y_cm * px_per_cm_y)
            box_w = int(target_w_cm * px_per_cm_x)
            box_h = int(target_h_cm * px_per_cm_y)

            lw, lh = logo.size
            scale = min(box_w / lw, box_h / lh, 1.0)
            new_w, new_h = int(lw * scale), int(lh * scale)
            
            logo_resized = logo.resize((new_w, new_h), Image.LANCZOS)
            x_offset = box_x + (box_w - new_w) // 2
            y_offset = box_y + (box_h - new_h) // 2

            base.alpha_composite(logo_resized, (x_offset, y_offset))
            return base, False
        except Exception as e:
            print(f"Image overlay error: {e}")
            return None, False'''

# Replace apply_logo_to_template
# First, remove the old one (which spans to the end of the file or next function)
code = re.sub(r'def apply_logo_to_template\(template, logo_bytes\):.*?(?=\n\S|\Z)', new_func + '\n', code, flags=re.DOTALL)

# Update _preview_view
preview_old = '''    logo_bytes = logo_file.read()
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

preview_new = '''    logo_bytes = logo_file.read()
    result, is_pdf = apply_logo_to_template(template, logo_bytes)
    if not result:
        return HttpResponseBadRequest('Błąd przetwarzania logo.')

    if is_pdf:
        result.seek(0)
        return FileResponse(result, content_type='application/pdf')

    buf = BytesIO()
    max_w = 1200
    if result.width > max_w:
        ratio = max_w / result.width
        new_h = int(result.height * ratio)
        from PIL import Image
        result = result.resize((max_w, new_h), Image.LANCZOS)

    result.convert('RGB').save(buf, 'JPEG', quality=85)
    buf.seek(0)
    return FileResponse(buf, content_type='image/jpeg')'''

code = code.replace(preview_old, preview_new)

# Update _download_view
download_old = '''    logo_bytes = logo_file.read()
    base = apply_logo_to_template(template, logo_bytes)

    if not base:
        messages.error(request, 'Błąd podczas generowania banera. Sprawdź czy format logo jest poprawny (PNG/JPG).')
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

download_new = '''    logo_bytes = logo_file.read()
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

code = code.replace(download_old, download_new)

with open(path, 'w') as f:
    f.write(code)
