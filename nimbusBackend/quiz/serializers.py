from quiz.models import Quiz, Question
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator


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