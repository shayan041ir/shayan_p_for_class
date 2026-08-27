from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.blogs_list)   # 127.0.0.1:8000/blog/list_blogs
]
