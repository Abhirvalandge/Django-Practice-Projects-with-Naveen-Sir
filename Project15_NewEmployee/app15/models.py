from django.db import models

class EmployeeModel(models.Model):
     idno=models.IntegerField(primary_key=True)
     name=models.CharField(max_length=30)
     sal=models.DecimalField(max_digits=5,decimal_places=2)
     gender=models.CharField(max_length=1)
     doj=models.DateField()