from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin

from gallery.serializers import GalleryPostSerializer
from gallery.models import GalleryPost

from departments.permissions import IsOwnerOrReadOnlyObject

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class GalleryListView(ListCreateAPIView):
    serializer_class = GalleryPostSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = GalleryPost.objects.all().order_by('upload_time')
        dept_id = self.request.query_params.get('dept_id', None)
        if dept_id == '1':
            queryset = queryset.filter(department="c_helix")
        elif dept_id == '2':
            queryset = queryset.filter(department="designocrats")
        elif dept_id == '3':
            queryset = queryset.filter(department="hermetica")
        elif dept_id == '4':
            queryset = queryset.filter(department="medextrous")
        elif dept_id == '5':
            queryset = queryset.filter(department="meta_morph")
        elif dept_id == '6':
            queryset = queryset.filter(department="nimbus")
        elif dept_id == '7':
            queryset = queryset.filter(department="ojas")
        elif dept_id == '8':
            queryset = queryset.filter(department="pixonoids")
        elif dept_id == '9':
            queryset = queryset.filter(department="team_.exe")
        elif dept_id == '10':
            queryset = queryset.filter(department="vibhav")
        elif dept_id == '11':
            queryset = queryset.filter(department="web_team")
        elif dept_id == '12':
            queryset = queryset.filter(department="app_team")

        year = self.request.query_params.get('year', None)
        if year is not None:
            queryset = queryset.filter(upload_time__year=year)
        return queryset   

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.create(request, **args, **kwargs)

class GalleryDestroyView(GenericAPIView , DestroyModelMixin, RetrieveModelMixin):

    serializer_class = GalleryPostSerializer

    def get_queryset(self):
        queryset = GalleryPost.objects.filter(pk=self.kwargs['pk'])
        return queryset

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnlyObject]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)