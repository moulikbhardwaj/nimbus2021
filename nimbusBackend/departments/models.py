from django.db.models import ImageField, CASCADE

from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.fields.related import OneToOneField


# Create your models here.
class Department(Model):
    name = CharField("name", primary_key=True, max_length=255, unique=True, null=False)
    user = OneToOneField(User, related_name='department', on_delete=CASCADE)
    image = ImageField('image', upload_to="department/images", null=True,blank=True)
    password = CharField('password', max_length=128, null=True, blank=True,
                         help_text='Leave empty if no change needed')

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        super(Department, self).save(*args, **kwargs)
        user:User = self.user
        user.password = self.password
        user.save()
        return self