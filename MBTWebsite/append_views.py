with open('MBTApp/oznakowanieViews.py', 'a', encoding='utf-8') as f:
    f.write('''
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
        font_path = os.path.join(settings.MEDIA_ROOT, 'fonts', 'SF-Pro (1).ttf')
        
        elements = [
            {'text': request.POST.get('rozpoczecie', ''), 'x': 353.6, 'y': 255.8, 'w': 321.8, 'h': 50.5, 'font_size': 186.3},
            {'text': request.POST.get('zakonczenie', ''), 'x': 353.6, 'y': 341.2, 'w': 321.8, 'h': 50.5, 'font_size': 186.3},
            {'text': request.POST.get('maks_prac', ''), 'x': 21.7, 'y': 478.7, 'w': 654.1, 'h': 57.4, 'font_size': 186.3},
            {'text': request.POST.get('plan_bioz', ''), 'x': 250.2, 'y': 612.8, 'w': 425.2, 'h': 49.1, 'font_size': 186.3},
        ]
        return generate_board(template_path, font_path, elements, is_bioz=True)

    elif board_type == 'informacyjna':
        template_path = os.path.join(settings.MEDIA_ROOT, 'tablice_szablony', 'tablica_informacyjna.pdf')
        font_path = os.path.join(settings.MEDIA_ROOT, 'fonts', 'SF-Pro (1).ttf')
        
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
''')
