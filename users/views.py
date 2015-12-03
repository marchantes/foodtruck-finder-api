from rest_framework import generics, permissions
from users.models import *
from users.serializers import UserSerializer, FavSerializer


class UserList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class FavList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = FavSerializer

    def perform_create(self, serializers):
        current_user = UserProfile.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=current_user)

    def dispatch(self, request, *args, **kwargs):
        self.queryset = UserProfile.objects.filter(pk=self.kwargs['pk'])
        return super(FavList, self).dispatch(request, *args, **kwargs)
