from django.shortcuts import render
from .models import Product

def show_products_list(request):
    return render(request, "merchstore/products_list.html", {"product_list": Product.objects.all()})

def show_product_details(request, num):
    return render(request, "merchstore/product_details.html", {"product": Product.objects.filter(id=num)})