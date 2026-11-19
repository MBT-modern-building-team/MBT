"""Eksport strony „Potencjał i referencje” do PDF 16:9 przez Google Chrome (headless).

Bez importów Django — używane przez widok (pobieranie PDF lokalnie) i skrypt export_potencjal_pdf.py.
"""
import os
import shutil
import subprocess
import tempfile

CHROME_CANDIDATES = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
    shutil.which('google-chrome') or '',
    shutil.which('chromium') or '',
    shutil.which('chrome') or '',
]


def chrome_path():
    return next((c for c in CHROME_CANDIDATES if c and os.path.exists(c)), None)


def render_pdf(url, out, timeout=180):
    """Drukuje `url` do pliku PDF (rozmiar strony z CSS @page). Rzuca RuntimeError przy błędzie."""
    chrome = chrome_path()
    if not chrome:
        raise RuntimeError('Nie znaleziono Google Chrome.')
    with tempfile.TemporaryDirectory() as profile:
        cmd = [chrome, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-pdf-header-footer',
               '--no-first-run', f'--user-data-dir={profile}',
               '--run-all-compositor-stages-before-draw', '--virtual-time-budget=60000',
               f'--print-to-pdf={out}', url]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=timeout)
    if not os.path.exists(out) or os.path.getsize(out) == 0:
        raise RuntimeError('Chrome nie zapisał pliku PDF.')
    return out
