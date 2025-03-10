from django.contrib import admin
from .models import PostCategory, Post

class PostCategoryAdmin(admin.ModelAdmin):
    model = PostCategory
    search_fields = ('name', )
    list_display = ('name', )


class PostAdmin(admin.ModelAdmin):
    model = Post
    search_fields = ('title', 'category__name', )
    list_display = ('title', 'category', 'created_on', 'updated_on')
    list_filter = ('category', 'created_on')
    ordering = ('-created_on',)
    
    
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)