from django.urls import path
from django.contrib.auth import views

from users.views import register, profile

urlpatterns = [
    # /users
    path("register/", register, name="register"),
    path("login/", views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("profile/", profile, name="profile")
]