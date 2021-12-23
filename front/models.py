from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# user = models.OneToOneField(User, on_delete=models.CASCADE)

class Profile(models.Model):
    profile_name = models.CharField(max_length=50, default='blank')
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

    class Meta:
        verbose_name = "profile"

    def __str__(self):
        return self.profile_name

class Project(models.Model):
    project_name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, default='blank')
    left = models.BooleanField()
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "project"

    def __str__(self):
        return self.project_name

class News(models.Model):
    news_name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, default='blank')
    photo = models.ImageField(upload_to='news/%Y/%m/%d', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "news"

    def __str__(self):
        return self.news_name

# class SiteManager(models.Model):