from django.urls import path
from . import views
urlpatterns = [
    path('blog_list/', views.blogs_list , name="blog_list"),   # 127.0.0.1:8000/blog/blog_list
    path('blog_detail/<int:id>/', views.blog_detail)   # 127.0.0.1:8000/blog/blog_detail/1
]
