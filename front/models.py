from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200, default='blank')
    about = models.CharField(max_length=50, default='blank')
    projects = models.CharField(max_length=50, default='blank')
    news = models.CharField(max_length=50, default='blank')
    contact = models.CharField(max_length=50, default='blank')
    intro_big_text = models.CharField(max_length=200, default='blank')
    intro_small_text = models.CharField(max_length=500, default='blank')
    intro_button = models.CharField(max_length=50, default='blank')
    about_title = models.CharField(max_length=100, default='blank')
    about_text = models.CharField(max_length=500, default='blank')
    about_link = models.CharField(max_length=150, default='blank')
    about_disc = models.CharField(max_length=100, default='blank')