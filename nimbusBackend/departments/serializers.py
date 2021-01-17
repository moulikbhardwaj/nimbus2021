from django.contrib.auth.hashers import make_password
from departments.models import Department
from rest_framework.serializers import ModelSerializer, CharField

from django.contrib.auth.models import User

class DepartmentSerializer(ModelSerializer):

    class Meta:
        model = Department

        fields = ['name', 'password', 'image']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4,
                                     'style': {'input_type': 'password', 'placeholder': 'Password', 'required': False}}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        department = Department(
            name=validated_data['name'],
            image=validated_data['image'],
            password=validated_data['password']
        )
        department.user = User(username=validated_data["name"], password=validated_data["password"])
        department.user.save()
        department.save()
        return department
