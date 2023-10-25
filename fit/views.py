from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import loader
from fit.models import Registration
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def Home(request):
    template=loader.get_template('Home.html')
    return HttpResponse(template.render())
def Challenges(request):
    template=loader.get_template('Challenges.html')
    return HttpResponse(template.render())
def SignUp(request):
    template=loader.get_template('SignUp.html')
    return HttpResponse(template.render({},request))

def SignIn(request):
    template=loader.get_template('SignIn.html')
    return HttpResponse(template.render({},request))

def CreateUser(request):
    # if request.method == 'POST':
    name=request.POST['Name']
    uname = request.POST['Username']
    Email = request.POST['Mail']
    phone=request.POST['Phone']
    Gender = request.POST['Gender']
    Password = request.POST['Password']
    val=Registration(full_name = name,username = uname,email = Email,phone_number = phone,gender = Gender,password=Password)
    val.save()
    return HttpResponseRedirect(reverse('SignIn'))
    # else:
    #     return render(request, 'SignUp')



def Login(request):
    if request.method == 'POST':
        try:
            username = request.POST['Uname']
            password = request.POST['Pass']
        except KeyError:
            return HttpResponse("Form data is incomplete")
        try:
            user = Registration.objects.get(username=username)
            if user.password == password:
                # Redirect to the 'challenges' page after successful authentication
                return redirect('Challenges')  # Redirect to the challenges page
            else:
                return HttpResponse("Wrong password")
        except Registration.DoesNotExist:
            return HttpResponse("User does not exist")
    else:
        return HttpResponse("Invalid request method")


