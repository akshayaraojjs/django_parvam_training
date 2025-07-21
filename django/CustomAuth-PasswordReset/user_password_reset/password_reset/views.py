from django.contrib.auth import login, logout, update_session_auth_hash  # to use the Django ORM - Authentication system
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm # to use the Django Default forms for authentication and password reset
from django.contrib.auth.models import User # To import user model
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView # To reset the password along with the email template, subject & the html page
from django.shortcuts import render, redirect # for rendering templates and redirecting users
from django.contrib import messages # To show success or error messages
from django import forms # To create custom forms - Here it is Register Form
from django.urls import reverse_lazy #To show the message that password reset is done
from django.contrib.auth.tokens import default_token_generator # To generate tokens for password reset
from django.core.exceptions import ValidationError # To show the error messages for the password validation
import re # To use regular expressions for password validation

# Registration Form Design
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 8 or len(password) > 14:
            raise ValidationError("Password must be between 8 and 14 characters.")
        if not re.search(r'[A-Z]', password):
            raise ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password):
            raise ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r'\d', password):
            raise ValidationError("Password must contain at least one digit.")
        if not re.search(r'[@$!%*?&]', password):
            raise ValidationError("Password must contain at least one special character.")

        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data

# For Actual Registration
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            messages.success(request, "Registration successful")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'password_reset/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'password_reset/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard_view(request):
    return render(request, 'password_reset/dashboard.html')

# logic for changing password using old password
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully")
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_reset/change_password.html', {'form': form})

# for changing password using mail
class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset/password_reset.html'
    email_template_name = 'password_reset/password_reset_email.html'
    subject_template_name = 'password_reset/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm
    token_generator = default_token_generator

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')
    form_class = SetPasswordForm
    token_generator = default_token_generator