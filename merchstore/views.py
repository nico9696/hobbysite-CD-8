from django.shortcuts import render
from .models import ProductType, Product

def show_products_list(request):
    product_types = list(ProductType.objects.all())  # Converts QuerySet to list
    has_null_products = Product.objects.filter(product_type__isnull=True).exists()  # Checks if null product type exists

    # If there are products with no product type, "Others" category is added manually
    if has_null_products:
        product_types.append(ProductType(name="Others", description="Products with no particular product type"))

    return render(request, "merchstore/products_list.html", {
        "product_type_list": product_types,
        "product_list": Product.objects.all(),
        "null_product_type_list": Product.objects.filter(product_type__isnull=True)
        })

def show_product_details(request, num):
    return render(request, "merchstore/product_details.html", {"product": Product.objects.filter(id=num)})