from rest_framework import serializers
from .models import CoreTeam, Sponsors


class CoreteamSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreTeam
        fields = ['name', 'position', 'image']

    def create(self, validated_data):
        coreTeamMember = CoreTeam(
            name=validated_data['name'],
            position=validated_data['position'],
            image=validated_data['image']
        )
        coreTeamMember.save()
        return coreTeamMember


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsors
        fields = ['name', 'link', 'image', 'position', 'priority']

    def create(self, validated_data):
        sponsor = Sponsors(
            name=validated_data['name'],
            position=validated_data['position'],
            image=validated_data['image'],
            link=validated_data['link'],
            priority=validated_data['priority'],
        )
        sponsor.save()
        return sponsor
