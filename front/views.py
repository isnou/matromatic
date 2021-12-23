from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.http import Http404
from .models import Profile, SiteManager

def index(request):
    profile_id = SiteManager.
    try:
        profile = Profile.objects.get(pk=profile_id)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")

    return render(request, 'base.html', {'profile': profile})
