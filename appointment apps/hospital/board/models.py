from django.db import models

# Create your models here.


class Doctor (models.Model):
    doctor_name = models.CharField( max_length=50, null = True )
    registration_date = models.DateField(auto_now_add = True)
    def __str__(self):
        return self.doctor_name

class Patient (models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.CharField( max_length=50, null = True)
    registration_date = models.DateField(auto_now_add = True)
    waiting_status = models.BooleanField(default = True)

    @property
    def is_waiting(self):
        return bool(self.waiting_status)

    def __str__(self):
        return self.patient