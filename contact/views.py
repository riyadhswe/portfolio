from django.shortcuts import render
from .models import contact

# Create your views here.
def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contactdata = contact(name= name,email = email,subject = subject,message = message)
        contactdata.save()
    return render(request, 'contact.html')