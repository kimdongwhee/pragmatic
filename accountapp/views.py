from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return render(request, "base.html")
    #render 인자로 request와 템플릿 파일 적용 ↑
    # return HttpResponse("Hello world")
