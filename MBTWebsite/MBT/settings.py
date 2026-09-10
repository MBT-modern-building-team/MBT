"""
Django settings for MBT project.

Ustawienia projektu dla Django 5.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Ustaw DJANGO_SECRET_KEY w zmiennych środowiskowych (lokalnie: .env, na Vercel: dashboard).
# Fallback tylko na potrzeby developmentu — nie używaj w produkcji bez env.
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'dev-insecure-key-change-me')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

# Domyślnie zezwól na localhost (dev); na produkcji ustaw DJANGO_ALLOWED_HOSTS
# np. 'mbt-site.vercel.app,www.mbt.pl,admin.mbt.pl' (przecinkami, bez spacji).
# Uwaga: Django nie wspiera wildcardów w ALLOWED_HOSTS — każdą subdomenę
# (np. admin.*) trzeba wpisać jawnie lub użyć '.' na początku wpisu,
# co obejmuje daną domenę i jej subdomeny ('.vercel.app' obejmie admin.x.vercel.app).
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
if DEBUG:
    ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://nowa-strona-xi.vercel.app', 'https://*.vercel.app']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Zezwól na osadzenie strony w iframe edytora CSS (/static/design/editor.html)
# — tylko w trybie DEBUG (lokalny development).
if DEBUG:
    X_FRAME_OPTIONS = 'SAMEORIGIN'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'MBTApp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'MBTApp.middleware.AdminSubdomainMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'MBTApp.middleware.AutoLanguageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MBT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'MBTApp', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'MBTApp.context.site_context',
                'MBTApp.context.translate_url',
            ],
        },
    },
]

WSGI_APPLICATION = 'MBT.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# Lokalnie: SQLite. Na Vercel: Postgres — ustaw zmienną DATABASE_URL
# (np. z Vercel Postgres / Neon). Format: postgres://USER:PASS@HOST:PORT/DB
import shutil

try:
    import dj_database_url
except ImportError:
    dj_database_url = None

DEFAULT_SQLITE_PATH = BASE_DIR / 'db.sqlite3'
# Na Vercel filesystem /var/task jest read-only. Jeśli nie ma DATABASE_URL,
# kopiujemy db.sqlite3 do /tmp/db.sqlite3 (jedyny zapisywalny katalog w AWS Lambda / Vercel),
# żeby SQLite nie rzucał OperationalError: unable to open database file.
if os.getenv('VERCEL') == '1' or not os.access(str(BASE_DIR), os.W_OK):
    TMP_SQLITE_PATH = Path('/tmp/db.sqlite3')
    try:
        if DEFAULT_SQLITE_PATH.exists() and not TMP_SQLITE_PATH.exists():
            shutil.copy2(DEFAULT_SQLITE_PATH, TMP_SQLITE_PATH)
        DEFAULT_SQLITE_PATH = TMP_SQLITE_PATH
    except Exception:
        DEFAULT_SQLITE_PATH = TMP_SQLITE_PATH

db_url = os.getenv('DATABASE_URL') or os.getenv('POSTGRES_URL')
if dj_database_url and db_url:
    DATABASES = {
        'default': dj_database_url.config(
            default=db_url,
            conn_max_age=0 if DEBUG else 600,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': str(DEFAULT_SQLITE_PATH),
            'OPTIONS': {'timeout': 30},
        }
    }


# Sessions
# Na środowiskach serverless (np. Vercel) sesje w podpisanych kryptograficznie
# ciasteczkach (signed_cookies) są bezstanowe i nie wymagają zapisu do bazy danych,
# co całkowicie zapobiega błędom bazy przy przełączaniu języka (/i18n/setlang/) czy sesjach anonimowych.
SESSION_ENGINE = os.getenv(
    'DJANGO_SESSION_ENGINE',
    'django.contrib.sessions.backends.signed_cookies'
)
SESSION_COOKIE_NAME = 'mbt_sessionid'


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'pl'

LANGUAGES = [
    ('pl', 'Polski'),
    ('en', 'English'),
    ('cs', 'Čeština'),
    ('sk', 'Slovenčina'),
    ('de', 'Deutsch'),
    ('hu', 'Magyar'),
    ('uk', 'Українська'),
]

# Prefiks URL-i tylko dla języków NIENATYWNEGO (PL jest domyślny, bez prefiksu).
# Dzięki temu strona działa jak mbt.pl: / = pl, /en/ = English, /cs/ = Čeština itd.
PREFIX_DEFAULT_LANGUAGE = False

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Katalogi z plikami tłumaczeń (.po/.mo) — per język: locale/<lang>/LC_MESSAGES/
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'MBTApp', 'locale'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Pliki statyczne na Vercel serwuje bezpośrednio Vercel (rule w vercel.json:
# /static/(.*) -> /MBTApp/static/$1), a lokalnie Django dev server.
# STATICFILES_DIRS wskazuje na katalog z plikami (MBTApp/static).

# --- Media (uploadowane zdjęcia z admina) ---
# Lokalnie: MEDIA_ROOT/uploads/ (serwowane przez urls.py w DEBUG).
# Na Vercel: upload trafia do Vercel Blob (BLOB_READ_WRITE_TOKEN), więc
# MEDIA_ROOT nie jest tam używany.
# Cloudflare R2: gdy ustawione R2_* — upload idzie na R2 (storage.py),
# MEDIA_ROOT nie jest wtedy używany do zapisu.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --- Cloudflare R2 (opcjonalny magazyn mediów) ---
# Ustaw w .env (lokalnie) / zmienne środowiskowe (Vercel):
#   R2_ACCOUNT_ID, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY,
#   R2_BUCKET (np. mbt-media), R2_PUBLIC_URL (np. https://pub-xxx.r2.dev)
R2_ACCOUNT_ID = os.getenv('R2_ACCOUNT_ID', '')
R2_BUCKET = os.getenv('R2_BUCKET', '')

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files configuration
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "MBTApp", "static"),
]

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins', 'file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'MBTApp': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# Create logs directory if it doesn't exist
# UWAGA: na Vercel filesystem jest READ-ONLY (poza /tmp) — zapis do pliku logów
# przy starcie aplikacji powodowalby crash. Dlatego: jeśli katalog nie jest
# zapisywalny, logujemy tylko do konsoli (StreamHandler).
LOG_DIR = os.path.join(BASE_DIR, 'logs')
LOG_TO_FILE = False
try:
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    # test zapisywalnosci
    _test = os.path.join(LOG_DIR, '.write_test')
    with open(_test, 'w') as _f:
        _f.write('ok')
    os.remove(_test)
    LOG_TO_FILE = True
except OSError:
    LOG_TO_FILE = False
    LOG_DIR = None

# Jeśli nie można pisać do pliku (np. Vercel — read-only FS), usuń handler 'file'
# z konfiguracji LOGGING, żeby Django nie próbował go utworzyć przy starcie.
if not LOG_TO_FILE:
    LOGGING['handlers'].pop('file', None)
    for _logger_conf in LOGGING['loggers'].values():
        if 'file' in _logger_conf.get('handlers', []):
            _logger_conf['handlers'] = [h for h in _logger_conf['handlers'] if h != 'file']

LOGIN_URL = '/admin-budowa/login/'
LOGIN_REDIRECT_URL = '/admin-budowa/panel/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
WHITENOISE_USE_FINDERS = True
