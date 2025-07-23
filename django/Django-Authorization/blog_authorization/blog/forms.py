from django import forms
from django.contrib.auth.models import User, Group
from .models import Blog  # 👈 Import your Blog model

ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('writer', 'Writer'),
    ('user', 'User')
]

# Custom Registration Form
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content'] # We are taking input for 2 fields, other 2 fields(created_by and create_at) will be taken care by model
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blog title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Write your blog content here...'})
        }