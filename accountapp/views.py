from django.http import HttpResponse
from django.shortcuts import render
from .models import HelloWorld

def hello_world(request):
    if request.method == "POST":
        # POST 방식 데이터 DB 저장
        # (1)POST방식에서 hello_world_input 이라는 데이터를 temp로 가져옴
        temp = request.POST.get("hello_world_input")
        # (2) models.py 모델클래스 객체 생성
        new_hello_world = HelloWorld()
        # (3) HelloWorld의 text 필드에 temp 데이터 저장
        new_hello_world.text = temp
        new_hello_world.save()
        #POST 방식으로 요청시 accountapp/hello_world.html 페이지로 전환 및 데이터가 담긴 hello_world_output을 함께 반환
        return render(request, "accountapp/hello_world.html", context={'hello_world_output':temp})
    else:
        #GET 방식으로 요청시 accountapp/hello_world.html 페이지로 전환 및 post method가 담긴 text를 context라는 꾸러미에 담아 함께 반환
        return render(request, "accountapp/hello_world.html", context={'text': 'GET METHOD!'})