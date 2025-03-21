from django.db import models
from django.contrib.auth.models import User

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ["name"]
        verbose_name = "Article Category"
        verbose_name_plural = "Article Category" 

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ArticleCategory, on_delete=models.SET_NULL, null=True, blank=True
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Article"
        verbose_name_plural = "Article" 

    def __str__(self):
        return self.title