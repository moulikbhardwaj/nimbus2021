from rest_framework import authentication, serializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication

from events.models import Event
from events.serializers import EventSerializer
from events.permissions import IsOwnerOrReadonly


# Create your views here.

class EventsView(GenericAPIView, ListModelMixin):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request:Request):
        """
        Returns a list of all events/talks/workshops/exhibitions
        """
        return self.list(self, request)

class DepartmentalEventsView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Event.objects.filter(Type=0)
    serializer_class = EventSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request:Request):
        """
        Returns a list of all Departmental Events
        """
        return self.list(request)
    
    def post(self, request:Request):
        """
        Creates a departmental event, if not exists
        """
        return self.create(request)


class DepartmentalEventView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Event.objects.filter(Type=0)
    serializer_class = EventSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadonly]

    def get(self, request:Request, *args, **kwargs):
        """
        Returns a single Departmental Event
        """
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request:Request, *args, **kwargs):
        """
        Updates a Departmental Event completely
        """
        return self.update(request, *args, **kwargs)
    
    def patch(self, request:Request, *args, **kwargs):
        """
        Updates a Departmental Event partially
        """
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request:Request, *args, **kwargs):
        """
        Deletes a Departmental Event
        """
        return self.destroy(request, *args, *kwargs)


class InstitutionalEventsView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Event.objects.filter(Type=1)
    serializer_class = EventSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request:Request):
        """
        Returns a list of all Institutional Events
        """
        return self.list(request)
    
    def post(self, request:Request):
        """
        Creates a Institutional event, if not exists
        """
        return self.create(request)


class InstitutionalEventView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Event.objects.filter(Type=1)
    serializer_class = EventSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadonly]

    def get(self, request:Request, *args, **kwargs):
        """
        Returns a single Institutional Event
        """
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request:Request, *args, **kwargs):
        """
        Updates a Institutional Event completely
        """
        return self.update(request, *args, **kwargs)
    
    def patch(self, request:Request, *args, **kwargs):
        """
        Updates a Institutional Event partially
        """
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request:Request, *args, **kwargs):
        """
        Deletes a Institutional Event
        """
        return self.destroy(request, *args, *kwargs)



class TalksView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Event.objects.filter(Type=2)
    serializer_class = EventSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request:Request):
        """
        Returns a list of all talks
        """
        return self.list(request)
    
    def post(self, request:Request):
        """
        Creates a talk, if not exists
        """
        return self.create(request)


class TalkView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Event.objects.filter(Type=2)
    serializer_class = EventSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadonly]

    def get(self, request:Request, *args, **kwargs):
        """
        Returns a single Talk
        """
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request:Request, *args, **kwargs):
        """
        Updates a Talk completely
        """
        return self.update(request, *args, **kwargs)
    
    def patch(self, request:Request, *args, **kwargs):
        """
        Updates a Talk partially
        """
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request:Request, *args, **kwargs):
        """
        Deletes a Talk
        """
        return self.destroy(request, *args, *kwargs)


class ExhibitionsView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Event.objects.filter(Type=3)
    serializer_class = EventSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request:Request):
        """
        Returns a list of all Exhibitions
        """
        return self.list(request)
    
    def post(self, request:Request):
        """
        Creates a Exhibition, if not exists
        """
        return self.create(request)


class ExhibitionView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Event.objects.filter(Type=3)
    serializer_class = EventSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadonly]

    def get(self, request:Request, *args, **kwargs):
        """
        Returns a single Exhibition
        """
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request:Request, *args, **kwargs):
        """
        Updates a Exhibition completely
        """
        return self.update(request, *args, **kwargs)
    
    def patch(self, request:Request, *args, **kwargs):
        """
        Updates a Exhibition partially
        """
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request:Request, *args, **kwargs):
        """
        Deletes a Exhibition
        """
        return self.destroy(request, *args, *kwargs)


class WorkshopsView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Event.objects.filter(Type=4)
    serializer_class = EventSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request:Request):
        """
        Returns a list of all Workshops
        """
        return self.list(request)
    
    def post(self, request:Request):
        """
        Creates a Workshop, if not exists
        """
        return self.create(request)


class WorkshopView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Event.objects.filter(Type=4)
    serializer_class = EventSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadonly]

    def get(self, request:Request, *args, **kwargs):
        """
        Returns a single Workshop
        """
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request:Request, *args, **kwargs):
        """
        Updates a Workshop completely
        """
        return self.update(request, *args, **kwargs)
    
    def patch(self, request:Request, *args, **kwargs):
        """
        Updates a Workshop partially
        """
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request:Request, *args, **kwargs):
        """
        Deletes a Workshop
        """
        return self.destroy(request, *args, *kwargs)