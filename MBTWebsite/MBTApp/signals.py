"""Sygnały Django — automatyczna regeneracja mbt_data.py po zapisie w CMS.

Gdy w adminie zapiszesz dowolny model (realizację, artykuł, pracownika...),
ten moduł odtwarza MBTApp/mbt_data.py z bazy. Dzięki temu Vercel (który nie
ma bazy SQLite) po Twoim `git push` pokazuje te same dane co localhost.
"""
import os
import subprocess
import sys
import threading

from django.db import transaction
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from MBTApp.models import Article, Job, Project, Reference, SiteConfig, SitePhotos, Worker, SalesRepresentative, Award

# Zabezpieczenie przed rekurencją: generator importuje mbt_data przy braku
# rekordu SiteConfig — ale nie zapisuje nic do bazy, więc nie wywoła sygnału.
_GENERATING = False


def _regenerate():
    global _GENERATING
    if _GENERATING:
        return
    _GENERATING = True
    try:
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        script = os.path.join(base, 'scripts', 'gen_mbt_data.py')
        python = sys.executable
        env = dict(os.environ)
        env.pop('PYTHONPATH', None)
        proc = subprocess.run(
            [python, script],
            capture_output=True, text=True, timeout=60,
            cwd=base, env=env,
        )
        if proc.returncode != 0:
            print(f'[signals] regeneracja mbt_data.py NIEUDANA: {proc.stderr[-300:]}')
        else:
            print('[signals] mbt_data.py zregenerowany po zapisie w CMS')
    except Exception as e:
        print(f'[signals] błąd regeneracji mbt_data.py: {e}')
    finally:
        _GENERATING = False


def _async_regenerate():
    t = threading.Thread(target=_regenerate, daemon=True)
    t.start()


_MODELS = (Project, Job, Worker, Reference, Article, SiteConfig, SitePhotos)


@receiver(post_save, sender=Project)
@receiver(post_save, sender=Job)
@receiver(post_save, sender=Worker)
@receiver(post_save, sender=Reference)
@receiver(post_save, sender=Article)
@receiver(post_save, sender=SiteConfig)
@receiver(post_save, sender=SitePhotos)
@receiver(post_save, sender=SalesRepresentative)
@receiver(post_save, sender=Award)
@receiver(post_delete, sender=Project)
@receiver(post_delete, sender=Job)
@receiver(post_delete, sender=Worker)
@receiver(post_delete, sender=Reference)
@receiver(post_delete, sender=Article)
@receiver(post_delete, sender=SiteConfig)
@receiver(post_delete, sender=SitePhotos)
@receiver(post_delete, sender=SalesRepresentative)
@receiver(post_delete, sender=Award)
def _on_change(sender, **kwargs):
    transaction.on_commit(_async_regenerate)
