from django.contrib.auth.hashers import make_password
from departments.models import Department
from rest_framework.serializers import ModelSerializer, CharField

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth.models import User


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department

        fields = ['name', 'password', 'image']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4,
                                     'style': {'input_type': 'password', 'placeholder': 'Password', 'required': False}}}

    def save(self, **kwargs):
        password = self.validated_data.get("password", '')
        if password is None and self.instance is not None:
            password = self.instance.password
        else:
            password = make_password(password)
        self.validated_data.update({'password': password})
        return super().save(**kwargs)

    def create(self, validated_data):
        department = Department(
            name=validated_data['name'],
            image=validated_data['image'],
            password=validated_data['password']
        )
        department.user = User(username=validated_data["name"], password=validated_data["password"])
        department.user.save()
        department.save()
        return department

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        try:
            data.update({"name": self.user.get_username()})
            data.update({"image": self.context['request'].build_absolute_uri(self.user.department.image.url)})
        except:
            pass
        return data
