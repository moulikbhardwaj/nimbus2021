from django.http.response import Http404
from departments.authentication import DepartmentAuthentication
from departments.models import Department
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView, get_object_or_404

from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, \
    RetrieveModelMixin

from departments.serializers import DepartmentSerializer


class DepartmentsView(GenericAPIView, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    serializer_class = DepartmentSerializer

    queryset = Department.objects.all()

    def get(self, request: Request):
        """
        Returns list of all departments
        """
        return self.list(request)

    def post(self, request: Request):
        """
        Creates a department, if not exists
        """
        return self.create(request)


class DepartmentView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def get_queryset(self, pk=None):
        try:
            if pk is None:
                return Department.objects.all()
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return Http404

    def update(self, request, *args, **kwargs):
        """
        Customising update method
        """

        def updateDepartment():
            department = get_object_or_404(Department, pk=kwargs["pk"])
            department.image = request.data['image']
            department.save()

        return DepartmentAuthentication(request=request, update=updateDepartment, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Customising partial update method
        """

        def updateDepartment():
            department = get_object_or_404(Department, pk=kwargs["pk"])
            keys = list(request.data.keys())
            if "image" in request.data.keys():
                department.image = request.data["image"]
            department.save()

        return DepartmentAuthentication(request=request, update=updateDepartment, *args, **kwargs)

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
