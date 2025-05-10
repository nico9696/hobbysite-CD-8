from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

app_name = "user_management"

urlpatterns = [
    path("", lambda request: redirect("user_management:home", permanent=False)),  # Redirect to 'home'
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("home/", views.home, name="home"),
    path("register/", views.register, name="register"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "user_management/reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "user_management/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "user_management/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "user_management/password_reset_done.html"), name ='password_reset_complete')
]