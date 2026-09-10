import fitz # PyMuPDF
doc = fitz.open("media/tablice_szablony/BIOZ.pdf")
pix = doc[0].get_pixmap(dpi=72)
pix.save("bioz_thumb.png")
