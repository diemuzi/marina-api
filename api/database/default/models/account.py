from django.core import validators
from django.db import models
from model_utils import FieldTracker

from database.default.models import manager


class Account(manager.AbstractBaseUser):
    email = models.EmailField(
        blank=False,
        null=True,
        unique=True,
        validators=[
            validators.MinLengthValidator(5),
            validators.EmailValidator
        ]
    )

    first_name = models.CharField(
        blank=False,
        max_length=255,
        null=False,
        validators=[
            validators.RegexValidator('^[a-zA-Z .\'-]+$')
        ]
    )

    is_staff = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    last_name = models.CharField(
        blank=False,
        max_length=255,
        null=False,
        validators=[
            validators.RegexValidator('^[a-zA-Z .\'-]+$')
        ]
    )

    schedule_friday = models.ForeignKey(
        'Schedule',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='schedule_friday'
    )

    schedule_monday = models.ForeignKey(
        'Schedule',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='schedule_monday'
    )

    schedule_saturday = models.ForeignKey(
        'Schedule',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='schedule_saturday'
    )

    schedule_sunday = models.ForeignKey(
        'Schedule',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='schedule_sunday'
    )

    schedule_thursday = models.ForeignKey(
        'Schedule',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='schedule_thursday'
    )

    schedule_tuesday = models.ForeignKey(
        'Schedule',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='schedule_tuesday'
    )

    schedule_wednesday = models.ForeignKey(
        'Schedule',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='schedule_wednesday'
    )

    tracker = FieldTracker()

    REQUIRED_FIELDS = [
        'first_name',
        'last_name'
    ]

    USERNAME_FIELD = 'email'

    objects = manager.UserManager()

    class Meta:
        db_table = 'account'

        default_permissions = ()

        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def friday(self):
        return {
            'has_break': self.schedule_friday.has_break,
            'name': self.schedule_friday.name,
            'time_start': self.schedule_friday.time_start,
            'time_end': self.schedule_friday.time_end
        }

    @property
    def monday(self):
        return {
            'has_break': self.schedule_monday.has_break,
            'name': self.schedule_monday.name,
            'time_start': self.schedule_monday.time_start,
            'time_end': self.schedule_monday.time_end
        }

    @property
    def saturday(self):
        return {
            'has_break': self.schedule_saturday.has_break,
            'name': self.schedule_saturday.name,
            'time_start': self.schedule_saturday.time_start,
            'time_end': self.schedule_saturday.time_end
        }

    @property
    def sunday(self):
        return {
            'has_break': self.schedule_sunday.has_break,
            'name': self.schedule_sunday.name,
            'time_start': self.schedule_sunday.time_start,
            'time_end': self.schedule_sunday.time_end
        }

    @property
    def thursday(self):
        return {
            'has_break': self.schedule_thursday.has_break,
            'name': self.schedule_thursday.name,
            'time_start': self.schedule_thursday.time_start,
            'time_end': self.schedule_thursday.time_end
        }

    @property
    def tuesday(self):
        return {
            'has_break': self.schedule_tuesday.has_break,
            'name': self.schedule_tuesday.name,
            'time_start': self.schedule_tuesday.time_start,
            'time_end': self.schedule_tuesday.time_end
        }

    @property
    def wednesday(self):
        return {
            'has_break': self.schedule_wednesday.has_break,
            'name': self.schedule_wednesday.name,
            'time_start': self.schedule_wednesday.time_start,
            'time_end': self.schedule_wednesday.time_end
        }
