from django.shortcuts import render
from django.views.generic import CreateView
from mainapp.forms import ContactForm
from django.urls import reverse_lazy


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def collection(request):
    return render(request, 'collection.html')


class Contactview(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
