from django.shortcuts import render
from jobs.models import Job
from blog.models import Blog

# Create your views here.
def home(request):
    jobs_data = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs_data':jobs_data})
