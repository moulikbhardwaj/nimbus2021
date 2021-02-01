from rest_framework import serializers
from .models import CampusAmbassadorPost
from users.models import User

class CampusAmbassadorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampusAmbassadorPost
        fields = '__all__'

class IsCampusAmbassadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['campusAmbassador']
