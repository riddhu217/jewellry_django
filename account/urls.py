from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

app_name = 'account'
urlpatterns = (

    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name="profile"),
    path('edit_profile/<int:pk>/', views.EditProfileView.as_view(), name="edit_profile"),

#ProfileView
    # path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name="profile"),

# Chanag password
    path('changepassword/',auth_views.PasswordChangeView.as_view( template_name = 'account/changepassword.html',
        success_url = '/'
       ),
         name="changepassword"),
# Forget Password

    path('password_reset/', auth_views.PasswordResetView.as_view(
             template_name='account/password_reset_form.html',success_url=reverse_lazy('account:password_reset_done')
    ), name='passwordreset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
             template_name='account/password_reset_done.html'), name='password_reset_done'),
    path(
        'password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/password_reset_confirm.html',
            success_url=reverse_lazy('account:password_reset_complete')
         ),
        name='password_reset_confirm'
    ),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(
             template_name='account/password_reset_complete.html'), name='password_reset_complete'),

)
