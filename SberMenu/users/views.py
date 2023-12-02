from django.views.generic.edit import CreateView

from users.forms import UserCreationForm


class RegistrationView(CreateView):
    template_name = "users/signup.html"
    form_class = UserCreationForm
    success_url = "/"
