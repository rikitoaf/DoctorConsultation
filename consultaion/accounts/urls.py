from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from.import views


urlpatterns = [
    path("",views.home, name="home"),
    path("profile/<str:pk>/",views.profile, name="profile"),
    path("profile_edit/",views.profile_edit, name="profile_edit"),

    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('about/', views.about, name="about"),
    
    path('testreport/', views.model_form_upload, name="testreport"),
    
    path('doctor/', include('hospitals.urls'))
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)