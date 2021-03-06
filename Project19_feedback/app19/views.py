from django.shortcuts import render
from django.shortcuts import redirect
from .models import Login
from .models import Feedback


def showIndex(request):
    return render(request,"index.html")


def logincheck(request):
    name = request.session["name"]
    if name:
        return render(request, "welcome.html", {"message": "Welcome User"})
    else:
        un = request.POST.get("username")
        up = request.POST.get("password")
        qs = Login.objects.filter(username=un, password=up)
        if qs:
            request.session["name"] = un  # writing username to session table
            return render(request, "welcome.html", {"message": "Welcome User", "id": "uname"})
        else:
           return render(request, "index.html", {"message": "Invalid User"})


def feedback(request):
    feedback_mess = request.POST.get("fb")
    name = request.session["name"]
    Feedback(username=name, message=feedback_mess).save()
    #return redirect("/logincheck/")
