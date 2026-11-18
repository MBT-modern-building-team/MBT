"""
Auto-translation service for MBT site.

Strategy:
1. Primary: GoogleTranslator via deep-translator (free, no API key needed)
2. Fallback: MyMemoryTranslator (free, 5000 chars/day anonymous)
3. Cache: SQLite-backed by hash(text + source + target) → translation
4. Detects PL leftovers in rendered HTML and translates them

WAŻNE (wydajność): domyślnie translate() NIE łączy się z zewnętrznym API
podczas obsługi żądania — zwraca tylko tłumaczenie z cache (plik
MBTApp/translation_cache.json dołączony do repo + cache SQLite/in-memory)
albo oryginalny tekst. Połączenia sieciowe są dozwolone tylko:
  * gdy AUTO_TRANSLATE_ONLINE=True w ustawieniach (np. lokalnie),
  * wewnątrz `with online_translation():` (komenda prefetch_translations).
Po dodaniu treści w CMS uruchom lokalnie:
    python manage.py prefetch_translations
i zacommituj zaktualizowany MBTApp/translation_cache.json.

When to use:
- Static content in templates (when {% trans %} misses) — auto-translates on first render
- Dynamic content from admin/CMS — translates on save
- User-edited content — translates on save
"""
import os
import time
import hashlib
import sqlite3
import threading
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

_circuit_open_until = 0

# Cache backend: SQLite on writable FS, in-memory fallback on read-only (e.g. Vercel).
CACHE_DB = os.path.join(settings.BASE_DIR, 'logs', 'translation_cache.sqlite3')

_inmemory = {}          # shared dict (thread-safe via _cache_lock)
_cache_lock = threading.Lock()
_cache_disabled = False  # set True when both SQLite and in-memory are unavailable


