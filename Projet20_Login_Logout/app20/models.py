from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=30)
    cno = models.IntegerField(max_length=9999999999)
    username = models.EmailField()
    password = models.CharField(max_length=8)
