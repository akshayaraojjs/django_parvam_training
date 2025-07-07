from django.urls import path
from . import views

urlpatterns = [
    path('', views.intern_list, name='list_intern'),
    path('create_candidate', views.register_intern, name='intern_register'),
    path('candidate/edit/<int:id>', views.edit_intern, name='intern_edit'),
    path('candidate/delete/<int:id>', views.delete_intern, name='intern_delete'),
    path('company_list', views.list_company, name='company_list'),
    path('add_company', views.register_company, name='company_register'),
    path('company/edit/<int:id>', views.edit_company, name='company_edit'),
    path('company/delete/<int:id>', views.delete_company, name='company_delete'),
    path('registration_add', views.add_registration, name='registration_create'),
    path('list_registration', views.list_registration, name='registration_list'),
]