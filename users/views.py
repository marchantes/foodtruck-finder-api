from rest_framework import generics
from users.models import *
from django.contrib.auth.models import User
from users.serializers import *


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FavList(generics.ListCreateAPIView):
    serializer_class = FavSerializer

    def perform_create(self, serializers):
        current_user = User.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=current_user)

    def dispatch(self, request, *args, **kwargs):
        self.queryset = User.objects.filter(pk=self.kwargs['pk'])
        return super(FavList, self).dispatch(request, *args, **kwargs)
