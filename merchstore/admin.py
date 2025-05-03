from django.contrib import admin
from .models import ProductType, Product, Transaction

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
    list_display = ('id', 'name', 'product_type', 'owner', 'description', 'price', 'stock', 'status')  # Shows these readably
    ordering = ('name',)  # Orders Product alphabetically by name
    list_filter = ('product_type', 'owner', 'status')

class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    search_fields = ('buyer', 'product' )
    list_display = ('buyer', 'product', 'amount', 'status', 'created_on')
    list_filter = ('buyer', 'product', 'status', 'created_on')

# models registered here.
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)