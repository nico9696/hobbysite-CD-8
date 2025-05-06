from django.contrib import admin
from .models import ArticleCategory, Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_on')
    list_filter = ('category', 'created_on')
    search_fields = ('title', 'entry')
    exclude = ['author']  # Hide author field from admin form

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set author during creation
            try:
                obj.author = request.user.profile
            except Exception:
                pass  # Optionally raise error if profile is required
        super().save_model(request, obj, form, change)

admin.site.register(ArticleCategory)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
