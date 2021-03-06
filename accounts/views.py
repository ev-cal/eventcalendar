from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method=="POST":
        name=request.POST['nickname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if len(password1)>=8:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already taken')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email already taken')
                    return redirect('register')
                else:
                    user=User.objects.create_user(first_name=name,username=username,email=email,password=password2)
                    user.save()
                    return redirect('login')
            else:
                messages.info(request,'Password must have atleast 8 characters')
                return redirect('register')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
           
    else:
        return render(request,"register.html")


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')