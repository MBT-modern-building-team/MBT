"""Formularze admina MBT — wygodny upload zdjęć.

Zamiast wpisywania ścieżek, w adminie jest przycisk „Wybierz plik":
- pojedyncze zdjęcie (hero/logo/photo/image) -> UploadImageWidget
- galeria (wiele zdjęć)                     -> GalleryUploadWidget

Po zapisie formularza pliki są wgrywane (Vercel Blob na produkcji,
lokalnie do MEDIA/uploads) i pole dostaje gotowy URL.

UWAGA (ważne dla uploadów): Django woła widget.value_from_datadict DWA razy
podczas jednego zapisu (raz przy walidacji, raz przy construct_change_message
-> changed_data). Plik tymczasowy znika po pierwszym zapisie, więc wynik
cache'ujemy. Cache NIE może żyć na instancji widgetu — Django kopiuje widget
płytko (deepcopy bez __init__), więc atrybut instancji byłby WSPÓŁDZIELONY
między wszystkimi formularzami (przeciek: zdjęcia projektu A trafiały do B).
Zamiast tego: threading.local kluczowany po id(pliku) + czyszczenie w __init__
formularza (każdy request tworzy nowy formularz -> świeży cache).
"""
import json
import threading

from django import forms
from django.contrib.admin.widgets import AdminFileWidget

from MBTApp.models import Award, Article, Project, SiteConfig, SitePhotos, Worker, SalesRepresentative, Sector
from MBTApp.storage import save_uploaded_image


# --- Cache uploadów: per-request, NIE na widgetcie (patrz docstring wyżej) ---

_upload_cache = threading.local()


def _get_upload_cache():
    if not hasattr(_upload_cache, 'urls'):
        _upload_cache.urls = {}
    return _upload_cache.urls


def _clear_upload_cache():
    if hasattr(_upload_cache, 'urls'):
        _upload_cache.urls = {}


def _cached_save(uploaded, name):
    """Zapisz plik raz; drugie wywołanie value_from_datadict zwraca cache.

    Klucz: (nazwa pola, id obiektu pliku) — unikalne w obrębie jednego
    requestu, bo request.FILES trzyma te same obiekty w obu wywołaniach.
    """
    key = (name, id(uploaded))
    cache = _get_upload_cache()
    if key in cache:
        return cache[key]
    url = save_uploaded_image(uploaded)
    cache[key] = url
    return url


# ---------------------------------------------------------------------------
# Widget: pojedyncze zdjęcie (plik + podgląd + URL)
# ---------------------------------------------------------------------------

class UploadImageWidget(AdminFileWidget):
    """Pole: wybierz plik z dysku (z podglądem aktualnego zdjęcia).

    Renderuje input[type=file] o nazwie {name}_file + ukryte pole {name}
    z aktualnym URL-em. FormField czyta wgrany plik z FILES i zapisuje URL.
    """

    template_name = 'admin/widgets/upload_image.html'

    class Media:
        # Pełna ścieżka od "/" — Django Media nie encoduje wtedy query stringa
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.6.1/cropper.min.css',
                '/static/admin/css/mbt-admin.css?v=6',
            )
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.6.1/cropper.min.js',
            '/static/admin/js/upload_image.js?v=6',
        )

    def __init__(self, *args, **kwargs):
        self.crop = kwargs.pop('crop', False)
        self.aspect_ratio = kwargs.pop('aspect_ratio', '')
        super().__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        ctx = super().get_context(name, value, attrs)
        ctx['widget']['file_name'] = f'{name}_file'
        ctx['widget']['current_url'] = value or ''
        ctx['widget']['data_crop'] = '1' if self.crop else '0'
        if self.aspect_ratio is not None and self.aspect_ratio != '':
            ctx['widget']['data_aspect_ratio'] = str(self.aspect_ratio)
        return ctx

    def value_from_datadict(self, data, files, name):
        # Wgrany plik ma priorytet nad wpisanym URL-em
        uploaded = files.get(f'{name}_file')
        if uploaded:
            return _cached_save(uploaded, name)
        return data.get(name, '')


class UploadUrlField(forms.CharField):
    """Pole URL z możliwością wgrania pliku z dysku."""

    def __init__(self, *args, **kwargs):
        self.crop = kwargs.pop('crop', False)
        self.aspect_ratio = kwargs.pop('aspect_ratio', '')
        kwargs.setdefault('required', False)
        kwargs.setdefault('label', 'Zdjęcie')
        # Setup widget explicitly here to pass kwargs
        kwargs['widget'] = UploadImageWidget(crop=self.crop, aspect_ratio=self.aspect_ratio)
        super().__init__(*args, **kwargs)


