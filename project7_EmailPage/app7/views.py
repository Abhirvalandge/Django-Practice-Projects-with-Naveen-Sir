from django.shortcuts import render
from django.shortcuts import HttpResponse

def showIndex(request):
    return render(request,"index.html")

def showDetails(request):
    #Getting Data From Html
    na=request.POST.get("t1")
    a=request.POST.get("t2")
    em=request.POST.get("t3")
    print(na,a,em)
    return HttpResponse("ok")