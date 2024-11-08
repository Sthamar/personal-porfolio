from django.shortcuts import render, HttpResponse
from .models import Profile, Skill, About
from blog.models import Blog


# Create your views here.
def home(request):
    projects = Blog.objects.all()[0:3]
    profile = Profile.objects.all()[0]
    skills = Skill.objects.all()
    about = About.objects.all()[0]
    context = {
        'projects':projects,
        'profile': profile,
        'skills': skills,
        'about': about
        
    }
    return render(request, 'app/index.html', context)



def about(request):
    profile = Profile.objects.all()[0]
    skills = Skill.objects.all()
    about = About.objects.all()[0]
    first_name = profile.name.split()[0]
    context = {
 
        'profile': profile,
        'skills': skills,
        'about': about,
        'first_name': first_name
    }
    return render(request, 'app/about.html', context)


def contact(request):

    profile = Profile.objects.all()[0]
    skills = Skill.objects.all()
    about = About.objects.all()[0]
    first_name = profile.name.split()[0]
    context = {
        'profile': profile,
        'skills': skills,
        'about': about,
    }
    return render(request, 'app/contact.html', context)