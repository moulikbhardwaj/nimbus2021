from django.shortcuts import render
from django.http.response import Http404

from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CampusAmbassadorPostSerializer, IsCampusAmbassadorSerializer
from .models import CampusAmbassadorPost
from users.models import User

# Create your views here.

class CampusAmbassadorPostsView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = CampusAmbassadorPostSerializer

    queryset = CampusAmbassadorPost.objects.all()

    def get(self, request: Request):
        """
        Returns list of all Posts by Campus Ambassadors
        """
        return self.list(request)

    def post(self, request: Request):
        """
        Creates a Campus Ambassador Post
        """
        return self.create(request)



class CampusAmbassadorPostView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin):
    serializer_class = CampusAmbassadorPostSerializer

    queryset = CampusAmbassadorPost.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.put(request, *args, **kwargs)

    def patch(self, request: Request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class IsCampusAmbassador(GenericAPIView, RetrieveModelMixin):
    serializer_class = IsCampusAmbassadorSerializer

    queryset = User.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)