from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator

from .decorators import account_ownership_required
from .forms import AccountUpdateForm
from .models import HelloWorld
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User  #장고 기본제공 User 테이블
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy  #reverse 와 reverse_lazy 는 함수형과 클래스형 뷰의 불러오는 결과에 따라 다름

#데코레이터 배열 변수설정
#(1) login_required 데코레이터 : FBV 용 데코레이터로 로그인 시에만 기능을 이용할수 있도록하는 데코레이터
#(2) account_ownership_required 데코레이터 : 커스터마이징하여 app > decorators.py에서 지정한 데코레이터로 작성자와 요청자가 다를 시 잘못됀 페이지가 표시돼도록 설정해주는 데코레이터
#(3) (1)~(2) 를 has_ownership 이라는 배열에 묶어 데코레이터에 사용하면 코드도 줄여지고 (1),(2) 번 데코레이터를 동시에 활용할 수 있는 코드를 짤 수 있음
has_ownership=[login_required, account_ownership_required]

@login_required
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
        return render(request, "accountapp/hello_world.html", context={'hello_world_list': hello_world_list})

# CBV : Class Based View
# (1)계정생성
class AccountCreateView(CreateView):
    #해당 CBV를 통해 활용할 모델객체 파라미터
    model = User  #User 로 모델 지정
    #해당 CBV를 통해 활용할 폼 파라미터
    form_class = UserCreationForm
    #해당 CBV를 통해 반환활 페이지
    success_url = reverse_lazy("accountapp:hello_world")
    #해당 CBV를 통해 볼 페이지
    template_name = "accountapp/create.html"


# (2)조회뷰
class AccountDetailView(DetailView):
    model = User
    # 인스타그램과 같이 사용자별 조회를 위해 context_object_name 지정. 지정이 안돼어 있다면 다른 사용자를 조회해도 사용자 본인정보로 조회가 됌.
    context_object_name = "target_user"
    template_name = "accountapp/detail.html"


# (3)수정뷰
# @method_decorator() 를 활용하여 클래스형 뷰에 대한 데코레이터 진행
# @method_decorator(함수기반 데코리이터명, 인자)
# @method_decorator(login_required, "get")
# @method_decorator(login_required, "post")
# @method_decorator(account_ownership_required, "get")
# @method_decorator(account_ownership_required, "post")
@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class AccountUpdateView(UpdateView):
    #해당 CBV를 통해 활용할 모델객체 파라미터
    model = User  #User 로 모델 지정
    #기존 django 제공 UserCreationForm을 리팩토리한 forms.py에서 정의한 AccountUpdatedForm 활용
    form_class = AccountUpdateForm
    context_object_name = "target_user"
    #해당 CBV를 통해 반환활 페이지
    success_url = reverse_lazy("accountapp:hello_world")
    # 해당 CBV를 통해 볼 페이지
    template_name = "accountapp/update.html"

    def get_success_url(self):
        return reverse("accountapp:detail", kwargs={'pk': self.object.pk})

# (4)삭제뷰
# @method_decorator(login_required, "get")
# @method_decorator(login_required, "post")
# @method_decorator(account_ownership_required, "get")
# @method_decorator(account_ownership_required, "post")
@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class AccountDeleteView(DeleteView):
    # 해당 CBV를 통해 활용할 모델객체 파라미터
    model = User  # User 로 모델 지정
    context_object_name = "target_user"
    #해당 CBV를 통해 반환활 페이지
    success_url = reverse_lazy("accountapp:login")
    template_name = "accountapp/delete.html"

