# Generated by Django 3.1.2 on 2020-10-15 14:11

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('default', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
            ],
            options={
                'verbose_name': 'Schedule',
                'verbose_name_plural': 'Schedules',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('default.schedule',),
        ),
    ]
