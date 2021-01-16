from django.db.models import Model
from django.db.models.fields import CharField, DateTimeField, IntegerField, URLField
from django.db.models import ImageField, CASCADE
from django.db.models.fields.files import FileField
from django.db.models.fields.related import ForeignKey

from departments.models import Department
# Create your models here.

class Event(Model):
    name = CharField("name", max_length=255, null=False)
    abstract = FileField("abstract",upload_to="events/abstract/")
    info = CharField("info", max_length=512)
    venue = CharField("venue", max_length=64)
    start = DateTimeField("start")
    end = DateTimeField("end")
    image = ImageField("image", upload_to="events/images")
    regURL = URLField("regURL")

    DEPARTMENT_EVENT = 0
    INSTITUTE_EVENT = 1
    TALK = 2
    EXHIBITION = 3
    WORKSHOP = 4

    choices = (
        (0,DEPARTMENT_EVENT),
        (1,INSTITUTE_EVENT),
        (2,TALK),
        (3,EXHIBITION),
        (4,WORKSHOP),
    )

    Type = IntegerField("type", choices=choices)

    department = ForeignKey(Department, on_delete=CASCADE)