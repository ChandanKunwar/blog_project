from django.contrib import auth
from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('sign_up/',views.sign_up, name='user-sign-up'),
    path('profile/',views.profile, name='user-profile'),
    path('',auth_view.LoginView.as_view(template_name="user/login.html"), name='user-login'),
    path('logout/',auth_view.LogoutView.as_view(template_name="user/logout.html"), name='user-logout'),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name="user/password_reset.html"), name="password_reset"),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetCompleteView.as_view(template_name="user/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"), name="password_reset_complete"),
]