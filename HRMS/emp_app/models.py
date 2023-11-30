from django.db import models

class Department(models.Model):   
    name = models.CharField("Name", max_length=100, null = False)
    location = models.CharField("Location", max_length=100)    

    def __str__(self):
        return self.name

class Role(models.Model):   
    name = models.CharField("Name", max_length=100, null = False)

    def __str__(self):
        return self.name
    
class Employee(models.Model):  
    emp_id = models.CharField(max_length=10, primary_key = True)  
    first_name = models.CharField("Name", max_length=100, null = False)
    last_name = models.CharField("Name", max_length=100)
    salary = models.IntegerField(default=0)
    email = models.EmailField("Email")
    bonus = models.IntegerField(default=0)
    dept  = models.ForeignKey(
        Department, on_delete=models.CASCADE
    )
    role =  models.ForeignKey(
        Role, on_delete=models.CASCADE)    
    phone= models.IntegerField(default=0)
    date_joining = models.DateField()

    def __str__(self):
        return self.emp_id
    
class Attendance(models.Model):  
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee} - {self.clock_in}"
    
class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.employee} - {self.start_date} to {self.end_date} ({'Approved' if self.is_approved else 'Pending'})"
    
