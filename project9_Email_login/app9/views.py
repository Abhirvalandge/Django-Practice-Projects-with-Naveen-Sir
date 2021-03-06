from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def showDetails(request):
    # Getting Data From Html
    email = request.POST.get("t1")
    pas = request.POST.get("t2")
    print(email,pas)
    if email=="Abhirva" and pas=="landge":
        return render(request,"details.html")
    else:
        return render(request,"index.html",{"message":"Invalid Data"})
