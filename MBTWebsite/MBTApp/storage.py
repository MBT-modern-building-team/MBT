"""Zapisywanie wgrywanych zdjęć — Cloudflare R2 + kompresja WebP.

Strategia (kolejność):
1. Jeśli ustawione zmienne R2 (R2_ACCOUNT_ID + R2_ACCESS_KEY_ID) — zdjęcie
   jest kompresowane do WebP (max ~1920px, jakość 82) i wgrywane na R2.
   Zwracamy pełny publiczny URL (https://pub-....r2.dev/...).
2. W przeciwnym razie (lokalny dev bez kluczy) — zapis do MEDIA_ROOT/uploads/,
   zwracamy względną ścieżkę /media/uploads/... (serwowaną przez urls.py w DEBUG).

Kompresja: oryginalne zdjęcia z aparatu ważą 13-68 MB — po konwersji do WebP
(1920px, q=82) dostajemy ~200-400 KB bez widocznej różnicy na ekranie.
Dzięki temu R2 pozostaje lekki, a strona ładuje się szybko.
"""
import io
import os
import uuid

from django.conf import settings

# Maksymalny rozmiar dłuższego boku po kompresji (px)
MAX_DIMENSION = 1920
# Jakość WebP (0-100)
WEBP_QUALITY = 82


def _r2_configured():
    return bool(
        os.getenv('R2_ACCOUNT_ID')
        and os.getenv('R2_ACCESS_KEY_ID')
        and os.getenv('R2_SECRET_ACCESS_KEY')
        and os.getenv('R2_BUCKET')
    )


def _upload_to_r2(key, data: bytes, content_type: str) -> str:
    """Wyślij bajty na R2 (S3-compatible API) i zwróć publiczny URL."""
    import boto3

    account_id = os.getenv('R2_ACCOUNT_ID')
    endpoint = f'https://{account_id}.r2.cloudflarestorage.com'
    bucket = os.getenv('R2_BUCKET')

    client = boto3.client(
        's3',
        endpoint_url=endpoint,
        aws_access_key_id=os.getenv('R2_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('R2_SECRET_ACCESS_KEY'),
        region_name='auto',
    )
    client.put_object(
        Bucket=bucket,
        Key=key,
        Body=data,
        ContentType=content_type,
        CacheControl='max-age=31536000, public',
    )
    # Publiczny URL: https://pub-<hash>.r2.dev/<key> — czytany z env,
    # fallback: endpoint z nazwą bucketa (działa, gdy bucket jest publiczny).
    public_base = os.getenv('R2_PUBLIC_URL')
    if public_base:
        return f'{public_base.rstrip("/")}/{key}'
    return f'https://{bucket}.{account_id}.r2.cloudflarestorage.com/{key}'


def _compress_image(uploaded_file) -> tuple[bytes, str]:
    """Skompresuj obraz do WebP (BytesIO) — zwraca (bajty, content_type)."""
    from PIL import Image

    img = Image.open(uploaded_file)
    # Exif: orientacja (zdjęcia z telefonu bywają obrócone)
    try:
        from PIL import ImageOps
        img = ImageOps.exif_transpose(img)
    except Exception:
        pass

    # Konwersja na RGB (WebP nie wspiera alpha w trybie P/CMYK)
    if img.mode not in ('RGB', 'RGBA'):
        img = img.convert('RGB')
    if img.mode == 'RGBA':
        # zachowaj przezroczystość jako białe tło? WebP wspiera alpha —
        # zostawiamy RGBA, żeby logo/png z alpha nie dostały czarnego tła
        pass

    # Zmniejszenie do MAX_DIMENSION
    w, h = img.size
    if max(w, h) > MAX_DIMENSION:
        ratio = MAX_DIMENSION / max(w, h)
        img = img.resize((int(w * ratio), int(h * ratio)), Image.Resampling.LANCZOS)

    buf = io.BytesIO()
    if img.mode == 'RGBA':
        img.save(buf, 'WEBP', quality=WEBP_QUALITY)
    else:
        img.save(buf, 'WEBP', quality=WEBP_QUALITY)
    return buf.getvalue(), 'image/webp'


def save_uploaded_image(uploaded_file, folder='uploads'):
    """Zapisz wgrany plik graficzny i zwróć URL (str)."""
    # --- Cloudflare R2 (produkcja / gdy skonfigurowane) ---
    if _r2_configured():
        try:
            ext = os.path.splitext(uploaded_file.name or '')[1].lower()
            if ext not in ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.avif'):
                ext = '.webp'
            if ext in ('.svg',):
                # SVG nie kompresujemy — wgrywamy oryginał
                data = uploaded_file.read()
                content_type = 'image/svg+xml'
                filename = f'{uuid.uuid4().hex[:12]}{ext}'
            else:
                data, content_type = _compress_image(uploaded_file)
                filename = f'{uuid.uuid4().hex[:12]}.webp'
            return _upload_to_r2(f'{folder}/{filename}', data, content_type)
        except Exception:
            # fallback: błąd R2 — lokalny zapis
            pass

    # --- Lokalny zapis (MEDIA_ROOT/uploads/) ---
    ext = os.path.splitext(uploaded_file.name or '')[1].lower()
    if ext not in ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.avif'):
        ext = '.jpg'
    filename = f'{uuid.uuid4().hex[:12]}{ext}'

    import django.core.files.storage as storage
    fs = storage.default_storage
    path = fs.save(f'{folder}/{filename}', uploaded_file)
    return f'{settings.MEDIA_URL}{path}'


# ---------------------------------------------------------------------------
# Wideo (hero strony głównej) — bez kompresji (PIL nie otworzy MP4)
# ---------------------------------------------------------------------------

VIDEO_EXTENSIONS = ('.mp4', '.webm', '.mov', '.ogg', '.m4v')


def save_uploaded_video(uploaded_file, folder='uploads'):
    """Zapisz wgrany plik wideo bez kompresji i zwróć URL (str).

    Zachowuje oryginalny format (mp4/webm/mov...) — wideo NIE jest
    przepuszczane przez PIL (nie umie otworzyć filmów). Na produkcji
    (R2) idzie jako oryginał; lokalnie do MEDIA_ROOT/uploads/.
    """
    ext = os.path.splitext(uploaded_file.name or '')[1].lower()
    if ext not in VIDEO_EXTENSIONS:
        ext = '.mp4'
    content_type = {
        '.mp4': 'video/mp4',
        '.webm': 'video/webm',
        '.mov': 'video/quicktime',
        '.ogg': 'video/ogg',
        '.m4v': 'video/x-m4v',
    }.get(ext, 'video/mp4')
    filename = f'{uuid.uuid4().hex[:12]}{ext}'

    # --- Cloudflare R2 (produkcja / gdy skonfigurowane) ---
    if _r2_configured():
        try:
            data = uploaded_file.read()
            return _upload_to_r2(f'{folder}/{filename}', data, content_type)
        except Exception:
            pass  # fallback: lokalny zapis

    # --- Lokalny zapis (MEDIA_ROOT/uploads/) ---
    import django.core.files.storage as storage
    fs = storage.default_storage
    path = fs.save(f'{folder}/{filename}', uploaded_file)
    return f'{settings.MEDIA_URL}{path}'
