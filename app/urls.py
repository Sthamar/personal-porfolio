from django.urls import path
from app import views

urlpatterns = [
    path('',view=views.home , name='home'),
    path('about/', view=views.about, name="about"),
    path('contact/', views.contact, name='contact')
]