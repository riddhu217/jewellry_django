from django.views.generic import CreateView
from django.urls import reverse_lazy
from account.forms import RegistrationForm, CustomLoginForm, EditProfileForm
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView, View
from django.views.generic.edit import UpdateView
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


