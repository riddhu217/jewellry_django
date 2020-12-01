from django.contrib import admin
#from django.contrib.auth.admin import ContactAdmin
from mainapp.models import Contact , Csv
import csv
from django.http import HttpResponse

#Register your models here.

admin.site.register(Csv)


def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;     filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow([
        "name",
        "email",
        "phone",
        "desc",
    ])
    for obj in queryset:
        writer.writerow([
            obj.name,
            obj.email,
            obj.phone,
            obj.desc,
        ])
    return response


class Contactadmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone','desc','date')
    search_fields = ('name','email')
    readonly_fields = ('date', 'desc')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    actions = [export_csv]


admin.site.register(Contact, Contactadmin)
