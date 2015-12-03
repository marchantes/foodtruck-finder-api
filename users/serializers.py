from rest_framework import serializers
from users.models import *


class FavSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fav
        fields = ('id', 'user', 'foodtruck')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'profile_picture', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
