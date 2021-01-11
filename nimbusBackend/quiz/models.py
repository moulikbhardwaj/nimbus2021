import django
from django.db.models import Model, CASCADE
from django.db.models.fields import CharField, IntegerField, DateTimeField
from django.db.models.fields.related import ForeignKey

from departments.models import Department

# Create your models here.

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

class Answer(Model):
	text = CharField('text', max_length=255)


class Question(Model):
	"""
	Quiz Question Details
	"""
	text = CharField('text', max_length=512)

	option1 = ForeignKey(Answer, related_name='option1', on_delete=CASCADE)
	option2 = ForeignKey(Answer, related_name='option2', on_delete=CASCADE)
	option3 = ForeignKey(Answer, related_name='option3', on_delete=CASCADE)
	option4 = ForeignKey(Answer, related_name='option4', on_delete=CASCADE)
	
	correct = ForeignKey(Answer, on_delete=CASCADE)

	quiz = ForeignKey(Quiz, on_delete=CASCADE)