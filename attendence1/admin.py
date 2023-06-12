from django.contrib import admin

from attendence1.models import EmployeeDetail, PresentEmployee, Department, Org


# Register your models here.
@admin.register(EmployeeDetail)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'emp_id', 'user', 'designation', 'department', 'org', 'image')




@admin.register(PresentEmployee)
class PresentEmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_detail', 'in_time', 'out_time')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Org)
class OrgAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
