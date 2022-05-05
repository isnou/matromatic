from django.contrib import admin
from .models import Project, Service, Partner, Team, Client, Content


admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Partner)
admin.site.register(Team)
admin.site.register(Client)
admin.site.register(Content)
