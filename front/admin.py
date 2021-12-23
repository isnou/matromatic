from django.contrib import admin
from .models import Profile, SiteProfile, News# , SiteManager


admin.site.register(SiteProfile)
admin.site.register(Project)
admin.site.register(News)
# admin.site.register(SiteManager)