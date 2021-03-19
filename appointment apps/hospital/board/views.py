from django.shortcuts import render,redirect
from . models import Doctor,Patient
from .forms import PatientForm

# Create your views here.

def IndexView(request):
    patient = Patient.objects.all()
    patients = Patient.objects.filter(waiting_status = True)
    context = {'patients': patients} 

    return render (request,"board/appointment.html",context)

def PatientCreateView (request):
    forms = PatientForm()
    if request.method == 'POST':
    #print('Printing Post :', request.POST)
        forms = PatientForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    context = {'form': forms}
    return render (request, 'board/create_patient.html',{'context' : context})

def PatientUpdateView (request,pk):
    patient = Patient.objects.get(id = pk)
    form = PatientForm(instance = patient)
    if request.method == 'POST':
        #print('Printing Post :', request.POST)
        form = PatientForm(request.POST,instance = patient)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render (request, 'board/update_patient.html',{'context' : context})

def PatientDeleteView (request,pk):
    patient = Patient.objects.get(id = pk)
    if request.method == "POST":
        patient.delete()
        return redirect('/')

    context = {'patient':patient}
    return render(request, 'board/delete_patient.html', context)



        
    
    