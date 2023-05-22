
import statistics
from django.urls import path,include

from ArtyProd import settings
from . import views
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from . import views
from .views import *
app_name='projet'
urlpatterns = [
  
    
     path('',views.index1,name='index1'),
     path('portfolio/', portfolio_view, name='portfolio'),
     path('services/', services_view, name='services'),
     path('home/',home,name='home'),
     path('equipes/',EquipeView,name='equipe'),
     path('contact/',contact,name='contact'),
     path('portfolio/<int:id>/',portfolio_detail,name='portfolio_detail'),
     path('profile/',profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
    path('register/', views.registerView, name='register'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name = 'logout'),
    path('ajouter_projet/',views.ajouter_projet,name='ajouter_projet'),
    path('projet/', views.projet, name='projet'),
    path('project/<int:project_id>/', views.project_details, name='project_details'),     
     ]
