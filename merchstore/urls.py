from django.urls import path
from . import views

urlpatterns = [
    path("items", views.show_products_list, name="show_products_list"), 
    path("item/<int:num>", views.show_product_details, name="show_product_details"),
]