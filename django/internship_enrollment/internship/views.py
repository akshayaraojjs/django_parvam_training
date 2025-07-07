from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Candidate, Company, Registration
from .forms import CandidateForm, CompanyForm, RegistrationForm

# Create your views here.
def intern_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'internship/candidate_list.html', {'candidates': candidates})

def register_intern(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            candidate = form.save()
            messages.success(request, 'Candidate registered successfully.')
            return redirect('list_intern')
        else:
            messages.error(request, 'Failed to add candidate.')
    else:
        form = CandidateForm()
    return render(request,  'internship/register_candidate.html', {'form': form})

def edit_intern(request, id):
    candidate = get_object_or_404(Candidate, pk=id)
    form = CandidateForm(request.POST or None, instance=candidate)
    if form.is_valid():
        form.save()
        messages.success(request, 'Candidate Details updated.')
        return redirect('list_intern')
    return render(request,  'internship/register_candidate.html', {'form': form})

def delete_intern(request, id):
    candidate = get_object_or_404(Candidate, pk=id)
    if request.method == 'POST':
        candidate.delete()
        messages.success(request, 'Candidate details deleted successfully!')
        return redirect('list_intern')
    return render(request, 'internship/delete_candidate.html', {'candidate': candidate})

def list_company(request):
    companies = Company.objects.all()
    return render(request,  'internship/company_list.html', {'companies': companies})

def register_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()
            messages.success(request, 'Company details added successfully.')
            return redirect('company_list')
        else:
            messages.error(request, 'Failed to add company details.')
    else:
        form = CompanyForm()
    return render(request,  'internship/add_company.html', {'form': form})

def edit_company(request, id):
    company = get_object_or_404(Company, pk=id)
    form = CompanyForm(request.POST or None, instance=company)
    if form.is_valid():
        form.save()
        messages.success(request, 'Company Details updated.')
        return redirect('company_list')
    return render(request,  'internship/add_company.html', {'form': form})

def delete_company(request, id):
    company = get_object_or_404(Company, pk=id)
    if request.method == 'POST':
        company.delete()
        messages.success(request, 'Company details deleted successfully!')
        return redirect('company_list')
    return render(request,  'internship/delete_company.html', {'company': company})

def add_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save()
            messages.success(request, 'Internship registration completed successfully.')
            return redirect('registration_create')
        else:
            messages.error(request, 'Failed to make registration.')
    else:
        form = RegistrationForm()
    return render(request,  'internship/internship_registration.html', {'form':form})

def list_registration(request):
    registrations = Registration.objects.all()
    return render(request,  'internship/registration_list.html', {'registrations': registrations})
    