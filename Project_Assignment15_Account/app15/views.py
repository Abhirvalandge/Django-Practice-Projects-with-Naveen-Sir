from urllib import request

from django.shortcuts import render, redirect

global balance,total
balance = int(5000)
total = int(0)


def login(request):
    try:
        if request.COOKIES["Status"]:
           return render(request,"welcome.html")
        else:
            return render(request,"login.html")
    except KeyError:
        return render(request,"login.html")

def loginCheck(request):
    accno = request.POST.get("uacc")
    password = request.POST.get("upass")
    try:
        login.Objects.get(accno="uacc",password="upass")
        response=render(request,"welcome.html")
        response.set_cookie("Status",True)
        return response
    except login.DoesNotExist:
        return render(request,"login.html")


def welcome(request):
    accno = request.POST.get("uacc")
    password = request.POST.get("upass")
    if accno == "12345" and password == "abhirva":
        return render(request, "welcome.html", {"message1": "Login Successfully","message2":"Abhirva","message3": balance})
    else:
        return render(request, "login.html", {"message": "Invalid Account"})

def deposite(request):
    #value = int(request.POST.get("d1"))
    return render(request,"deposite.html")

def saveDepo(request):

    deposite = int(request.POST.get("d1"))
    total = balance + deposite
    return render(request,"welcome.html",{"message2":"Abhirva","message3": total})

def withdraw(request):
    return render(request,"withdraw.html")

def draw(request):
    mdraw = int(request.POST.get("m1"))
    total2 = balance - mdraw
    return render(request,"welcome.html",{"message2":"Abhirva","message3": total2})

def logoutuser(request):
    del request.COOKIES["Status"]
    return login(request)

