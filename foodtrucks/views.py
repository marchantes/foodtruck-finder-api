from rest_framework import generics
from foodtrucks.models import Foodtruck
from foodtrucks.serializers import FoodtruckSerializer


class FoodtruckList(generics.ListCreateAPIView):
    queryset = Foodtruck.objects.all()
    serializer_class = FoodtruckSerializer


class FoodtruckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Foodtruck.objects.all()
    serializer_class = FoodtruckSerializer
