from django.urls import path
from . import views

app_name = 'product'
urlpatterns = (
    path('ring/', views.ProductViewRing.as_view(), name="ring"),
    path('earrings/', views.ProductViewEarrings.as_view(), name="earrings"),
    path('earrings-detail/<int:pk>/', views.EarringsDetailView.as_view(), name="earrings_detail"),
    path('ring-detail/<int:pk>/', views.RingDetailView.as_view(), name="ring_detail"),
    path('neckless/', views.ProductViewNeckless.as_view(), name="neckless"),
    path('neckless-detail/<int:pk>/', views.NecklessDetailView.as_view(), name="neckless_detail"),
    path('bracelet/', views.ProductViewBracelete.as_view(), name="bracelet"),
    path('bracelet-detail/<int:pk>/', views.BraceleteDetailView.as_view(), name="bracelet_detail"),
    path('add-cart/', views.AddToCartView.as_view(), name="add_cart"),
    #Cart View
    path('cart/',views.CartTemplateView.as_view(), name="cart"),
    path('cart-detail/',views.CartDetailView.as_view(), name="cart_detail"),
    path('cart-delete/<int:pk>', views.CartDeleteView.as_view(), name="cart_delete"),
    path('checkout/', views.CheckOutView.as_view(), name="checkout"),
    path('feedback/<int:pk>', views.FeedBackView.as_view(), name="feedback"),

    #payment
    path('paypalprocess/', views.PaymentProcess, name='paypalprocess'),


)