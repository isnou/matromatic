from django.contrib import admin
from .models import Profile, Project, News# , SiteManager


admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(News)
# admin.site.register(SiteManager)