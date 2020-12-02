from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUser
import csv
from django.http import HttpResponse
# Register your models here.


def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="user.csv"'
    writer = csv.writer(response)
    writer.writerow([
        "email",
        "username",
        "gender",
        "Address",
        "city",
        "state",
        "contact_number",
    ])
    for obj in queryset:
        writer.writerow([
            obj.email,
            obj.username,
            obj.gender,
            obj.Address,
            obj.city,
            obj.state,
            obj.contact_number,
        ])
    return response



class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'contact_number', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    actions = [export_csv]


admin.site.register(CustomUser, UserAdmin)
