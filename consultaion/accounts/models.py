from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Patient(models.Model):
# 	name = models.CharField(max_length=200, null=True)
#     age = models.IntegerField(null=True)
# 	phone = models.CharField(max_length=200, null=True)
#     address = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)

# 	def __str__(self):
# 		return self.name

# class Department(models.Model):
# 	name = models.CharField(max_length=200, null=True)

# 	def __str__(self):
# 		return self.name

# class Doctor(models.Model):
# 	name = models.CharField(max_length=200, null=True)
# 	phone = models.CharField(max_length=200, null=True)
#     address = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#     department = models.ForeignKey(Department, null=True, on_delete= models.SET_NULL)

# 	def __str__(self):
# 		return self.name