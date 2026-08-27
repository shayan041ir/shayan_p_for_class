from django.shortcuts import render
from django.http import HttpResponse

def blogs_list(request):
    return render(request , "blog/blog_list.html")