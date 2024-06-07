from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from fit.models import Registration
from django.contrib import messages
from django.urls import reverse

def Home(request):
    return render(request, 'Home.html')

def Challenges(request):
    username = request.session.get('username', None)
    return render(request, 'Challenges.html', {'username': username})

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
                request.session['username'] = username
                return redirect('Challenges')
            else:
                messages.error(request, "Wrong password.")
                return redirect('SignIn')
        except Registration.DoesNotExist:
            messages.error(request, "User does not exist.")
            return redirect('SignIn')
    else:
        return HttpResponse("Invalid request method.")
