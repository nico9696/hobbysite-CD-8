# left off: Users should not be able to purchase their own products.

from django.shortcuts import render
from .models import ProductType, Product
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.db.models import Q
from .forms import ProductForm, TransactionForm
from django.shortcuts import redirect
from django.contrib import messages


# @login_required(login_url='login')
def show_products_list(request):
    user = request.user  # the logged-in user

    # if the user is logged in
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=user)  # fetch the user's profile
        is_users = Product.objects.filter(owner=profile)
        is_not_users = Product.objects.filter(~Q(owner=profile))
    else:
        is_users = None
        is_not_users = Product.objects.all()

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


# @login_required(login_url='login')
def show_product_details(request, num):
    user = request.user  # the logged-in user
    
    # if the user is logged in
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=user)  # fetch the user's profile
    else:
        profile = None

    product_qs = Product.objects.filter(id=num) # returns queryset (for iterating in template)
    product_obj = Product.objects.get(id=num) # returns object (to get one field/attribute of object in template)

    if (request.method == "POST"):
        transaction_form = TransactionForm(request.POST, prefix="transaction")

        if not request.user.is_authenticated:
            return redirect('login') 

        if transaction_form.is_valid():
            transaction = transaction_form.save(commit=False) # Create but don't save yet
            transaction.buyer = profile # Set the desired field value
            transaction.product = product_obj
            transaction.save() # Now save to the database

            # Prevent overselling
            if transaction.amount > product_obj.stock:
                messages.error(request, "Not enough stock available.")
                return redirect('show_product_details', num=num)  
            
            product_obj.stock -= transaction.amount # reduces stock based on quantity bought
            if product_obj.stock <= 0: # change status based on stock
                product_obj.status = 'out_of_stock'
            elif product_obj.stock >= 1:
                product_obj.status = 'available'
            product_obj.save()
        return redirect('show_products_list')

    transaction_form = TransactionForm(prefix="transaction")

    return render(request, "merchstore/product_details.html", {
        "product_qs": product_qs,
        "product_obj": product_obj,
        "profile": profile,
        'buy_product_form': transaction_form,
    })


@login_required(login_url='login')
def add_product(request):
    if (request.method == "POST"): 
        user = request.user  # the logged-in user
        profile = Profile.objects.get(user=user)  # fetch the user's profile
        product_form = ProductForm(request.POST, prefix="product")

        if product_form.is_valid():
            product = product_form.save(commit=False) # Create but don't save yet
            product.owner = profile # Set the desired field value
            product.save() # Now save to the database

        return redirect('show_products_list')
    
    product_form = ProductForm(prefix="product")

    return render(request, 'merchstore/add_product.html', {
        'add_product_form': product_form,
    })