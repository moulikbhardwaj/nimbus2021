from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from .serializers import ScheduleSerializer
from .models import Schedule

# Create your views here.


class ScheduleView(GenericAPIView, ListModelMixin):
    serializer_class = ScheduleSerializer

    queryset = Schedule.objects.all()

    def get(self, request: Request):
        return self.list(request)
 