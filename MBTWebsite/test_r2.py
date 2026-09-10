import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MBT.settings')
django.setup()
from MBTApp.storage import _upload_to_r2, _r2_configured
print("R2 configured?", _r2_configured())
try:
    _upload_to_r2('uploads/test_test.png', b'hello', 'image/png')
    print("Success")
except Exception as e:
    import traceback
    traceback.print_exc()
