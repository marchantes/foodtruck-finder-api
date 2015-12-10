from foodtrucks.models import *
from rest_framework import serializers


class FoodtruckSerializer(serializers.ModelSerializer):

    location_object = serializers.ReadOnlyField(source='location_parser')
    score = serializers.ChoiceField(
            choices=[1, 2, 3, 4, 5]
        )
    owner = serializers.ReadOnlyField(source='owner.email')
    rating = serializers.ReadOnlyField(source='average_rating')
    votes = serializers.ReadOnlyField()

    class Meta:
        model = Foodtruck
        fields = ('id', 'facebook', 'food_type',
                  'location', 'name', 'owner', 'photo', 'price',
                  'rating', 'score', 'twitter', 'location_object', 'votes')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    foodtruck = serializers.ReadOnlyField(source='foodtruck.id')

    class Meta:
        model = Comment
        fields = ('id', 'user', 'foodtruck', 'comment', 'date_added', 'likes')
