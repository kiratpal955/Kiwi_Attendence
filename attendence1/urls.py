from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('user', views.admin, name='adminuser'),
    path('adduser', views.add_user, name='adduser'),
    path('all_employee', views.employee, name='all_employee'),
    path('present_emp', views.present_emp, name='present_emp'),
    path('present_employee', views.present_employee, name='present_employee'),
    path('filter', views.filter_data, name='filter')
]
