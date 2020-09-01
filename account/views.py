from django.views.generic import CreateView
from django.urls import reverse_lazy
from account.forms import RegistrationForm, CustomLoginForm
from django.contrib.auth.views import LoginView


# Create your views here.

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
