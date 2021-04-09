from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import Doctor,TakeAppointment

class DoctorEditForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = {'user'}


class SetDoctorProfile(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = {'user'}

class SetAppointment (forms.ModelForm):
    class Meta:
        model = TakeAppointment
        exclude = {'user','date','is_visited','doctor'}
