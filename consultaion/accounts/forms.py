from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile,Document

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            'username',
            'email'
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = {'user','is_doctor'}


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document' )

# class DoctorEditForm(forms.ModelForm):
#     class Meta:
#         model = Doctor
#         exclude = {'doc_name'}