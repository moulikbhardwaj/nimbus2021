from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from .serializers import *
from .models import *

# Create your views here.

class CoreTeamView(GenericAPIView, ListModelMixin):
    serializer_class = CoreteamSerializer
    queryset = CoreTeam.objects.all()

    def get(self, request: Request):
        return self.list(request)


class SponsorView(GenericAPIView, ListModelMixin):
    serializer_class = SponsorSerializer
    queryset = Sponsors.objects.all()

    def get(self, request: Request):
        return self.list(request)
