from django.db import models

class EmployeeModel(models.Model):
     idno=models.IntegerField(primary_key=True)
     name=models.IntegerField(max_length=30)
     sal=models.DecimalField(max_digits=10,decimal_places=2)
     gender=models.CharField()
     doj=models.DateField()