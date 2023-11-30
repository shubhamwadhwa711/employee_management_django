from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from .models import (    
    Department,
    Role,    
    Employee,
    Attendance,
    Leave
    )
from datetime import datetime
from django.contrib.auth.models import User,Group
from .forms import RegisterForm, EditUserForm, EditAdminForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account created successfully !!!")
            user = fm.save()
            group = Group.objects.get(name ='Employee')
            user.groups.add(group)
    else:
        fm = RegisterForm()
    return render(request, 'register.html', {'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request, data = request.POST)
            if fm.is_valid():
                username =  fm.cleaned_data['username']
                pwd = fm.cleaned_data['password']
                user = authenticate(username = username, password = pwd)
                if user is not None:
                    login(request,user)
                    messages.success(request, "Logged in successfully")
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminForm(request.POST, instance = request.user)
                users = User.objects.all()
            else:
                fm = EditUserForm(request.POST, instance = request.user)
                users = None
            if fm.is_valid():
                fm = EditUserForm(instance = request.user)
                messages.success(request, "Profile updated successfully")
                if fm.is_valid():
                    fm.save()
        else:
             if request.user.is_superuser == True:
                 fm = EditAdminForm(instance = request.user)
                 users = User.objects.all()
             else:
                fm = EditUserForm(instance = request.user)
                users = None
        return render(request, "profile.html", {'name':request.user.username, 'form':fm, 'users':users})
    else:
        return HttpResponseRedirect('/login/')
    
def user_dashboard(request,id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminForm(instance = pi)
        return render(request, "userdashboard.html", {'name':request.user.username,'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def index(request):
    return render(request, "index.html")

def add_employee(request):
    return render(request, "add_employee.html")

# def view_employees(request):
#     emp_list = Employee.objects.all()
#     context = {'emps':emp_list}
#     return render(request, "employee.html", context)

def search_employee(request):
    return render(request, "employee.html")

def delete_employee(request):
    return render(request, "employee.html")

def leave_apply(request):
    return render(request, "leave.html")

def role(request):
    context = {'HR':'HR','Admin':'Admin', 'Employee':'Employee'}
    return render(request, "role.html",context=context)


#---------------class based views--------------------------------------
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee.html'
    context_object_name = 'emps'

class AddEmployee(View): 
    template_name = "add_employee.html" 

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        emp_id = request.POST.get("emp_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        salary = int(request.POST.get("salary"))
        email = request.POST.get("email")
        bonus = int(request.POST.get("bonus"))
        dept  = int(request.POST.get("dept"))
        role =  int(request.POST.get("role"))
        phone= int(request.POST.get("phone"))        
        new_employee = Employee(emp_id = emp_id, first_name = first_name, last_name = last_name, salary =salary,
                                email = email, bonus = bonus, dept_id = dept, role_id = role, phone = phone,
                                date_joining = datetime.now()       
        )
        new_employee.save()
        return HttpResponse("Employee added successfully")





