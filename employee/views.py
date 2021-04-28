from django.shortcuts import render
from django.http import HttpResponse


def employee(request):
    return HttpResponse("This is our employee page    !")


def profile(request):
    return render(request, 'profile.html')
