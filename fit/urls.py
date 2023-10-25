from django.urls import path
from . import views
urlpatterns=[
    path('Home/',views.Home,name='Home'),
    path('Home/SignUp/',views.SignUp,name='SignUp'),
    path('Home/SignIn/',views.SignIn,name='SignIn'),
    path('Home/SignIn/SignUp/',views.SignUp,name='SignUp'),
    path('Home/Challenges/',views.Challenges,name='Challenges'),
    path('Home/SignIn/SignUp/CreateUser/',views.CreateUser,name='CreateUser'),
    path('Home/SignIn/Challenges/',views.Challenges,name='Challenges'),    
]
