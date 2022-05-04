from django.contrib import admin
from .models import Project, Service,Client, Team, Skill, Content


admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Client)
admin.site.register(Team)
admin.site.register(Skill)
admin.site.register(Content)