from django.urls import path
from django.contrib.auth import views as auth_views # Import built-in auth views
from .views import UserRegistrationView # Keep the custom registration view

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    # Use built-in LoginView
    path('login/', auth_views.LoginView.as_view(
            template_name='accounts/login.html', # Specify the template
            redirect_authenticated_user=True # Optional: Redirect if already logged in
         ), name='login'),
    # Use built-in LogoutView
    path('logout/', auth_views.LogoutView.as_view(
            # next_page is automatically handled by LOGOUT_REDIRECT_URL in settings
            # Or you can specify it here: next_page='home'
         ), name='logout'),
]