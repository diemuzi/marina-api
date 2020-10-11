from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from employee.manage import models
from employee.manage import serializers


class Create(generics.CreateAPIView):
    """
    Create account
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Account.objects.all()

    serializer_class = serializers.CreateSerializer


class Delete(generics.DestroyAPIView):
    """
    Delete account
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Account.objects.all()


class Profile(generics.RetrieveUpdateAPIView):
    """
    View account profile
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Account.objects.all()

    serializer_class = serializers.ProfileSerializer


class Search(generics.ListAPIView):
    """
    Search accounts
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Account.objects.all()

    serializer_class = serializers.SearchSerializer
