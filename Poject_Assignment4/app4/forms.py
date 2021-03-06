from django import forms

class EmployeeForm(forms.Form):
    eno=forms.IntegerField(min_value=1000,label="Employee No",max_value=99999)
    ename=forms.IntegerField(min_length=2,label="Employee Name",max_length=30)
    bsal=forms.DecimalField(max_value=9999999999,label="Basic Salary",min_value=10000)
