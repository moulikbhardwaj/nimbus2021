from django.db import models

from django.db.models import Model
from django.db.models.fields import CharField, DateTimeField, EmailField, IntegerField, URLField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class User(Model):
    firebase = CharField('firebaseID', max_length=128, null=False, unique=True,
                         primary_key=True, blank=False)

    username = CharField('username', max_length=255, null=False, unique=True,
                         blank=False)

    phone = CharField('phone', max_length=13)
    
    email = EmailField('email', unique=True)

    firstName = CharField('firstName', max_length=255, null=False, blank=False)
    lastName = CharField('lastName', max_length=255, blank=True, null=True)

class Department(Model):
    name = CharField('name', max_length=255, null=False, unique=True, primary_key=True)
    password = CharField('password', max_length=128, null=False, blank=False,
                         help_text='Leave empty if no change needed')
    image = URLField('image')

    def __str__(self) -> str:
        return "Department/Club: " + self.name

class Quiz(Model):
    name = CharField('name', max_length=255, null=False)

    count = IntegerField('count', default=0)
    sendCount = IntegerField('sendCount', default=1)

    startTime = DateTimeField('startTime', null=False,
                               help_text='Format: YYYY-MM-DDThh:mm, example 2021-01-01T15:30')
    endTime = DateTimeField('endTime', null=False,
                               help_text='Format: YYYY-MM-DDThh:mm, example 2021-01-01T15:30')

    department = ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return "Quiz:" + self.name

class Question(Model):
    text = CharField('text', max_length=512)
    option1 = CharField('option1', max_length=256)
    option2 = CharField('option2', max_length=256)
    option3 = CharField('option3', max_length=256)
    option4 = CharField('option4', max_length=256)
    
    quiz = ForeignKey(Quiz, on_delete=models.CASCADE)