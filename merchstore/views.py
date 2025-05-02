from django.shortcuts import render
from .models import ProductType, Product
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.db.models import Q

@login_required(login_url='login')
def show_products_list(request):
    user = request.user  # the logged-in user
    profile = Profile.objects.get(user=user)  # fetch the user's profile
    is_users = Product.objects.filter(owner=profile)
    is_not_users = Product.objects.filter(~Q(owner=profile))

    product_types = list(ProductType.objects.all())  # Converts QuerySet to list
    has_null_products = Product.objects.filter(product_type__isnull=True).exists()  # Checks if null product type exists

    # If there are products with no product type, "Others" category is added manually
    if has_null_products:
        product_types.append(ProductType(name="Others", description="Products with no particular product type"))

    return render(request, "merchstore/products_list.html", {
        "users_products_list": is_users,
        "not_users_products_list": is_not_users,

        "product_type_list": product_types,
        "product_list": Product.objects.all(),
        "null_product_type_list": Product.objects.filter(product_type__isnull=True)
        })

@login_required(login_url='login')
def show_product_details(request, num):
    return render(request, "merchstore/product_details.html", {"product": Product.objects.filter(id=num)})