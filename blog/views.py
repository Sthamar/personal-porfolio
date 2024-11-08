from django.shortcuts import render, HttpResponse
from .models import Blog
from app.models import *

# Create your views here.
def blog(request):
    projects = Blog.objects.all()
    profile = Profile.objects.all()[0]
    skills = Skill.objects.all()
    about = About.objects.all()[0]
    context = {
        'projects':projects,
        'profile': profile,
        'skills': skills,
        'about': about
        
    }
    return render(request, 'blog/blog.html', context)

