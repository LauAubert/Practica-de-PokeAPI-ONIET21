from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import login_auth, logout_auth, register

urlpatterns = [
    path("login/", login_auth, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout_auth, name="logout"),
]
