"""
Connor Warner
CIS 218
2/28/24
"""

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView



class SignUpView(CreateView):
    """Sign Up View"""

    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"