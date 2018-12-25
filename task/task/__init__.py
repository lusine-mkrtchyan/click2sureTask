from __future__ import absolute_import, unicode_literals

import os

from .celery import app as celery_app


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task.settings")
__all__ = ('celery_app',)