from django.db import models

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    # Ensures that product types are displayed by their names (instead of IDs) in admin
    def __str__(self):
        return str(self.name) 
    
    class Meta:
        ordering = ['name']  # Orders ProductType alphabetically by name

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name="products")
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)  

    class Meta:
        ordering = ['name']  # Orders Product alphabetically by name