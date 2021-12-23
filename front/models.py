from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# user = models.OneToOneField(User, on_delete=models.CASCADE)

class Profile(models.Model):
    about = models.CharField(max_length=50)
    projects = models.CharField(max_length=50)
    news = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    intro_big_text = models.TextField(max_length=200, default='blank')
    intro_small_text = models.TextField(max_length=500, default='blank')
    intro_button = models.CharField(max_length=50)
    about_title = models.CharField(max_length=100, default='blank')
    about_text = models.TextField(max_length=500, default='blank')
    about_link = models.CharField(max_length=150)
    about_disc = models.CharField(max_length=100)

# class SiteManager(models.Model):