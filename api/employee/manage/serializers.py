from django.contrib.auth.base_user import BaseUserManager
from rest_framework import serializers

from employee.manage import models


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account

        fields = [
            'first_name',
            'last_name'
        ]

    def create(self, validated_data):
        password = BaseUserManager().make_random_password()

        user = super(CreateSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account

        fields = [
            'id',
            'first_name',
            'is_active',
            'last_name'
        ]


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account

        fields = [
            'id',
            'first_name',
            'is_active',
            'last_name'
        ]
