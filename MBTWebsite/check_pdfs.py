from pypdf import PdfReader
import sys

def check_pdf(path):
    try:
        reader = PdfReader(path)
        box = reader.pages[0].mediabox
        w_pt = float(box.width)
        h_pt = float(box.height)
        w_mm = w_pt * 25.4 / 72.0
        h_mm = h_pt * 25.4 / 72.0
        print(f"{path}: {w_pt:.1f}x{h_pt:.1f} pt ({w_mm:.1f}x{h_mm:.1f} mm)")
    except Exception as e:
        print(f"Error checking {path}: {e}")

check_pdf("media/tablice_szablony/BIOZ.pdf")
check_pdf("media/tablice_szablony/tablica_informacyjna.pdf")
