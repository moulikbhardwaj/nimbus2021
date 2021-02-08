from django.db import models

# Create your models here.

class Schedule(models.Model):
    schedulePdfUrl = models.URLField('schedule pdf')
