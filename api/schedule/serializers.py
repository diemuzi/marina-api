from rest_framework import serializers

from schedule import models


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule

        fields = '__all__'

    def validate_name(self, value):
        if models.Schedule.objects.filter(
                name__iexact=value
        ).exists():
            raise serializers.ValidationError(
                'Name already exists.',
                code='exists'
            )

        return value


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule

        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule

        fields = '__all__'
