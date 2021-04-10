from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_sex = (('MALE', 'Male'), ('FEMALE', 'Female'))
    user_gender = models.CharField(max_length=6, default='Male', choices=user_sex)
    user_age = models.IntegerField(null=True)
    user_phone = models.CharField(max_length=200, null=True)
    user_address = models.CharField(max_length=200, null=True)
    user_img = models.ImageField(upload_to='profile_pics', default='default.jpg')
  

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def _post_save_receiver(sender,created,instance, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    instance.profile.save()
    




class Document(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
# class Department(models.Model):
#     dept_name = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return self.dept_name

