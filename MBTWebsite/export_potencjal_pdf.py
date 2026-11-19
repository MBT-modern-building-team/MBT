#!/usr/bin/env python3
"""Zapisuje stronę „Potencjał i referencje” do PDF (16:9, poziomo) przez Chrome w trybie headless.

Wymaga uruchomionego serwera (python manage.py runserver) i Google Chrome. Ten sam wynik daje
adres http://127.0.0.1:8000/potencjal-i-referencje/?pdf=1&download=1 (pobiera PDF w przeglądarce).

    python3 export_potencjal_pdf.py                       # PL -> ~/Desktop/potencjal-i-referencje.pdf
    python3 export_potencjal_pdf.py --lang en --out mbt-en.pdf
"""
import argparse
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('portfolio_pdf', os.path.join(HERE, 'MBTApp', 'portfolio_pdf.py'))
portfolio_pdf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(portfolio_pdf)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', default='http://127.0.0.1:8000')
    ap.add_argument('--lang', default='pl', help='pl, en, de, cs, sk, hu, uk')
    ap.add_argument('--out', default=os.path.expanduser('~/Desktop/potencjal-i-referencje.pdf'))
    args = ap.parse_args()
    prefix = '' if args.lang == 'pl' else f'/{args.lang}'
    out = os.path.abspath(os.path.expanduser(args.out))
    try:
        portfolio_pdf.render_pdf(f'{args.base}{prefix}/potencjal-i-referencje/?pdf=1', out)
    except RuntimeError as e:
        sys.exit(str(e))
    print(f'Zapisano: {out} ({os.path.getsize(out) / 1048576:.1f} MB)')


if __name__ == '__main__':
    main()
