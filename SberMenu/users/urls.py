from django.contrib.auth import views as auth_views
from django.urls import path

from users import views
from users.forms import CustomAuthenticationForm

app_name = "users"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="users/login.html",
            form_class=CustomAuthenticationForm,
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path("signup/", views.RegistrationView.as_view(), name="signup"),
]
