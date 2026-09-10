from django.apps import AppConfig


class MbtAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MBTApp'

    def ready(self):
        # Sygnały: po zapisie w CMS automatycznie regenerują mbt_data.py
        # (fallback dla Vercel — patrz MBTApp/signals.py)
        import MBTApp.signals  # noqa: F401
