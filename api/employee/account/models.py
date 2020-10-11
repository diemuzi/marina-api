from django.db import models as django_models

from database.default import models


class AccountManager(django_models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_staff=True
        )


class Account(models.Account):
    objects = AccountManager()

    class Meta:
        default_permissions = (
            'change',
            'view'
        )

        proxy = True

        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
