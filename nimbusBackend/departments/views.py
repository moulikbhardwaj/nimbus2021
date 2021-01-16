from django.http.response import Http404
from rest_framework import permissions
from departments.models import Department
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView, get_object_or_404

from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, \
    RetrieveModelMixin

from departments.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from departments.serializers import DepartmentSerializer

class DepartmentsView(GenericAPIView, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]


    def get(self, request: Request):
        """
        Returns list of all departments
        """
        return self.list(request)

    def post(self, request: Request):
        """
        Creates a department, if not exists
        """
        print(request.data)
        return self.create(request)


class DepartmentView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request: Request, *args, **kwargs):
        """
        Retrieve department
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        """
        Update Department completely
        """
        return self.update(request, *args, **kwargs)

    def patch(self, request: Request, *args, **kwargs):
        """
        Update Department partially
        """
        return self.partial_update(request, *args, **kwargs)