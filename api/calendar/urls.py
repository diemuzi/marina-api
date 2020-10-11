from django.urls import path

from calendar import views

urlpatterns = [
    path(
        'account',
        views.Account.as_view(),
        name='account'
    ),

    path(
        'account/profile/<int:pk>',
        views.AccountProfile.as_view(),
        name='account-profile'
    ),

    path(
        'choices',
        views.Choices.as_view(),
        name='choices'
    ),

    path(
        'schedule',
        views.Schedule.as_view(),
        name='schedule'
    ),

    path(
        'schedule/accounts',
        views.ScheduleAccounts.as_view(),
        name='schedule/accounts'
    ),

    path(
        'schedule/<int:pk>/friday',
        views.ScheduleFriday.as_view(),
        name='schedule-friday'
    ),

    path(
        'schedule/<int:pk>/monday',
        views.ScheduleMonday.as_view(),
        name='schedule-monday'
    ),

    path(
        'schedule/<int:pk>/saturday',
        views.ScheduleSaturday.as_view(),
        name='schedule-saturday'
    ),

    path(
        'schedule/<int:pk>/sunday',
        views.ScheduleSunday.as_view(),
        name='schedule-sunday'
    ),

    path(
        'schedule/<int:pk>/thursday',
        views.ScheduleThursday.as_view(),
        name='schedule-thursday'
    ),

    path(
        'schedule/<int:pk>/tuesday',
        views.ScheduleTuesday.as_view(),
        name='schedule-tuesday'
    ),

    path(
        'schedule/<int:pk>/wednesday',
        views.ScheduleWednesday.as_view(),
        name='schedule-wednesday'
    )
]
