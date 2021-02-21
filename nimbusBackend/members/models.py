from django.db import models


# Create your models here.

class CoreTeam(models.Model):
    name = models.CharField(max_length=255, null=False)
    position = models.CharField(max_length=255, null=False)
    image = models.URLField('image')

    def __str__(self):
        return '{}-{}'.format(self.name, self.position)


class Sponsors(models.Model):
    name = models.CharField(max_length=255, null=True)
    image = models.URLField('image', null=True)
    link = models.URLField('link', null=True)
    position = models.CharField("position", max_length= 255, null=True)
    priority = models.IntegerField("priority", default=1)

    def __str__(self):
        return self.name
