from django.conf.urls import url
from users.views import *

urlpatterns = [
    url(r'^users/$', UserList.as_view(), name='user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user_detail'),
    url(r'^users/(?P<pk>[0-9]+)/favs/$', FavList.as_view(), name='user_favs'),
]
