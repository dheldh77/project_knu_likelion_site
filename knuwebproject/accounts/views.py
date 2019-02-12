from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        passwd = request.POST['passwd']
        user = auth.authenticate(request,username=user_id,password=passwd)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,"login.html",{'error':'user ID or password is incorrect'})
    else:
        return render(request,"login.html")

def signup(request):
    if request.method == "POST":
        if request.POST['passwd1'] == request.POST['passwd2']:
            user = User.objects.create_user(username=request.POST['user_id'], password=request.POST['passwd1'])
            auth.login(request, user)
            return redirect('home')
    return render(request,"signup.html")

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return render(request,'login.html')