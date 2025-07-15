from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.select_related('department', 'salary')

    # Optional filters via query params
    gender = request.GET.get('gender')
    dept = request.GET.get('dept')
    sort_by = request.GET.get('sort')  # e.g., 'salary', '-salary'

    if gender:
        employees = employees.filter(gender=gender)

    if dept:
        employees = employees.filter(department__name=dept)

    if sort_by == 'salary':
        employees = employees.order_by('salary__amount')
    elif sort_by == '-salary':
        employees = employees.order_by('-salary__amount')
    elif sort_by == 'dept':
        employees = employees.order_by('department__name')
    elif sort_by == '-dept':
        employees = employees.order_by('-department__name')

    return render(request, 'staff/employee_list.html', {'employees': employees})