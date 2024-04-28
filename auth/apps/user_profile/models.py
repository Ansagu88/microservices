from django.conf import settings
User = settings.AUTH_USER_MODEL
from djoser.signals import user_registered

from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    picture = models.ImageField(default='users/user_default_profile.png', upload_to='media/users/pictures/', blank=True, null=True)
    banner = models.ImageField(default='users/user_default_bg.jpg',  upload_to='media/users/banners/', blank=True, null=True)

    location = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=80, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_info = models.TextField(max_length=150, blank=True, null=True)

    facebook = models.CharField(max_length=50, blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)
    youtube = models.CharField(max_length=50, blank=True, null=True)
    linkedin = models.CharField(max_length=50, blank=True, null=True)
    github = models.CharField(max_length=50, blank=True, null=True)



def post_user_registered(user, request, *args, **kwargs):
    #1. Create a profile for the user
    user = user
    Profile.objects.create(user=user)

user_registered.connect(post_user_registered)