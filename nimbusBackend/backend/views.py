from django.db.models import query
from django.http.response import Http404
from .models import Department, User, Quiz, Question

from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.generics import GenericAPIView

from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, UpdateModelMixin

from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

from .serializers import DepartmentSerializer, UserSerializer, QuizSerializer, QuestionSerializer


# Create your views here.

class UsersView(GenericAPIView):
    serializer_class = UserSerializer

    queryset = User.objects.all()

    def get(self, request):
        """
        Returns list of all users
        """
        users = self.get_queryset()
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
            print(e)
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


class DepartmentsView(GenericAPIView, ListModelMixin, CreateModelMixin):
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


class DepartmentView(GenericAPIView, ListModelMixin, UpdateModelMixin):
    serializer_class = DepartmentSerializer

    def get_queryset(self, pk=None):
        try:
            if pk is None:
                return Department.objects.all()
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return Http404

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.put(request, *args, **kwargs)

    def patch(self, request: Request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class QuizzesView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = QuizSerializer

    queryset = Quiz.objects.all()

    def get(self, request: Request):
        """
        Returns list of all Quizs
        """
        return self.list(request)

    def post(self, request: Request):
        """
        Creates a Quiz, if not exists
        """
        return self.create(request)


class QuizView(GenericAPIView, ListModelMixin, UpdateModelMixin):
    serializer_class = QuizSerializer

    def get_queryset(self, pk=None):
        try:
            if pk is None:
                return Quiz.objects.all()
            return Quiz.objects.get(pk=pk)
        except Quiz.DoesNotExist:
            return Http404

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.put(request, *args, **kwargs)

    def patch(self, request: Request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class QuestionsView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = QuestionSerializer

    queryset = Question.objects.all()

    def get(self, request: Request):
        """
        Returns list of all Questions
        """
        return self.list(request)

    def post(self, request: Request):
        """
        Creates a Question, if not exists
        """
        return self.create(request)


class QuestionView(GenericAPIView, ListModelMixin, UpdateModelMixin):
    serializer_class = QuestionSerializer

    def get_queryset(self, pk=None):
        try:
            if pk is None:
                return Question.objects.all()
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Http404

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.put(request, *args, **kwargs)

    def patch(self, request: Request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
