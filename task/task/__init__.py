from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app
import os
import sys


def add_path(path):
    if path not in sys.path: sys.path.insert(0, path)


add_path(os.path.join(os.path.dirname(__file__), 'swagger_doc', 'swagger_schema'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task.settings")
__all__ = ('celery_app',)