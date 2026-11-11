from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from .forms import ProductForm


# def product_create(request):


#     if request.method == "POST":

#         print("POST received")
#     else:

#         form = ProductForm()
#         # form = ProductForm(request.POST)  form ra ba post por mikonim


#     return render(
#         request,
#         "product/product_create.html",
#         {"form": form}
#     )
# def product_create(request):

#     if request.method == "POST":

#         name = request.POST.get("name")
#         price = request.POST.get("price")

#         print(name)
#         print(price)

#     form = ProductForm()

#     return render(
#         request,
#         "product/product_create.html",
#         {"form": form}
#     )


# def product_create(request):

#     if request.method == "POST":

#         form = ProductForm(request.POST)

#         if form.is_valid():
#             print("اطلاعات معتبر است")

#     else:

#         form = ProductForm()

#     return render(
#         request,
#         "product/product_create.html",
#         {"form": form}
#     )

def product_create(request):

    if request.method == "POST":

        form = ProductForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            price = form.cleaned_data["price"]

            print(name)
            print(description)
            print(price)

    else:

        form = ProductForm()

    return render(
        request,
        "product/product_create.html",
        {"form": form}
    )


def product_list(request):

    search = request.GET.get("search")

    if search:
        products = Product.objects.filter(
            name__icontains=search
        )
    else:
        products = Product.objects.all()

    return render(
        request,
        "product/product_list.html",
        {
            "products": products,
            "search": search,
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