from django.forms import ModelForm
from  .models import *

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['doctor','patient']