def _init_sqlite():
    """Try to initialize SQLite cache; return connection or None on failure."""
    try:
        os.makedirs(os.path.dirname(CACHE_DB), exist_ok=True)
        conn = sqlite3.connect(CACHE_DB, timeout=30)
        conn.execute('''CREATE TABLE IF NOT EXISTS cache (
            hash TEXT PRIMARY KEY,
            source TEXT NOT NULL,
            target TEXT NOT NULL,
            original TEXT NOT NULL,
            translated TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit()
        return conn
    except OSError as e:
        # Read-only filesystem (Vercel /lambda) — fall back to in-memory cache.
        logger.warning(f'SQLite cache unavailable, using in-memory fallback: {e}')
        return None


_local = threading.local()

# Plik z gotowymi tłumaczeniami (read-only na produkcji, commitowany do repo).
BUNDLED_CACHE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'translation_cache.json')
_bundled = None


def _get_bundled():
    """Ładuje translation_cache.json raz na proces: {hash: translated}."""
    global _bundled
    if _bundled is None:
        try:
            import json
            with open(BUNDLED_CACHE_PATH, encoding='utf-8') as f:
                data = json.load(f)
            _bundled = {k: v['translated'] if isinstance(v, dict) else v for k, v in data.items()}
        except FileNotFoundError:
            _bundled = {}
        except Exception as e:
            logger.warning(f'Bundled translation cache unreadable: {e}')
            _bundled = {}
    return _bundled


_online_state = threading.local()


class online_translation:
    """Context manager: zezwala na zapytania do zewnętrznego API (tylko komendy/admin)."""

    def __enter__(self):
        self._prev = getattr(_online_state, 'enabled', False)
        _online_state.enabled = True
        return self

    def __exit__(self, *exc):
        _online_state.enabled = self._prev
        return False


def _online_allowed():
    return getattr(_online_state, 'enabled', False) or getattr(settings, 'AUTO_TRANSLATE_ONLINE', False)


def _get_conn():
    """Get thread-local SQLite connection (or None if cache disabled)."""
    global _cache_disabled
    if _cache_disabled:
        return None
    if not hasattr(_local, 'conn'):
        _local.conn = _init_sqlite()
        if _local.conn is None:
            _cache_disabled = True
    return _local.conn


def _hash(text, source, target):
    key = f'{source}|{target}|{text}'.encode('utf-8')
    return hashlib.sha256(key).hexdigest()[:32]


def get_cached(text, source='pl', target='en'):
    """Look up translation in cache. Returns None if not cached."""
    h = _hash(text, source, target)
    bundled = _get_bundled().get(h)
    if bundled is not None:
        return bundled
    conn = _get_conn()
    if conn is not None:
        try:
            cur = conn.execute(
                'SELECT translated FROM cache WHERE hash = ?', (h,)
            )
            row = cur.fetchone()
            return row[0] if row else None
        except Exception as e:
            logger.warning(f'SQLite cache read failed: {e}')
            return None
    # In-memory fallback
    with _cache_lock:
        return _inmemory.get(h)


def set_cached(text, translated, source='pl', target='en'):
    """Store translation in cache."""
    if translated == text:
        return
    h = _hash(text, source, target)
    recorder = getattr(_online_state, 'recorder', None)
    if recorder is not None:
        recorder[h] = {'source': source, 'target': target, 'original': text, 'translated': translated}
    conn = _get_conn()
    if conn is not None:
        try:
            conn.execute(
                'INSERT OR REPLACE INTO cache (hash, source, target, original, translated) VALUES (?, ?, ?, ?, ?)',
                (h, source, target, text, translated)
            )
            conn.commit()
            return
        except Exception as e:
            logger.warning(f'SQLite cache write failed: {e}')
    # In-memory fallback (best-effort; cleared between invocations on serverless)
    with _cache_lock:
        _inmemory[h] = translated


# Map of Django lang code → Google Translate target code
LANG_MAP = {
    'pl': 'pl',  # Source
    'en': 'en',
    'cs': 'cs',
    'sk': 'sk',
    'de': 'de',
    'hu': 'hu',
    'uk': 'uk',
}


def translate(text, source='pl', target='en', use_cache=True):
    """
    Translate text from source to target language.
    Uses cache, then GoogleTranslator.
    Falls back to MyMemory if Google fails.
    Returns translated text or original on failure.
    """
    if not text or not text.strip():
        return text
    if source == target:
        return text

    if use_cache:
        cached = get_cached(text, source, target)
        if cached is not None:
            return cached

    # Bez zgody na sieć (domyślnie podczas żądania) — zwróć oryginał,
    # zamiast blokować renderowanie strony na zapytaniach HTTP.
    if not _online_allowed():
        return text

    # Skip very short strings (likely markup/CSS/JS fragments)
    if len(text.strip()) < 3:
        return text

    # Skip strings that look like code/paths
    if text.startswith(('/', '#', 'http', '{%', '{{', '<script', '<style')):
        return text

    global _circuit_open_until
    if time.time() < _circuit_open_until:
        return text

    translated = None
    try:
        import urllib.request
        import urllib.parse
        import json
        gt_target = LANG_MAP.get(target, target)
        gt_source = LANG_MAP.get(source, source)
        
        # Free Google Translate API endpoint (gtx)
        url = "https://translate.googleapis.com/translate_a/single"
        params = {
            "client": "gtx",
            "sl": gt_source,
            "tl": gt_target,
            "dt": "t",
            "q": text
        }
        query_string = urllib.parse.urlencode(params)
        full_url = f"{url}?{query_string}"
        
        req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                if data and isinstance(data, list) and len(data) > 0:
                    translated_parts = [part[0] for part in data[0] if part[0]]
                    translated = "".join(translated_parts)
    except Exception as e:
        err_msg = str(e)
        if '403' in err_msg or 'Forbidden' in err_msg:
            _circuit_open_until = time.time() + 600  # Pause for 10 minutes
            logger.warning(f'Translation service returned 403, pausing external requests for 10 minutes: {e}')
        else:
            logger.warning(f'GoogleTranslator direct API failed for {source}->{target}: {e}')

    if (not translated or translated == text) and time.time() >= _circuit_open_until:
        try:
            import urllib.request
            import urllib.parse
            import json
            # MyMemory Translator fallback
            url = "https://api.mymemory.translated.net/get"
            params = {
                "q": text,
                "langpair": f"{source}|{target}"
            }
            query_string = urllib.parse.urlencode(params)
            full_url = f"{url}?{query_string}"
            
            req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    if data.get('responseStatus') == 200:
                        translated = data['responseData']['translatedText']
        except Exception as e:
            err_msg = str(e)
            if '403' in err_msg or 'Forbidden' in err_msg:
                _circuit_open_until = time.time() + 600
            logger.warning(f'MyMemory fallback failed: {e}')

    if not translated:
        translated = text  # Return original on total failure

    if use_cache and translated != text:
        set_cached(text, translated, source, target)

    return translated


def translate_batch(texts, source='pl', target='en', use_cache=True):
    """Translate multiple texts in one call when possible."""
    results = []
    for text in texts:
        results.append(translate(text, source, target, use_cache))
    return results


def get_cache_stats():
    """Return cache statistics for monitoring."""
    conn = _get_conn()
    if conn is None:
        # In-memory cache on read-only FS (e.g. Vercel) — count in-process entries.
        with _cache_lock:
            total = len(_inmemory)
        return {'total_translations': total, 'language_pairs': 0, 'backend': 'memory'}
    try:
        cur = conn.execute('SELECT COUNT(*), COUNT(DISTINCT source||target) FROM cache')
        total, langs = cur.fetchone()
        return {'total_translations': total, 'language_pairs': langs, 'backend': 'sqlite'}
    except Exception as e:
        logger.warning(f'SQLite cache stats failed: {e}')
        return {'total_translations': 0, 'language_pairs': 0, 'backend': 'error'}