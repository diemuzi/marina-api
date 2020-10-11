from rest_framework import views
from rest_framework.permissions import IsAdminUser

from download import excel


class DownloadEmployee(views.APIView):
    """
    Download employee schedule
    """

    permission_classes = (
        IsAdminUser,
    )

    def get(self, request, pk):
        return excel.generate_employee(
            account_id=pk
        )


class DownloadEmployeeAll(views.APIView):
    """
    Download all employee schedules
    """

    permission_classes = (
        IsAdminUser,
    )

    def get(self, request):
        return excel.generate_employee_all()


class DownloadSchedule(views.APIView):
    """
    Download employee schedule
    """

    permission_classes = (
        IsAdminUser,
    )

    def get(self, request, pk):
        return excel.generate_schedule(
            schedule_id=pk
        )


class DownloadScheduleAll(views.APIView):
    """
    Download all employee schedules
    """

    permission_classes = (
        IsAdminUser,
    )

    def get(self, request):
        return excel.generate_schedule_all()
