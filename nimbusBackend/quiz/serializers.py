from quiz.models import Quiz, Question, ScoreBoard, QuizScoreBoard
from rest_framework.serializers import ModelSerializer
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
    class Meta:
        model = Question
        fields = '__all__'
        extra_fields = ['quiz_name']
        validators = [
            UniqueTogetherValidator(
                queryset=Question.objects.all(),
                fields=['quiz', 'name']
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
