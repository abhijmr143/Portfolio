from django.shortcuts import render
from blog.models import Blog
# Create your views here.
def allblogs(request):
    all_blog = Blog.objects.all()
    return render(request, 'blog/all_blog_home.html', {'blogs':all_blog})
