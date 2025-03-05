from django.contrib import admin
from .models import ProductType, Product

class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    search_fields = ('name', )
    list_display = ('id', 'name')  # Shows readable names

class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ('name', )
    list_display = ('id', 'name')  # Shows readable names

# Register your models here.
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)