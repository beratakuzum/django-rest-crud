from rest_framework import serializers
from sessions.models import Session
from events.models import Event


class SessionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, allow_blank=False, allow_null=False)
    start_date = serializers.DateTimeField(allow_null=False)
    end_date = serializers.DateTimeField(allow_null=False)
    speaker = serializers.CharField(max_length=100, allow_blank=False, allow_null=False)
    event = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Event.objects)

    def create(self, validated_data):
        """
        Create and return a new `Session` instance, given the validated data.
        """
        return Session.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Session` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.speaker = validated_data.get('speaker', instance.speaker)
        instance.event = validated_data.get('event', instance.event)
        instance.save()
        return instance
