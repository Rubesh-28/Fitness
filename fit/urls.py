from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('SignUp/', views.SignUp, name='SignUp'),
    path('SignIn/', views.SignIn, name='SignIn'),
    path('CreateUser/', views.CreateUser, name='CreateUser'),
    path('Login/', views.Login, name='Login'),
    path('Challenges/', views.Challenges, name='Challenges'),
]
