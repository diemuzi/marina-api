from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from employee.account import models
from employee.account import serializers


class Password(generics.RetrieveUpdateAPIView):
    """
    Update account password
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Account.objects.all()

    serializer_class = serializers.PasswordSerializer

    def get_object(self):
        return models.Account.objects.get(
            pk=self.request.user.pk
        )


class Profile(generics.RetrieveUpdateAPIView):
    """
    View account profile
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Account.objects.all()

    serializer_class = serializers.ProfileSerializer

    def get_object(self):
        return models.Account.objects.get(
            pk=self.request.user.pk
        )
