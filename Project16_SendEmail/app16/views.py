import smtplib

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.mail import send_mail
from Project16_SendEmail import settings as se
from django.core.mail import EmailMessage

def login(request):
    send_mail("check","This is a check mail.Hii Sourabh",se.EMAIL_HOST_USER,["__@gmail.com","__@gmail.com"])
    return HttpResponse("valid")

#def send_mail(subject,message,from_email,recipient_list):
    em = EmailMessage(subject,message,se.EMAIL_HOST_USER,[email])
    try:
        mess = em.send(fail_silently=True)
        print(mess)
    except smtplib.SMTPException as smtp:
        print(smtp)



