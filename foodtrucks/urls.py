from django.conf.urls import include, url
from foodtrucks.views import *


urlpatterns = [
    url(r'^foodtrucks/', FoodtruckList.as_view(), name='entry'),
]
