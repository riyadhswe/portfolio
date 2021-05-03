from django.contrib import admin
from .models import *
# Register your models here.
class contactadmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message']

admin.site.register(contact,contactadmin)
