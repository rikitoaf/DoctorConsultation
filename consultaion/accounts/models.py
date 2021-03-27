from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_sex = (('MALE', 'Male'), ('FEMALE', 'Female'))
    user_gender = models.CharField(max_length=6, default='Male', choices=user_sex)
    user_age = models.IntegerField(null=True)
    user_phone = models.CharField(max_length=200, null=True)
    user_address = models.CharField(max_length=200, null=True)
    user_email = models.CharField(max_length=200, null=True)
    user_img = models.ImageField(upload_to='profile_pics', default='default.jpg')
    is_doctor = models.BooleanField(default = False)

    def __str__(self):
        return self.user.username

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