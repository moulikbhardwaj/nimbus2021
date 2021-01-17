from django.contrib.auth.hashers import make_password
from django.db.models import fields
from rest_framework.response import Response
from events.models import Event
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CharField

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ['department']

    def create(self, validated_data):
        validated_data['department'] = self.context['request'].user.department
        event = Event(**validated_data)
        event.save()
        return event