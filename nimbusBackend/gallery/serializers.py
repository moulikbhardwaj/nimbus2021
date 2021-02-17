from rest_framework.serializers import ModelSerializer

from gallery.models import GalleryPost

class GalleryPostSerializer(ModelSerializer):
    class Meta:
        model = GalleryPost
        fields = "__all__"

        read_only_fields = ['department']

    def save(self, **kwargs):
        self.validated_data.update({'department': self.context['request'].user.department})
        return super().save(**kwargs)