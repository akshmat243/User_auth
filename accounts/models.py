from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser):
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='media/profile_images/', blank=True, null=True)
    background_image = models.ImageField(upload_to='media/background_images/', blank=True, null=True)

    def __str__(self):
        return self.username

class SlideCarousel(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/carousel_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    
class TeamMember(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='media/team_image/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class WebServices(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media/webservices/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    