from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def validate(request):
    username = request.POST.get("uname")
    password = request.POST.get("upass")

    if username == "Abhirva" and password == "landge":
        return render(request,"welcome.html")
    else:
        return render(request,"index.html",{"message":"Invalid User"})
