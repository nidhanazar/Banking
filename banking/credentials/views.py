from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('new')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,"login.html")



def register(request):
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['password']
        cpassword=request.POST['confirm_password']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                messages.info(request, "User created")
                return redirect('login')
        else:
            messages.info(request,"password not matches")
            return redirect('register')

    else:
        return render(request,"register.html")


def new(request):
    return render(request,'new.html')


def form(request):
    if request.method=='POST':
        name=request.POST['name']
        dob=request.POST['dob']
        age=request.POST['age']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        gender = request.POST['gridRadios']
        district = request.POST['district']
        branch = request.POST['branch']
        account_type = request.POST['account_type']

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
        else:
            messages.success(request, "Form submitted")
        return redirect('form')

    return render(request, 'form.html')






def logout(request):
    auth.logout(request)
    return redirect('/')