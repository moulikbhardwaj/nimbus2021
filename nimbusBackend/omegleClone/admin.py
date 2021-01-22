from django.contrib import admin

from .models import VCQueue, VCLog

# Register your models here.
admin.site.register(VCQueue)
admin.site.register(VCLog)