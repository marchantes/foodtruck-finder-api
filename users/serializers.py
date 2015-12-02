from rest_framework import serializers
from users.models import *
from django.contrib.auth.models import User
from foodtrucks.models import Foodtruck


class FavSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fav
        fields = ('id', 'user', 'foodtruck')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')
