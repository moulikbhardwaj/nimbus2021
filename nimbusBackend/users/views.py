import logging
from django.http.response import Http404
from users.models import User
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView

from rest_framework.mixins import DestroyModelMixin , UpdateModelMixin

from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

from users.serializers import UserSerializer

# Logger
logger = logging.getLogger(__name__)

# Create your views here.

class UsersView(GenericAPIView):
    serializer_class = UserSerializer

    queryset = User.objects.all()

    def get(self, request):
        """
        Returns list of all users
        """
        users = UserSerializer(self.get_queryset(), many=True)
        return Response(users.data)

    def post(self, request: Request):
        """
        Creates a user, if not already exists
        """
        try:
            user = UserSerializer(data=request.data)
            if user.is_valid():
                user.save()
                return Response(data=user.data, status=HTTP_201_CREATED)
            else:
                data = {"Message": "Invalid user data", "Errors:": user.errors}
                return Response(data=data, status=HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)


class UserView(GenericAPIView, UpdateModelMixin, DestroyModelMixin):
    serializer_class = UserSerializer

    def get_queryset(self, pk=None):
        try:
            if pk == None:
                return User.objects.all()
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk):
        """
        Returns user with given firebase id
        """
        user = UserSerializer(self.get_queryset(pk))
        return Response(user.data)

    def put(self, request: Request, *args, **kwargs):
        """
        Updates user with given firebase id
        """
        return self.update(request, *args, **kwargs)

    def patch(self, request: Request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)