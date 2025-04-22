from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistrationForm(UserCreationForm):
    """
    User registration form.
    Inherits from Django's built-in UserCreationForm and adds Bootstrap classes.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mb-2'}) # Add Bootstrap class

class LoginForm(AuthenticationForm):
    """
    User login form.
    Inherits from Django's built-in AuthenticationForm and adds Bootstrap classes.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Password'})