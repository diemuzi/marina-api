from django.db import models as django_models

from database.default import models


class AccountManager(django_models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_active=True,
            is_superuser=False
        )


class Account(models.Account):
    objects = AccountManager()

    class Meta:
        proxy = True

        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'


class ScheduleManager(django_models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_active=True
        )


class Schedule(models.Schedule):
    objects = ScheduleManager()

    class Meta:
        proxy = True

        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
