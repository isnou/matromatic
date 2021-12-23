from django.contrib import admin
from .models import SiteProfile, Project, News# , SiteManager


admin.site.register(SiteProfile)
admin.site.register(Project)
admin.site.register(News)
# admin.site.register(SiteManager)