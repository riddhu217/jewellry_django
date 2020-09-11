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

)