from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def showMain(request):
    fN =int(request.POST.get("f1"))
    lN =int(request.POST.get("f2"))
    op=request.POST.get("a1")
    if op=="add":
        d1=fN+lN
    elif op=="sub":
        d1=fN-lN
    elif op=="mul":
        d1=fN*lN
    else:
        d1=fN/lN


    return render(request,"index.html",{'data':op,"data2":d1})
