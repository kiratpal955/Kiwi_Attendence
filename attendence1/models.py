import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Org(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class EmployeeDetail(models.Model):
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=50, null=True)
    designation = models.CharField(max_length=50)
    org = models.ForeignKey(Org, related_name="org", on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img/", null=True)

    def __str__(self):
        return self.user.username


class PresentEmployee(models.Model):
    employee_detail = models.ForeignKey(EmployeeDetail, related_name="employee_detail", on_delete=models.CASCADE)
    in_time = models.DateTimeField(null=True, blank=True)
    out_time = models.DateTimeField(null=True, blank=True)
