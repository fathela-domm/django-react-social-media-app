from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("update/<str:pk>/", views.update_user_profile, name="update_user_profile"),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),
         name='password-reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='user/password_reset_done.html'),
        name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='user/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path("logout/", auth_views.LogoutView.as_view(template_name="user/logout.html"), name="logout"),
] 
