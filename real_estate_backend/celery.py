from __future__ import absolute_import
import os


from celery import Celery
from real_estate_backend.settings import base

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "real_estate_backend.settings.development"
)

app = Celery("real_estate_website")

app.config_from_object("real_estate_backend.settings.development", namespace="CELERY")

app.autodiscover(lambda: base.INSTALLED_APPS)
