from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #   API Endpoints
    url(r'^api/v1/', include('foodtrucks.urls',
                             namespace='foodtrucks')),
]
