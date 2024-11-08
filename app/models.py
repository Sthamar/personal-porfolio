from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    profile_image = models.ImageField(upload_to='profile/images/')
    expertise_des = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='education')
    institution_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True) 
    
    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=50, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert')
    ])
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
class About(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='about_info')
    description = models.TextField(blank=True)
    skill = models.ManyToManyField(Skill, related_name='about_profile')
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    profile_summary = models.TextField(blank=True)
    
    def __str__(self):
        return f'About {self.profile.name}'
    
    