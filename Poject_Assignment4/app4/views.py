from django.shortcuts import render
from .forms import EmployeeForm

def showIndex(request):
    em=EmployeeForm
    return render(request,"index.html",{"form":em})

def showEmployee(request):
    eno=request.POST.get("e1")
    ename=request.POST.get("e2")
    bsal=int(request.POST.get("e3"))
    DA=0.2*bsal
    HRA=0.4*bsal
    TotalSal=bsal+DA+HRA
    result={"DA":DA,
            "HRA":HRA,
            "TotalSal":TotalSal}
    return render(request,"index.html",{"data":bsal,"data1":DA,"data2":HRA,"data3":TotalSal})