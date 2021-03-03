from django.db.models import ForeignKey, CASCADE, Model
from django.db.models.fields import DateTimeField
from django.db.models import ImageField

from departments.models import Department

# Create your models here.

class GalleryPost(Model):
    department = ForeignKey(Department, on_delete=CASCADE)
    image = ImageField("image", upload_to="gallery/images")
    upload_time = DateTimeField("upload_time", auto_now=True, editable=False)
