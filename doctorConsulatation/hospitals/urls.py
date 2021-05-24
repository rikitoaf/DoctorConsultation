from django.urls import path
from . import views

urlpatterns = [
     path('createdocprofile/',views.set_doctor_profile, name = 'createdocprofile'),
     path('doctoredit/', views.doctor_edit, name="doctoredit"),
     path('dashboard/', views.dashboard, name="dashboard"),
     path('doctorview/', views.doctor_view, name="doctorview"),
     path('appointment/<str:pk>/', views.appointment, name="appointment"),
     path('visiting/<str:pk>/', views.visiting, name="visiting"),
     path('sendsupport/',views.sendanemail, name = "appointmentmail"),
]
