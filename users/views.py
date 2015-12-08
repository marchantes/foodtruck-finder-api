from rest_framework import generics, permissions
from users.models import *
from users.serializers import UserSerializer, FavSerializer
from users.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response


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

    def handle_exception(self, exc):
        e = str(exc)
        # Handle error if foodtruck is already in user's favorites
        if 'unique constraint failed' in e.lower():
            exc.status_code = status.HTTP_406_NOT_ACCEPTABLE
            data = {'detail': 'Foodtruck already in favorites.'}
            return Response(data, exc.status_code)

        exception_handler = self.settings.EXCEPTION_HANDLER

        context = self.get_exception_handler_context()
        response = exception_handler(exc, context)

        if response is None:
            raise

        response.exception = True
        return response


class FavDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
                          permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,
                          )
    lookup_field = "fav_pk"
    lookup_url_kwarg = "fav_pk"
    serializer_class = FavSerializer
    queryset = Fav.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['fav_pk'],
            )
        self.check_object_permissions(self.request, obj)
        return obj
