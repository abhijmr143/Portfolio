from django.contrib import admin
from blog.models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publish_date', 'image', 'body']
admin.site.register(Blog, BlogAdmin)