import re

path = 'Construz/MBTApp/oznakowanieViews.py'
with open(path, 'r') as f:
    code = f.read()

func_old = '''def apply_logo_to_template(template, logo_bytes):
    try:
        from PIL import Image
    except ImportError:
        return None

    import os
    from io import BytesIO

    tmpl_path = template.template_image.path
    if not os.path.exists(tmpl_path):
        return None

    base = Image.open(tmpl_path).convert('RGBA')
    logo = Image.open(BytesIO(logo_bytes))
    if logo.mode != 'RGBA':
        logo = logo.convert('RGBA')'''

func_new = '''def apply_logo_to_template(template, logo_bytes):
    try:
        from PIL import Image
    except ImportError:
        return None

    import os
    from io import BytesIO
    import tempfile

    tmpl_path = template.template_image.path
    if not os.path.exists(tmpl_path):
        print(f"Error: Template path does not exist {tmpl_path}")
        return None

    try:
        base = Image.open(tmpl_path).convert('RGBA')
    except Exception as e:
        print(f"Error opening template {tmpl_path}: {e}")
        return None
        
    try:
        # Save SVG to temp if it's svg, but PIL still can't open it. 
        # So we just try opening with PIL, if it fails, we catch it.
        logo = Image.open(BytesIO(logo_bytes))
        if logo.mode != 'RGBA':
            logo = logo.convert('RGBA')
    except Exception as e:
        print(f"Error opening logo (unsupported format?): {e}")
        return None'''

if func_old in code:
    code = code.replace(func_old, func_new)
    with open(path, 'w') as f:
        f.write(code)
    print("Fixed apply_logo_to_template exceptions.")
else:
    print("Could not find func_old.")
