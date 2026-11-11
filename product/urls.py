from django.urls import path
from . import views

urlpatterns = [
    path("product_list/", views.product_list, name="product_list"),
    path("product_detail/<int:id>/", views.product_detail, name="product_detail"),
    path("category/<int:id>/", views.category_products, name="category_products"),

    
    path("create/", views.product_create, name="product_create"),
]
