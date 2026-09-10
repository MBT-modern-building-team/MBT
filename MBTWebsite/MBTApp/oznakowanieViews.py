"""Panel Oznakowanie Budowy — kierownicy pobierają banery z wgranym logo."""
import io
import os
import uuid
from datetime import datetime
from io import BytesIO

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import FileResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _

from MBTApp.models import BannerDownload, BannerTemplate, UserProfile

# Lazy PIL (Pillow nie jest w .venv Django — używamy hermes-agent venv przez subprocess)
# Na serwerze deweloperskim importujemy PIL; w razie braku zwrócimy fallback.


def _login_view(request):
    """Logowanie do panelu. Wymusza zmianę hasła jeśli must_change_password."""
    lang = request.LANGUAGE_CODE
    # już zalogowany?
    if request.user.is_authenticated:
        return redirect('oznakowanie_panel')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        pwd = request.POST.get('password', '')
        user = authenticate(request, username=username, password=pwd)
        if user is None:
            return render(request, 'oznakowanie/login.html', {
                'error': _('Nieprawidłowy email lub hasło.'),
                'username': username,
                'lang': lang,
            }, status=401)
        if not user.is_active:
            return render(request, 'oznakowanie/login.html', {
                'error': _('Konto jest wyłączone. Skontaktuj się z administratorem.'),
                'username': username,
                'lang': lang,
            }, status=403)
        login(request, user)
        # czy musi zmienić hasło?
        profile = getattr(user, 'profile', None)
        if profile and profile.must_change_password:
            return redirect('oznakowanie_change_password')
        return redirect('oznakowanie_panel')
    return render(request, 'oznakowanie/login.html', {'lang': lang})


def _logout_view(request):
    logout(request)
    return redirect('oznakowanie_login')


@login_required
def _change_password_view(request):
    """Wymuszenie zmiany hasła przy pierwszym logowaniu."""
    lang = request.LANGUAGE_CODE
    user = request.user
    profile = getattr(user, 'profile', None)
    if request.method == 'POST':
        new_pwd = request.POST.get('new_password', '')
        new_pwd2 = request.POST.get('new_password2', '')
        if not new_pwd or len(new_pwd) < 8:
            return render(request, 'oznakowanie/change_password.html', {
                'error': _('Hasło musi mieć minimum 8 znaków.'),
                'must_change': profile.must_change_password if profile else False,
                'lang': lang,
            }, status=400)
        if new_pwd != new_pwd2:
            return render(request, 'oznakowanie/change_password.html', {
                'error': _('Hasła nie są identyczne.'),
                'must_change': profile.must_change_password if profile else False,
                'lang': lang,
            }, status=400)
        user.set_password(new_pwd)
        user.save()
        if profile:
            profile.must_change_password = False
            profile.last_password_change = timezone.now()
            profile.save()
        update_session_auth_hash(request, user)
        messages.success(request, _('Hasło zostało zmienione.'))
        return redirect('oznakowanie_panel')
    return render(request, 'oznakowanie/change_password.html', {
        'must_change': profile.must_change_password if profile else False,
        'lang': lang,
    })


def _forgot_password_view(request):
    """Zapomniałeś hasła — wyświetla komunikat (bez SMTP, hasło resetuje admin)."""
    lang = request.LANGUAGE_CODE
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            # sprawdź czy user istnieje
            User.objects.filter(username=email).exists()  # info tylko
        # zawsze pokazuj ten sam komunikat (security)
        return render(request, 'oznakowanie/forgot_password_done.html', {
            'lang': lang,
        })
    return render(request, 'oznakowanie/forgot_password.html', {'lang': lang})


@login_required
def _panel_view(request):
    """Główny panel — podział na ogólne i personalizowane."""
    lang = request.LANGUAGE_CODE
    general_templates = BannerTemplate.objects.filter(is_active=True, is_personalized=False).order_by('order', 'id')
    personalized_templates = BannerTemplate.objects.filter(is_active=True, is_personalized=True).order_by('order', 'id')

    my_downloads = BannerDownload.objects.filter(
        user=request.user
    ).select_related('template')[:20]

    return render(request, 'oznakowanie/panel.html', {
        'general_templates': general_templates,
        'personalized_templates': personalized_templates,
        'my_downloads': my_downloads,
        'lang': lang,
    })


