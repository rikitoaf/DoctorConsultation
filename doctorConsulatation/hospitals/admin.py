from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

admin.site.register(Doctor)

admin.site.register(TakeAppointment)
admin.site.register(Department)
admin.site.register(MeetLink)
