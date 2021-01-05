from django.db.models import CASCADE
from django.db.models import Model
from django.db.models.fields import CharField, DateTimeField, EmailField, IntegerField, URLField, TextField
from django.db.models.fields.related import ForeignKey


# Create your models here.

class User(Model):
    """
    User Details
    """
    firebase = CharField('firebaseID', max_length=128, null=False, unique=True,
                         primary_key=True, blank=False)

    username = CharField('username', max_length=255, null=False, unique=True,
                         blank=False)

    phone = CharField('phone', max_length=13, null=False, unique=False)

    email = EmailField('email', unique=True)

    firstName = CharField('firstName', max_length=255, null=False, blank=False)
    lastName = CharField('lastName', max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.username


class Department(Model):
    name = CharField('name', max_length=255, null=False, unique=True, primary_key=True)
    password = CharField('password', max_length=128, null=False, blank=False,
                         help_text='Leave empty if no change needed')
    image = URLField('image')

    def __str__(self) -> str:
        return "Department/Club: " + self.name


class Quiz(Model):
    """
    Quiz
    """
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


class Question(Model):
    """
    Quiz Question Details
    """
    text = CharField('text', max_length=512)
    option1 = CharField('option1', max_length=256)
    option2 = CharField('option2', max_length=256)
    option3 = CharField('option3', max_length=256)
    option4 = CharField('option4', max_length=256)

    quiz = ForeignKey(Quiz, on_delete=CASCADE)


class Schedule(Model):
    """
    Schedule by various departments
    """
    name = CharField('scheduleName', max_length=256, null=False, blank=False)
    info = TextField('info', max_length=1000)
    platform = CharField('platform', max_length=256)
    date = DateTimeField('date', null=False, blank=False,
                         help_text='Format: YYYY-MM-DDThh:mm, example 2021-01-01T15:30')
    department = ForeignKey(Department, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Sponsor(Model):
    """
    Sponsor details
    """
    name = CharField('sponsorName', max_length=256, unique=True, null=False, blank=False)
    image = URLField('imageUrl', max_length=256)

    def __str__(self):
        return self.name


class Event(Model):
    """
    Event
    """
    # choices = (
    #     (0, "DepartmentEvent"),
    #     (1, "InstituteEvent"),
    #     (2, "Talk"),
    #     (3, "Exhibition"),
    #     (4, "Workshop")¸
    # )
    name = CharField('EventName', max_length=256)
    info = CharField('info', max_length=256)
    platform = CharField('platform', max_length=256)
    date = DateTimeField('date')
    image = URLField('imageUrl', max_length=256)
    abstract = TextField('abstract', max_length=1000)
    type = IntegerField('type')

    def __str__(self):
        return self.name


class Member(Model):
    """
    Member of App Team
    """
    name = CharField('memberName', max_length=256, null=False, blank=False)
    position = CharField('position', max_length=256, null=False, blank=False)
    image = URLField('imageUrl', max_length=256, null=False, blank=False)

    def __str__(self):
        return self.name
