
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import *
from . import forms
from .forms import SetDoctorProfile,SetAppointment,DoctorEditForm



def set_doctor_profile(request):
	if request.method == "POST":
		form = forms.SetDoctorProfile(request.POST, request.FILES)
		form.name = request.user
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()

			return redirect('home')
	else:
		form = forms.SetDoctorProfile()
	return render(request, 'hospitals/set_doctor_profile.html',{"form": form})


def doctor_edit (request):
	# doctor_ins = Doctor.objects.get(doc_name=request.user)
	if request.method == 'POST':
		doc_form = DoctorEditForm(data=request.POST or None,instance=request.user.doctor)
		if doc_form.is_valid():
			doc_form.save()
			
			
			return redirect("/")
	else:
		doc_form = DoctorEditForm (instance = request.user.doctor)
	
	context = {
		'doc_form' : doc_form
	}
	return render(request, 'hospitals/doctor_edit.html', context)

def dashboard(request):
	
	doc = Doctor.objects.get(user = request.user)

	appointment = TakeAppointment.objects.filter(doctor = doc )
	total = appointment.count()
	visited = TakeAppointment.objects.filter(is_visited = True , doctor = doc)
	visited = visited.count()
	remaining = total - visited
	context = {'appointment' : appointment, 'total' : total, 'remaining' : remaining, 'visited' : visited}

	return render(request, 'hospitals/dashboard.html',context)

def visiting(request,pk):
	doc = Doctor.objects.get(user = request.user)
	user = User.objects.get(username =pk)
	appointment = TakeAppointment.objects.get(doctor = doc, user = user )
	appointment.is_visited = True
	appointment.save()
	appointment = TakeAppointment.objects.filter(doctor = doc )
	total = appointment.count()
	visited = TakeAppointment.objects.filter(is_visited = True , doctor = doc)
	visited = visited.count()
	remaining = total - visited
	context = {'appointment' : appointment, 'total' : total, 'remaining' : remaining, 'visited' : visited}

	return render(request, 'hospitals/dashboard.html',context)


def doctor_view(request):
	doctors=Doctor.objects.all()
	context={'doctors':doctors}
	for d in doctors:
		print(d)

	return render(request, 'hospitals/doctorView.html',context)

def appointment(request,pk):
	user=User.objects.filter(username = pk).first()
	doc = Doctor.objects.get(user = user)
	if request.method == "POST":
		form = forms.SetAppointment(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.doctor = doc
			instance.save()
			messages.info(request, 'successfully appointed')
			return redirect('home')
	else:
		form = forms.SetAppointment()
	return render(request, 'hospitals/appointment.html',{"form": form})

	