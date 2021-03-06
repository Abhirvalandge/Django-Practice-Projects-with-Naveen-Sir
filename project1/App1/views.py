from django.shortcuts import HttpResponse

def showMain(request):
    return HttpResponse("Hello World")
