from django.contrib import admin
from .models import ArticleCategory, Article, Comment

@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_on', 'updated_on')
    list_filter = ('category', 'author', 'created_on')
    search_fields = ('title', 'entry')
    raw_id_fields = ('author',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'article', 'created_on', 'updated_on')
    list_filter = ('created_on', 'author')
    search_fields = ('entry',)
    raw_id_fields = ('author', 'article')
