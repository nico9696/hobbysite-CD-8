from django.db import models

class ProductType(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()

    # Ensures that product types display their id instead of "ProductType object (num)" in BOTH cmd line AND admin
    def __str__(self):
        return str(self.id) 