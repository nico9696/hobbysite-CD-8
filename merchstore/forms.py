from django import forms
from .models import Product

class Product(forms.ModelForm):
    class Meta:
        model = Product
        fields= ['name', 'owner', 'description', 'price', 'stock', 'status', ]