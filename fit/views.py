from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from fit.models import Registration
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def Home(request):
    return render(request, 'Home.html')

def Challenges(request):
    return render(request, 'Challenges.html')

def SignUp(request):
    return render(request, 'SignUp.html')

def SignIn(request):
    return render(request, 'SignIn.html')

def CreateUser(request):
    if request.method == 'POST':
        name = request.POST['Name']
        uname = request.POST['Username']
        email = request.POST['Mail']
        phone = request.POST['Phone']
        gender = request.POST['Gender']
        password = request.POST['Password']
        
        if not all([name, uname, email, phone, gender, password]):
            messages.error(request, "All fields are required.")
            return redirect('SignUp')

        # You should hash the password before saving it
        user = Registration(full_name=name, username=uname, email=email, phone_number=phone, gender=gender, password=password)
        user.save()
        return HttpResponseRedirect(reverse('SignIn'))
    else:
        return render(request, 'SignUp.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('Uname')
        password = request.POST.get('Pass')
        
        if not all([username, password]):
            messages.error(request, "Both username and password are required.")
            return redirect('SignIn')
        
        try:
            user = Registration.objects.get(username=username)
            if user.password == password:
                # Redirect to the 'challenges' page after successful authentication
                return redirect('Challenges')
            else:
                messages.error(request, "Wrong password.")
                return redirect('SignIn')
        except Registration.DoesNotExist:
            messages.error(request, "User does not exist.")
            return redirect('SignIn')
    else:
        return HttpResponse("Invalid request method.")
