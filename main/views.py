from django.shortcuts import render, redirect
from .models import destinations, subscribers, messages


# Create your views here.
def index(request):
    dest = destinations.objects.all()
    return render(request, 'index.html', {'dest': dest})


def about(request):
    a = {}
    for x in destinations.type_of_vacation:
        a[x[0]] = len(destinations.objects.filter(type=x[0]))
    return render(request, 'about.html', a)


def home(request):
    return redirect("/")


def news(request):
    return render(request, 'news.html')


def contact(request):
    return render(request, 'contact.html')


def subscribe(request):
    email = request.POST['email']
    name = request.POST['Name']
    sub = subscribers(email=email, name=name)
    sub.save()
    return redirect("/")


def getintouch(request):
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    touch = messages(name=name, email=email, subject=subject, text=message)
    touch.save()
    return redirect('/contact')
