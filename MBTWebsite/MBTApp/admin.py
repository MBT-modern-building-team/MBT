"""Panel admina MBT — zarządzanie treścią strony.

Wejdź na /admin (login: superuser). Zdjęcia wgrywasz przyciskiem
„Wybierz plik…" — bez wpisywania ścieżek (lokalnie: MEDIA/uploads,
na Vercel: Vercel Blob).
"""
import types

from django.contrib import admin
from django.db import models as dj_models
from django.utils.html import format_html

from MBTApp import models
from MBTApp import forms as mbt_forms

admin.site.site_header = 'MBT — panel zarządzania'
admin.site.site_title = 'MBT CMS'
admin.site.index_title = 'Zarządzaj treścią strony'

TR_DESCRIPTION = 'Wpisz tłumaczenie w polu danego języka. Puste pole = na stronie pokaże się tekst polski.'


# ============================================================
# Grupowanie modeli na stronie głównej panelu i w menu bocznym
# ============================================================

ADMIN_GROUPS = (
    ('Treści strony', ('Project', 'Article', 'Sector', 'Job', 'Reference', 'Award', 'TrustedBrand')),
    ('Zespół i handlowcy', ('Worker', 'SalesRepresentative')),
    ('Dane firmy i zdjęcia', ('SiteConfig', 'SitePhotos')),
    ('Oznakowanie budowy', ('BannerTemplate', 'BannerDownload', 'UserProfile')),
)

_original_get_app_list = admin.site.get_app_list


def _grouped_app_list(self, request, app_label=None):
    app_list = _original_get_app_list(request, app_label)
    if app_label:
        return app_list
    result = []
    for app in app_list:
        if app['app_label'] != 'MBTApp':
            result.append(app)
            continue
        by_name = {m['object_name']: m for m in app['models']}
        used = set()
        for group_name, names in ADMIN_GROUPS:
            group_models = [by_name[n] for n in names if n in by_name]
            if not group_models:
                continue
            used.update(m['object_name'] for m in group_models)
            result.append({**app, 'name': group_name, 'models': group_models})
        rest = [m for m in app['models'] if m['object_name'] not in used]
        if rest:
            result.append({**app, 'name': 'Inne', 'models': rest})
    # Grupy MBT na górze, „Uwierzytelnianie" (auth) na końcu
    return sorted(result, key=lambda a: a['app_label'] != 'MBTApp')


admin.site.get_app_list = types.MethodType(_grouped_app_list, admin.site)


def _thumb(url, round_=False):
    if not url:
        return format_html('<span class="mbt-thumb mbt-thumb--empty">—</span>')
    return format_html(
        '<img src="{}" alt="" loading="lazy" class="mbt-thumb{}">',
        url, ' mbt-thumb--round' if round_ else '',
    )


class MBTModelAdmin(admin.ModelAdmin):
    """Wspólna baza: pola t_* (JSON {lang: tekst}) edytowane osobnymi polami per język."""

    list_per_page = 50
    save_on_top = False

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, request, **kwargs)
        if (formfield is not None and isinstance(db_field, dj_models.JSONField)
                and db_field.name.startswith('t_')):
            try:
                base = db_field.model._meta.get_field(db_field.name[2:])
                multiline = isinstance(base, dj_models.TextField)
            except Exception:
                multiline = True
            formfield.widget = mbt_forms.TranslationsWidget(multiline=multiline)
            formfield.help_text = ''
        return formfield


