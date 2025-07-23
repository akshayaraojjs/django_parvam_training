from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='welcome'),
    path('list/', views.blog_list, name='blog_list'),
    path('create/', views.blog_create, name='blog_create'),
    path('edit/<int:blog_id>/', views.blog_edit, name='blog_edit'),
    path('delete/<int:blog_id>/', views.blog_delete, name='blog_delete'),
    path('permissions/', views.user_permissions_view, name='user_permissions'),
]