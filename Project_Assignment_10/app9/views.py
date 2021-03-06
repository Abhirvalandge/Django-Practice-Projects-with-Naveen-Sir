from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def showOne(request):
    uname = request.POST.get("A1")
    upass = request.POST.get("A2")
    admin = request.POST.get("ad")
    employee = request.POST.get("ad")
    faculty = request.POST.get("ad")
    student = request.POST.get("ad")
    if uname == "Mohan" and upass == "Mohan" and admin == "adm":
      return render(request,"Admin.html")

    elif uname == "Swapnil" and upass == "Swapnil" and employee == "emp":
       return render(request,"Employee.html")

    elif uname == "Shilpa" and upass == "Shilpa" and faculty == "fac":
       return render(request,"Faculty.html")

    elif uname == "Abhirva" and upass == "Abhirva" and student == "stu":
        return render(request, "Student.html")

    else:
        return render(request, "index.html", {"message": "Invalid Username and Password"})