def _public_view(request):
    """Publiczny widok /oznakowanie-budowy/ — bez logowania.
    Pokazuje listę szablonów i CTA 'Zaloguj się aby pobrać'."""
    lang = request.LANGUAGE_CODE
    templates = BannerTemplate.objects.filter(is_active=True).order_by('order', 'id')
    return render(request, 'oznakowanie/public.html', {
        'templates': templates,
        'lang': lang,
    })


def apply_logo_to_template(template, logo_bytes, billboard_text=''):
    import os
    from io import BytesIO
    
    tmpl_path = template.template_image.path
    if not os.path.exists(tmpl_path):
        return None, False
        
    is_pdf = tmpl_path.lower().endswith('.pdf')
    
    if is_pdf:
        try:
            from pypdf import PdfReader, PdfWriter, filters
            from reportlab.pdfgen import canvas
            from reportlab.pdfbase import pdfmetrics
            from reportlab.pdfbase.ttfonts import TTFont
            from django.conf import settings
            
            # Zwiększamy limity pypdf dla ogromnych plików do druku (do 1GB)
            filters.MAX_DECLARED_STREAM_LENGTH = 1_000_000_000
            filters.MAX_ARRAY_BASED_STREAM_OUTPUT_LENGTH = 1_000_000_000
            filters.JBIG2_MAX_OUTPUT_LENGTH = 1_000_000_000
            filters.LZW_MAX_OUTPUT_LENGTH = 1_000_000_000
            filters.RUN_LENGTH_MAX_OUTPUT_LENGTH = 1_000_000_000
            filters.ZLIB_MAX_OUTPUT_LENGTH = 1_000_000_000
            filters.ZLIB_MAX_RECOVERY_INPUT_LENGTH = 1_000_000_000
            filters.FLATE_MAX_BUFFER_SIZE = 1_000_000_000
            from reportlab.lib.utils import ImageReader
            
            reader = PdfReader(tmpl_path)
            if not reader.pages:
                return None, False
            page = reader.pages[0]
            
            pdf_width = float(page.mediabox.width)
            pdf_height = float(page.mediabox.height)

            if template.size in ['200x100', '200x100_apology']:
                cm_w, cm_h = 200.0, 100.0
                target_x_cm, target_y_cm = 128.07, 12.28
                target_w_cm, target_h_cm = 31.03, 28.96
            elif template.size == '300x100_apology':
                cm_w, cm_h = 300.0, 100.0
                target_x_cm, target_y_cm = 187.85, 5.76
                target_w_cm, target_h_cm = 41.11, 38.37
            elif template.size == '300x100':
                cm_w, cm_h = 300.0, 100.0
                target_x_cm, target_y_cm = 187.85, 10.14
                target_w_cm, target_h_cm = 41.11, 38.37
            elif template.size == '600x200_billboard':
                cm_w, cm_h = 600.0, 200.0
                target_x_cm = 420.7
                # User's y=30.17 is from the bottom. Convert to top-left target_y_cm:
                # 200 - 30.17 - 143.98 = 25.85 cm from top.
                target_y_cm = 25.85
                target_w_cm, target_h_cm = 154.26, 143.98
            elif template.size.startswith('znak_'):
                cm_w, cm_h = 29.7, 21.0
                target_x_cm, target_y_cm = 18.82, 4.73
                target_w_cm, target_h_cm = 6.75, 4.71
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

            # Draw billboard text
            if template.size == '600x200_billboard' and billboard_text:
                try:
                    font_name = 'Technor-Bold'
                    font_path = os.path.join(settings.MEDIA_ROOT, 'fonts', 'Technor-Bold.ttf')
                    if os.path.exists(font_path):
                        pdfmetrics.registerFont(TTFont(font_name, font_path))
                    else:
                        font_name = 'Helvetica-Bold' # fallback
                        font_path_alt = os.path.join(settings.MEDIA_ROOT, 'fonts', 'SF-Pro (1).ttf')
                        if os.path.exists(font_path_alt):
                            pdfmetrics.registerFont(TTFont('SF-Pro-Bold', font_path_alt))
                            font_name = 'SF-Pro-Bold'

                    font_size_pt = 438.3
                    c.setFont(font_name, font_size_pt)
                    
                    full_text = billboard_text.upper()
                    
                    text_x_cm, text_y_cm = 119.7, 149.84 # User's coords (y from bottom)
                    text_w_cm, text_h_cm = 179.17, 15.84
                    
                    max_w_pt = text_w_cm * pts_per_cm_x
                    text_w_pt = pdfmetrics.stringWidth(full_text, font_name, font_size_pt)
                    
                    if text_w_pt > max_w_pt:
                        font_size_pt = font_size_pt * (max_w_pt / text_w_pt)
                        c.setFont(font_name, font_size_pt)
                    
                    text_x = text_x_cm * pts_per_cm_x
                    # y from bottom is text_y_cm. Adjust slightly for baseline vs bounding box.
                    text_y = text_y_cm * pts_per_cm_y
                    
                    c.setFillColorRGB(236/255.0, 101/255.0, 47/255.0) # #EC652F
                    c.drawString(text_x, text_y, full_text)
                except Exception as e:
                    print(f"Error drawing billboard text: {e}")

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
            from PIL import Image, ImageDraw, ImageFont
            from django.conf import settings
            base = Image.open(tmpl_path).convert('RGBA')
            
            logo = Image.open(BytesIO(logo_bytes))
            if logo.mode != 'RGBA':
                logo = logo.convert('RGBA')

            bw, bh = base.size
            if template.size in ['200x100', '200x100_apology']:
                cm_w, cm_h = 200.0, 100.0
                target_x_cm, target_y_cm = 128.07, 12.28
                target_w_cm, target_h_cm = 31.03, 28.96
            elif template.size == '300x100_apology':
                cm_w, cm_h = 300.0, 100.0
                target_x_cm, target_y_cm = 187.85, 5.76
                target_w_cm, target_h_cm = 41.11, 38.37
            elif template.size == '300x100':
                cm_w, cm_h = 300.0, 100.0
                target_x_cm, target_y_cm = 187.85, 10.14
                target_w_cm, target_h_cm = 41.11, 38.37
            elif template.size == '600x200_billboard':
                cm_w, cm_h = 600.0, 200.0
                target_x_cm = 420.7
                target_y_cm = 25.85 # 200 - 30.17(from bottom) - 143.98
                target_w_cm, target_h_cm = 154.26, 143.98
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

            if template.size == '600x200_billboard' and billboard_text:
                draw = ImageDraw.Draw(base)
                
                font_path = os.path.join(settings.MEDIA_ROOT, 'fonts', 'Technor-Bold.ttf')
                if not os.path.exists(font_path):
                    font_path = os.path.join(settings.MEDIA_ROOT, 'fonts', 'SF-Pro (1).ttf')
                
                try:
                    font_size_px = int(438.3 * (px_per_cm_y / 28.346)) # approx scaling from pt to px
                    font = ImageFont.truetype(font_path, font_size_px)
                except:
                    font = ImageFont.load_default()
                    font_size_px = 40
                
                full_text = billboard_text.upper()
                
                text_w_cm, text_h_cm = 179.17, 15.84
                max_w_px = int(text_w_cm * px_per_cm_x)
                
                if hasattr(font, 'getbbox'):
                    bbox = font.getbbox(full_text)
                    text_w_px = bbox[2] - bbox[0]
                else:
                    text_w_px = draw.textlength(full_text, font=font)
                
                if text_w_px > max_w_px:
                    scale_factor = max_w_px / text_w_px
                    font_size_px = int(font_size_px * scale_factor)
                    try:
                        font = ImageFont.truetype(font_path, font_size_px)
                    except:
                        pass
                
                text_x_cm, text_y_bl = 119.7, 149.84 # User's coords (y from bottom)
                # Convert Bottom-Left to Top-Left for PIL
                text_y_tl = 200.0 - text_y_bl - text_h_cm
                
                text_x = int(text_x_cm * px_per_cm_x)
                text_y = int(text_y_tl * px_per_cm_y)
                
                draw.text((text_x, text_y), full_text, font=font, fill=(236, 101, 47, 255))

            return base, False
        except Exception as e:
            print(f"Image overlay error: {e}")
            return None, False

