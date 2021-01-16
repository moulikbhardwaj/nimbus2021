from django.contrib.auth.hashers import make_password
from events.models import Event
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CharField

class EventSerializer(ModelSerializer):
	class Meta:
		model = Event
		fields = "__all__"
