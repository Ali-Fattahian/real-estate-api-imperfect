import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "real_estate_backend.settings.development"
)

application = get_wsgi_application()
