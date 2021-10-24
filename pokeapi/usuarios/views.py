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
        user = request.POST.get("user")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=user, password=password)
        except:
            user = User.objects.create_user(username=user, password=password)
            return redirect("menu")       
    return render(request, "register.html")


def logout(request):
    return redirect(request, "menu")

