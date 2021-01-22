from django.http.response import Http404
from quiz.models import Quiz, ScoreBoard
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView

from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin

from quiz.serializers import QuizSerializer, ScoreBoardSerializer


# Create your views here.
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


class LeaderBoard(GenericAPIView, ListModelMixin):
    model = ScoreBoard
    serializer_class = ScoreBoardSerializer
    queryset = ScoreBoard.objects.all().order_by('-score')

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
