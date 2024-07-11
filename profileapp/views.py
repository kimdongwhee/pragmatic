from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from .decorators import profile_ownership_required
from .models import Profile
from .forms import ProfileCreationForm

# 프로필 생성
class ProfileCreate(CreateView):
    #(1)저장모델
    model = Profile
    #(2)해당 뷰 호칭
    context_object_name = "target_profile"
    #(3)상속 및 활용 폼
    form_class = ProfileCreationForm
    #(4)해당 뷰 동작완료 후 반환 url / CBV시 reverse_lazy 활용
    # succes_url로 지정을 하면 detail 페이지로 바로 못넘어감. detail관련 url에 pk를 인수로 받게 지정했기 때문임. 따라서 별도 빼서 get_success_url로 지정해야함. 즉 효율적인 동적처리를 위해 진행.
    # success_url = reverse_lazy("accountapp:detail")
    #(5)해당 뷰 담당 템플릿
    template_name = "profileapp/create.html"

    #아래 코드가 없다면 프로필 생성시 pk 부여돼지 않음에 오류가 발생
    #아래 코드를 바탕으로 프로필 생성자의 pk가 등록자(로그인한자)의 pk라는 것을 명시하여 오류 해결
    #create form이 인자로 들어옴 > 데이터를 메모리에 올려놓음 > 폼 유저 pk를 작성자 pk 유저로 지정 > 폼 데이터 저장
    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("accountapp:detail", kwargs={"pk":self.object.user.pk})

# 프로필 수정
# 데코레이터를 활용해 로그인한 사용자만이 수정가능하도록 지정
@method_decorator(profile_ownership_required, "get")
@method_decorator(profile_ownership_required, "post")
class ProfileUpdate(UpdateView):
    #(1)저장모델
    model = Profile
    #(2)해당뷰 호칭
    context_object_name = "target_profile"
    #(3)상속 및 활용폼
    form_class = ProfileCreationForm
    #(4)해당 뷰 동작완료 후 반환 url / CBV시 reverse_lazy 활용
    # success_url = reverse_lazy("accountapp:detail")
    #(5)해당 뷰 담당 템플릿
    template_name = "profileapp/update.html"

    def get_success_url(self):
        return reverse_lazy("accountapp:detail", kwargs={"pk":self.object.user.pk})
