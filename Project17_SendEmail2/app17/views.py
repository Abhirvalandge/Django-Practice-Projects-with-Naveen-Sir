from django.shortcuts import render

import smtplib
from django.shortcuts import redirect

from app17.forms import EmployeeForm
from .models import EmployeeModel
from Project17_SendEmail2 import settings
from django.core.mail import EmailMessage, send_mail


def showIndex(request):
    form = EmployeeForm()
    return render(request, "index.html", {"form": form})


def saveDetails(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    salary = request.POST.get("salary")
    email = request.POST.get("email")
    send_mail("Registration Mail", "Hello User" + name + "Your Account is created\n"
                                                         "For more information please call us on 9131994504",
              settings.EMAIL_HOST_USER, [email])

    EmployeeModel(idno=idno, name=name, salary=salary, email=email).save()
    form = EmployeeForm()

    if request.method == "POST":
        idno = request.POST.get("t1")
        name = request.POST.get("t2")
        salary = request.POST.get("t3")
        email = request.POST.get("t4")
        EmployeeModel(idno=idno, name=name, salary=salary, email=email).save()
        subject = "Registration Confirmation"
        message = "Thanks for registering to employee application"
        em = EmailMessage(subject, message, settings.EMAIL_HOST_USER, ["abhirvalandge@gmail.com"])

        try:
            mess = em.send(fail_silently=True)
            print(mess)
        except ModuleNotFoundError as smtp:
            print(smtp)

    return redirect('index')