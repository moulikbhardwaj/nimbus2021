from rest_framework import serializers
from .models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['schedulePdfUrl']

    def create(self, validated_data):
        scheduleItem = Schedule(
            schedulePdfUrl=validated_data['schedulePdfUrl'],
        )
        scheduleItem.save()
        return scheduleItem