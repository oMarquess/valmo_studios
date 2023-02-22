from django.shortcuts import render, redirect
from .models import Project
from django.core.mail import mail_admins

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'projects':projects})

def flyer(request):
    projects = Project.objects.filter(project_type='flyer')
    return render(request, 'portfolio/flyer.html', {'projects':projects})

def logo(request):
    projects = Project.objects.filter(project_type='logo')
    return render(request, 'portfolio/logo.html', {'projects':projects})

def three_d(request):
    projects = Project.objects.filter(project_type='3d')
    return render(request, 'portfolio/three_d.html', {'projects':projects})

def services(request):
    return render(request, 'portfolio/services.html')

def contact(request):

    if request.method == 'POST' or None:
        name    = request.POST['name'],
        email       = request.POST['email'],
        #message
        text        = request.POST['text'],        
        subject = 'Customer Enquiry'
        message = 'Name: {}, Email: {}, text: {}'.format(name, email, text)
        print(text, name, message)
        mail_admins(subject, message)
        return redirect ('/success')
    return render(request, 'portfolio/contact.html')

def about(request):
    return render(request, 'portfolio/about.html')

def success(request):
    return render(request, 'portfolio/success.html')