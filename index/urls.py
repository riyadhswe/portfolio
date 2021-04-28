from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = 'home'),
    path('aboutus', views.aboutus, name='about'),
    path('contact', views.contactus, name='contact'),
]
