from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .models import HelloWorld

def hello_world(request):
    if request.method == "POST":
        # POST 방식 데이터 DB 저장
        # (1)POST방식에서 hello_world_input 이라는 데이터를 temp로 가져옴
        # └ 템플릿에서 받아올 인자를 get함
        temp = request.POST.get("hello_world_input")
        # (2) models.py 모델클래스 객체 생성
        new_hello_world = HelloWorld()
        # (3) HelloWorld의 text 필드에 temp 데이터 저장
        # └ POST로 받은 데이터를 DB에 삽입
        new_hello_world.text = temp
        new_hello_world.save()

        # 저장 데이터 모두 가져오기
        # └ DB 즉, Model 클래스 객체의 모든 데이터 불러오기 객체명.objects.all()
        hello_world_list = HelloWorld.objects.all()
        # app > urls.py 에서 지정한 app_name과 reverse를 활용하여 위 코드가 실행시 해당 url로 리다이렉트
        # └ accountapp의 hello_world url로 이동
        return HttpResponseRedirect(reverse("accountapp:hello_world"))
    else:
        hello_world_list = HelloWorld.objects.all()
        #GET 방식으로 요청시 accountapp/hello_world.html 페이지로 전환 및 post method가 담긴 hello_world_list를 context라는 꾸러미에 담아 함께 반환
        return render(request, "accountapp/hello_world.html", context={'hello_world_list' : hello_world_list})


from django.views.generic import CreateView
from django.contrib.auth.models import User #장고 기본제공 User 테이블
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy #reverse 와 reverse_lazy 는 함수형과 클래스형 뷰의 불러오는 결과에 따라 다름
# CBV : Class Based View
# (1)계정생성
class AccountCreateView(CreateView):
    #해당 CBV를 통해 활용할 모델객체 파라미터
    model = User #User 로 모델 지정
    #해당 CBV를 통해 활용할 폼 파라미터
    form_class = UserCreationForm
    #해당 CBV를 통해 반환활 페이지
    success_url = reverse_lazy("accountapp:hello_world")
    #해당 CBV를 통해 볼 페이지
    template_name = "accountapp/create.html"
