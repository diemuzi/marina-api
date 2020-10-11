from rest_framework import serializers

from calendar import models


class AccountSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = models.Account

        fields = [
            'id',
            'name',
            'friday',
            'monday',
            'saturday',
            'sunday',
            'thursday',
            'tuesday',
            'wednesday'
        ]

    def get_name(self, obj):
        return str(obj)


class AccountProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = models.Account

        fields = [
            'id',
            'friday',
            'monday',
            'name',
            'saturday',
            'schedule_friday',
            'schedule_monday',
            'schedule_saturday',
            'schedule_sunday',
            'schedule_thursday',
            'schedule_tuesday',
            'schedule_wednesday',
            'sunday',
            'thursday',
            'tuesday',
            'wednesday'
        ]

    def get_name(self, obj):
        return str(obj)


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule

        fields = '__all__'


class ScheduleAccountSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = models.Account

        fields = [
            'id',
            'name'
        ]

    def get_name(self, obj):
        return str(obj)


class ScheduleFridaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule

        fields = [
            'account_friday',
            'has_break',
            'name',
            'time_end',
            'time_start'
        ]

        read_only_fields = [
            'name',
            'time_end',
            'time_start'
        ]


class ScheduleMondaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule

        fields = [
            'account_monday',
            'has_break',
            'name',
            'time_end',
            'time_start'
        ]

        read_only_fields = [
            'name',
            'time_end',
            'time_start'
        ]


class ScheduleSaturdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule

        fields = [
            'account_saturday',
            'has_break',
            'name',
            'time_end',
            'time_start'
        ]

        read_only_fields = [
            'name',
            'time_end',
            'time_start'
        ]


class ScheduleSundaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule

        fields = [
            'account_sunday',
            'has_break',
            'name',
            'time_end',
            'time_start'
        ]

        read_only_fields = [
            'name',
            'time_end',
            'time_start'
        ]


class ScheduleThursdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule

        fields = [
            'account_thursday',
            'has_break',
            'name',
            'time_end',
            'time_start'
        ]

        read_only_fields = [
            'name',
            'time_end',
            'time_start'
        ]


class ScheduleTuesdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule

        fields = [
            'account_tuesday',
            'has_break',
            'name',
            'time_end',
            'time_start'
        ]

        read_only_fields = [
            'name',
            'time_end',
            'time_start'
        ]


class ScheduleWednesdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule

        fields = [
            'account_wednesday',
            'has_break',
            'name',
            'time_end',
            'time_start'
        ]

        read_only_fields = [
            'name',
            'time_end',
            'time_start'
        ]
