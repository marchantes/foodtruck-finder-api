from rest_framework import serializers
from users.models import *


class FavSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fav
        fields = ('id', 'user', 'foodtruck')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'profile_picture_url')
