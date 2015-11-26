from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #   API Endpoints
    url(r'^api/v1/', include('foodtrucks.urls',
                             namespace='foodtrucks')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
