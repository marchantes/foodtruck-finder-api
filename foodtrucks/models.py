from django.db import models
from location_field.models.plain import PlainLocationField
from users.models import UserProfile


class Foodtruck(models.Model):
    city = models.CharField(max_length=50, default='Mexico City')
    facebook = models.URLField()
    food_type = models.CharField(max_length=100)
    location = PlainLocationField(based_fields=[city], zoom=7)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(UserProfile)
    photo = models.ImageField(upload_to='img/foodtrucks/', blank=True)
    price = models.PositiveIntegerField(default=0)
    score = models.PositiveIntegerField(default=0)
    twitter = models.URLField()
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "\nName: {}\nRating: {}\nFoodtype: {}\n".format(self.name,
                                                               self.average_rating,
                                                               self.food_type)

    @property
    def location_parser(self):
        location_object = {}
        if ',' in self.location:
            data = self.location.split(',')
            location_object['lat'] = float(data[0])
            location_object['long'] = float(data[1])
            return location_object
        else:
            return "No available location."

    @property
    def average_rating(self):
        try:
            rating = self.score / self.votes
            return round(rating, 1)
        except:
            return 0

    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = Foodtruck.objects.get(pk=self.pk)
            if orig.score != self.score:
                new_score = orig.score + self.score
                self.votes += 1
                self.score = new_score
        super(Foodtruck, self).save(*args, **kwargs)


class Comment(models.Model):
    foodtruck = models.ForeignKey('Foodtruck')
    user = models.ForeignKey(UserProfile)
    comment = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0, null=True)
