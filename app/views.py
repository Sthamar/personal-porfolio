from django.shortcuts import render, HttpResponse
from .models import Project, Profile, Skill, About


# Create your views here.
def home(request):
    projects = Project.objects.all()[0]
    profile = Profile.objects.all()[0]
    skills = Skill.objects.all()
    about = About.objects.all()[0]
    context = {
        'projects': projects,
        'profile': profile,
        'skills': skills,
        'about': about
        
    }
    return render(request, 'app/index.html', context)



def about(request):
    projects = Project.objects.all()[0]
    profile = Profile.objects.all()[0]
    skills = Skill.objects.all()
    about = About.objects.all()[0]
    first_name = profile.name.split()[0]
    context = {
        'projects': projects,
        'profile': profile,
        'skills': skills,
        'about': about,
        'first_name': first_name
    }
    return render(request, 'app/about.html', context)


def contact(request):
    projects = Project.objects.all()[0]
    profile = Profile.objects.all()[0]
    skills = Skill.objects.all()
    about = About.objects.all()[0]
    first_name = profile.name.split()[0]
    context = {
        'projects': projects,
        'profile': profile,
        'skills': skills,
        'about': about,
    }
    return render(request, 'app/contact.html', context)