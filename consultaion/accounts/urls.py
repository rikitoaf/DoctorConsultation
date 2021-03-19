from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from.import views


urlpatterns = [
    path("",views.home, name="home"),
    
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('about/', views.about, name="about"),
]