
from django.shortcuts import render
from front.forms import ContactUs
from django.core.mail import BadHeaderError, EmailMessage
from django.conf import settings
from django.http import Http404
from .models import Project, Service, Client, Team, Skill, Content


def index(request):

    try:
        content = Content.objects.get(pk=1)
    except Content.DoesNotExist:
        raise Http404("Content does not exist")

    try:
        projects = Project.objects.all()
    except Project.DoesNotExist:
        raise Http404("Project does not exist")

    try:
        services = Service.objects.all()
    except Service.DoesNotExist:
        raise Http404("Service does not exist")

    try:
        clients = Client.objects.all()
    except Client.DoesNotExist:
        raise Http404("Client does not exist")

    try:
        team = Team.objects.all()
    except Project.DoesNotExist:
        raise Http404("Team does not exist")

    try:
        skill = Skill.objects.all()
    except Skill.DoesNotExist:
        raise Http404("skill does not exist")

    form = ContactUs(request.POST or None)
    if form.is_valid():
        subject = 'Subject:' + form.cleaned_data['subject']
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        message = form.cleaned_data['message']
        recipient_list = [settings.EMAIL_HOST_USER]
        email_message = EmailMessage(subject, message, from_email, recipient_list, reply_to=[email])
        try:
            email_message.send()
        except BadHeaderError:
            return HttpResponse('Un en-tête non valide a été détecté.')

    context = {
        'content': content,
        'projects': projects,
        'services': services,
        'clients': clients,
        'team': team,
        'skill': skill
    }

    return render(request, "base.html", context)