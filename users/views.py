from rest_framework import generics, permissions
from users.models import *
from users.serializers import UserSerializer, FavSerializer
from users.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404


class UserList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
            )
        self.check_object_permissions(self.request, obj)
        return obj


class FavList(generics.ListCreateAPIView):
    permission_classes = (
                          permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,
                          )
    serializer_class = FavSerializer

    def perform_create(self, serializers):
        current_user = UserProfile.objects.get(pk=self.kwargs['pk'])
        serializers.save(user=current_user)

    def dispatch(self, request, *args, **kwargs):
        self.queryset = Fav.objects.filter(user=self.kwargs['pk'])
        return super(FavList, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
            )
        self.check_object_permissions(self.request, obj)
        return obj
