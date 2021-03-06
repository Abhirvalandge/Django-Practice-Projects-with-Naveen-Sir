from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")


def aboutUs(request):
    return render(request,"about.html")


def doctor(request):
    return render(request,"doctor.html")


def services(request):
    return render(request, "services.html")


def department(request):
    return render(request, "dep.html")


def appointment(request):
    return render(request, "appointment.html")

def appointmentData(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    return render(request,"appointment.html",{"message" : "Your Appointment has been sent" + email})


def blog(request):
    return render(request, "blog.html")


def singleblog(request):
    return render(request, "single-blog.html")


def contact(request):
    return render(request, "contact.html")
