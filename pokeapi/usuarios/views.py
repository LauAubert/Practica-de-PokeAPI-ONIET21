from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def login_auth(request):
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
        user = request.POST.get("username")
        name = request.POST.get("first_name")
        nickname = request.POST.get("last_name")
        password = request.POST.get("password")
        mail = request.POST.get("email")
        try:
            user = User.objects.create_user(username=user, password=password, first_name=name, last_name=nickname, email=mail)
            return redirect("menu",0) 
        except Exception:
            return render(request, "register.html", {"failed": True})
    return render(request, "register.html")


def logout_auth(request):
    return redirect(request, "menu")

