from math import ceil

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import  CreateUserForm,UserEditForm,ProfileEditForm,DocumentForm
from django.db import IntegrityError
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from hospitals.models import TakeAppointment
from .models import *

def home (request):
    return render(request,'accounts/index.html')

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def about(request):
	
	return render(request, 'accounts/about.html')


def profile(request,pk):
	
	u=User.objects.filter(username=pk).first()
	appointment = TakeAppointment.objects.filter(user = u )
	context={'u':u, 'appointment' : appointment}

	return render(request, 'accounts/profile.html',context)


def profile_edit(request):
    if request.method == 'POST':
        u_form = UserEditForm(data=request.POST or None, instance=request.user)
        p_form = ProfileEditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('home')

    else:
        u_form = UserEditForm(instance=request.user)
        p_form = ProfileEditForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/profile_edit.html', context)

# def doctor_edit (request):
# 	# doctor_ins = Doctor.objects.get(doc_name=request.user)
# 	if request.method == 'POST':

# 		doc_form = DoctorEditForm(data=request.POST or None)
# 		if doc_form.is_valid():
# 			form = doc_form.save(commit = False)
# 			form.doc_name = request.user
# 			form.save()
			
			
# 			return redirect("/")
# 	else:
# 		doc_form = DoctorEditForm (instance = request.user)
	
# 	context = {
# 		'doc_form' : doc_form
# 	}
# 	return render(request, 'accounts/doctor_edit.html', context)

def model_form_upload(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit = False)
			form.user = request.user
			try:
				form.save()
			except IntegrityError:
				pass
			return redirect('home')
	else:
		form = DocumentForm()
	return render(request, 'accounts/testreport.html', {
		'form': form
		})	


