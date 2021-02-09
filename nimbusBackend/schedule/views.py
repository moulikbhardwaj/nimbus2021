from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin

from .serializers import ScheduleSerializer
from .models import Schedule

# Create your views here.


class ScheduleListView(GenericAPIView, ListModelMixin):
    serializer_class = ScheduleSerializer

    queryset = Schedule.objects.all()

    def get(self, request: Request):
        """
        Returns list of all Schedule
        """
        return self.list(request)

class ScheduleView(GenericAPIView, RetrieveModelMixin):
    serializer_class = ScheduleSerializer
    query_set = Schedule.objects.all()
    
    def get(self, request: Request, *args, **kwargs):
        """
        Retrieve Single Event Schedule
        """
        return self.retrieve(request, *args, **kwargs)