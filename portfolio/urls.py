"""
PORTFOLIO MAIN PROJECT
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('employee/',include('employee.urls'))
]
