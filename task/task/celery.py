from __future__ import absolute_import, unicode_literals
from celery import Celery
import os, sys
import dotenv
from os.path import dirname, join

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task.settings")
app = Celery('task',
             broker='amqp://root:lusine_admin@rabbit',
             backend='amqp://',
             include=['task.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')
# app.loader.override_backends['django-db'] = 'django_celery_results.backends.database:DatabaseBackend'

if __name__ == '__main__':
    app.start()