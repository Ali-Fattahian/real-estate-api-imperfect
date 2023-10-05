from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
import os

urlpatterns = [
    path(os.getenv('ADMIN_URL'), admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
