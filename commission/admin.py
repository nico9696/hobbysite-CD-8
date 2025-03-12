from django.contrib import admin
from .models import Commission, Comment

class CommissionAdmin(admin.ModelAdmin):
     model = Commission
     search_fields = ('title', )
     list_display = ('id', 'title','description', 'created_on', 'updated_on', 'people_required')
 
class CommentAdmin(admin.ModelAdmin):
     model = Comment
     search_fields = ('entry', 'commission__title')
     list_display = ('id', 'entry', 'commission', 'created_on', 'updated_on')
     list_filter = ('commission', )

 
admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)
