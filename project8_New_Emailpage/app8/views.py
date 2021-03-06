from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def showDetails(request):
    #Getting Data From Html
    na=request.POST.get("t1")
    a=request.POST.get("t2")
    em=request.POST.get("t3")
    print(na,a,em)
    return render(request,"Details.html",{"data":a,"data1":na,"data2":em})


