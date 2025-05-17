from django.urls import path
from . import views

urlpatterns = [
    # Student
    path('', views.student_list, name='student_list'),
    path('student/add/', views.student_add, name='student_add'),
    path('student/edit/<int:id>/', views.student_edit, name='student_edit'),
    path('student/delete/<int:id>/', views.student_delete, name='student_delete'),

    # Course
    path('courses/', views.course_list, name='course_list'),
    path('course/add/', views.course_add, name='course_add'),
    path('course/edit/<int:id>/', views.course_edit, name='course_edit'),
    path('course/delete/<int:id>/', views.course_delete, name='course_delete'),

    # Enrollment
    path('enrollments/', views.enrollment_list, name='enrollment_list'),
    path('enrollment/add/', views.enrollment_add, name='enrollment_add'),
    path('enrollment/edit/<int:id>/', views.enrollment_edit, name='enrollment_edit'),
    path('enrollment/delete/<int:id>/', views.enrollment_delete, name='enrollment_delete'),
]