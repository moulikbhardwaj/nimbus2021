from django.db import models

from users.models import User

# Create your models here.

class CampusAmbassadorPost(models.Model):
    Media_Choices = (
        ('image', 'image'),
        ('video', 'video'),
    )
    text = models.TextField(null = True)
    mediaUrl = models.URLField('media', null = True)
    mediaType = models.CharField(max_length = 5, choices = Media_Choices, null = True)
    ambassadorFirebase = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return '{}-{}'.format(self.text, self.mediaType)
