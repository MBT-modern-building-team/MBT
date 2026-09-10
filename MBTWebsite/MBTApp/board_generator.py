import os
from io import BytesIO
try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    pass
try:
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
except ImportError:
    pass

def generate_board(template_path, font_path, elements, is_bioz=False):
    reader = PdfReader(template_path)
    page = reader.pages[0]
    w_pt = float(page.mediabox.width)
    h_pt = float(page.mediabox.height)
    
    if is_bioz:
        scale_x = w_pt / (700 * 72 / 25.4)
        scale_y = h_pt / (700 * 72 / 25.4)
    else:
        scale_x = w_pt / (700 * 72 / 25.4)
        scale_y = h_pt / (1030 * 72 / 25.4)

    font_name = "SF-Pro"
    try:
        pdfmetrics.registerFont(TTFont(font_name, font_path))
    except Exception as e:
        print("Błąd czcionki:", e)
        return None

    overlay = BytesIO()
    c = canvas.Canvas(overlay, pagesize=(w_pt, h_pt))
    
    for el in elements:
        text = str(el.get('text', ''))
        if not text.strip():
            continue
            
        u_x = el['x']
        u_y = el['y']
        u_w = el['w']
        u_h = el['h']
        base_font_pt = el['font_size']
        
        x_pt = u_x * (72 / 25.4) * scale_x
        y_pt_top = u_y * (72 / 25.4) * scale_y
        w_pt_box = u_w * (72 / 25.4) * scale_x
        h_pt_box = u_h * (72 / 25.4) * scale_y
        
        y_pt = h_pt - y_pt_top - h_pt_box
        
        lines = text.split('\n')
        if len(lines) == 1 and 'alt_y' in el:
            text_w = pdfmetrics.stringWidth(lines[0], font_name, base_font_pt)
            if text_w > w_pt_box:
                words = lines[0].split(' ')
                line1, line2 = "", ""
                for i in range(len(words), 0, -1):
                    cand = " ".join(words[:i])
                    if pdfmetrics.stringWidth(cand, font_name, base_font_pt) <= w_pt_box:
                        line1 = cand
                        line2 = " ".join(words[i:])
                        break
                if not line1: 
                    line1 = lines[0]
                lines = [line1]
                if line2:
                    lines.append(line2)

        c.setFillColorRGB(0, 0, 0)
        
        if len(lines) == 2 and 'alt_y' in el:
            for idx, line in enumerate(lines):
                f_size = base_font_pt
                while f_size * 0.75 > h_pt_box * 0.85 and f_size > 10:
                    f_size -= 1
                while pdfmetrics.stringWidth(line, font_name, f_size) > w_pt_box and f_size > 10:
                    f_size -= 1
                    
                text_w = pdfmetrics.stringWidth(line, font_name, f_size)
                
                # Osobna logika horyzontalna: BIOZ - centrowanie, Informacyjna - do lewej + wcięcie (4 spacje)
                if is_bioz:
                    cx = x_pt + (w_pt_box - text_w) / 2.0
                else:
                    padding = pdfmetrics.stringWidth("    ", font_name, f_size)
                    cx = x_pt + padding
                
                if idx == 0:
                    c.setFont(font_name, f_size)
                    ascent = f_size * 0.72
                    c.drawString(cx, y_pt + (h_pt_box - ascent) / 2.0, line)
                else:
                    alt_y = el['alt_y'] * (72 / 25.4) * scale_y
                    alt_y_pt = h_pt - alt_y - h_pt_box
                    c.setFont(font_name, f_size)
                    ascent = f_size * 0.72
                    c.drawString(cx, alt_y_pt + (h_pt_box - ascent) / 2.0, line)
        else:
            for idx, line in enumerate(lines):
                f_size = base_font_pt
                
                while f_size * 0.75 > h_pt_box * 0.85 and f_size > 10:
                    f_size -= 1
                while pdfmetrics.stringWidth(line, font_name, f_size) > w_pt_box and f_size > 10:
                    f_size -= 1
                
                text_w = pdfmetrics.stringWidth(line, font_name, f_size)
                
                # Osobna logika horyzontalna: BIOZ - centrowanie, Informacyjna - do lewej + wcięcie (4 spacje)
                if is_bioz:
                    cx = x_pt + (w_pt_box - text_w) / 2.0
                else:
                    padding = pdfmetrics.stringWidth("    ", font_name, f_size)
                    cx = x_pt + padding
                
                c.setFont(font_name, f_size)
                ascent = f_size * 0.72
                ly = y_pt + (h_pt_box - ascent) / 2.0
                c.drawString(cx, ly, line)

    c.save()
    overlay.seek(0)
    
    overlay_reader = PdfReader(overlay)
    page.merge_page(overlay_reader.pages[0])
    
    writer = PdfWriter()
    writer.add_page(page)
    
    output = BytesIO()
    writer.write(output)
    output.seek(0)
    
    return output
