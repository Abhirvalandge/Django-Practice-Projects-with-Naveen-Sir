from django.shortcuts import render

def login(request):
    try:
        if request.COOKIES["Status"]:
           return render(request,"welcome.html",{"message":"Welcome User"})
        else:
            return render(request,"login.html")
    except KeyError:
        return render(request,"login.html")

def loginCheck(request):
    accno = request.POST.get("uacc")
    password = request.POST.get("upass")
    try:
        login.Objects.get(accno="uacc",password="upass")
        response=render(request,"welcome.html",{"message":"Welcome User"})
        response.set_cookie("Status",True)
        return response
    except login.DoesNotExist:
        return render(request,"login.html",{"message1":"Invalid User"})

def logoutUser(request):
    del request.COOKIES["Status"]
    return login(request)