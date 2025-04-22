from django.shortcuts import render, redirect
from django.contrib.auth import login
# Removed logout, LoginView, LogoutView imports as they are no longer used here
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistrationForm # Removed LoginForm import

class UserRegistrationView(CreateView):
    """
    View for user registration.
    Uses the RegistrationForm and redirects to the login page upon successful registration.
    """
    form_class = RegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login') # Redirect to login page after successful registration

    def form_valid(self, form):
        # Log the user in directly after registration
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

# Removed UserLoginView and UserLogoutView as they are now handled by built-in Django views in urls.py
