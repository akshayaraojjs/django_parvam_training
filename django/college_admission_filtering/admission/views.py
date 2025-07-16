from django.shortcuts import render
from .models import Student
from datetime import datetime

def student_list(request):
    students = Student.objects.select_related('branch', 'admission')

    gender_filter = request.GET.get('gender')
    branch = request.GET.get('branch')
    sort_by = request.GET.get('sort')

    if gender_filter:
        students = students.filter(gender=gender_filter)

    if branch:
        students = students.filter(branch__name=branch)

    # if 'start' in request.GET and 'end' in request.GET:
    #     start_date = request.GET.get('start')
    #     end_date = request.GET.get('end')
    #     students = students.filter(registration_date__range=[start_date, end_date])

    start_date_str = request.GET.get('start')
    end_date_str = request.GET.get('end')
    
    if start_date_str and end_date_str:
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            students = students.filter(registration_date__range=[start_date, end_date])
        except ValueError:
            pass
            # print("Invalid date format. Please use YYYY-MM-DD.")

    if sort_by == 'fees':
        students = students.order_by('admission__fees')
    elif sort_by == '-fees':
        students = students.order_by('-admission__fees')
    elif sort_by == 'branch':
        students = students.order_by('branch__name')
    elif sort_by == '-branch':
        students = students.order_by('-branch__name')
    elif sort_by == 'age':
        students = students.order_by('age')
    elif sort_by == '-age':
        students = students.order_by('-age')

    return render(request, 'admission/student_list.html', {'students': students})
