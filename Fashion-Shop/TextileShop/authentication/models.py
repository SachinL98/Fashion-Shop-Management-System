from django.forms import ModelForm
from django.db import models



class EmployeesReg(models.Model):
    empid = models.CharField(max_length=45,null=True)
    fname = models.CharField(max_length=45,null=True)
    lname = models.CharField(max_length=45,null=True)
    email = models.EmailField()
    position = models.CharField(max_length=45,null=True)
    password = models.CharField(max_length=255,null=True)
    class Meta:
        db_table = "Employee"



class Leave(models.Model):
    date = models.CharField(max_length=45,null=True)
    empid = models.CharField(max_length=45,null=True)
    reason = models.CharField(max_length=255,null=True)
    status = models.CharField(max_length=45,null=True)
    leaveType = models.CharField(max_length=45,null=True)
    class Meta:
        db_table = "leave"


class employee_positions(models.Model):

    name = models.CharField(max_length=45,null=True)
    description = models.CharField(max_length=45,null=True)
   
    class Meta:
        db_table = "emp_positions"


class leave_types(models.Model):

    leave_type = models.CharField(max_length=45,null=True)
    description = models.CharField(max_length=45,null=True)
   
    class Meta:
        db_table = "leave_types"