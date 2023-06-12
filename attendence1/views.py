from pyexpat.errors import messages

from django.shortcuts import render, redirect
from attendence1.models import EmployeeDetail, PresentEmployee, Org, Department
from . import constants
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import AbstractUser, User


# Create your views here.

def admin(request):
    return render(request, "all_employee.html")


def login_page(request):
    message = ''
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('uname'),
            password=request.POST.get('psw'),
        )
        if user is not None:
            login(request, user)
            message = f'Hello {user.username}! You have been logged in'

            return render(request, 'receptionist.html', {'message': message})
        else:
            message = 'Login failed!'
            return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')


def add_user(request):

    if request.method == "POST":

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        designation = request.POST['designation']
        email = request.POST['email']
        org = request.POST['org']
        password = request.POST['psw']
        confirm_password = request.POST['psw-repeat']
        department = request.POST['department']
        contact = request.POST['contact_number']
        image = request.FILES.get('uploaded_image')

        if password == confirm_password:
            org_object = Org.objects.filter(id=org).first()
            department_object = Department.objects.filter(id=department).first()
            user_object = User.objects.create(username=username, first_name=first_name, last_name=last_name,
                                              password=make_password(password), email=email)

            user_detail = EmployeeDetail.objects.create(user=user_object, designation=designation,
                                                 org=org_object, contact_number=contact,
                                                 department=department_object, image=image)
            user_detail.emp_id = constants.EMP_PREFIX_ID + str(user_detail.id)
            user_detail.save()
            return redirect('login')
        else:
            return redirect('adduser')
    departments = Department.objects.all()
    orgs = Org.objects.all()
    return render(request, "register.html", {'departments': departments, 'orgs': orgs})


def employee(request):
    employees = EmployeeDetail.objects.all()
    return render(request, "all_employee.html", {'employees': employees})


def present_emp(request):
    if request.method == "POST":
        emp_id = request.POST.get('in_emp_id')

        e_d = EmployeeDetail.objects.filter(emp_id=emp_id).first()
        if e_d:
            PresentEmployee.objects.create(employee_detail=e_d, in_time=datetime.now())
            total_employee = PresentEmployee.objects.all()
            # return render(request, 'receptionist.html', {'total_employee': total_employee})
            return redirect('present_emp')
    total_employee = PresentEmployee.objects.all()
    return render(request, 'receptionist.html', {'total_employee': total_employee})


def present_employee(request):
    present = PresentEmployee.objects.all()
    return render(request, "in_office_employee.html", {'present_employees': present})


def filter_data(request):

    search_from = request.POST['date_from']
    search_to = request.POST['date_to']
    date_from = datetime.strptime(search_from, '%Y-%m-%d').date()
    date_to = datetime.strptime(search_to, '%Y-%m-%d').date()
    present = PresentEmployee.objects.filter(in_time__range=[date_from, date_to])
    return render(request, "in_office_employee.html", {'present_employees': present})
