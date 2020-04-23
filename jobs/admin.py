from django.contrib import admin
from jobs.models import Job
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'summary']
admin.site.register(Job, JobAdmin)


