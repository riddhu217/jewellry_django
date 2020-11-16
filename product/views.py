from django.shortcuts import render
from product.models import Product, Category, Cart, CartItem, Order
from django.views.generic import ListView, DetailView, View, TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from product.forms import FeedBackForm, BillingAddressForm
from django.views.generic import CreateView
import stripe
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
import csv
from django.utils.encoding import smart_str
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


#def PaymentProcess(request):
 #   return render(request, 'product/paypalprocess.html')


class FeedBackView(CreateView):
    form_class = FeedBackForm
    template_name = 'product/feedback.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StripeView(TemplateView):
    template_name = 'product/stripe.html'


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'ring',
                        'quantity': 1,
                        'currency': 'INR',
                        'amount': '2000',
                        }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


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


class OrderSummaryView(View):
    model = Order
    template_name = 'product/ordersummary.html'

    def get(self, *args, **kwargs):
        try:
             order = Order.objects.get(user=user.request,Ordered=False)
             context = {
                 'objects' : order
             }
             return render(self.request, 'ordersummary.html', context)
        except ObjectDoesNotExist:
            message.warring(self.request, "you do not have an active order")
            return redirect("/")


def download_csv_data(request):
    response = HttpResponse(content_type='text/csv')
    # decide the file name
    response['Content-Disposition'] = 'attachment; filename="User.csv"'


    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))

# write the headers
    writer.writerow([
        smart_str(u"user name"),
        smart_str(u"email"),
        smart_str(u"gender"),
        smart_str(u"address"),
    ])
# get data from database or from text file....
    user = user_services.get_CustomUser_by_login(login)  # dummy function to fetch data
    for CustomUser in user:
        writer.writerow([
            smart_str(CustomUser.name),
            smart_str(CustomUser.email),
            smart_str(CustomUser.gender),
            smart_str(CustomUser.address),
        ])
    return response
