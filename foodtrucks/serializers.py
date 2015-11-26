from foodtrucks.models import *
from rest_framework import serializers


class FoodtruckSerializer(serializers.ModelSerializer):

    location_object = serializers.ReadOnlyField(source='location_parser',
                                                read_only=True)

    class Meta:
        model = Foodtruck
        fields = ('id', 'facebook', 'food_type',
                  'location', 'name', 'photo', 'price',
                  'rating', 'twitter', 'location_object')
