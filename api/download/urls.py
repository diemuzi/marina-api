from django.urls import path

from download import views

urlpatterns = [
    path(
        '<int:pk>/employee',
        views.DownloadEmployee.as_view(),
        name='employee'
    ),

    path(
        'all/employee',
        views.DownloadEmployeeAll.as_view(),
        name='employee-all'
    ),

    path(
        '<int:pk>/schedule',
        views.DownloadSchedule.as_view(),
        name='schedule'
    ),

    path(
        'all/schedule',
        views.DownloadScheduleAll.as_view(),
        name='schedule-all'
    )
]
