from django.urls import path
from . import views

urlpatterns = [
    path("items/", views.show_products_list, name="show_products_list"), 
    path("item/<int:num>/", views.show_product_details, name="show_product_details"),
    path("item/add/", views.add_product, name="add_product"),
    path("cart/<str:profile>", views.show_cart, name="show_cart"),
    path("cart/<str:profile>", views.update_product, name="update_product"),
]