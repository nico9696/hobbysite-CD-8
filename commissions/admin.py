from django.contrib import admin
from .models import Commission, Job, JobApplication

class CommissionAdmin(admin.ModelAdmin):
     model = Commission
     search_fields = ('title', )
     list_display = ('id', 'title','description', 'created_on', 'updated_on', 'status')
     list_filter = ('status',)
 
class JobAdmin(admin.ModelAdmin):
     model = Job
     search_fields = ('entry', 'role', 'commission__title')
     list_display = ('id', 'entry', 'commission', 'role', 'people_required', 'created_on', 'updated_on', 'status')
     list_filter = ('commission', 'status',)

class JobApplicationAdmin(admin.ModelAdmin):
     model = JobApplication
     search_fields = ('job', 'author__display_name')
     list_display = ('id', 'job', 'commission', 'applied_on', 'applicant', 'status')
     list_filter = ('commission', 'job', 'status',)
 
admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
