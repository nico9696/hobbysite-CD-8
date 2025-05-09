from django.contrib import admin
from .models import *


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    search_fields = ('name', )
    list_display = ('name', )


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    search_fields = ('title', 'author', 'category__name')
    list_display = ('title', 'author', 'category', 'created_on', 'updated_on')


class CommentAdmin(admin.ModelAdmin):
    model = Article
    search_fields = ('author', 'article')
    list_display = ('author', 'article', 'entry', 'created_on', 'updated_on')
    
    
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
