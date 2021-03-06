from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def saveName(request):
    firstN = request.POST.get("f1")
    lastN = request.POST.get("f2")
    return render(request,"index.html",{'data1':firstN , 'data':lastN})