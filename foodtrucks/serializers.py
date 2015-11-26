from foodtrucks.models import *
from rest_framework import serializers


class FoodtruckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Foodtruck
        fields = ('id', 'facebook', 'food_type',
                  'location', 'name', 'photo', 'price',
                  'rating', 'twitter')
