from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course, Enrollment
from .forms import StudentForm, CourseForm, EnrollmentForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

# STUDENT VIEWS
def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            # Send email
            send_mail(
                'Student Registered',
                f'{student.name} has been registered successfully!',
                settings.EMAIL_HOST_USER,
                [student.email],
                fail_silently=True,
            )
            messages.success(request, 'Student added and email sent.')
            return redirect('student_list')
        else:
            messages.error(request, 'Failed to add student.')
    else:
        form = StudentForm()
    return render(request, 'core/student_form.html', {'form': form})

def student_edit(request, id):
    student = get_object_or_404(Student, pk=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        messages.success(request, 'Student updated.')
        return redirect('student_list')
    return render(request, 'core/student_form.html', {'form': form})

def student_delete(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    messages.success(request, 'Student deleted.')
    return redirect('student_list')

# COURSE VIEWS
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'core/course_list.html', {'courses': courses})

def course_add(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Course added.')
        return redirect('course_list')
    return render(request, 'core/course_form.html', {'form': form})

def course_edit(request, id):
    course = get_object_or_404(Course, pk=id)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        messages.success(request, 'Course updated.')
        return redirect('course_list')
    return render(request, 'core/course_form.html', {'form': form})

def course_delete(request, id):
    course = get_object_or_404(Course, pk=id)
    course.delete()
    messages.success(request, 'Course deleted.')
    return redirect('course_list')

# ENROLLMENT VIEWS
def enrollment_list(request):
    enrollments = Enrollment.objects.select_related('student', 'course')
    return render(request, 'core/enrollment_list.html', {'enrollments': enrollments})

def enrollment_add(request):
    form = EnrollmentForm(request.POST or None)
    if form.is_valid():
        enrollment = form.save()
        # Send HTML email to student
        html_message = render_to_string('core/email_enrollment.html', {
            'name': enrollment.student.name,
            'course': enrollment.course.name
        })
        email = EmailMessage(
            'Enrollment Confirmation',
            html_message,
            settings.EMAIL_HOST_USER,
            [enrollment.student.email]
        )
        email.content_subtype = "html"
        email.send(fail_silently=True)

        messages.success(request, 'Enrollment created and email sent.')
        return redirect('enrollment_list')
    return render(request, 'core/enrollment_form.html', {'form': form})

def enrollment_edit(request, id):
    enrollment = get_object_or_404(Enrollment, pk=id)
    form = EnrollmentForm(request.POST or None, instance=enrollment)
    if form.is_valid():
        form.save()
        messages.success(request, 'Enrollment updated.')
        return redirect('enrollment_list')
    return render(request, 'core/enrollment_form.html', {'form': form})

def enrollment_delete(request, id):
    enrollment = get_object_or_404(Enrollment, pk=id)
    enrollment.delete()
    messages.success(request, 'Enrollment deleted.')
    return redirect('enrollment_list')