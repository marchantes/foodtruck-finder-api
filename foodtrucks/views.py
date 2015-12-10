from rest_framework import generics, permissions
from foodtrucks.models import Foodtruck, Comment
from foodtrucks.serializers import FoodtruckSerializer, CommentSerializer
from foodtrucks.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class FoodtruckList(generics.ListCreateAPIView):
    permission_classes = (
                          permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,
                          )
    queryset = Foodtruck.objects.all()
    serializer_class = FoodtruckSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
            )
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FoodtruckDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
                          permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,
                          )
    queryset = Foodtruck.objects.all()
    serializer_class = FoodtruckSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
            )
        self.check_object_permissions(self.request, obj)
        return obj


class CommentList(generics.ListCreateAPIView):
    permission_classes = (
                          permissions.IsAuthenticatedOrReadOnly,
                          )
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        current_foodtruck = Foodtruck.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, foodtruck=current_foodtruck)

    def dispatch(self, request, *args, **kwargs):
        self.queryset = Comment.objects.filter(foodtruck=self.kwargs['pk'])
        return super(CommentList, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
            )
        self.check_object_permissions(self.request, obj)
        return obj
