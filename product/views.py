from django.shortcuts import render
from product.models import Product, Category
from django.views.generic import ListView, DetailView


# Create your views here.


class ProductViewRing(ListView):
    model = Product
    template_name = 'product/ring.html'
    context_object_name = 'products'

    def get_queryset(self):
        category = Category.objects.get(category_name='Ring')
        return self.model.objects.filter(category_id=category)


class ProductViewEarrings(ListView):
    model = Product
    template_name = 'product/earrings.html'
    context_object_name = 'products'

    def get_queryset(self):
        category = Category.objects.get(category_name='earrings')
        return self.model.objects.filter(category_id=category)


class EarringsDetailView(DetailView):
    model = Product
    template_name = 'product/earringsdetail.html'


class RingDetailView(DetailView):
    model = Product
    template_name = 'product/ringdetail.html'


class ProductViewNeckless(ListView):
    model = Product
    template_name = 'product/neckless.html'
    context_object_name = 'products'

    def get_queryset(self):
        category = Category.objects.get(category_name='neckless')
        return self.model.objects.filter(category_id=category)


class NecklessDetailView(DetailView):
    model = Product
    template_name = 'product/necklessdetail.html'


