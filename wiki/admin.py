from django.contrib import admin
from .models import ArticleCategory, Article

'''
TO-DO: Add more admin panel features 
'''

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    search_fields = ('name', )
    list_display = ('name', )


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    search_fields = ('title', 'category__name', )
    list_display = ('title', 'category', 'created_on', 'updated_on')
    
    
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
