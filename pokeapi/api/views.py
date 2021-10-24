from django.shortcuts import render, redirect
import json,requests
from django.contrib.auth.models import User
# Create your views here.

def prueba(request):
    return render(request, 'prueba.html')


