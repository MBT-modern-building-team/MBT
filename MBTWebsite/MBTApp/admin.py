"""Panel admina MBT — zarządzanie treścią strony.

Wejdź na /admin (login: superuser). Zdjęcia wgrywasz przyciskiem
„Wybierz plik…" — bez wpisywania ścieżek (lokalnie: MEDIA/uploads,
na Vercel: Vercel Blob).
"""
from django.contrib import admin
from MBTApp import models
from MBTApp import forms as mbt_forms

admin.site.site_header = 'MBT — panel zarządzania'
admin.site.site_title = 'MBT CMS'
admin.site.index_title = 'Zarządzaj treścią strony'


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    form = mbt_forms.ProjectForm
    list_display = ('title', 'type', 'status', 'order')
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
            'description': 'JSON {lang: text}. Puste = pokaż tekst polski. Format: {"en":"...","de":"...","cs":"...","sk":"...","hu":"..."}.',
        }),
        ('Zdjęcia', {
            'fields': ('hero', 'logo', 'gallery'),
            'description': 'Wybierz plik z dysku albo wklej URL zdjęcia.',
        }),
        ('Porządek', {'fields': ('order',)}),
    )


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('order',)
    fieldsets = (
        ('PL', {'fields': ('title', 'slug', 'text')}),
        ('Tłumaczenia (en/cs/sk/de/hu)', {
            'classes': ('collapse',),
            'fields': ('t_title', 't_text'),
            'description': 'JSON {lang: text}. Puste = pokaż tekst polski.',
        }),
        ('Porządek', {'fields': ('order',)}),
    )


@admin.register(models.Worker)
class WorkerAdmin(admin.ModelAdmin):
    form = mbt_forms.WorkerForm
    list_display = ('name', 'position', 'order')
    search_fields = ('name', 'position')
    list_editable = ('order',)
    fieldsets = (
        ('PL', {'fields': ('name', 'position', 'opis', 'photo', 'linkedin')}),
        ('Tłumaczenia (en/cs/sk/de/hu)', {
            'classes': ('collapse',),
            'fields': ('t_position', 't_opis'),
            'description': 'JSON {lang: text}. Puste = pokaż tekst polski.',
        }),
        ('Porządek', {'fields': ('order',)}),
    )


@admin.register(models.SalesRepresentative)
class SalesRepresentativeAdmin(admin.ModelAdmin):
    form = mbt_forms.SalesRepresentativeForm
    list_display = ('name', 'position', 'email', 'phone', 'order')
    search_fields = ('name', 'position', 'email', 'phone')
    list_editable = ('order',)
    fieldsets = (
        ('PL', {'fields': ('name', 'position', 'email', 'phone', 'photo')}),
        ('Tłumaczenia (en/cs/sk/de/hu)', {
            'classes': ('collapse',),
            'fields': ('t_position',),
            'description': 'JSON {lang: text}. Puste = pokaż tekst polski.',
        }),
        ('Porządek', {'fields': ('order',)}),
    )


@admin.register(models.Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('firma', 'osoba', 'stanowisko', 'order')
    search_fields = ('firma', 'osoba', 'tresc')
    list_editable = ('order',)
    fieldsets = (
        ('PL', {'fields': ('firma', 'osoba', 'stanowisko', 'tresc')}),
        ('Tłumaczenia (en/cs/sk/de/hu)', {
            'classes': ('collapse',),
            'fields': ('t_osoba', 't_stanowisko', 't_tresc'),
            'description': 'JSON {lang: text}. Puste = pokaż tekst polski.',
        }),
        ('Porządek', {'fields': ('order',)}),
    )


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    form = mbt_forms.ArticleForm
    list_display = ('title', 'published', 'created')
    list_filter = ('published',)
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('published',)
    fieldsets = (
        ('PL', {'fields': ('title', 'slug', 'excerpt', 'text', 'image', 'gallery', 'published')}),
        ('Tłumaczenia (en/cs/sk/de/hu)', {
            'classes': ('collapse',),
            'fields': ('t_title', 't_excerpt', 't_text'),
            'description': 'JSON {lang: text}. Puste = pokaż tekst polski.',
        }),
        ('Porządek', {'fields': ('order',)}),
    )


@admin.register(models.SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
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
        ('Social media', {'fields': ('social_linkedin', 'social_youtube', 'social_facebook')}),
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
class SitePhotosAdmin(admin.ModelAdmin):
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
class BannerTemplateAdmin(admin.ModelAdmin):
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
        }),
    )


@admin.register(models.BannerDownload)
class BannerDownloadAdmin(admin.ModelAdmin):
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
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_kierownik', 'must_change_password', 'last_password_change')
    list_filter = ('is_kierownik', 'must_change_password')
    search_fields = ('user__username', 'user__email')
@admin.register(models.Award)
class AwardAdmin(admin.ModelAdmin):
    form = mbt_forms.AwardForm
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name',)


@admin.register(models.Sector)
class SectorAdmin(admin.ModelAdmin):
    form = mbt_forms.SectorForm
    list_display = ('title', 'view_name', 'slug', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'opis')
    fieldsets = (
        ('PL', {'fields': ('title', 'view_name', 'slug', 'opis', 'icon', 'image')}),
        ('Tłumaczenia (en/cs/sk/de/hu)', {
            'classes': ('collapse',),
            'fields': ('t_title', 't_opis'),
        }),
        ('Porządek', {'fields': ('order',)}),
    )
