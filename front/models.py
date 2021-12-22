from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=50)
    projects = models.CharField(max_length=50)
    news = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    intro_big_text = models.CharField(max_length=200)
    intro_small_text = models.CharField(max_length=500)
    intro_button = models.CharField(max_length=50)
    about_title = models.CharField(max_length=100, default='blank')
    about_text = models.CharField(max_length=500)
    about_link = models.CharField(max_length=150)
    about_disc = models.CharField(max_length=100)

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, default=1)