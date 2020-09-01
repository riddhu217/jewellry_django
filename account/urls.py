from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = 'account'
urlpatterns = [

    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]