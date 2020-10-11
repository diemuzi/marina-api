from django.apps import AppConfig


class Config(AppConfig):
    label = 'default'

    name = 'database.default'

    verbose_name = 'Default Database'
