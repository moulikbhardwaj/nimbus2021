from django.db import models
import datetime

# Create your models here.

class VCQueue(models.Model):
    uid = models.CharField(max_length=128, primary_key=True, blank=False, null=False)
    enterTime = models.DateTimeField(auto_now_add=True)
    lastPingTime = models.DateTimeField(auto_now=True)
    channel = models.CharField(max_length=100, default='')
    token = models.CharField(max_length=256, default='')

    class Meta:
        ordering = ['enterTime']

    def __str__(self):
        return (self.uid + ' - '
            + self.channel + ' - '
            + str(self.enterTime.timestamp()) + ' - '
            + str(self.lastPingTime.timestamp()) + ' - '
            + self.token)

class VCLog(models.Model):
    channel = models.CharField(max_length=100)
    uid1 = models.CharField(max_length=128)
    uid2 = models.CharField(max_length=128)
    startTime = models.DateTimeField(auto_now_add=True)
    endTime = models.DateTimeField(auto_now=True)