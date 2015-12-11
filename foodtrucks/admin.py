from django.contrib import admin
from foodtrucks.models import *


@admin.register(Foodtruck)
class FoodtruckAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['city', 'facebook', 'food_type',
                                    'location', 'name', 'photo', 'price',
                                    'socre', 'twitter']}
         )
    ]
    list_display = ('id', 'city', 'facebook', 'food_type',
                    'location', 'name', 'photo', 'price',
                    'score', 'average_rating', 'twitter')
