from django.conf import settings
from django.conf.urls import include
from django.urls import path
from rest_framework.schemas import get_schema_view

urlpatterns = [
    # Marina URLs
    path('calendar/', include('calendar.urls')),
    path('download/', include('download.urls')),
    path('employee/account/', include('employee.account.urls')),
    path('employee/manage/', include('employee.manage.urls')),
    path('schedule/', include('schedule.urls')),

    # Rest API URLs
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),

    # API Documentation
    path('openapi', get_schema_view(title="Marina API"), name='openapi-schema')
]

# Debug Settings
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
