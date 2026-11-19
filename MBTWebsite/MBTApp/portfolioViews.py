import json
import mimetypes
import os
import tempfile
import urllib.parse
import urllib.request
from io import BytesIO

from django.conf import settings
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import render
from django.urls import NoReverseMatch, reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

from MBTApp import mbt_orm, portfolio, portfolio_pdf
from MBTApp.portfolio_records import page_is_public

SITE_URL = 'https://mbt.pl'


def _json_ld(request, ctx, lang):
    p = ctx['p']
    c = p['contact']
    hq = next((o for o in p['offices'] if o.get('typ') == 'Siedziba'), p['offices'][0])
    page_url = SITE_URL + request.path
    org = {
        '@context': 'https://schema.org',
        '@type': 'GeneralContractor',
        'name': p['company_name'],
        'url': c.get('www') or SITE_URL,
        'foundingDate': str(p['since']),
        'telephone': c.get('telefon'),
        'email': c.get('email'),
        'address': {
            '@type': 'PostalAddress',
            'streetAddress': hq.get('adres'),
            'addressLocality': hq.get('miasto'),
            'addressCountry': 'PL',
        },
        'knowsAbout': p['specializations'],
    }
    crumbs = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'MBT', 'item': SITE_URL + reverse('index')},
            {'@type': 'ListItem', 'position': 2, 'name': p['texts']['hero_kicker'], 'item': page_url},
        ],
    }
    # Bezpieczne osadzenie w <script>: bez sekwencji </ i znaków rozbijających parser HTML.
    dump = lambda o: json.dumps(o, ensure_ascii=False).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    return mark_safe(dump(org)), mark_safe(dump(crumbs))


IMG_HOSTS = {'media.mbt.pl', 'pub-055b6d77c1e84acda77dbc29041f73ff.r2.dev'}


def _pdf_img(request, src, width=800):
    """Adres zdjęcia przez lokalny proxy zmniejszający obraz (PDF jest wtedy kilka MB, nie kilkadziesiąt)."""
    if not src:
        return src
    return '%s?u=%s&w=%s' % (reverse('portfolioImg'), urllib.parse.quote(src, safe=''), width)


def _fetch(src):
    """Pobiera zdalne zdjęcie (tylko hosty z białej listy). Certyfikaty: certifi -> system -> (lokalnie) bez weryfikacji."""
    import ssl
    contexts = []
    try:
        import certifi
        contexts.append(ssl.create_default_context(cafile=certifi.where()))
    except ImportError:
        pass
    contexts.append(ssl.create_default_context())
    if settings.DEBUG:
        contexts.append(ssl._create_unverified_context())  # python.org na macOS bywa bez certyfikatów CA
    for ctx in contexts:
        try:
            req = urllib.request.Request(src, headers={'User-Agent': 'mbt-pdf'})
            with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
                return r.read(30_000_000)
        except Exception:
            continue
    return None


def _resized_image(src, width):
    """(bajty, content-type) zmniejszonego zdjęcia; wynik trzymany w katalogu tymczasowym. None gdy się nie da."""
    import hashlib
    cache_dir = os.path.join(tempfile.gettempdir(), 'mbt_pdf_img')
    os.makedirs(cache_dir, exist_ok=True)
    key = hashlib.sha1(('%s|%s' % (src, width)).encode()).hexdigest()
    meta = os.path.join(cache_dir, key + '.type')
    data = os.path.join(cache_dir, key + '.bin')
    if os.path.exists(meta) and os.path.exists(data):
        with open(meta) as f, open(data, 'rb') as g:
            return g.read(), f.read()
    if src.startswith('/static/'):
        base = os.path.realpath(os.path.join(settings.BASE_DIR, 'MBTApp', 'static'))
        path = os.path.realpath(os.path.join(base, src[len('/static/'):]))
        if os.path.commonpath([base, path]) != base or not os.path.isfile(path):
            return None
        with open(path, 'rb') as f:
            raw = f.read()
    else:
        parsed = urllib.parse.urlparse(src)
        if parsed.scheme != 'https' or parsed.hostname not in IMG_HOSTS:
            return None
        raw = _fetch(src)
        if raw is None:
            return None
    if src.lower().endswith('.svg'):
        out, ctype = raw, 'image/svg+xml'
    else:
        try:
            from PIL import Image
            img = Image.open(BytesIO(raw))
            img.load()
        except Exception:
            out, ctype = raw, mimetypes.guess_type(src)[0] or 'application/octet-stream'
        else:
            if img.width > width:
                img = img.resize((width, round(img.height * width / img.width)), Image.LANCZOS)
            buf = BytesIO()
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                img.convert('RGBA').save(buf, 'PNG', optimize=True)
                ctype = 'image/png'
            else:
                img.convert('RGB').save(buf, 'JPEG', quality=84, optimize=True)
                ctype = 'image/jpeg'
            out = buf.getvalue()
    with open(data, 'wb') as g, open(meta, 'w') as f:
        g.write(out)
        f.write(ctype)
    return out, ctype


def potencjal_img(request):
    """Zmniejsza zdjęcie na potrzeby eksportu PDF. Tylko lokalnie (DEBUG) lub dla personelu; adres z białej listy."""
    user = getattr(request, 'user', None)
    if not settings.DEBUG:
        raise Http404()
    try:
        width = max(100, min(int(request.GET.get('w', 800)), 2000))
    except ValueError:
        width = 800
    result = _resized_image(request.GET.get('u', ''), width)
    if result is None:
        raise Http404()
    resp = HttpResponse(result[0], content_type=result[1])
    resp['Cache-Control'] = 'private, max-age=3600'
    return resp


