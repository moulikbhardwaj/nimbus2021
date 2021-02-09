from rest_framework import authentication, serializers
from rest_framework import permissions
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication

from events.models import Event
from events.serializers import EventSerializer
from events.permissions import IsOwnerOrReadonly

from datetime import datetime

# Create your views here.

class EventsView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all().order_by('start')
        if self.request.query_params.get('type') == 'departmental':
            queryset = queryset.filter(Type=0)
        elif self.request.query_params.get('type') == 'institutional':
            queryset = queryset.filter(Type=1)
        elif self.request.query_params.get('type') == 'talk':
            queryset = queryset.filter(Type=2)
        elif self.request.query_params.get('type') == 'exhibition':
            queryset = queryset.filter(Type=3)
        elif self.request.query_params.get('type') == 'workshop':
            queryset = queryset.filter(Type=4)

        if self.request.query_params.get('department', None) != None:
            queryset = queryset.filter(department__name=self.request.query_params.get("department"))
        
        if self.request.query_params.get('date', None) != None:
            datestr = "2020-12-30T23:20:00+05:30"
            format = "%Y-%m-%dT%H:%M:%S%z"
            datestr = ''.join(datestr.rsplit(":",1))
            date = datetime.strptime(datestr, format)
            queryset = queryset.filter(start__gte=date)
            
        return queryset

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request: Request):
        """
        Returns a list of all events/talks/workshops/exhibitions
        """
        return self.list(self, request)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EventView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadonly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
