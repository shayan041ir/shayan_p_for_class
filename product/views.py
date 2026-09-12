from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        "product/product_list.html",
        {
            "products": products
        }
    )


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(
        request,
        "product/product_detail.html",
        {
            "product": product
        }
    )


def category_products(request, id):
    category = get_object_or_404(Category, id=id)

    products = Product.objects.filter(
        category=category
    )

    return render(
        request,
        "product/category_products.html",
        {
            "category": category,
            "products": products
        }
    )