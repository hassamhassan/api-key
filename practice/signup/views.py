from rest_framework import generics
from rest_framework import permissions

from signup.models import SignUp, KeyCredential
from signup.serializers import SignUpSerializer


class ApiKeyPermission(permissions.BasePermission):
    """
    Global permission check for API_KEY and save the REMOTE_ADDRESS.
    """

    def has_permission(self, request, view):
        """
        This method extracts the remote address and api key from Http request
        and check in key is present in predefined keys then add a record to
        KeyCredentials model.
        :param request: Http request object
        :param view: Calling view
        :return: Boolean
        """
        ip_addr = request.META['REMOTE_ADDR']
        api_key = request.META['HTTP_AUTHORIZATION']
        if api_key in ['Basic aGFzc2FtOmx6dDEyMzQ1',
                       'Basic d2FxYXI6bHp0MTIzNDU=']:
            key_cred = KeyCredential(api_key=api_key, remote_addr=ip_addr)
            key_cred.save()
            return True
        return False


class SignUpList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, ApiKeyPermission)
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer

    def perform_create(self, serializer):
        """
        THis method allows us to modify how the instance save is managed.
        :param serializer: instance of SignUpSerializer
        :return: None
        """
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        THis method allows to filter on the basis of logged in user
        :return: filtered SignUp objects
        """
        user = self.request.user
        return SignUp.objects.filter(owner=user)
