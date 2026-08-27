from urllib import request

from django.shortcuts import render

def home(request):
    name = "shayan"
    return render(request, "home.html", {"name": name})