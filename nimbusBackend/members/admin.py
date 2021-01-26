from django.contrib import admin

from members.models import Sponsors,CoreTeam

# Register your models here.

admin.site.register(CoreTeam)
admin.site.register(Sponsors)
