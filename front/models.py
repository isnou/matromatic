from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# user = models.OneToOneField(User, on_delete=models.CASCADE)


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)
    left = models.BooleanField()
    photo = models.ImageField(upload_to='project/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "project"

    def __str__(self):
        return self.project_name


class News(models.Model):
    news_name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='news/', height_field=None, width_field=None, max_length=100)
    entry_date = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = "news"

    def __str__(self):
        return self.news_name


class Profile(models.Model):
    profile_name = models.CharField(max_length=50, blank=True)
    about = models.CharField(max_length=50)
    projects = models.CharField(max_length=50)
    news = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    intro_big_text = models.TextField(max_length=200, blank=True)
    intro_small_text = models.TextField(max_length=500, blank=True)
    intro_button = models.CharField(max_length=50)
    about_title = models.CharField(max_length=100, blank=True)
    about_text = models.TextField(max_length=500, blank=True)
    about_link = models.CharField(max_length=150)
    about_disc = models.CharField(max_length=100)
    news_id = models.OneToOneField(News, on_delete=models.CASCADE, blank=True, default=1)
    contact_title = models.CharField(max_length=100, blank=True)
    contact_link_area = models.CharField(max_length=200, blank=True)
    contact_button = models.CharField(max_length=50, blank=True)
    address_title = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=500, blank=True)
    email_title = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=300, blank=True)
    phone_title = models.CharField(max_length=50, blank=True)
    phone = PhoneNumberField(blank=True)

    class Meta:
        verbose_name = "profile"

    def __str__(self):
        return self.profile_name

# class SiteManager(models.Model):
