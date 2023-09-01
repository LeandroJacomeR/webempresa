from django.contrib import admin
from django.urls import path, include
from core import urls as core_urls

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urls))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)