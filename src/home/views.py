from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from manager.models import Home, MainContent, ContactUs, Service, OurProcess, SocialMedia, Client, Project, RightValue, \
    LeftValue

from django.core.mail import BadHeaderError, EmailMessage
from django.conf import settings


def home(request):
    if not request.session.get('language', None):
        request.session['language'] = 'en-us'
    direction = request.session.get('language')
    url = direction + "/home/home.html"

    try:
        home_page = Home.objects.get(language='en')
    except Home.DoesNotExist:
        raise Http404("Home does not exist")

    try:
        main_content = MainContent.objects.get(language='en')
    except MainContent.DoesNotExist:
        raise Http404("Content does not exist")

    try:
        services = Service.objects.all()
    except Service.DoesNotExist:
        raise Http404("services informations do not exist")

    try:
        process_steps = OurProcess.objects.all().order_by('process_number')
    except OurProcess.DoesNotExist:
        raise Http404("Process informations do not exist")

    try:
        clients = Client.objects.all()
    except Client.DoesNotExist:
        raise Http404("Clients informations do not exist")

    try:
        right_values = RightValue.objects.all()
    except RightValue.DoesNotExist:
        raise Http404("Our values informations do not exist")

    try:
        left_values = LeftValue.objects.all()
    except LeftValue.DoesNotExist:
        raise Http404("Our values informations do not exist")
    try:
        projects = Project.objects.all()
    except Project.DoesNotExist:
        raise Http404("Projects informations do not exist")

    try:
        socials_media = SocialMedia.objects.all()
    except SocialMedia.DoesNotExist:
        raise Http404("Socials media do not exist")

    try:
        contact_us = ContactUs.objects.get(language='en')
    except ContactUs.DoesNotExist:
        raise Http404(" Contact Us info do not exist")

    context = {
        'home_page': home_page,
        'main_content': main_content,
        'process_steps': process_steps,
        'clients': clients,
        'projects': projects,
        'services': services,
        'socials_media': socials_media,
        'contact_us': contact_us,
        'right_values': right_values,
        'left_values': left_values,

    }

    return render(request, url, context)


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        # send an email
        from_email = '{name} <{email}>'.format(name=message_name, email=message_email)
        recipient_list = [settings.EMAIL_HOST_USER]
        email_message = EmailMessage(message_name, message, from_email, recipient_list, reply_to=[message_email])
        try:
            email_message.send()
        except BadHeaderError:
            return HttpResponse('Un en-tête non valide a été détecté.')

    return redirect('home')
