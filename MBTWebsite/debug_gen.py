from pypdf import PdfReader
from reportlab.pdfbase.ttfonts import TTFont

def debug_pdf(path):
    reader = PdfReader(path)
    box = reader.pages[0].mediabox
    print(f"{path}: {box}")

debug_pdf("media/tablice_szablony/BIOZ.pdf")
debug_pdf("media/tablice_szablony/tablica_informacyjna.pdf")

try:
    font = TTFont("SF-Pro", "media/fonts/SF-Pro (1).ttf")
    print(f"Font loaded: {font.face.name}, {font.face.familyName}")
except Exception as e:
    print(f"Font error: {e}")
