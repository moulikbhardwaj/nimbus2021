from django.contrib import admin

# Register your models here.
from quiz.models import ScoreBoard

admin.site.register([
    ScoreBoard
])