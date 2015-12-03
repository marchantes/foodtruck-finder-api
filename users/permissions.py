from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        """
        For some reason this only works with the ID's of both objects
        If it is made with emails,
        it will deny every write action in the API
        """
        return obj.id == request.user.id
