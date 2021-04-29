from django.shortcuts import render
from .models import *

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    aboutdata = about.objects.all()[0]
    sliderdata = slider.objects.all()
    contex={
        'about':aboutdata,
        'slider':sliderdata
    }
    return render(request, 'index.html',contex)


def aboutus(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contact.html')
