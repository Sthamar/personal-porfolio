from django.shortcuts import render, HttpResponse
from .models import Blog

# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    context = {"blogs":blogs}
    return render(request, 'blog/blog.html', context)