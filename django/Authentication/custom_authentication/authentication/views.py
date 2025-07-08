from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful.")
            return redirect('signin')
    else:
        form = RegisterForm()
    return render(request, 'authentication/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            user = authenticate(username=uname, password=pwd)
            if user:
                login(request, user)
                if user.role == 'Admin':
                    return redirect('admin_page')
                else:
                    return redirect('user_page')
            else:
                messages.error(request, "Invalid credentials")
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='login')
def user_dashboard(request):
    return render(request, 'authentication/dashboard.html')

@login_required(login_url='login')
def admin_dashboard(request):
    return render(request, 'authentication/admin_dashboard.html')