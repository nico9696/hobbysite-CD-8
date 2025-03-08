from django.db import models
from django.urls import reverse


'''
TO-DO: Add __str__() and get_absolute_url() methods
     : Implement sorting feature
'''

# Model for a category of articles
class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


# Model for an article under a category
class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ArticleCategory,
        null=True, # Allows articles to be created with a null category 
        on_delete=models.SET_NULL # Becomes null upon deletion of the category
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # Set only once upon article creation
    updated_on = models.DateTimeField(auto_now=True) # Set every time the article is edited
    
    
