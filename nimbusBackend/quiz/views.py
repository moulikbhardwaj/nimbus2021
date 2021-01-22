from django.http.response import Http404
from quiz.models import Quiz, ScoreBoard, Question, Answer, QuizScoreBoard
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
from datetime import datetime
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin
from django.utils import timezone
from quiz.serializers import QuizSerializer, ScoreBoardSerializer, QuizScoreBoardSerializer, QuestionSerializer, \
    QuestionSerializerFull
from rest_framework.status import HTTP_400_BAD_REQUEST

# Create your views here.
from rest_framework.response import Response

from utils.helper_response import InternalServerErrorResponse, InvalidQuizIdResponse, QuizNotStartedResponse


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
    """
    Retrieve OverAll LeaderBoard
    """
    model = ScoreBoard
    serializer_class = ScoreBoardSerializer
    queryset = ScoreBoard.objects.all().order_by('-score')

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class QuizLeaderBoard(GenericAPIView, ListModelMixin):
    """
    Retrieve LeaderBoard Quiz Wise
    """
    model = QuizScoreBoard
    serializer_class = QuizScoreBoardSerializer
    queryset = QuizScoreBoard.objects.all()

    def get(self, request: Request, *args, **kwargs):
        try:
            if len(Quiz.objects.all().filter(id=kwargs["pk"])) == 0:
                return InvalidQuizIdResponse
            quizScoreBoardSerializer = QuizScoreBoardSerializer(
                QuizScoreBoard.objects.all().filter(quiz_id=kwargs["pk"]), many=True)
            return Response(quizScoreBoardSerializer.data)
        except:
            return InternalServerErrorResponse


class QuestionView(GenericAPIView, CreateModelMixin):
    """
    Create Quiz Question
    """
    model = Question
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request: Request, pk):
        try:
            quiz = Quiz.objects.get(id=pk)
        except Quiz.DoesNotExist:
            return InvalidQuizIdResponse
        if quiz.startTime <= timezone.now() <= quiz.endTime:
            return Response(QuestionSerializerFull(Question.objects.all().filter(quiz_id=quiz), many=True).data)
        else:
            return QuizNotStartedResponse

    def post(self, request: Request, pk):
        try:
            quiz = Quiz.objects.get(id=pk)
        except Quiz.DoesNotExist:
            return InvalidQuizIdResponse
        questionSerializer = QuestionSerializer(data=request.POST)
        if questionSerializer.is_valid():
            data = questionSerializer.data
            option1 = Answer.objects.create(
                text=data['option1']
            )
            option2 = Answer.objects.create(
                text=data['option2']
            )
            option3 = Answer.objects.create(
                text=data['option3']
            )
            option4 = Answer.objects.create(
                text=data['option4']
            )
            option1.save()
            option2.save()
            option3.save()
            option4.save()
            question = Question.objects.create(
                text=data["text"],
                option1=option1,
                option2=option2,
                option3=option3,
                option4=option4,
                quiz=quiz,
                correct=getCorrectOption(option1, option2, option3, option4, data['correct'])
            )
            question.save()

            return Response(QuestionSerializerFull(question, many=False).data)
        else:
            return Response(questionSerializer.errors, HTTP_400_BAD_REQUEST)


def getCorrectOption(option1, option2, option3, option4, correct):
    if correct == 1:
        return option1
    elif correct == 2:
        return option2
    elif correct == 3:
        return option3
    else:
        return option4
