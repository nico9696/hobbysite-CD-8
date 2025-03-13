from django.db import models

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    # Ensures that product types are displayed by their names (instead of IDs) in admin
    def __str__(self):
        return str(self.name) 
    
    # Orders ProductType alphabetically by name
    class Meta:
        ordering = ['name']  
        verbose_name = "Product type"
        verbose_name_plural = "Product type" 

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType, 
        on_delete=models.SET_NULL, # When product type is deleted, all its products will have null product type
        null=True,  # Allows for null values
        blank=True,  # Allows for blank values
        related_name="products")
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)  

    # Orders Product alphabetically by name
    class Meta:
        ordering = ['name']  