@login_required
def _preview_view(request, slug):
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
    billboard_text = request.POST.get('billboard_text', '')
    result, is_pdf = apply_logo_to_template(template, logo_bytes, billboard_text=billboard_text)
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

    if result.mode in ('RGBA', 'LA') or (result.mode == 'P' and 'transparency' in result.info):
        bg = Image.new('RGB', result.size, (255, 255, 255))
        if result.mode == 'RGBA':
            bg.paste(result, mask=result.split()[3])
        else:
            bg.paste(result.convert('RGBA'), mask=result.convert('RGBA').split()[3])
        result = bg
    else:
        result = result.convert('RGB')

    result.save(buf, 'JPEG', quality=85)
    buf.seek(0)
    return FileResponse(buf, content_type='image/jpeg')

@login_required
def _download_view(request, slug):
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
    billboard_text = request.POST.get('billboard_text', '')
    result, is_pdf = apply_logo_to_template(template, logo_bytes, billboard_text=billboard_text)

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
        result.save(buf, 'PNG', dpi=(300, 300))
        buf.seek(0)
        filename = f'baner_{slug}_{datetime.now():%Y%m%d_%H%M%S}.png'
        return FileResponse(buf, as_attachment=True, filename=filename)

# --- Tablice budowlane (BIOZ, Informacyjna) ---
from MBTApp.board_generator import generate_board

