from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.http import Http404
from .models import Profile# , SiteManager

def index(request):
    try:
        profile = Profile.objects.get(pk=1)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")

    return render(request, 'base.html', {'profile': profile})

def news(request):
    try:
        profile = Profile.objects.get(pk=1)
        news = profile.news_id.objects.get(pk=1)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")

    return render(request, 'news.html', {'news': news})

def projects(request):
    try:
        project = Profile.projects_id.objects.all()
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")

    return render(request, 'project.html', {'project': project})
