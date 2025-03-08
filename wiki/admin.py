from django.contrib import admin
from .models import ArticleCategory, Article


'''
TO-DO: Add admin panels for each
'''

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    
    
admin.site.register(ArticleCategory)
admin.site.register(Article)
