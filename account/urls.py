from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView

app_name = 'account'
urlpatterns = (

    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('changepassword/',auth_views.PasswordChangeView.as_view( template_name = 'account/changepassword.html',
        success_url = '/'
       ),
         name="changepassword"),


)
