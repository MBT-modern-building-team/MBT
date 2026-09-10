"""
URL routing for the language switcher.

Pozwala {% url 'set_language' %} z header.html odwoływać się do naszego
własnego widoku z i18n_views.py (zamiast wbudowanego django.views.i18n.set_language),
który poprawnie tłumaczy URL-e w obie strony — szczególnie przy PREFIX_DEFAULT_LANGUAGE=False,
gdy aktywny język (np. pl) nie ma prefiksu URL.
"""
from django.urls import path

from .i18n_views import set_language

urlpatterns = [
    path('', set_language, name='set_language'),
]