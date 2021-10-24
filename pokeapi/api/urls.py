from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [

    path('prueba/', views.prueba),
    path('menu/', views.menu, name='menu'),
    path('profile/', views.profile, name='profile')
    
]