@admin.register(models.Project)
class ProjectAdmin(MBTModelAdmin):
    form = mbt_forms.ProjectForm
    list_display = ('miniatura', 'title', 'type', 'status', 'order')
    list_display_links = ('miniatura', 'title')
    list_filter = ('type', 'status')
    search_fields = ('title', 'slug', 'opis')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('order',)
    fieldsets = (
        ('Podstawowe (PL)', {'fields': ('title', 'slug', 'type', 'status')}),
        ('Szczegóły (PL)', {'fields': ('czas', 'formula', 'opis')}),
        ('Lokalizacja inwestycji na mapie', {'fields': ('latitude', 'longitude'), 'description': 'Wpisz szerokość (latitude) i długość (longitude) geograficzną by pinezka automatycznie pojawiła się na mapie na stronie głównej.'}),
        ('Tłumaczenia (en/cs/sk/de/hu)', {
            'classes': ('collapse',),
            'fields': ('t_title', 't_status', 't_czas', 't_formula', 't_opis'),
            'description': TR_DESCRIPTION,
        }),
        ('Zdjęcia', {
            'fields': ('hero', 'logo', 'gallery'),
            'description': 'Wybierz plik z dysku albo wklej URL zdjęcia.',
        }),
        ('Porządek', {'fields': ('order',)}),
    )

    @admin.display(description='')
    def miniatura(self, obj):
        return _thumb(obj.hero)


