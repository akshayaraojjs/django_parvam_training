from django import forms
from .models import Employee

class EmployeeJoiningForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'