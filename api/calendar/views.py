from rest_framework import generics
from rest_framework import views
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from calendar import models
from calendar import serializers


class Account(generics.ListAPIView):
    """
    Search calendar by account
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Account.objects.all()

    serializer_class = serializers.AccountSerializer


class AccountProfile(generics.RetrieveUpdateAPIView):
    """
    Account profile
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Account.objects.all()

    serializer_class = serializers.AccountProfileSerializer


class Choices(views.APIView):
    """
    View available choices
    """

    permission_classes = (
        IsAdminUser,
    )

    def get(self, request):
        result = {}

        # Schedules
        for schedule in models.Schedule.objects.all():
            result.update({
                schedule.pk: f"{schedule.name} - {schedule.time_start} - {schedule.time_end}"
            })

        return Response(result)


class Schedule(generics.ListAPIView):
    """
    Search calendar by schedule
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.ScheduleSerializer


class ScheduleAccounts(generics.ListAPIView):
    """
    Schedule Accounts
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Account.objects.all()

    serializer_class = serializers.ScheduleAccountSerializer


class ScheduleFriday(generics.RetrieveUpdateAPIView):
    """
    Schedule Friday
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.ScheduleFridaySerializer


class ScheduleMonday(generics.RetrieveUpdateAPIView):
    """
    Schedule Monday
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.ScheduleMondaySerializer


class ScheduleSaturday(generics.RetrieveUpdateAPIView):
    """
    Schedule Saturday
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.ScheduleSaturdaySerializer


class ScheduleSunday(generics.RetrieveUpdateAPIView):
    """
    Schedule Sunday
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.ScheduleSundaySerializer


class ScheduleThursday(generics.RetrieveUpdateAPIView):
    """
    Schedule Thursday
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.ScheduleThursdaySerializer


class ScheduleTuesday(generics.RetrieveUpdateAPIView):
    """
    Schedule Tuesday
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.ScheduleTuesdaySerializer


class ScheduleWednesday(generics.RetrieveUpdateAPIView):
    """
    Schedule Wednesday
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.ScheduleWednesdaySerializer
