from django.contrib import admin
from .models import ProductType, Product

# can add product type straight from product table
class ProductInline(admin.TabularInline):  
    model = Product

class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    search_fields = ('name', )
    list_display = ('id', 'name', 'description')  # Shows these readably
    ordering = ('name',)  # Orders ProductType alphabetically by name

class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ('name', )
    list_display = ('id', 'name', 'product_type', 'description', 'price')  # Shows these readably
    ordering = ('name',)  # Orders ProductType alphabetically by name

# Register your models here.
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)