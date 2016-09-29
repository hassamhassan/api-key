from rest_framework import permissions

SAFER_METHODS = ('HEAD', 'OPTIONS')


class OwnerOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        """
        This method checks whether the request method is in SAFER_METHODS
        if not then allow only to owner to view and write only.
        """
        if request.method in SAFER_METHODS:
            return True

        # Write permissions are only allowed to the owner of the signup.
        return obj.owner == request.user
