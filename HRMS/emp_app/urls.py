from django.shortcuts import render
from django.urls import path
from . import views
from .views import EmployeeListView, AddEmployee


urlpatterns = [path("", views.index, name="index"),
               path("login/", views.user_login, name = "login"),
               path("logout/", views.user_logout, name = "logout"),
            #    path("add/employee", views.add_employee, name= "add_employee"),
               path('add/employee/', AddEmployee.as_view(), name='add-employee'),
               path("search/employee", views.search_employee, name= "search_employee"),
               path("delete/employee", views.delete_employee, name= "delete_employee"),
               path('employees/', EmployeeListView.as_view(), name='employee-list'),
            #    path("employees", views.view_employees, name= "view_employees"),
               path("leave/apply", views.leave_apply, name= "leave_apply"),
            #    path("attendance", views.attendance, name= "attendance"),
               path("role", views.role, name= "role"),
               path("register/", views.register, name= "register"),
               path("profile/", views.user_profile, name= "profile"),
               path("userdetails/<int:id>", views.user_dashboard, name= "userdetails"),
               ]
   

   