def _warm_images(ctx):
    """Pobiera i zmniejsza wszystkie zdjęcia równolegle, zanim Chrome zacznie drukować."""
    from concurrent.futures import ThreadPoolExecutor
    p = ctx['p']
    jobs = [(pr['thumb'], 700) for g in p['sectors'] for pr in g['projects'] if pr['thumb']]
    for m in p['board'] + p['directors']:
        jobs += [(x['photo'], 500) for x in [m] + list(m.get('reports', [])) if x['photo']]
    hero = (mbt_orm.get_photos() or {}).get('gw_hero')
    if hero:
        jobs.append((hero, 1600))
    with ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(lambda j: _resized_image(*j), jobs))


def _pdfify(request, ctx):
    """W trybie PDF podmienia zdjęcia na zmniejszone kopie."""
    p = ctx['p']
    for g in p['sectors']:
        for pr in g['projects']:
            pr['thumb'] = _pdf_img(request, pr['thumb'], 700)
    for m in p['board'] + p['directors']:
        m['photo'] = _pdf_img(request, m['photo'], 500)
        for r in m.get('reports', []):
            r['photo'] = _pdf_img(request, r['photo'], 500)
    hero = (mbt_orm.get_photos() or {}).get('gw_hero')
    ctx['pdf_cover'] = _pdf_img(request, hero, 1600) if hero else ''


def _project_slides(sectors):
    """Realizacje do PDF: wiersze po 4 karty, 2 wiersze na slajd; nagłówek sektora tylko gdy się zmienia."""
    rows = []
    for g in sectors:
        for i in range(0, len(g['projects']), 4):
            rows.append({'sector': g['slug'], 'code': g['code'], 'name': g['full_name'],
                         'cards': g['projects'][i:i + 4], 'first': i == 0})
    slides = [rows[i:i + 2] for i in range(0, len(rows), 2)]
    for slide in slides:
        prev = None
        for row in slide:
            row['show_head'] = row['sector'] != prev
            prev = row['sector']
    return slides


def _download_pdf(request, lang):
    """Lokalnie: Chrome headless drukuje podgląd ?pdf=1 do PDF, który zwracamy jako plik do pobrania."""
    url = request.build_absolute_uri(request.path) + '?pdf=1'
    fd, out = tempfile.mkstemp(suffix='.pdf')
    os.close(fd)
    try:
        portfolio_pdf.render_pdf(url, out)
    except Exception as e:
        os.unlink(out)
        return HttpResponse('Nie udało się wygenerować PDF: %s' % e, status=500, content_type='text/plain; charset=utf-8')
    resp = FileResponse(open(out, 'rb'), as_attachment=True, filename='MBT-potencjal-i-referencje-%s.pdf' % lang,
                        content_type='application/pdf')
    resp['Cache-Control'] = 'no-store'
    return resp


def potencjal(request):
    public = page_is_public()
    user = getattr(request, 'user', None)
    if not (public or settings.DEBUG):
        raise Http404()  # na produkcji niewidoczna dla nikogo (także personelu), dopóki PORTFOLIO_PAGE_PUBLIC nie jest włączone
    lang = request.LANGUAGE_CODE
    ctx = portfolio.build_context(lang)
    try:
        pdf_url = reverse('portfolioPdf')
    except NoReverseMatch:
        pdf_url = ''  # generator Karty Wykonawcy PDF jeszcze nie podpięty (etap 2)
    ld_org, ld_crumbs = _json_ld(request, ctx, lang)
    ctx.update({
        'title': _('Potencjał i referencje'),
        'meta_title': _('Potencjał i referencje – %(n)s realizacji, kadra, struktura | MBT Modern Building Team') % {'n': ctx['p']['total']},
        'meta_description': _('Portfolio prekwalifikacyjne MBT: kapitał spółki, struktura organizacyjna, kadra, technologie oraz %(n)s realizacji w %(s)s sektorach. Generalne Wykonawstwo i Zaprojektuj i Wybuduj.') % {'n': ctx['p']['total'], 's': len(ctx['p']['sectors'])},
        'pdf_url': pdf_url,
        'sales_reps': mbt_orm.get_sales_reps(lang),
        'json_ld_org': ld_org,
        'json_ld_breadcrumbs': ld_crumbs,
        'site': mbt_orm.get_site(lang),
        'breadcrumb': True,  # własny hero zamiast globalnego breadcrumb-a
        'pdf_mode': request.GET.get('pdf') == '1',  # eksport do PDF: bez lazy-load, wszystkie realizacje
        'show_pdf_button': settings.DEBUG,
    })
    if ctx['pdf_mode']:
        can_download = settings.DEBUG and bool(portfolio_pdf.chrome_path())
        if can_download and (request.GET.get('download') == '1' or request.GET.get('print') == '1'):
            _warm_images(ctx)
            return _download_pdf(request, lang)
        _pdfify(request, ctx)
        ctx['can_download'] = can_download
        ctx['project_slides'] = _project_slides(ctx['p']['sectors'])
        ctx['print_now'] = request.GET.get('print') == '1'
        response = render(request, 'pages/potencjal_pdf.html', ctx)
    else:
        response = render(request, 'pages/potencjal.html', ctx)
    if not public:
        # Podgląd przed publikacją: bez indeksowania i bez cache'owania.
        response['X-Robots-Tag'] = 'noindex, nofollow'
        response['Cache-Control'] = 'private, no-store'
    return response
