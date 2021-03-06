from django.shortcuts import render
from .forms import studentForm

def showIndex(request):
    st=studentForm()
    return render(request,"index.html",{"form":st})

def saveDetail(request):
    rno=request.POST.get("rno")
    na=request.POST.get("name")
    cno=request.POST.get("contactno")
    em=request.POST.get("email")
    pas=request.POST.get("password")

def showSave(request):
    return render(request,"save.html")

