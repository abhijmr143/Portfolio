from django.shortcuts import render, get_object_or_404
from blog.models import Blog
# Create your views here.
def allblogs(request):
    all_blog = Blog.objects.all()
    return render(request, 'blog/all_blog_home.html', {'blogs':all_blog})

def details(request, id):
    blog_detail = get_object_or_404(Blog, id = id)
    return render(request, 'blog/detail.html', {'blog_detail':blog_detail})
    
