from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=5)

class Feedback(models.Model):
    username = models.CharField(max_length=30)
    message = models.TextField()




