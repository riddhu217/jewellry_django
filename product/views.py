from django.shortcuts import render
from product.models import Product, Category, Cart, CartItem, Order
from django.views.generic import ListView, DetailView, View, TemplateView
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


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


class ProductViewBracelete(ListView):
    model = Product
    template_name = 'product/bracelet.html'
    context_object_name = 'products'

    def get_queryset(self):
        category = Category.objects.get(category_name='bracelet')
        return self.model.objects.filter(category_id=category)


class BraceleteDetailView(DetailView):
    model = Product
    template_name = 'product/braceletdetail.html'


class AddToCartView(View):

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id', None)
        if product_id:
            cart, _ = Cart.objects.get_or_create(user=request.user)
            if cart:
                obj = CartItem.objects.create(cart=cart, product_id=product_id)
                if obj:
                    result = 'success'
                else:
                    result = 'not success'
        return JsonResponse({'result': result})


class CartTemplateView(TemplateView):
    model = Cart
    template_name = 'product/cart.html'

    def get_context_data(self):
        context = super(CartTemplateView, self).get_context_data()
        user_obj = self.request.user
        context['cart'] = Cart.objects.get(user=user_obj)

        return context


class CartDeleteView(DeleteView):
    model = CartItem
    success_url = reverse_lazy('product:cart')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CartDetailView(DetailView):
    model = CartItem


class OrderTotal():
    model = Order
