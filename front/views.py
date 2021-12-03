from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("matromatic the best choice for your industry")
