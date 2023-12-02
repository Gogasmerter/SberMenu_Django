from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm

from core.forms import BootstrapClassFormMixin
from users.models import User


class CustomAuthenticationForm(AuthenticationForm, BootstrapClassFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control email", "placeholder": "Почта", "type": "email"})
        self.fields["password"].widget.attrs.update({"class": "form-control password", "placeholder": "Пароль"})


class CustomUserCreationForm(UserCreationForm, BootstrapClassFormMixin):
    class Meta:
        model = User
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm, BootstrapClassFormMixin):
    class Meta:
        model = User
        fields = ("email",)
