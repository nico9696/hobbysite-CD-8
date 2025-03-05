from django.db import models

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    # Ensures that product types display their id instead of "ProductType object (num)" in BOTH cmd line AND admin
    def __str__(self):
        return str(self.id) 
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name="product_type")
    description = models.TextField()
    price = price = models.DecimalField(decimal_places=2)  

    # Ensures that product types display their id instead of "ProductType object (num)" in BOTH cmd line AND admin
    def __str__(self):
        return str(self.id) 