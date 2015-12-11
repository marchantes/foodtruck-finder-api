from rest_framework import serializers
from users.models import *
from foodtrucks.models import Foodtruck
from foodtrucks.serializers import FoodtruckSerializer


class FavCreateSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.email')
    foodtruck = serializers.PrimaryKeyRelatedField(
            queryset=Foodtruck.objects.all(),
        )

    class Meta:
        model = Fav
        fields = ('id', 'user', 'foodtruck')


class FavListSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.email')
    foodtruck = FoodtruckSerializer(read_only=True)

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
