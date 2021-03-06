from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def showMain(request):
    sno=request.POST.get("s1")
    sname=request.POST.get("s2")
    sub1 = int(request.POST.get("s3"))
    sub2= int(request.POST.get("s4"))
    sub3 = int(request.POST.get("s5"))
    marks=(sub1+sub2+sub3)
    average=marks/3

    if sub1>=35:
        st1="Pass"
    else:
        st1="Fail"
    if sub2>=35:
        st2="Pass"
    else:
        st2="Fail"
    if sub3>=35:
        st3="Pass"
    else:
        st3="Fail"

    return render(request,"index.html",{"data":marks,"data1":sub1,"data2":sub2,
                                        "data3":sub3,"data4":average,"s1":st1,"s2":st2,"s3":st3})

