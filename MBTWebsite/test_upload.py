import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MBT.settings')
django.setup()

from MBTApp.storage import save_uploaded_image
from django.core.files.uploadedfile import SimpleUploadedFile

with open('media/uploads/765a3c15eec4.png', 'rb') as f:
    upload = SimpleUploadedFile("test_img.png", f.read(), content_type="image/png")

import traceback
try:
    from MBTApp.storage import _r2_configured
    print("R2 Configured:", _r2_configured())
    res = save_uploaded_image(upload)
    print("Result:", res)
except Exception:
    traceback.print_exc()
