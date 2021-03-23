from django.contrib import admin

# Register your models here.
from quiz.models import ScoreBoard, Quiz, QuizScoreBoard, Question, Answer

admin.site.register([
    ScoreBoard,
    Quiz,
    QuizScoreBoard,
    Question,
    Answer
])
