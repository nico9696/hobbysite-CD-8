from django.contrib import admin
from .models import ArticleCategory, Article, Comment


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    search_fields = ('name',)
    list_display = ('id', 'name', 'description')
    ordering = ('name',)  # Categories should be ordered by name

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_on')
    list_filter = ('category', 'created_on')
    search_fields = ('title', 'entry')
    readonly_fields = ('author',)  # Author is shown but not editable

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set author during creation
            try:
                obj.author = request.user.profile
            except Exception:
                pass  # Optionally raise error if profile is required
        super().save_model(request, obj, form, change)


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    search_fields = ('author', 'entry')
    list_display = ('author', 'article', 'created_on', 'updated_on')
    list_filter = ('article', 'created_on', 'updated_on')

# Register the models with their customized admin views
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
