from django.db.models import Model
from django.db.models.fields import CharField, URLField

# Create your models here.
class Department(Model):
    name = CharField('name', max_length=255, null=False, unique=True, primary_key=True)
    password = CharField('password', max_length=128, null=False, blank=False,
                         help_text='Leave empty if no change needed')
    image = URLField('image')

    def __str__(self) -> str:
        return "Department/Club: " + self.name
