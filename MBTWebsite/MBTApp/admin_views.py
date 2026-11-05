"""Widoki administracyjne panelu CMS MBT.

Obsługa asynchronicznego przesyłania plików na Cloudflare R2 bezpośrednio
z widgetów formularzy (pojedyncze zdjęcia, galeria, wideo) w panelu admina.
"""
import logging
import os

from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from MBTApp.storage import (
    VIDEO_EXTENSIONS,
    generate_r2_presigned_upload_url,
    save_uploaded_image,
    save_uploaded_video,
)

logger = logging.getLogger(__name__)


@staff_member_required
@require_POST
def ajax_admin_upload_r2(request):
    """Asynchroniczny upload plików na Cloudflare R2 (bezpośredni lub przez serwer).

    Obsługuje 2 tryby:
    1. action='get_presigned_url': generuje presigned PUT URL dla dużych plików/filmów,
       co pozwala przeglądarce wgrywać pliki bezpośrednio na R2, omijając limit Vercel (4.5 MB).
    2. Bezpośrednie przesłanie pliku (dla mniejszych zdjęć i lokalnego dev).
    """
    action = request.POST.get('action')
    folder = request.POST.get('folder', 'uploads').strip('/')

    if action == 'get_presigned_url':
        filename = request.POST.get('filename', 'upload.bin')
        content_type = request.POST.get('content_type')
        try:
            upload_url, public_url, key, ctype = generate_r2_presigned_upload_url(
                filename=filename,
                folder=folder,
                content_type=content_type,
            )
            return JsonResponse({
                'success': True,
                'presigned': True,
                'upload_url': upload_url,
                'public_url': public_url,
                'content_type': ctype,
                'key': key,
            })
        except Exception as exc:
            logger.exception('Błąd podczas generowania presigned URL dla R2: %s', exc)
            return JsonResponse({'success': False, 'error': str(exc)}, status=500)

    uploaded_file = request.FILES.get('file')
    if not uploaded_file:
        return JsonResponse(
            {'success': False, 'error': 'Nie przesłano żadnego pliku (brak request.FILES["file"]).'},
            status=400,
        )

    folder = request.POST.get('folder', 'uploads').strip('/')
    ext = os.path.splitext(uploaded_file.name or '')[1].lower()

    try:
        if ext in VIDEO_EXTENSIONS:
            url = save_uploaded_video(uploaded_file, folder=folder, raise_on_error=True)
        else:
            url = save_uploaded_image(uploaded_file, folder=folder, raise_on_error=True)

        return JsonResponse({
            'success': True,
            'url': url,
            'filename': uploaded_file.name,
            'size': uploaded_file.size,
        })
    except Exception as exc:
        logger.exception('Błąd podczas uploadu na Cloudflare R2: %s', exc)
        err_msg = str(exc)
        if 'not allowed by policy' in err_msg or '403' in err_msg or 'Forbidden' in err_msg:
            err_msg = (
                'Cloudflare R2 odrzucił połączenie (błąd 403 Forbidden / not allowed by policy). '
                'Upewnij się, że token R2 w panelu Cloudflare ma uprawnienia "Admin Read & Write" '
                'oraz że klucze w .env są aktualne.'
            )
        return JsonResponse(
            {
                'success': False,
                'error': err_msg,
                'filename': uploaded_file.name,
            },
            status=500,
        )
