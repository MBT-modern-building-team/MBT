path = 'Construz/MBTApp/oznakowanieViews.py'
with open(path, 'r') as f:
    code = f.read()

import re

# Find the block where pypdf is imported
pattern = r"            from pypdf import PdfReader, PdfWriter\n            from reportlab\.pdfgen import canvas"

new_code = '''            from pypdf import PdfReader, PdfWriter, filters
            from reportlab.pdfgen import canvas
            
            # Zwiększamy limity pypdf dla ogromnych plików do druku (do 1GB)
            filters.MAX_DECLARED_STREAM_LENGTH = 1_000_000_000
            filters.MAX_ARRAY_BASED_STREAM_OUTPUT_LENGTH = 1_000_000_000
            filters.JBIG2_MAX_OUTPUT_LENGTH = 1_000_000_000
            filters.LZW_MAX_OUTPUT_LENGTH = 1_000_000_000
            filters.RUN_LENGTH_MAX_OUTPUT_LENGTH = 1_000_000_000
            filters.ZLIB_MAX_OUTPUT_LENGTH = 1_000_000_000
            filters.ZLIB_MAX_RECOVERY_INPUT_LENGTH = 1_000_000_000
            filters.FLATE_MAX_BUFFER_SIZE = 1_000_000_000'''

if "filters.MAX_DECLARED_STREAM_LENGTH" not in code:
    code = re.sub(pattern, new_code, code)

    with open(path, 'w') as f:
        f.write(code)
    print("Limits patched.")
else:
    print("Limits already patched.")
