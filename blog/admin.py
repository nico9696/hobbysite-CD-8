from django.contrib import admin
from .models import ArticleCategory, Article, Comment


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    search_fields = ('name',)
    list_display = ('id', 'name', 'description')
    ordering = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_on')
    list_filter = ('category', 'created_on')
    search_fields = ('title', 'entry')
    readonly_fields = ('author',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            try:
                obj.author = request.user.profile
            except Exception:
                pass
        super().save_model(request, obj, form, change)


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    search_fields = ('author', 'entry')
    list_display = ('author', 'article', 'created_on', 'updated_on')
    list_filter = ('article', 'created_on', 'updated_on')

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
