from django.conf.urls import url
from foodtrucks.views import *


urlpatterns = [
    url(r'^foodtrucks/$', FoodtruckList.as_view(), name='foodtrucks'),
    url(r'^foodtrucks/(?P<pk>[0-9]+)/$', FoodtruckDetail.as_view(),
        name='foodtruck_detail'),
    url(r'^foodtrucks/(?P<pk>[0-9]+)/comments/$', CommentList.as_view(),
        name='foodtruck_comments')
]
