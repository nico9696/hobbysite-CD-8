from django.shortcuts import render
from .models import ProductType, Product

def show_product_types(request):
    return render(request, "merchstore/product_list.html", {"product_list": Product.objects.all()})