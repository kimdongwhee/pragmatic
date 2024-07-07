from django.urls import path
from accountapp.views import hello_world, AccountCreateView

#앱네임 지정
#ex) 127.0.0.1/account/hello_world/ = accountapp:hello_world
app_name = "accountapp"

urlpatterns = [
    path("hello_world/", hello_world, name="hello_world"),
    # 로그인은 템플릿을 별도 설정해야함
    path("login/", LoginViews.as_view(template_name=""),name="login"),
    path("logout/", hello_world, name="logout"),
    # CBV를 지정할때는 CBV.as_view()로 지정
    path("create/", AccountCreateView.as_view(), name="create")
]