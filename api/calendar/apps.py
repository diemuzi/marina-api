from django.apps import AppConfig


class Config(AppConfig):
    label = 'calendar'

    name = label

    verbose_name = 'Calendar'
