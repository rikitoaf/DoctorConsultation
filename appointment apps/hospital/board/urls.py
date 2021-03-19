from django.urls import path
from . import views


urlpatterns = [
    path('',views.IndexView, name = "home"),
    
    path('create_patient/',views.PatientCreateView, name = 'create_patient'),
    path('update_patient/<str:pk>',views.PatientUpdateView, name = 'update_patient'),
    path('delete_patient/<str:pk>',views.PatientDeleteView, name = 'delete_patient'),
    
    
]