@admin.register(models.Job)
class JobAdmin(MBTModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('order',)
    fieldsets = (
        ('PL', {'fields': ('title', 'slug', 'text')}),
        ('Tłumaczenia (en/cs/sk/de/hu)', {
            'classes': ('collapse',),
            'fields': ('t_title', 't_text'),
            'description': TR_DESCRIPTION,
        }),
        ('Porządek', {'fields': ('order',)}),
    )


@admin.register(models.Worker)
class WorkerAdmin(MBTModelAdmin):
    form = mbt_forms.WorkerForm
    list_display = ('miniatura', 'name', 'position', 'order')
    list_display_links = ('miniatura', 'name')
    search_fields = ('name', 'position')
    list_editable = ('order',)
    fieldsets = (
        ('PL', {'fields': ('name', 'position', 'opis', 'photo', 'linkedin')}),
        ('Tłumaczenia (en/cs/sk/de/hu)', {
            'classes': ('collapse',),
            'fields': ('t_position', 't_opis'),
            'description': TR_DESCRIPTION,
        }),
        ('Porządek', {'fields': ('order',)}),
    )

    @admin.display(description='')
    def miniatura(self, obj):
        return _thumb(obj.photo, round_=True)


@admin.register(models.SalesRepresentative)
class SalesRepresentativeAdmin(MBTModelAdmin):
    form = mbt_forms.SalesRepresentativeForm
    list_display = ('miniatura', 'name', 'position', 'email', 'phone', 'order')
    list_display_links = ('miniatura', 'name')
    search_fields = ('name', 'position', 'email', 'phone')
    list_editable = ('order',)
    fieldsets = (
        ('PL', {'fields': ('name', 'position', 'email', 'phone', 'photo')}),
        ('Tłumaczenia (en/cs/sk/de/hu)', {
            'classes': ('collapse',),
            'fields': ('t_position',),
            'description': TR_DESCRIPTION,
        }),
        ('Porządek', {'fields': ('order',)}),
    )

    @admin.display(description='')
    def miniatura(self, obj):
        return _thumb(obj.photo, round_=True)


@admin.register(models.Reference)
class ReferenceAdmin(MBTModelAdmin):
    list_display = ('firma', 'osoba', 'stanowisko', 'order')
    search_fields = ('firma', 'osoba', 'tresc')
    list_editable = ('order',)
    fieldsets = (
        ('PL', {'fields': ('firma', 'osoba', 'stanowisko', 'tresc')}),
        ('Tłumaczenia (en/cs/sk/de/hu)', {
            'classes': ('collapse',),
            'fields': ('t_osoba', 't_stanowisko', 't_tresc'),
            'description': TR_DESCRIPTION,
        }),
        ('Porządek', {'fields': ('order',)}),
    )


@admin.register(models.Article)
class ArticleAdmin(MBTModelAdmin):
    form = mbt_forms.ArticleForm
    list_display = ('miniatura', 'title', 'published', 'created')
    list_display_links = ('miniatura', 'title')
    list_filter = ('published',)
    date_hierarchy = 'created'
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('published',)
    fieldsets = (
        ('PL', {'fields': ('title', 'slug', 'excerpt', 'text', 'image', 'gallery', 'published')}),
        ('Tłumaczenia (en/cs/sk/de/hu)', {
            'classes': ('collapse',),
            'fields': ('t_title', 't_excerpt', 't_text'),
            'description': TR_DESCRIPTION,
        }),
        ('Porządek', {'fields': ('order',)}),
    )

    @admin.display(description='')
    def miniatura(self, obj):
        return _thumb(obj.image)


@admin.register(models.SiteConfig)
class SiteConfigAdmin(MBTModelAdmin):
    """Dane firmy — jeden rekord (id=1), edytujesz wszystko w jednym miejscu."""

    form = mbt_forms.SiteConfigForm

    fieldsets = (
        ('Kontakt', {'fields': ('phone', 'phone_href', 'email', 'hours', 'hours_long')}),
        ('Biura', {'fields': (
            'office_zabrze', 'office_zabrze_photo',
            'office_katowice', 'office_katowice_photo',
            'office_krakow', 'office_krakow_photo',
            'office_site_label', 'office_site_adres', 'office_site_photo', 'office_site_gallery'
        )}),
        ('Dane firmy', {'fields': ('nip', 'regon', 'krs', 'founded', 'tagline', 'about_short')}),
        ('Liczniki (strona główna)', {'fields': (
            'counter_years', 'counter_years_label',
            'counter_projects', 'counter_projects_label',
            'counter_ontime', 'counter_ontime_suffix', 'counter_ontime_label',
            'counter_brands', 'counter_brands_label',
        )}),
        ('Strona główna — Hero Teksty', {'fields': (
            'hero_subtitle', 'hero_title1', 'hero_title2', 'hero_text'
        )}),
        ('Strona główna — film w tle', {'fields': ('hero_video',),
                                          'description': 'Opcjonalny film MP4 odtwarzany w pętli w tle sekcji hero (górny baner) strony głównej. Jeśli pole puste — pozostaje obecne zdjęcie.'}),
        ('Social media', {'fields': ('social_linkedin', 'social_youtube', 'social_facebook', 'social_instagram')}),
        ('Tłumaczenia — strona główna (hero)', {
            'classes': ('collapse',),
            'fields': ('t_hero_subtitle', 't_hero_title1', 't_hero_title2', 't_hero_text'),
            'description': TR_DESCRIPTION,
        }),
        ('Tłumaczenia — liczniki', {
            'classes': ('collapse',),
            'fields': ('t_counter_years_label', 't_counter_projects_label',
                       't_counter_ontime_label', 't_counter_brands_label'),
            'description': TR_DESCRIPTION,
        }),
        ('Tłumaczenia — kontakt, biura i opis firmy', {
            'classes': ('collapse',),
            'fields': ('t_hours', 't_hours_long', 't_office_zabrze', 't_office_katowice',
                       't_office_krakow', 't_tagline', 't_about_short'),
            'description': TR_DESCRIPTION,
        }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        from django.shortcuts import redirect
        from django.urls import reverse
        obj, created = models.SiteConfig.objects.get_or_create(id=1)
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return redirect(url)


@admin.register(models.SitePhotos)
class SitePhotosAdmin(MBTModelAdmin):
    """Zdjęcia strony — podmieniaj z poziomu CMS (upload na R2)."""

    form = mbt_forms.SitePhotosForm

    fieldsets = (
        ('Strona główna — hero i sekcje', {'fields': (
            'home_hero_bg', 'home_att8', 'home_o_nas_2', 'home_o_nas_zespol',
            'home_realizacja', 'home_client_group', 'home_testi_2',
        )}),
        ('Strona główna — tła', {'fields': (
            'home_bg_why', 'home_bg_cta', 'home_bg_contact',
        )}),
        ('Galeria pracy („Zobacz jak pracujemy")', {'fields': (
            'work_gallery',
        )}),
        ('O nas', {'fields': ('about_1',)}),
        ('Oferta', {'fields': ('service_1', 'service_2')}),
        ('Landing „Generalne Wykonawstwo"', {'fields': (
            'gw_hero', 'gw_1', 'gw_2', 'gw_3', 'gw_4', 'gw_5', 'gw_6',
            'gw_7', 'gw_8', 'gw_9', 'gw_10', 'gw_11', 'gw_12',
            'general_contracting_1', 'general_contracting_2',
        )}),
        ('Landing „Hale Przemysłowe"', {'fields': (
            'hale_przemyslowe_hero', 'hale_przemyslowe_1', 'hale_przemyslowe_2',
        )}),
        ('Landing „Hale Magazynowe"', {'fields': (
            'hale_magazynowe_hero', 'hale_magazynowe_1',
        )}),
        ('Landing „Obiekty Komercyjne"', {'fields': (
            'obiekty_komercyjne_hero', 'obiekty_komercyjne_1', 'obiekty_komercyjne_2',
        )}),
        ('Tła wspólne (header, stopka, podstrony)', {'fields': (
            'bg_header', 'bg_footer', 'bg_breadcrumb',
        )}),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        from django.shortcuts import redirect
        from django.urls import reverse
        obj, created = models.SitePhotos.objects.get_or_create(id=1)
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return redirect(url)


# ============================================================
# Oznakowanie budowy
# ============================================================

@admin.register(models.BannerTemplate)
class BannerTemplateAdmin(MBTModelAdmin):
    list_display = ('title', 'size', 'is_personalized', 'is_active', 'order', 'created')
    list_filter = ('is_active', 'size', 'is_personalized')
    search_fields = ('title', 'slug', 'description')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('slug', 'title', 'size', 'description', 'is_active', 'order')
        }),
        ('Szablon graficzny', {
            'fields': ('template_image',)
        }),
        ('Pozycja logo na banerze', {
            'fields': ('is_personalized',)
        }),
        ('Tłumaczenia (wielojęzyczne)', {
            'classes': ('collapse',),
            'fields': ('t_title', 't_description'),
            'description': TR_DESCRIPTION,
        }),
    )


@admin.register(models.BannerDownload)
class BannerDownloadAdmin(MBTModelAdmin):
    list_display = ('user_email', 'template_title_snapshot', 'downloaded_at', 'ip_address')
    list_filter = ('downloaded_at',)
    search_fields = ('user_email', 'template_title_snapshot', 'user__username')
    readonly_fields = ('user', 'user_email', 'template', 'template_title_snapshot',
                       'downloaded_at', 'ip_address', 'user_agent')
    date_hierarchy = 'downloaded_at'
    list_per_page = 50

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(models.UserProfile)
class UserProfileAdmin(MBTModelAdmin):
    list_display = ('user', 'is_kierownik', 'must_change_password', 'last_password_change')
    list_filter = ('is_kierownik', 'must_change_password')
    search_fields = ('user__username', 'user__email')


@admin.register(models.Award)
class AwardAdmin(MBTModelAdmin):
    form = mbt_forms.AwardForm
    list_display = ('miniatura', 'name', 'order', 'is_active')
    list_display_links = ('miniatura', 'name')
    list_editable = ('order', 'is_active')
    search_fields = ('name',)

    @admin.display(description='')
    def miniatura(self, obj):
        return _thumb(obj.image)


@admin.register(models.TrustedBrand)
class TrustedBrandAdmin(MBTModelAdmin):
    form = mbt_forms.TrustedBrandForm
    list_display = ('miniatura', 'name', 'order', 'is_active')
    list_display_links = ('miniatura', 'name')
    list_editable = ('order', 'is_active')
    search_fields = ('name',)

    @admin.display(description='')
    def miniatura(self, obj):
        return _thumb(obj.image)


@admin.register(models.Sector)
class SectorAdmin(MBTModelAdmin):
    form = mbt_forms.SectorForm
    list_display = ('miniatura', 'title', 'view_name', 'slug', 'order')
    list_display_links = ('miniatura', 'title')
    list_editable = ('order',)
    search_fields = ('title', 'opis')
    fieldsets = (
        ('PL', {'fields': ('title', 'view_name', 'slug', 'opis', 'icon', 'image')}),
        ('Tłumaczenia (en/cs/sk/de/hu)', {
            'classes': ('collapse',),
            'fields': ('t_title', 't_opis'),
            'description': TR_DESCRIPTION,
        }),
        ('Porządek', {'fields': ('order',)}),
    )

    @admin.display(description='')
    def miniatura(self, obj):
        return _thumb(obj.image)
