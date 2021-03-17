from django.urls import path
from . import views


urlpatterns = [
    path('',views.IndexView, name = "home"),
    
 #   path('create_patient/',views.PatientCreateView, name = 'create_patient'),
    # path('update_order/<str:pk>',views.updateOrder, name = 'update_order'),
    # path('delete_order/<str:pk>',views.deleteOrder, name = 'delete_order'),
    
]