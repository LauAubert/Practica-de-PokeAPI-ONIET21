from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import login, register, logout

urlpatterns = [
    path("login", login, name="login"),
    path("register", register, name="register"),
    path("logout", logout, name="logout"),
]