# ---------------------------------------------------------------------------
# Widget: pojedyncze wideo (plik + podgląd + URL) — hero strony głównej
# ---------------------------------------------------------------------------

class UploadVideoWidget(AdminFileWidget):
    """Pole: wybierz plik wideo z dysku (z podglądem <video>).

    Analogiczne do UploadImageWidget — ale accept="video/*" i podgląd
    odtwarzalny. Plik zapisywany przez save_uploaded_video (bez kompresji).
    """

    template_name = 'admin/widgets/upload_video.html'

    class Media:
        # Pełna ścieżka od "/" — Django Media nie encoduje wtedy query stringa
        css = {'all': ('/static/admin/css/mbt-admin.css?v=5',)}
        js = ('/static/admin/js/upload_image.js?v=5',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        ctx = super().get_context(name, value, attrs)
        ctx['widget']['file_name'] = f'{name}_file'
        ctx['widget']['current_url'] = value or ''
        return ctx

    def value_from_datadict(self, data, files, name):
        # Wgrany plik ma priorytet nad wpisanym URL-em
        uploaded = files.get(f'{name}_file')
        if uploaded:
            return _cached_save_video(uploaded, name)
        return data.get(name, '')


def _cached_save_video(uploaded, name):
    """Zapisz wideo raz; drugie wywołanie value_from_datadict zwraca cache.

    Analogicznie do _cached_save — cache w threading.local kluczowany
    po id(pliku), żeby uniknąć przecieku między formularzami.
    """
    key = (name, id(uploaded))
    cache = _get_upload_cache()
    if key in cache:
        return cache[key]
    from MBTApp.storage import save_uploaded_video
    url = save_uploaded_video(uploaded)
    cache[key] = url
    return url


class UploadVideoField(forms.CharField):
    """Pole URL wideo z możliwością wgrania pliku z dysku."""

    widget = UploadVideoWidget

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('required', False)
        kwargs.setdefault('label', 'Film')
        super().__init__(*args, **kwargs)


# ---------------------------------------------------------------------------
# Widget: galeria (wiele zdjęć)
# ---------------------------------------------------------------------------

class GalleryUploadWidget(forms.Textarea):
    """Galeria jako lista URL-i + możliwość wgrania wielu plików naraz.

    W polu tekstowym widać JSON (lista URL-i). Dodatkowy input[type=file
    multiple] wgrywa wybrane zdjęcia przy zapisie — nowe URL-e są doklejane
    do listy.
    """

    template_name = 'admin/widgets/gallery_upload.html'

    class Media:
        # Pełna ścieżka od "/" — Django Media nie encoduje wtedy query stringa
        css = {'all': ('/static/admin/css/mbt-admin.css?v=5',)}
        js = ('/static/admin/js/upload_image.js?v=5',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        ctx = super().get_context(name, value, attrs)
        ctx['widget']['file_name'] = f'{name}_files'
        if isinstance(value, list):
            urls = value
        else:
            try:
                urls = json.loads(value) if value else []
            except (TypeError, ValueError):
                urls = []
        ctx['widget']['gallery_urls'] = urls
        return ctx

    def value_from_datadict(self, data, files, name):
        # Aktualna lista z pola tekstowego (może zawierać placeholdery __new_N__)
        try:
            current = json.loads(data.get(name, '[]') or '[]')
        except (TypeError, ValueError):
            current = []
        if not isinstance(current, list):
            current = []
        # Nowo wgrany pliki (multiple) — w kolejności dodania
        uploaded = files.getlist(f'{name}_files')
        new_urls = [_cached_save(f, f'{name}_files') for f in uploaded]
        new_urls = [u for u in new_urls if u]
        # Placeholder __new_N__ -> URL N-tego nowego pliku (kolejność drag&drop)
        result = []
        new_idx = 0
        for item in current:
            if isinstance(item, str) and item.startswith('__new_') and item.endswith('__'):
                if new_idx < len(new_urls):
                    result.append(new_urls[new_idx])
                new_idx += 1
            else:
                result.append(item)
        # Gdyby JSON nie zawierał placeholderów (np. starszy zapis) — doklej na koniec
        for u in new_urls[new_idx:]:
            result.append(u)
        return json.dumps(result)


class GalleryField(forms.JSONField):
    """Pole JSON (lista URL-i) z multi-uploadem zdjęć."""

    widget = GalleryUploadWidget

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('required', False)
        kwargs.setdefault('label', 'Galeria (zdjęcia)')
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        # JSONField zamienia pustą listę [] na None (empty_values),
        # a kolumna gallery jest NOT NULL — zwracamy [] zamiast None.
        if value == []:
            return []
        return super().to_python(value)


# ---------------------------------------------------------------------------
# Formularze modeli — pola zdjęć używają widgetów uploadu
# ---------------------------------------------------------------------------

class ProjectForm(forms.ModelForm):
    hero = UploadUrlField(label='Zdjęcie główne')
    logo = UploadUrlField(label='Logo firmy')
    gallery = GalleryField(label='Galeria')
    # Ukryte pole wymusza enctype="multipart/form-data" w formularzu
    _multipart = forms.FileField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        # Każdy request tworzy nowy formularz — czyścimy cache uploadów,
        # żeby zdjęcia z poprzedniego projektu nie "przeciekły" do tego.
        _clear_upload_cache()
        super().__init__(*args, **kwargs)

    class Meta:
        model = Project
        fields = '__all__'
        widgets = {'_multipart': forms.HiddenInput()}


class WorkerForm(forms.ModelForm):
    photo = UploadUrlField(label='Zdjęcie', crop=True, aspect_ratio='')
    _multipart = forms.FileField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        _clear_upload_cache()
        super().__init__(*args, **kwargs)

    class Meta:
        model = Worker
        fields = '__all__'
        widgets = {'_multipart': forms.HiddenInput()}


class SalesRepresentativeForm(forms.ModelForm):
    photo = UploadUrlField(label='Zdjęcie', crop=True, aspect_ratio='1')
    _multipart = forms.FileField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        _clear_upload_cache()
        super().__init__(*args, **kwargs)

    class Meta:
        model = SalesRepresentative
        fields = '__all__'
        widgets = {'_multipart': forms.HiddenInput()}


class ArticleForm(forms.ModelForm):
    image = UploadUrlField(label='Zdjęcie główne')
    gallery = GalleryField(label='Galeria (wiele zdjęć)')
    _multipart = forms.FileField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        _clear_upload_cache()
        super().__init__(*args, **kwargs)

    class Meta:
        model = Article
        fields = '__all__'
        widgets = {'_multipart': forms.HiddenInput()}


class SiteConfigForm(forms.ModelForm):
    """Dane firmy — zdjęcia biur wgrywane przyciskiem „Wybierz plik"."""
    office_zabrze_photo = UploadUrlField(label='Zdjęcie biura Zabrze (wybierz plik)')
    office_katowice_photo = UploadUrlField(label='Zdjęcie siedziby Katowice (wybierz plik)')
    office_krakow_photo = UploadUrlField(label='Zdjęcie oddziału Kraków (wybierz plik)')
    office_site_photo = UploadUrlField(label='Zdjęcie placu budowy (wybierz plik) - stare')
    office_site_gallery = GalleryField(label='Galeria placu budowy')
    hero_video = UploadVideoField(label='Film w tle (strona główna) — wybierz plik MP4')
    _multipart = forms.FileField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        _clear_upload_cache()
        super().__init__(*args, **kwargs)

    class Meta:
        model = SiteConfig
        fields = '__all__'
        widgets = {'_multipart': forms.HiddenInput()}


class SitePhotosForm(forms.ModelForm):
    """Zdjęcia strony — każde pole to osobny upload (przycisk „Wybierz plik").

    Fieldsety w admin.py grupują je czytelnie wg miejsca na stronie.
    """
    
    work_gallery = GalleryField(label='Galeria pracy')

    def __init__(self, *args, **kwargs):
        _clear_upload_cache()
        super().__init__(*args, **kwargs)
        # Każde pole zdjęciowe dostaje widget uploadu z podglądem
        for field_name, field in self.fields.items():
            if field_name in ['_multipart', 'work_gallery']:
                continue
            field.widget = UploadImageWidget()
            field.label = field.label or field_name

    _multipart = forms.FileField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = SitePhotos
        fields = '__all__'
        widgets = {'_multipart': forms.HiddenInput()}

class AwardForm(forms.ModelForm):
    image = UploadUrlField(label='Logotyp / Grafika')
    _multipart = forms.FileField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        _clear_upload_cache()
        super().__init__(*args, **kwargs)

    class Meta:
        model = Award
        fields = '__all__'
        widgets = {'_multipart': forms.HiddenInput()}

class SectorForm(forms.ModelForm):
    image = UploadUrlField(label='Zdjęcie')
    _multipart = forms.FileField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        _clear_upload_cache()
        super().__init__(*args, **kwargs)

    class Meta:
        model = Sector
        fields = '__all__'
        widgets = {'_multipart': forms.HiddenInput()}
