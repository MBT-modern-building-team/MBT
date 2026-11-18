#!/usr/bin/env python3
"""Zapisuje stronę „Potencjał i referencje” do PDF (16:9, poziomo) przez Chrome w trybie headless.

Wymaga uruchomionego serwera (python manage.py runserver) i Google Chrome.

    python3 export_potencjal_pdf.py                       # PL -> ~/Desktop/potencjal-i-referencje.pdf
    python3 export_potencjal_pdf.py --lang en --out mbt-en.pdf
    python3 export_potencjal_pdf.py --base http://127.0.0.1:8000

Strona musi być widoczna (lokalnie przy DEBUG lub PORTFOLIO_PAGE_PUBLIC=1).
"""
import argparse
import os
import shutil
import subprocess
import sys

CHROME_CANDIDATES = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
    shutil.which('google-chrome') or '',
    shutil.which('chromium') or '',
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', default='http://127.0.0.1:8000')
    ap.add_argument('--lang', default='pl', help='pl, en, de, cs, sk, hu, uk')
    ap.add_argument('--out', default=os.path.expanduser('~/Desktop/potencjal-i-referencje.pdf'))
    args = ap.parse_args()

    chrome = next((c for c in CHROME_CANDIDATES if c and os.path.exists(c)), None)
    if not chrome:
        sys.exit('Nie znaleziono Google Chrome.')
    prefix = '' if args.lang == 'pl' else f'/{args.lang}'
    url = f'{args.base}{prefix}/potencjal-i-referencje/?pdf=1'
    out = os.path.abspath(os.path.expanduser(args.out))
    cmd = [chrome, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-pdf-header-footer',
           '--run-all-compositor-stages-before-draw', '--virtual-time-budget=25000',
           f'--print-to-pdf={out}', url]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    size = os.path.getsize(out) / 1048576
    try:
        import pymupdf  # opcjonalnie: pip install pymupdf — zmniejsza zdjęcia w PDF
        doc = pymupdf.open(out)
        doc.rewrite_images(dpi_threshold=220, dpi_target=160, quality=82)
        tmp = out + '.tmp'
        doc.save(tmp, garbage=4, deflate=True)
        doc.close()
        os.replace(tmp, out)
        print(f'Zmniejszono: {size:.1f} MB -> {os.path.getsize(out) / 1048576:.1f} MB')
    except ImportError:
        print(f'PDF ma {size:.1f} MB. Aby go zmniejszyć: pip install pymupdf i uruchom ponownie.')
    print(f'Zapisano: {out}')


if __name__ == '__main__':
    main()
