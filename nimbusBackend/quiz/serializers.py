from abc import ABC

from quiz.models import Quiz, Question, ScoreBoard, QuizScoreBoard, Answer
from rest_framework.serializers import ModelSerializer, CharField, IntegerField, Serializer, ListField, DictField
from rest_framework.validators import UniqueTogetherValidator

from users.serializers import UserSerializerForScoreBoard


class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Quiz.objects.all(),
                fields=['department', 'name']
            )
        ]


class QuestionSerializer(ModelSerializer):
    text = CharField(help_text="Question Text", max_length=256, min_length=5)
    option1 = CharField(help_text="Option 1", max_length=256, min_length=1)
    option2 = CharField(help_text="Option 2", max_length=256, min_length=1)
    option3 = CharField(help_text="Option 3", max_length=256, min_length=1)
    option4 = CharField(help_text="Option 4", max_length=256, min_length=1)
    correct = IntegerField(help_text="Enter Correct Option: 1 - 4", min_value=1, max_value=4)

    class Meta:
        model = Question
        exclude = ['quiz']
        validators = [
            UniqueTogetherValidator(
                queryset=Question.objects.all(),
                fields=['text']
            )
        ]


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class QuestionSerializerFull(ModelSerializer):
    quiz = QuizSerializer()
    option1 = AnswerSerializer()
    option2 = AnswerSerializer()
    option3 = AnswerSerializer()
    option4 = AnswerSerializer()
    correct = AnswerSerializer()

    class Meta:
        model = Question
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Question.objects.all(),
                fields=['text']
            )
        ]


class ScoreBoardSerializer(ModelSerializer):
    user = UserSerializerForScoreBoard()

    class Meta:
        model = ScoreBoard
        fields = "__all__"


class QuizScoreBoardSerializer(ModelSerializer):
    user = UserSerializerForScoreBoard()

    class Meta:
        model = QuizScoreBoard
        fields = "__all__"


class QuestionResponse(DictField):
    questionId = IntegerField(min_value=1)
    answerId = IntegerField(min_value=1)


class ResponseSerializer(Serializer):
    quizId = CharField(help_text="Quiz Id", max_length=256)
    userId = CharField(help_text="User Firebase Id", max_length=256)
    responses = ListField(child=QuestionResponse(), min_length=1)


class QuizResponseSerializer(Serializer):
    questionId = IntegerField(min_value=1)
    answerId = IntegerField(min_value=1)


class QuizPlayedOrNotSerializer(Serializer):
    quizId = CharField(max_length=256)
    userId = CharField(max_length=256)
