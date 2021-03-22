from django.db import models
import datetime

from users.models import User

# Create your models here.

class VCQueue(models.Model):
    uid = models.CharField(max_length=128, primary_key=True, blank=False, null=False)
    enterTime = models.DateTimeField(auto_now_add=True)
    lastPingTime = models.DateTimeField(auto_now=True)
    channel = models.CharField(max_length=100, default='')
    token = models.CharField(max_length=256, default='')
    uid2 = models.CharField(max_length=128, default='')

    class Meta:
        ordering = ['enterTime']

    def __str__(self):
        return (self.uid + ' - '
            + self.channel + ' - '
            + str(self.enterTime) + ' - '
            + str(self.lastPingTime) + ' - '
            + self.token)

class VCLog(models.Model):
    channel = models.CharField(max_length=100)
    uid1 = models.CharField(max_length=128)
    uid2 = models.CharField(max_length=128)
    startTime = models.DateTimeField(auto_now_add=True)
    endTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            self.channel + ' - '
            + self.uid1 + ' - '
            + self.uid2 + ' - '
            + str(self.startTime) + ' - '
            + str(self.endTime)
        )

class Report(models.Model):
    channel = models.CharField(max_length=100)
    reporter = models.ForeignKey(User, related_name='reporter_user', on_delete=models.CASCADE)
    reported = models.ForeignKey(User, related_name='reported_user', on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return (
            self.channel + ' - '
            + self.reporter.username + ' - '
            + 'reported - '
            + self.reported.username + ' - '
            + self.reason
        )
