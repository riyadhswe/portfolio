from django.contrib import admin
from .models import *

# Register your models here.
class aboutadmin(admin.ModelAdmin):
    list_display = ['title','description','image']

class slideradmin(admin.ModelAdmin):
    list_display = ['title','description','image']


admin.site.register(about,aboutadmin)
admin.site.register(slider,slideradmin)