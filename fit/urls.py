from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'), 
    path('SignUp/', views.SignUp, name='SignUp'),
    path('SignIn/', views.SignIn, name='SignIn'),
    path('SignIn/SignUp/', views.SignUp, name='SignUp'),
    path('Challenges/', views.Challenges, name='Challenges'),
    path('SignIn/SignUp/CreateUser/', views.CreateUser, name='CreateUser'),
    path('SignIn/Challenges/', views.Challenges, name='Challenges'),
]

