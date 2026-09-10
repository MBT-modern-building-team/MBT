import os
import pypdf.filters
pypdf.filters.MAX_DECLARED_STREAM_LENGTH = 500_000_000
from pypdf import PdfReader
reader = PdfReader('Construz/media/oznakowanie/szablony/baner_2x1_.pdf')
print("Successfully loaded PDF pages:", len(reader.pages))
