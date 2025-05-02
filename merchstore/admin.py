from django.contrib import admin
from .models import ProductType, Product

# enables adding product type straight from product table
class ProductInline(admin.TabularInline):  
    model = Product

class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    search_fields = ('name', )
    list_display = ('id', 'name', 'description')  # Shows these readably
    ordering = ('name',)  # Orders ProductType alphabetically by name

    # got help from ChatGPT
    # fulfills: "determined by developers and cannot be modified by regular users"
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser  # or some custom group check
    def has_add_permission(self, request):
        return request.user.is_superuser
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ('name', )
    list_display = ('id', 'name', 'product_type', 'description', 'price')  # Shows these readably
    ordering = ('name',)  # Orders Product alphabetically by name
    list_filter = ('product_type', )

# models registered here.
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)