from django.apps import AppConfig


class Config(AppConfig):
    label = 'schedule'

    name = label

    verbose_name = 'Schedule'
