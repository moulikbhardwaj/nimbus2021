from django.db.models import Model
from django.db.models.fields import CharField, DateTimeField, IntegerField, URLField
from django.db.models import ImageField, CASCADE
from django.db.models.fields.files import FileField
from django.db.models.fields.related import ForeignKey

from departments.models import Department
# Create your models here.

class Event(Model):
    name = CharField("name", max_length=255, null=False)
    abstract = FileField("abstract",upload_to="events/abstract/", blank=True, null=True)
    info = CharField("info", max_length=512, blank=True, null=True)
    venue = CharField("venue", max_length=64, blank=True, null=True)
    start = DateTimeField("start", null=False)
    end = DateTimeField("end", blank=True, null=True)
    image = ImageField("image", upload_to="events/images", blank=True)
    regURL = URLField("regURL", blank=True, null=True)

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

    def __str__(self) -> str:
        return f"{self.department.name}: {self.name}"
    
    def __repr__(self) -> str:
        if self.Type == 0:
            return f"<Department_Event: {self.__str__()}>"
        if self.Type == 1:
            return f"<Institution_Event: {self.__str__()}>"
        if self.Type == 2:
            return f"<Talk: {self.__str__()}>"
        if self.Type == 3:
            return f"<Exhibition: {self.__str__()}>"
        if self.Type == 0:
            return f"<Workshop: {self.__str__()}>"