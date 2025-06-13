from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeJoiningForm

# Create your views here.
def show_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employee/emp_list.html', {'employee_details': employees})

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeJoiningForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employees_list')
    else:
        form = EmployeeJoiningForm()
    return render(request, 'employee/emp_form.html', {'form': form})

def view_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee/view_emp.html', {'employee_detail': employee})

def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeJoiningForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees_list')
    else:
        form = EmployeeJoiningForm(instance=employee)
    return render(request, 'employee/emp_form.html', {'form': form})

def show_faqs(request):
    return render(request, 'employee/faqs.html')

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('employees_list')
    return render(request, 'employee/delete_emp.html', {'employee': employee})
    student = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    return render(request, "student_registration/delete_registration.html", {'student': student})