from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    text = {
        "name"  : "Riyadh",
        "age"   : 24,
        "phone" :'8801740280586',
        'friend_name': ['A','B','C','D']
    }
    return render(request,'index.html',text)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
