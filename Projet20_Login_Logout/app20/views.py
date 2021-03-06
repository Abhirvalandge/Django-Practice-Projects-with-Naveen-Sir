from django.shortcuts import render, redirect
from .models import Register

def showindex(request):
    return render(request,"index.html")


def register(request):
    return render(request,"registration.html")


def SaveDetails(request):
    if request.method=="POST":
        name = request.POST.get("name")
        cno = request.POST.get("contact")
        username = request.POST.get("uname")
        password = request.POST.get("password")
        Register(name=name,cno=cno,username=username,password=password).save()
        return render(request,"index.html",{"message":"Registered"})

def validate(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("password")
        qs = Register.objects.filter(username=username,password=password)
        if qs:
            request.session["uname"]=username
            return render(request,"home.html")
        else:
            return render(request,"index.html",{"message":"Invalid User"})


def logout(request):
    del request.session["uname"]
    request.session.modified = True
    return redirect('index')