from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def showImage(request):
    return render(request,"image.html",{"image1":"I1","image2":"I2","image3":"I3"})