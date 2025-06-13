from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_employees, name='employees_list'),
    path('create/', views.create_employee, name='new_employee'),
    path('<int:pk>/view/', views.view_employee, name='show_employee'),
    path('<int:pk>/edit/', views.edit_employee, name='update_employee'),
    path('<int:pk>/delete/', views.delete_employee, name='remove_employee'),
    path('faqs/', views.show_faqs, name='faqs_page'),
    # Explanation: 'route/path', views.method_name, name='name_of_the_route'
]