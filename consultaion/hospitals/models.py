from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
from django.utils import timezone


department = (
    ('Dentistry', "Dentistry"),
    ('Cardiology', "Cardiology"),
    ('ENT Specialists', "ENT Specialists"),
    ('Astrology', 'Astrology'),
    ('Neuroanatomy', 'Neuroanatomy'),
    ('Blood Screening', 'Blood Screening'),
    ('Eye Care', 'Eye Care'),
    ('Physical Therapy', 'Physical Therapy'),
)



class Doctor(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(choices=department, max_length=100)
    name = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    institution = models.CharField(max_length=50, default = "DMC")


    start_time = models.CharField( max_length=50)
    end_time = models.CharField( max_length=50)

    week_sat = models.BooleanField(default = False)
    week_sun = models.BooleanField(default = False)
    week_mon = models.BooleanField(default = False)
    week_tues = models.BooleanField(default = False)
    week_wed = models.BooleanField(default = False)
    week_thurs = models.BooleanField(default = False)
    week_fri = models.BooleanField(default = False)


    def __str__(self):
        return "Dr. " + self.name


  
class TakeAppointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    message = models.CharField( max_length=100)
    date = models.DateTimeField(default=timezone.now)
    is_visited = models.BooleanField(default = False)


