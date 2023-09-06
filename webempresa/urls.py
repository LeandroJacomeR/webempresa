from django.contrib import admin
from django.urls import path, include
from core import urls as core_urls
from services import urls as services_urls
from blog import urls as blog_url
from social import urls as social_urls
from pages import urls as pages_urls
from contact import urls as contact_urls

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urls)),
    path('', include(services_urls)),
    path('', include(blog_url)),
    path('', include(social_urls)),
    path('', include(pages_urls)),
    path('', include(contact_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)