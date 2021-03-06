from django.shortcuts import HttpResponse

def showIndex(Request):
    return HttpResponse("<html><body><h1>Helloworld</h1></body></html>")



