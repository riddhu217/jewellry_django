from django.contrib import admin
#from django.contrib.auth.admin import ContactAdmin
from mainapp.models import Contact

#Register your models here.


class Contactadmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone','desc','date')
    search_fields = ('name','email')
    readonly_fields = ('date', 'desc')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Contact, Contactadmin)

