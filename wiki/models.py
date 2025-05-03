from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    # Sort category names in alphabetical order
    class Meta:
        ordering = ['name']
        verbose_name = "Article Category"
        verbose_name_plural = "Article Category" 


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        "user_management.Profile",
        null=True,
        on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        ArticleCategory,
        null=True, # Allows articles to belong to a null category
        on_delete=models.SET_NULL # Becomes null upon deletion of the category
    )
    entry = models.TextField()
    header_image = models.ImageField(
        upload_to="header_images/",
        null=True,
        blank=True
    )
    created_on = models.DateTimeField(auto_now_add=True) # Set only once upon article creation
    updated_on = models.DateTimeField(auto_now=True) # Set every time the article is edited
        
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
        
    # Sort articles from newest created to oldest created
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"
        verbose_name_plural = "Article" 
    