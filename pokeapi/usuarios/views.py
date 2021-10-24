from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def login(request):
    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=user, password=password)
        if user is not None:
            return redirect("menu")
        else:
            return render(request, "login.html", {"Failed": True})  
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        if request.POST.get("submit") == "submit":
            user = request.POST.get("user")
            password = request.POST.get("password")
            repeat_password = request.POST.get("repeat_password")
            email = request.POST.get("email")
            if password == repeat_password:
                User.create_user(user, password, email)
                print(user, password, repeat_password, email)
            else:
                return render(request, "register.html")        
    return render(request, "thomasLogin.html")


def logout(request):
    return redirect(request, "menu")

