from django.urls import path
from . import views
# from اسم اپ import views

urlpatterns = [
    path('', views.home , name = "home")   # 127.0.0.1:8000
]
