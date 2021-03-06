from django.shortcuts import render
from ContactForm_SendEmail.forms import contactFormEmail
from django.core.mail import send_mail

def contactsendmail(request):
    if request.method == "GET":
        form = contactFormEmail()
    else:
        form = contactFormEmail(request.POST)
        if form.is_valid():
            frommail = form.cleaned_data['fromemail']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject,message,frommail,['landgeabhirva44@gmail.com',frommail])
    return render(request,"contactForm.html",{'form':form})
