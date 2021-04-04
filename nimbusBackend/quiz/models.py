from uuid import uuid4

import django
from django.db.models import Model, CASCADE
from django.db.models.fields import CharField, IntegerField, DateTimeField, PositiveIntegerField, URLField
from django.db.models.fields.related import ForeignKey

from django.core.validators import MinValueValidator, MaxValueValidator

from departments.models import Department

# Create your models here.
from users.models import User


class Quiz(Model):
    """
    Quiz
    """
    id = CharField(primary_key=True, default=uuid4(), max_length=256)
    name = CharField('name', max_length=255, null=False)
    count = IntegerField('count', default=0)
    sendCount = IntegerField('sendCount', default=1)

    startTime = DateTimeField('startTime', null=False,
                              help_text='Format: YYYY-MM-DDThh:mm, example 2021-01-01T15:30')
    endTime = DateTimeField('endTime', null=False,
                            help_text='Format: YYYY-MM-DDThh:mm, example 2021-01-01T15:30')

    department = ForeignKey(Department, on_delete=CASCADE)

    def __str__(self):
        return "Quiz:" + self.name


class Answer(Model):
    text = CharField('text', max_length=255, blank=True, null=True)
    image = URLField('image', blank=True, null=True)



class Question(Model):
    """
    Quiz Question Details
    """
    text = CharField('text', max_length=512)
    image = URLField("image", blank=True, null=True)

    optionCount = IntegerField("optionCount", default=4,
                    validators= [MaxValueValidator(4), MinValueValidator(2)]
    )

    option1 = ForeignKey(Answer, related_name='option1', on_delete=CASCADE)
    option2 = ForeignKey(Answer, related_name='option2', on_delete=CASCADE)
    option3 = ForeignKey(Answer, related_name='option3', on_delete=CASCADE)
    option4 = ForeignKey(Answer, related_name='option4', on_delete=CASCADE)

    correct = ForeignKey(Answer, on_delete=CASCADE)
    quiz = ForeignKey(Quiz, on_delete=CASCADE)

    timeLimit = IntegerField("timeLimit", default=15)
<<<<<<< HEAD
=======

    marks = PositiveIntegerField("marks", default=5)
    negativeMarks = PositiveIntegerField("negativeMarks", default=0)
>>>>>>> 010f764b1fbe446c310bcf1a32f7b1b036baa836

class ScoreBoard(Model):
    """
    Contains User Scores
    """
    user = ForeignKey(User, on_delete=CASCADE)
    score = IntegerField(default=0)
    timestamp = DateTimeField("timestamp",auto_now=True)

    def __str__(self):
        return self.user.email


class QuizScoreBoard(Model):
    """
    Contain quiz LeaderBoard
    """
    user = ForeignKey(User, on_delete=CASCADE)
    quiz = ForeignKey(Quiz, on_delete=CASCADE)
    score = IntegerField(default=0)
    timestamp = DateTimeField("timestamp",auto_now=True)

    class Meta:
        unique_together = ("user", "quiz")

    def __str__(self):
        return self.user.email + " " + self.quiz.name