def _handle_board_generation(request, board_type):
    """
    Pomocnicza funkcja generująca BytesIO z PDF dla podglądu lub pobrania.
    board_type: 'bioz' lub 'informacyjna'
    """
    import os
    from django.conf import settings
    if board_type == 'bioz':
        template_path = os.path.join(settings.MEDIA_ROOT, 'tablice_szablony', 'BIOZ.pdf')
        font_path = os.path.join(settings.MEDIA_ROOT, 'fonts', 'SF-Pro-Compressed-Heavy.ttf')
        
        elements = [
            {'text': request.POST.get('rozpoczecie', ''), 'x': 353.6, 'y': 255.8, 'w': 321.8, 'h': 50.5, 'font_size': 186.3},
            {'text': request.POST.get('zakonczenie', ''), 'x': 353.6, 'y': 341.2, 'w': 321.8, 'h': 50.5, 'font_size': 186.3},
            {'text': request.POST.get('maks_prac', ''), 'x': 21.7, 'y': 478.7, 'w': 654.1, 'h': 57.4, 'font_size': 186.3},
            {'text': request.POST.get('plan_bioz', ''), 'x': 250.2, 'y': 612.8, 'w': 425.2, 'h': 49.1, 'font_size': 186.3},
        ]
        return generate_board(template_path, font_path, elements, is_bioz=True)

    elif board_type == 'informacyjna':
        template_path = os.path.join(settings.MEDIA_ROOT, 'tablice_szablony', 'tablica_informacyjna.pdf')
        font_path = os.path.join(settings.MEDIA_ROOT, 'fonts', 'SF-Pro-Compressed-Heavy.ttf')
        
        elements = [
            {'text': request.POST.get('budowa', ''), 'x': 211.9, 'y': 217.9, 'w': 463.5, 'h': 61.7, 'font_size': 216},
            {'text': request.POST.get('adres', ''), 'x': 169.2, 'y': 285.4, 'w': 506.2, 'h': 60.4, 'font_size': 216},
            {'text': request.POST.get('data_pozwolenia', ''), 'x': 24.6, 'y': 415.2, 'w': 650.8, 'h': 63.7, 'font_size': 216},
            {'text': request.POST.get('organ', ''), 'x': 23.9, 'y': 548.7, 'w': 651.5, 'h': 58.1, 'font_size': 216},
            {'text': request.POST.get('nadzor', ''), 'x': 308.4, 'y': 622.3, 'w': 367.0, 'h': 57.7, 'font_size': 216, 'alt_y': 691.6},
            {'text': request.POST.get('inwestor', ''), 'x': 246.0, 'y': 752.9, 'w': 429.4, 'h': 62.1, 'font_size': 216, 'alt_y': 827.1},
            {'text': request.POST.get('kierownik', ''), 'x': 327.8, 'y': 884.3, 'w': 347.6, 'h': 62.4, 'font_size': 216},
        ]
        return generate_board(template_path, font_path, elements, is_bioz=False)

    return None

@login_required(login_url='oznakowanie_login')
def _board_preview_view(request, board_type):
    if request.method != 'POST':
        return HttpResponseForbidden()
    
    result = _handle_board_generation(request, board_type)
    if not result:
        return JsonResponse({'error': 'Błąd generowania tablicy'}, status=400)
        
    return FileResponse(result, content_type='application/pdf')

@login_required(login_url='oznakowanie_login')
def _board_download_view(request, board_type):
    if request.method != 'POST':
        return HttpResponseForbidden()
        
    result = _handle_board_generation(request, board_type)
    if not result:
        from django.contrib import messages
        messages.error(request, 'Błąd podczas generowania tablicy.')
        return redirect(reverse('oznakowanie_panel'))
        
    from datetime import datetime
    filename = f"tablica_{board_type}_{datetime.now():%Y%m%d_%H%M%S}.pdf"
    return FileResponse(result, as_attachment=True, filename=filename)
