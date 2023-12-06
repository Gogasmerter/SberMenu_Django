from django.views.generic.edit import CreateView

from users.forms import CustomUserCreationForm


class RegistrationView(CreateView):
    template_name = "users/signup.html"
    form_class = CustomUserCreationForm
    success_url = "/"
