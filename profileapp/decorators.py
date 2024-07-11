#데코레이터 생성
from django.http import HttpResponseForbidden
from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs["pk"])
        #사용자와 요청자가 다르면 잘못됀 페이지 반환
        if not profile.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated