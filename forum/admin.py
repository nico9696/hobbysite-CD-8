from django.contrib import admin
from .models import ThreadCategory, Thread, Comment

class ThreadCategoryAdmin(admin.ModelAdmin):
    model = ThreadCategory
    list_display = ('name', 'description')
    search_fields = ('name',)


class ThreadAdmin(admin.ModelAdmin):
    model = Thread
    list_display = ('title', 'author', 'category', 'created_on', 'updated_on')
    search_fields = ('title', 'category__name')
    list_filter = ('category', 'created_on')
    ordering = ('-created_on',)

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('author', 'thread', 'created_on')
    search_fields = ('entry', 'author__display_name')
    list_filter = ('created_on',)
    
admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment, CommentAdmin)