from django.db import models
from django.contrib.auth.models import User


class Fav(models.Model):
    user = models.ForeignKey(User, default=1)
    foodtruck = models.OneToOneField('foodtrucks.Foodtruck',
                                     related_name='foodtrucks')
