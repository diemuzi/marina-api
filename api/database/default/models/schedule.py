from django.conf import settings
from django.core import validators
from django.db import models
from model_utils import FieldTracker


class Schedule(models.Model):
    account_friday = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        limit_choices_to={
            'is_active': True,
            'is_superuser': False
        },
        related_name='account_friday'
    )

    account_monday = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        limit_choices_to={
            'is_active': True,
            'is_superuser': False
        },
        related_name='account_monday'
    )

    account_saturday = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        limit_choices_to={
            'is_active': True,
            'is_superuser': False
        },
        related_name='account_saturday'
    )

    account_sunday = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        limit_choices_to={
            'is_active': True,
            'is_superuser': False
        },
        related_name='account_sunday'
    )

    account_thursday = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        limit_choices_to={
            'is_active': True,
            'is_superuser': False
        },
        related_name='account_thursday'
    )

    account_tuesday = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        limit_choices_to={
            'is_active': True,
            'is_superuser': False
        },
        related_name='account_tuesday'
    )

    account_wednesday = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        limit_choices_to={
            'is_active': True,
            'is_superuser': False
        },
        related_name='account_wednesday'
    )

    has_break = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    name = models.CharField(
        blank=False,
        max_length=255,
        null=False,
        unique=True,
        validators=[
            validators.RegexValidator('^[a-zA-Z0-9 _.\'-]+$')
        ]
    )

    time_end = models.TimeField(
        blank=False,
        null=False
    )

    time_start = models.TimeField(
        blank=False,
        null=False
    )

    tracker = FieldTracker()

    class Meta:
        db_table = 'schedule'

        default_permissions = ()

        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'

    def __str__(self):
        return self.name
