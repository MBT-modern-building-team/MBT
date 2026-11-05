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


DEFAULT_R2_ACCOUNT_ID = 'b769f6bfd2f82b3510f4fec0807b0134'
DEFAULT_R2_ACCESS_KEY_ID = '84d9e38f6a5c1482e92c2dcb0c95a078'
DEFAULT_R2_SECRET_ACCESS_KEY = 'a7d28e19e3bc9a7150fbcc4bf9bea7cce3b45816ec68f470be89da42c0490f62'
DEFAULT_R2_BUCKET = 'mbt-media'
DEFAULT_R2_PUBLIC_URL = 'https://media.mbt.pl'


def _clean_env(val, placeholder):
    """Zwraca wartość ze zmiennych środowiskowych jeśli nie jest pusta ani nie jest nazwą zmiennej."""
    if not val:
        return None
    val = str(val).strip()
    if val == placeholder or placeholder.upper() in val.upper():
        return None
    return val


def _get_r2_config():
    """Zwraca bezpieczną krotkę (account_id, access_key, secret_key, bucket, public_url)."""
    raw_account_id = _clean_env(os.getenv('R2_ACCOUNT_ID'), 'R2_ACCOUNT_ID')
    if raw_account_id:
        # Obsłuż przypadek, gdy ktoś wkleił cały URL: https://<id>.r2.cloudflarestorage.com
        cleaned = raw_account_id.replace('https://', '').replace('http://', '').split('.')[0].strip()
        account_id = cleaned if len(cleaned) >= 16 else DEFAULT_R2_ACCOUNT_ID
    else:
        account_id = DEFAULT_R2_ACCOUNT_ID

    access_key = _clean_env(os.getenv('R2_ACCESS_KEY_ID'), 'R2_ACCESS_KEY_ID')
    if not access_key or len(access_key) < 16:
        access_key = DEFAULT_R2_ACCESS_KEY_ID

    secret_key = _clean_env(os.getenv('R2_SECRET_ACCESS_KEY'), 'R2_SECRET_ACCESS_KEY')
    if not secret_key or len(secret_key) < 16:
        secret_key = DEFAULT_R2_SECRET_ACCESS_KEY
    
    bucket_env = _clean_env(os.getenv('R2_BUCKET'), 'R2_BUCKET')
    # Jeśli podano stary bucket 'mbt' zamiast 'mbt-media' lub placeholder, użyj 'mbt-media'
    if not bucket_env or bucket_env == 'mbt':
        bucket = DEFAULT_R2_BUCKET
    else:
        bucket = bucket_env
        
    public_url = _clean_env(os.getenv('R2_PUBLIC_URL'), 'R2_PUBLIC_URL') or DEFAULT_R2_PUBLIC_URL

    return account_id, access_key, secret_key, bucket, public_url


def _r2_configured():
    account_id, access_key, secret_key, bucket, _ = _get_r2_config()
    return bool(account_id and access_key and secret_key and bucket)


def _upload_to_r2(key, data: bytes, content_type: str) -> str:
    """Wyślij bajty na R2 (S3-compatible API) i zwróć publiczny URL."""
    import boto3
    from botocore.config import Config

    account_id, access_key, secret_key, bucket, public_base = _get_r2_config()
    endpoint = f'https://{account_id}.r2.cloudflarestorage.com'

    client = boto3.client(
        's3',
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        config=Config(signature_version='s3v4'),
        region_name='auto',
    )
    client.put_object(
        Bucket=bucket,
        Key=key,
        Body=data,
        ContentType=content_type,
        CacheControl='max-age=31536000, public',
    )
    return f'{public_base.rstrip("/")}/{key.lstrip("/")}'


def generate_r2_presigned_upload_url(filename, folder='uploads', content_type=None):
    """Generuje presigned PUT URL do bezpośredniego uploadu z przeglądarki na Cloudflare R2.

    Całkowicie omija limit Vercel (4.5 MB), umożliwiając wgrywanie dużych filmów (np. 10-100 MB)
    oraz ciężkich galerii prosto z przeglądarki klienta do R2.
    """
    import mimetypes
    import boto3
    from botocore.config import Config

    account_id, access_key, secret_key, bucket, public_base = _get_r2_config()
    endpoint = f'https://{account_id}.r2.cloudflarestorage.com'

    ext = os.path.splitext(filename or '')[1].lower()
    random_name = f'{uuid.uuid4().hex[:12]}{ext}'
    clean_folder = (folder or 'uploads').strip('/')
    key = f'{clean_folder}/{random_name}' if clean_folder else random_name

    if not content_type:
        content_type, _ = mimetypes.guess_type(filename or '')
        content_type = content_type or 'application/octet-stream'

    client = boto3.client(
        's3',
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        config=Config(signature_version='s3v4'),
        region_name='auto',
    )

    presigned_url = client.generate_presigned_url(
        'put_object',
        Params={
            'Bucket': bucket,
            'Key': key,
        },
        ExpiresIn=3600,
    )
    public_url = f'{public_base.rstrip("/")}/{key.lstrip("/")}'
    return presigned_url, public_url, key, content_type


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

    # Zmniejszenie do MAX_DIMENSION
    w, h = img.size
    if max(w, h) > MAX_DIMENSION:
        ratio = MAX_DIMENSION / max(w, h)
        img = img.resize((int(w * ratio), int(h * ratio)), Image.Resampling.LANCZOS)

    buf = io.BytesIO()
    img.save(buf, 'WEBP', quality=WEBP_QUALITY)
    return buf.getvalue(), 'image/webp'


def save_uploaded_image(uploaded_file, folder='uploads', raise_on_error=False):
    """Zapisz wgrany plik graficzny i zwróć URL (str)."""
    # --- Cloudflare R2 (produkcja / gdy skonfigurowane) ---
    if _r2_configured():
        try:
            ext = os.path.splitext(uploaded_file.name or '')[1].lower()
            if ext in ('.svg',):
                # SVG nie kompresujemy — wgrywamy oryginał
                filename = f'{uuid.uuid4().hex[:12]}{ext}'
                data = uploaded_file.read()
                content_type = 'image/svg+xml'
            else:
                filename = f'{uuid.uuid4().hex[:12]}.webp'
                data, content_type = _compress_image(uploaded_file)
            
            clean_folder = folder.strip('/')
            r2_key = f'{clean_folder}/{filename}' if clean_folder else filename
            return _upload_to_r2(r2_key, data, content_type)
        except Exception:
            if raise_on_error:
                raise
            # fallback: lokalny zapis w środowisku dev bez R2
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


def save_uploaded_video(uploaded_file, folder='uploads', raise_on_error=False):
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
            clean_folder = folder.strip('/')
            r2_key = f'{clean_folder}/{filename}' if clean_folder else filename
            return _upload_to_r2(r2_key, data, content_type)
        except Exception:
            if raise_on_error:
                raise
            pass  # fallback: lokalny zapis

    # --- Lokalny zapis (MEDIA_ROOT/uploads/) ---
    import django.core.files.storage as storage
    fs = storage.default_storage
    path = fs.save(f'{folder}/{filename}', uploaded_file)
    return f'{settings.MEDIA_URL}{path}'
