from django import forms
from .models import Candidate, Company, Registration

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
        
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'