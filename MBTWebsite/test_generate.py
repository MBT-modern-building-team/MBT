import os
from io import BytesIO
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import math

def generate_board(template_path, font_path, elements, out_path, is_bioz=False):
    reader = PdfReader(template_path)
    page = reader.pages[0]
    w_pt = float(page.mediabox.width)
    h_pt = float(page.mediabox.height)
    
    # Calculate scale factor if user coords were based on a different size
    if is_bioz:
        scale_x = w_pt / (700 * 72 / 25.4) # PDF is 800mm, user thought 700mm
        scale_y = h_pt / (700 * 72 / 25.4)
    else:
        scale_x = w_pt / (700 * 72 / 25.4) # PDF is 706mm, user thought 700mm
        scale_y = h_pt / (1030 * 72 / 25.4)

    # Register font
    font_name = "SF-Pro"
    try:
        pdfmetrics.registerFont(TTFont(font_name, font_path))
    except Exception as e:
        print("Font error:", e)
        return

    overlay = BytesIO()
    c = canvas.Canvas(overlay, pagesize=(w_pt, h_pt))
    
    for el in elements:
        text = el['text']
        
        # User coords in mm
        u_x = el['x']
        u_y = el['y']
        u_w = el['w']
        u_h = el['h']
        base_font_pt = el['font_size']
        
        # Convert to points and scale to PDF size
        x_pt = u_x * (72 / 25.4) * scale_x
        y_pt_top = u_y * (72 / 25.4) * scale_y
        w_pt_box = u_w * (72 / 25.4) * scale_x
        h_pt_box = u_h * (72 / 25.4) * scale_y
        
        # In reportlab, y is from bottom
        y_pt = h_pt - y_pt_top - h_pt_box
        
        # Draw bounding box for debugging
        # c.setStrokeColorRGB(1, 0, 0)
        # c.rect(x_pt, y_pt, w_pt_box, h_pt_box)
        
        # Multi-line handling
        lines = text.split('\n')
        if len(lines) == 1 and 'alt_y' in el:
            # check if fits in one line
            text_w = pdfmetrics.stringWidth(lines[0], font_name, base_font_pt)
            if text_w > w_pt_box:
                # split by space
                words = lines[0].split(' ')
                line1, line2 = "", ""
                for i in range(len(words), 0, -1):
                    cand = " ".join(words[:i])
                    if pdfmetrics.stringWidth(cand, font_name, base_font_pt) <= w_pt_box:
                        line1 = cand
                        line2 = " ".join(words[i:])
                        break
                if not line1: 
                    line1 = lines[0] # Too long anyway
                lines = [line1]
                if line2:
                    lines.append(line2)

        # Draw lines
        c.setFillColorRGB(0, 0, 0)
        
        if len(lines) == 2 and 'alt_y' in el:
            # We have specific coords for the second line
            for idx, line in enumerate(lines):
                if idx == 0:
                    c.setFont(font_name, base_font_pt)
                    # Vertically center text in its box
                    ascent = base_font_pt * 0.75 # approx
                    c.drawString(x_pt, y_pt + (h_pt_box - ascent) / 2.0, line)
                else:
                    alt_y = el['alt_y'] * (72 / 25.4) * scale_y
                    alt_y_pt = h_pt - alt_y - h_pt_box
                    c.setFont(font_name, base_font_pt)
                    ascent = base_font_pt * 0.75
                    c.drawString(x_pt, alt_y_pt + (h_pt_box - ascent) / 2.0, line)
        else:
            # Single line (or multi without specific alt_y -> shrink to fit)
            for idx, line in enumerate(lines):
                # Auto shrink
                f_size = base_font_pt
                while pdfmetrics.stringWidth(line, font_name, f_size) > w_pt_box and f_size > 10:
                    f_size -= 1
                
                c.setFont(font_name, f_size)
                ascent = f_size * 0.75
                # draw
                ly = y_pt + (h_pt_box - ascent) / 2.0
                c.drawString(x_pt, ly, line)

    c.save()
    overlay.seek(0)
    
    overlay_reader = PdfReader(overlay)
    page.merge_page(overlay_reader.pages[0])
    
    writer = PdfWriter()
    writer.add_page(page)
    with open(out_path, "wb") as f:
        writer.write(f)
    print(f"Generated {out_path}")

bioz_el = [
    {'text': '12.10.2026', 'x': 353.6, 'y': 255.8, 'w': 321.8, 'h': 50.5, 'font_size': 186.3},
    {'text': '15.08.2028', 'x': 353.6, 'y': 341.2, 'w': 321.8, 'h': 50.5, 'font_size': 186.3},
    {'text': '150', 'x': 21.7, 'y': 478.7, 'w': 654.1, 'h': 57.4, 'font_size': 186.3},
    {'text': 'W BIURZE KIER. BUD.', 'x': 250.2, 'y': 612.8, 'w': 425.2, 'h': 49.1, 'font_size': 186.3},
]

info_el = [
    {'text': 'BUDOWA HALI MAGAZYNOWEJ Z CZĘŚCIĄ SOCJALNĄ', 'x': 211.9, 'y': 217.9, 'w': 463.5, 'h': 61.7, 'font_size': 216},
    {'text': 'UL. PRZYKŁADOWA 12, 00-123 WARSZAWA', 'x': 169.2, 'y': 285.4, 'w': 506.2, 'h': 60.4, 'font_size': 216},
    {'text': 'DEC. NR 123/2026 Z 10.01.2026', 'x': 24.6, 'y': 415.2, 'w': 650.8, 'h': 63.7, 'font_size': 216},
    {'text': 'STAROSTA POWIATOWY', 'x': 23.9, 'y': 548.7, 'w': 651.5, 'h': 58.1, 'font_size': 216},
    {'text': 'POWIATOWY INSPEKTOR NADZORU BUDOWLANEGO W WARSZAWIE', 'x': 308.4, 'y': 622.3, 'w': 367.0, 'h': 57.7, 'font_size': 216, 'alt_y': 691.6},
    {'text': 'JAN KOWALSKI, UL. KOWALSKA 1, WARSZAWA', 'x': 246.0, 'y': 752.9, 'w': 429.4, 'h': 62.1, 'font_size': 216, 'alt_y': 827.1},
    {'text': 'MGR INŻ. ADAM NOWAK', 'x': 327.8, 'y': 884.3, 'w': 347.6, 'h': 62.4, 'font_size': 216},
]

generate_board("media/tablice_szablony/BIOZ.pdf", "media/fonts/SF-Pro (1).ttf", bioz_el, "test_bioz.pdf", is_bioz=True)
generate_board("media/tablice_szablony/tablica_informacyjna.pdf", "media/fonts/SF-Pro (1).ttf", info_el, "test_info.pdf", is_bioz=False)
