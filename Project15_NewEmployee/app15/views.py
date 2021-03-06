from django.shortcuts import render
from .models import EmployeeModel


def showIndex(request):
    return render(request, "index.html")


def newEmployee(request):
    return render(request, "newemployee.html")


def viewEmployee(request):
    qs = EmployeeModel.objects.all()
    return render(request, "viewall.html", {"data": qs})


def saveEmployee(request):
    id = request.POST.get("id")
    name = request.POST.get("name")
    sal = request.POST.get("sal")
    gen = request.POST.get("gender")
    doj = request.POST.get("doj")

    # To save a employee record into table
    em = EmployeeModel(idno=id, name=name, salary=sal, gender=gen, doj=doj)
    em.save()
    return render(request, "index.html", {"message": "Employee Saved"})


def deleteEmployee(request):
    id = request.GET.get("i")
    EmployeeModel.objects.filter(idno=id).delete()

    # Reusing ViewEmployees Function
    return viewEmployee(request)


def updateEmployee(request):
    x = request.POST.get("u_id")
    result = EmployeeModel.objects.get(idno=x)
    return render(request, "update.html", {"data": result})
