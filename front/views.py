from django.shortcuts import render

def index(request):
    return HttpResponse("matromatic.com is on the way")
