from django.http.response import Http404
from quiz.models import Quiz, ScoreBoard, Question, Answer, QuizScoreBoard
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin
from django.utils import timezone
from quiz.serializers import QuizSerializer, ScoreBoardSerializer, QuizScoreBoardSerializer, QuestionSerializer, \
    QuestionSerializerFull, ResponseSerializer, QuizResponseSerializer
from utils.helper_response import InternalServerErrorResponse, InvalidQuizIdResponse, QuizNotStartedResponse, \
    InvalidUserIdResponse, QuizAlreadyAttemptedResponse, InvalidQuestionIdResponse
from quiz.serializers import QuizSerializer, ScoreBoardSerializer, QuizScoreBoardSerializer, QuizPlayedOrNotSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from users.models import User


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
        """
        Get Quiz Questions
        """
        try:
            quiz = Quiz.objects.get(id=pk)
        except Quiz.DoesNotExist:
            return InvalidQuizIdResponse

        if quiz.startTime <= timezone.now() <= quiz.endTime:
            return Response(
                QuestionSerializerFull(Question.objects.all().filter(quiz_id=quiz).order_by('?')[:quiz.sendCount],
                                       many=True).data)
        else:
            return QuizNotStartedResponse

    def post(self, request: Request, pk):
        """
        Create Quiz Question
        """
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
            quiz.count = quiz.count + 1
            quiz.save()
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


class CheckResponses(GenericAPIView):
    """
    Match User Responses
    """
    serializer_class = ResponseSerializer

    def post(self, request: Request):
        """
        Mark Quiz Responses
        """
        marks = 2
        score = 0
        data = request.data
        serializer = ResponseSerializer(data=data)
        if serializer.is_valid():
            try:
                quiz = Quiz.objects.get(id=serializer.data['quizId'])
            except Quiz.DoesNotExist:
                return InvalidQuizIdResponse
            try:
                user = User.objects.get(firebase=serializer.data['userId'])
            except User.DoesNotExist:
                return InvalidUserIdResponse
            if len(QuizScoreBoard.objects.filter(quiz=quiz, user=user)) != 0:
                return QuizAlreadyAttemptedResponse
            data = serializer.data
            for answer in data['responses']:
                responseSerializer = QuizResponseSerializer(data=answer)
                if responseSerializer.is_valid():
                    questionId = int(answer['questionId'])
                    answerId = int(answer['answerId'])
                    try:
                        question = Question.objects.get(id=questionId)
                    except Question.DoesNotExist:
                        return InvalidQuestionIdResponse
                    if question.correct.id == answerId:
                        score += marks
                else:
                    return Response(responseSerializer.errors)
            scoreForUser = QuizScoreBoard.objects.create(quiz=quiz, user=user, score=score)
            scoreForUser.save()
            centralScore = ScoreBoard.objects.filter(user=user)
            if len(centralScore) == 0:
                ScoreBoard.objects.create(user=user, score=score).save()
            else:
                centralScore = centralScore[0]
                centralScore.score += centralScore.score
                centralScore.save()
            return Response({"score": score})
        else:
            return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class CheckQuizPlayedOrNot(GenericAPIView):
    serializer_class = QuizPlayedOrNotSerializer

    def post(self, request):
        serializer = QuizPlayedOrNotSerializer(data=request.data)
        if serializer.is_valid():
            try:
                quiz = Quiz.objects.get(id=serializer.data['quizId'])
            except Quiz.DoesNotExist:
                return InvalidQuizIdResponse
            try:
                user = User.objects.get(firebase=serializer.data['userId'])
            except User.DoesNotExist:
                return InvalidUserIdResponse
            if len(QuizScoreBoard.objects.filter(quiz=quiz, user=user)) != 0:
                return Response({"attempted": True})
            else:
                return Response({"attempted": False})
        else:
            return Response(serializer.errors, HTTP_400_BAD_REQUEST)
