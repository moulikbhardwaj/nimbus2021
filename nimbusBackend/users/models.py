from django.db.models import Model, CASCADE
from django.db.models.fields import CharField, EmailField

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
