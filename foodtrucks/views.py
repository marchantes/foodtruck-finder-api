from rest_framework import generics
from foodtrucks.models import Foodtruck, Comment
from foodtrucks.serializers import FoodtruckSerializer, CommentSerializer


class FoodtruckList(generics.ListCreateAPIView):
    queryset = Foodtruck.objects.all()
    serializer_class = FoodtruckSerializer


class FoodtruckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Foodtruck.objects.all()
    serializer_class = FoodtruckSerializer


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        current_foodtruck = Foodtruck.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, foodtruck=current_foodtruck)

    def dispatch(self, request, *args, **kwargs):
        self.queryset = Comment.objects.filter(foodtruck=self.kwargs['pk'])
        return super(CommentList, self).dispatch(request, *args, **kwargs)
