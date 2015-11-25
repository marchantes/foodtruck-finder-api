from django.db import models
from location_field.models.plain import PlainLocationField


class Foodtruck(models.Model):
    city = models.CharField(max_length=50)
    facebook = models.URLField()
    food_type = models.CharField(max_length=100)
    location = PlainLocationField(based_fields=[city], zoom=7)
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    price = models.IntegerField()
    rating = models.IntegerField()
    twitter = models.URLField()
