from django.shortcuts import render
from product.models import Product, Category, Cart, CartItem, Order, OrderItem
from django.views.generic import ListView, DetailView, View, TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from product.forms import FeedBackForm, BillingAddressForm
from django.views.generic import CreateView
import stripe
from django.http.response import JsonResponse, HttpResponse
import csv
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt # new


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
                if not CartItem.objects.filter(cart=cart, product_id=product_id).exists():
                    obj = CartItem.objects.create(cart=cart, product_id=product_id)
                    if cart_item.quantity < cart_item.product.stock:
                        cart_item.quantity += 1
                    cart_item.save()
                    if obj:
                        result = 'success'
                    else:
                        result = 'not success'
                else:
                    result = 'Item is Exists'
            else:
                result = 'Cart not Exists '
        else:
            result = 'Product not Exists'

        return JsonResponse({'result': result})


class CartTemplateView(TemplateView):
    model = Cart
    template_name = 'product/cart.html'

    def get_context_data(self):
        context = super(CartTemplateView, self).get_context_data()
        user_obj = self.request.user

        cart = Cart.objects.get(user=user_obj)
        context['cart'] = cart
        total = 00
        for item in cart.cartitem_set.all():
            total = total + item.product.p_price
        context['total'] = total
        return context


class CartDeleteView(DeleteView):
    model = CartItem
    success_url = reverse_lazy('product:cart')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CartDetailView(DetailView):
    model = CartItem


class CartOrderView(ListView):
    model = Order
    template_name = 'product/cart.html'


class CheckOutView(ListView):
    model = Order
    template_name = 'product/checkout.html'


class FeedBackView(CreateView):
    form_class = FeedBackForm
    template_name = 'product/feedback.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'product/success.html'


class CancelledView(TemplateView):
    template_name = 'product/cancelled.html'


class BillingAddressView(CreateView):
    form_class = BillingAddressForm
    template_name = 'product/bill.html'
    success_url = reverse_lazy('product:ordersummary')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class OrderSummaryView(DetailView):
    model = Order
    template_name = 'product/ordersummary.html'

    def get(self, *args, **kwargs):
        user_obj = self.request.user
        try:

            order = Order.objects.filter(user=user_obj)
            context = {
                'objects': order
             }
            return render(self.request, 'product/ordersummary.html', context)
        except ObjectDoesNotExist:
            message.warring(self.request, "you do not have an active order")
        return redirect("/")






