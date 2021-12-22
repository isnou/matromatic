from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.http import Http404
from .models import Profile

def index(request):
    profile_id = 1
    try:
        profile = Profile.objects.get(pk=profile_id)
    except Question.DoesNotExist:
        raise Http404("Profile does not exist")

    return render(request, 'base.html', {'profile': profile})
