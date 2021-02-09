from django.db import models

from django.db.models import Model, CASCADE
from django.db.models.fields.related import ForeignKey

from departments.models import Department

# Create your models here.

class Schedule(models.Model):
    eventName = models.CharField('Event Name',max_length = 255, null = False)
    venue = models.CharField('Venue',max_length = 255, null = False)
    time = models.DateTimeField('Time', null=False,
							  help_text='Format: YYYY-MM-DDThh:mm, example 2021-01-01T15:30')
    department = ForeignKey(Department, on_delete=CASCADE)
    