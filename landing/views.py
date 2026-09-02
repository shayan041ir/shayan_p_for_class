from urllib import request

from django.shortcuts import render

def home(request):
    std = {
        "name":"shayan",
        "age" : 23,
        "city" : "tabriz",
        }

    return render(request, "home.html", {"std": std})
