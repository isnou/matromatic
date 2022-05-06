from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Project(models.Model):
    project_name = models.CharField(max_length=50, unique=True)
    project_description = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to='project/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "project"

    def __str__(self):
        return self.project_name


class Service(models.Model):
    service_title = models.CharField(max_length=50, unique=True)
    service_description = models.TextField(max_length=200, blank=True)
    icon = models.ImageField(upload_to='service/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "service"

    def __str__(self):
        return self.service_title


class Partner(models.Model):
    partner_name = models.CharField(max_length=50, unique=True)
    partner_logo = models.ImageField(upload_to='partner/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "partner"

    def __str__(self):
        return self.partner_name


class Team(models.Model):
    member_name = models.CharField(max_length=50, unique=True)
    member_function = models.TextField(max_length=100, blank=True)
    function_description = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='team/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "team"

    def __str__(self):
        return self.member_name


class Client(models.Model):
    client_name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "client"

    def __str__(self):
        return self.client_name


class Content(models.Model):
    profile_name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "content"

    def __str__(self):
        return self.profile_name
