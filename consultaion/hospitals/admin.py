from django.contrib import admin

from .models import *

admin.site.register(Doctor)

admin.site.register(TakeAppointment)