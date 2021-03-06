from django.shortcuts import render

def showMain(request):
        return render(request,"index.html")


def showIndex(request):
    oroom = 1500
    droom = 2500
    sroom = 5000
    comp = 1000
    gy = 250
    min = 50
    gname = request.POST.get("gn")
    gcont = request.POST.get("gc")
    add = request.POST.get("add")
    ordi = request.POST.get("ord")
    delux = request.POST.get("del")
    suite = request.POST.get("sui")
    computer = request.POST.get("com")
    gym = request.POST.get("gym")
    mineral = request.POST.get("min")
    if ordi == "oroom" and computer == "comp":
     a1=oroom+comp

    return render(request,"confirmation.html", {"data1":a1})

