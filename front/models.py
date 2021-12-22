from django.db import models

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
    about_text = models.CharField(max_length=500)
    about_link = models.CharField(max_length=150)
    about_disc = models.CharField(max_length=100)