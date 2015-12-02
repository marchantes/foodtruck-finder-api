from foodtrucks.models import *
from rest_framework import serializers


class FoodtruckSerializer(serializers.ModelSerializer):

    location_object = serializers.ReadOnlyField(source='location_parser',
                                                read_only=True)
    rating = serializers.ChoiceField(
            choices=[1, 2, 3, 4, 5]
        )

    class Meta:
        model = Foodtruck
        fields = ('id', 'facebook', 'food_type',
                  'location', 'name', 'photo', 'price',
                  'rating', 'twitter', 'location_object')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    foodtruck = serializers.ReadOnlyField(source='foodtruck.id')

    class Meta:
        model = Comment
        fields = ('id', 'user', 'foodtruck', 'comment', 'date_added', 'likes')
