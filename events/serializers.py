import pytz
from rest_framework import serializers, fields
from events.models import Event

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class EventSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, allow_blank=False, allow_null=False)
    start_date = serializers.DateTimeField(allow_null=False)
    end_date = serializers.DateTimeField(allow_null=False)
    time_zone = serializers.ChoiceField(allow_blank=False, choices=TIMEZONES)

    def create(self, validated_data):
        """
        Create and return a new `Event` instance, given the validated data.
        """
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.time_zone = validated_data.get('time_zone', instance.time_zone)
        instance.save()
        return instance