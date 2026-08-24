from django.shortcuts import render ,Https_response

def blogs_list(request):
    name = "shayan"
    return render(request , "home.html" , { name : "name" })