from django.shortcuts import render

def showIndex(request):
    d1={
          {"idno":101,"name":"Ravi","designation":"Manager"},
          {"idno":102,"name":"Kumar","designation":"Developer"},
          {"idno":103,"name":"Mohan","designation":"Manager"},
          {"idno":104,"name":"Sourabh","designation":"Developer"},
          {"idno":105,"name":"Akash","designation":"Tester"},
          {"idno":106,"name":"Purvesh","designation":"Developer"},
          {"idno":107,"name":"Suresh","designation":"Tester"},
          {"idno":108,"name":"Abhirva","designation":"Manager"}
    }
    return render(request,"index.html",d1)

