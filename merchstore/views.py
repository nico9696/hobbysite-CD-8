from django.shortcuts import render
from .models import ProductType, Product

def show_products_list(request):
    return render(request, "merchstore/product_list.html", {"product_list": Product.objects.all()})

def show_product_detail(request):
    return render(request, "merchstore/product_detail.html", {"product": Product.objects.all()})