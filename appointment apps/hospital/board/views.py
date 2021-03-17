from django.shortcuts import render,redirect
from . models import Doctor,Patient
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def IndexView(request):
    patient = Patient.objects.all()
    patients = Patient.objects.filter(waiting_status = True)
    context = {patients: 'patients'} 

    return render (request,"board/appointment.html",context)

# class PatientCreateView (CreateView):
#     model = Patient
#     fields = ["doctor","patient"]
#     success_url = reverse_lazy("board:appointment")