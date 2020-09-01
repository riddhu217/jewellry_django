from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from mainapp.models import Contact


 #Register your models here.

admin.site.register(Contact)