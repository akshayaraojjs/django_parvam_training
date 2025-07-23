from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group, Permission # importing the predefined models: Group & Permission from auth models
from django.contrib.auth import authenticate, login, logout # To use the predefined methods for login, authenticate & logout functionality
from .forms import UserRegisterForm # To import the custom registration form from forms.py 
from django.contrib import messages # To print the success/ failure messages
from django.contrib.auth.decorators import login_required, permission_required # To use decorators we need to import this
from .models import Blog

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
            user.set_password(password)
            user.save()
            # role = admin
            # if group exist with the name admin, then the user will be assigned to that group
            group = Group.objects.get(name=role)
            user.groups.add(group)

            messages.success(request, 'Registration successful.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome {user.username}!')
            return redirect('welcome')  # All roles go to blog list
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'blog/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return render(request, 'blog/welcome.html')

@login_required
@permission_required('blog.view_blog', raise_exception=True) # checks whether the current user has the permission to view blog (all the groups has this permission)
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

@login_required # decorator - Used for checking whether the user has logged in or not
# Syntax to check the permission: 
# @permission_required('app_name.permission_name')
@permission_required('blog.add_blog', raise_exception=True) # checks whether the current user has the permission to add blog (only admin & writer can do this)
def blog_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Blog.objects.create(title=title, content=content, created_by=request.user)
        return redirect('blog_list')
    return render(request, 'blog/blog_create.html')

@login_required
@permission_required('blog.change_blog', raise_exception=True) # checks whether the current user has the permission to edit blog (only admin can do this)
def blog_edit(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.save()
        return redirect('blog_list')
    return render(request, 'blog/blog_edit.html', {'blog': blog})

@login_required
@permission_required('blog.delete_blog', raise_exception=True) # checks whether the current user has the permission to delete blog (only admin can do this)
def blog_delete(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('blog_list')

@login_required
def user_permissions_view(request):
    permissions = request.user.get_all_permissions() # get_all_permissions() method is used to list out all the permissions of the current user
    permission_objects = Permission.objects.filter(codename__in=[
        perm.split('.')[1] for perm in permissions # codename is given as reference to get the descriptive name of the permission
    ])

    return render(request, 'blog/user_permissions.html', {
        'permission_list': permission_objects
    })