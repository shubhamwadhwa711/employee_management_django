from django.contrib import admin
from .models import (
    Department,
    Role,
    Employee,   
    Attendance,
    Leave
)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=('id','name', 'location')


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
     list_display=('id','name')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["emp_id","first_name","last_name", "salary",
                     "email","bonus","dept","role","phone", "date_joining"]

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["id", "employee","clock_in", "clock_out"]

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ["id", "employee","start_date","end_date","reason","is_approved"]

