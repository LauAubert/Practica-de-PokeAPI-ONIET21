from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    if request.method == "POST":
        if request.POST.get("submit") == "submit":
            user = request.POST.get("user")
            password = request.POST.get("password")
            
        if request.POST.get("register") == "register":
            return redirect("register")    
        
    return render(request, "login.html")


def register(request):
    
    User.create_user(username=user, password=password)
            
    return render(request, "register.html")


def logout(request):
    
    return render(request, "login.html")

