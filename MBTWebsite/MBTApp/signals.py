"""Sygnały Django — odświeżanie danych publicznej strony po zapisie w CMS.

Dane z bazy czytane są przez MBTApp.mbt_orm z krótkim cache'em w pamięci
procesu. Po zapisie/usunięciu dowolnego modelu treści czyścimy ten cache, żeby
zmiana z panelu admina była widoczna od razu (w tym procesie). Inne instancje
(np. funkcje Vercel) odświeżą się po CACHE_TTL, a CDN po PUBLIC_PAGE_CACHE_SECONDS.
"""
import logging

from django.db import transaction
from django.db.models.signals import post_delete, post_save

from MBTApp.models import (
    Article, Award, Job, Project, Reference, SalesRepresentative, Sector,
    SiteConfig, SitePhotos, TrustedBrand, Worker,
)

logger = logging.getLogger(__name__)

_MODELS = (
    Project, Job, Worker, Reference, Article, SiteConfig, SitePhotos,
    SalesRepresentative, Award, Sector, TrustedBrand,
)


def _clear_cache():
    from MBTApp import mbt_orm
    mbt_orm._CACHE.clear()


def _on_change(sender, **kwargs):
    # Po commicie, żeby kolejny odczyt widział już zapisane dane.
    transaction.on_commit(_clear_cache)


for _model in _MODELS:
    post_save.connect(_on_change, sender=_model, dispatch_uid=f'mbt_cache_save_{_model.__name__}')
    post_delete.connect(_on_change, sender=_model, dispatch_uid=f'mbt_cache_delete_{_model.__name__}')
