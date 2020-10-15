# Generated by Django 3.1.2 on 2020-10-15 14:11

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('default', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
                'proxy': True,
                'default_permissions': ('change', 'view'),
                'indexes': [],
                'constraints': [],
            },
            bases=('default.account',),
        ),
    ]
