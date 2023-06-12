from django.contrib import admin
from django.urls import path, include

from admin_app import views

urlpatterns = [
    path("admin_user", views.AdminLogin, name="adminuser")
]
