from django.views.generic import CreateView
from django.urls import reverse_lazy
from account.forms import RegistrationForm, CustomLoginForm, EditProfileForm
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView, View
from django.views.generic.edit import UpdateView
import csv
from django.http import HttpResponse


#from reportlab.pdfgen import canvas
# Create your views here.
from account.models import CustomUser


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'account/login.html'


class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = 'account/profile.html'


class EditProfileView(UpdateView):
    model = CustomUser
    form_class = EditProfileForm
    template_name = 'account/edit_profile.html'
    success_url = reverse_lazy('account/profile.html')


def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    customusers = CustomUser.objects.all()
    writer = csv.writer(response)
    for customuser in customusers:
        writer.writerow([customuser.username, customuser.email, customuser.Address, customuser.gender])
    return response


class CSVFileView(View):
    def get(self,request, *args,**kwargs):
        response = HttpResponse(content_type='text/csv')
        cd = 'attachment; filename"{0}"'.format('user.csv')
        response['Content-Disposition'] = cd

        fieldnames = ('username', 'email', 'contact_number', 'Address' )
        data= CustomUser.objects.values(*fieldnames)

        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

        return response
