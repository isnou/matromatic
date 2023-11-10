from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Project(models.Model):
    auto_inc = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50, unique=True)
    project_description = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to='project/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "project"

    def __str__(self):
        return self.project_name


class Service(models.Model):
    auto_inc = models.AutoField(primary_key=True)
    service_title = models.CharField(max_length=50, unique=True)
    service_description = models.TextField(max_length=200, blank=True)
    icon = models.ImageField(upload_to='service/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "service"

    def __str__(self):
        return self.service_title


class Team(models.Model):
    member_name = models.CharField(max_length=50, unique=True)
    member_function = models.TextField(max_length=100, blank=True)
    function_description = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='team/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "team"

    def __str__(self):
        return self.member_name


class Partner(models.Model):
    partner_name = models.CharField(max_length=50, unique=True)
    partner_logo = models.ImageField(upload_to='partner/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "partner"

    def __str__(self):
        return self.partner_name


class Client(models.Model):
    client_name = models.CharField(max_length=50, unique=True)
    client_logo = models.ImageField(upload_to='partner/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "client"

    def __str__(self):
        return self.client_name


class Content(models.Model):
    profile_name = models.CharField(max_length=50, unique=True)

    head_title = models.CharField(max_length=50, blank=True)
    head_text = models.CharField(max_length=80, blank=True)

    head_logo = models.ImageField(upload_to='content/head', height_field=None, width_field=None, max_length=100,
                                  blank=True)
    main_logo = models.ImageField(upload_to='content/main', height_field=None, width_field=None, max_length=100,
                                  blank=True)

    intro_title = models.CharField(max_length=100, blank=True)
    intro_text = models.TextField(max_length=200, blank=True)

    welcome_title = models.CharField(max_length=50, blank=True)
    welcome_box_title = models.CharField(max_length=50, blank=True)
    welcome_text = models.CharField(max_length=200, blank=True)

    about_us_title = models.CharField(max_length=50, blank=True)
    about_us_box_title = models.CharField(max_length=50, blank=True)
    about_us_text = models.CharField(max_length=200, blank=True)
    team_text = models.CharField(max_length=200, blank=True)
    partners_text = models.CharField(max_length=200, blank=True)

    projects_title = models.CharField(max_length=50, blank=True)
    projects_box_title = models.CharField(max_length=50, blank=True)
    projects_text = models.CharField(max_length=200, blank=True)
    clients_text = models.CharField(max_length=200, blank=True)

    contact_title = models.CharField(max_length=50, blank=True)
    contact_box_title = models.CharField(max_length=50, blank=True)
    contact_text = models.CharField(max_length=200, blank=True)
    contact_address = models.CharField(max_length=500, blank=True)
    contact_phone_title = models.CharField(max_length=50, blank=True)
    contact_phone = PhoneNumberField(blank=True)
    contact_email_title = models.CharField(max_length=50, blank=True)
    contact_email = models.EmailField(max_length=300, blank=True)
    contact_name_placeholder = models.CharField(max_length=100, blank=True)
    contact_email_placeholder = models.CharField(max_length=100, blank=True)
    contact_subject_placeholder = models.CharField(max_length=100, blank=True)
    contact_message_placeholder = models.CharField(max_length=100, blank=True)
    contact_submit_button = models.CharField(max_length=50, blank=True)
    contact_facebook = models.URLField(max_length=500, blank=True)
    contact_twitter = models.URLField(max_length=500, blank=True)
    contact_instagram = models.URLField(max_length=500, blank=True)

    class Meta:
        verbose_name = "content"

    def __str__(self):
        return self.profile_name
