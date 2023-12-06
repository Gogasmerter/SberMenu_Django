from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm

from core.forms import BootstrapClassFormMixin
from users.models import User


class CustomAuthenticationForm(AuthenticationForm, BootstrapClassFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control email", "placeholder": "Почта", "type": "email"},
        )
        self.fields["password"].widget.attrs.update({"class": "form-control password", "placeholder": "Пароль"})


class CustomUserCreationForm(UserCreationForm, BootstrapClassFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {"class": "form-control email", "type": "text", "placeholder": "Имя", "required": "required"},
        )
        self.fields["last_name"].widget.attrs.update(
            {
                "class": "form-control email",
                "type": "text",
                "placeholder": "Фамилия",
                "required": "required",
            },
        )
        self.fields["email"].widget.attrs.update(
            {"class": "form-control email", "type": "email", "placeholder": "E-mail"},
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control password", "type": "password", "placeholder": "Пароль"},
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control password", "type": "password", "placeholder": "Повторите пароль"},
        )

    class Meta:
        model = User
        fields = (
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
        )


class CustomUserChangeForm(UserChangeForm, BootstrapClassFormMixin):
    class Meta:
        model = User
        fields = ("email",)
