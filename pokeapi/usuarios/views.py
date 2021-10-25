from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



def login_auth(request):
    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=user, password=password)
        if user is not None:
            login(request=request, user=user)
            return redirect("menu", 0)
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
            login(request=request, user=user)
            return redirect("menu",0) 
        except Exception:
            return render(request, "register.html", {"failed": True})
    return render(request, "register.html")




@login_required()
def logout_auth(request):
    logout(request)
    return redirect("menu", 0)

