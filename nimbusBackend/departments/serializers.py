from django.contrib.auth.hashers import make_password
from departments.models import Department
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CharField

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department

        password = CharField(max_length=128, allow_blank=True,
                             help_text='Leave empty if no change needed',
                             style={'input_type': 'password', 'placeholder': 'Password'})
        fields = ['name', 'password', 'image']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4,
                                     'style': {'input_type': 'password', 'placeholder': 'Password', 'required': False}}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        department = Department(
            name=validated_data['name'],
            password=validated_data['password'],
            image=validated_data['image']
        )
        department.save()
        return department
