from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.http import Http404
from .models import Profile, Project# , SiteManager

def index(request):
    try:
        profile = Profile.objects.get(pk=1)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")
    context = {
        'profile': profile
    }

    return render(request, 'base.html',context)

def projects(request):
    try:
        project = project.projects_id.objects.all()
    except Project.DoesNotExist:
        raise Http404("Project does not exist")

    return render(request, 'project.html', {'project': project})
