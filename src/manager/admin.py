from django.contrib import admin
from .models import Home, MainContent, RightValue, LeftValue, ContactUs, Service, OurProcess, SocialMedia, Client, \
    Project

# Register your models here.
admin.site.register(Home)
admin.site.register(MainContent)
admin.site.register(RightValue)
admin.site.register(LeftValue)
admin.site.register(Service)
admin.site.register(OurProcess)
admin.site.register(Project)
admin.site.register(Client)
admin.site.register(ContactUs)
admin.site.register(SocialMedia)
