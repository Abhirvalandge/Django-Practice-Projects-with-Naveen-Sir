from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from Project25 import settings


def showIndex(request):
    subject = "Test Mail"
    message = "Hello this is navee from sathya tech sending a test mail"
    send_mail(subject,
              message,
              settings.EMAIL_HOST_USER,
              ['mailmenaveenkumar@gmail.com'])
    return HttpResponse("Mail Sent")