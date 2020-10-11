from django.urls import path

from employee.account import views

urlpatterns = [
    path(
        'password',
        views.Password.as_view(),
        name='password'
    ),

    path(
        'profile',
        views.Profile.as_view(),
        name='profile'
    )
]
