from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from schedule import models
from schedule import serializers


class Create(generics.CreateAPIView):
    """
    Create schedule
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.CreateSerializer


class Delete(generics.DestroyAPIView):
    """
    Delete schedule
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Schedule.objects.all()


class Profile(generics.RetrieveUpdateAPIView):
    """
    View schedule profile
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.ProfileSerializer


class Search(generics.ListAPIView):
    """
    Search schedules
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.SearchSerializer
