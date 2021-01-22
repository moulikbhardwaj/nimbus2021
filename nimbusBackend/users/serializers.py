from rest_framework.serializers import ModelSerializer
from users.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserSerializerForScoreBoard(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'firstName', 'lastName']
