from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.select_related('branch', 'admission')

    gender = request.GET.get('gender')
    branch = request.GET.get('branch')
    sort_by = request.GET.get('sort')

    if gender:
        students = students.filter(gender=gender)

    if branch:
        students = students.filter(branch__name=branch)

    if 'start' in request.GET and 'end' in request.GET:
        start_date = request.GET.get('start')
        end_date = request.GET.get('end')
        students = students.filter(registration_date__range=[start_date, end_date])

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
