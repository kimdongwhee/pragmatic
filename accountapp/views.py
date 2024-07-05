from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    if request.method == "POST":
        #POST 방식으로 요청시 accountapp/hello_world.html 페이지로 전환 및 post method가 담긴 text를 context라는 꾸러미에 담아 함께 반환
        return render(request, "accountapp/hello_world.html", context={'text':'POST METHOD!'})
    else:
        #GET 방식으로 요청시 accountapp/hello_world.html 페이지로 전환 및 post method가 담긴 text를 context라는 꾸러미에 담아 함께 반환
        return render(request, "accountapp/hello_world.html", context={'text': 'GET METHOD!'})