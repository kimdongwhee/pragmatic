from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import hello_world, AccountCreateView

#앱네임 지정
#ex) 127.0.0.1/account/hello_world/ = accountapp:hello_world
app_name = "accountapp"

urlpatterns = [
    path("hello_world/", hello_world, name="hello_world"),
    # 장고 기본제공 LoginView, LogoutView는 views.py를 별도 지정안해도됌 
    # (1)로그인뷰는 템플릿을 별도 설정해야함
    path("login/", LoginView.as_view(template_name="accountapp/login.html"), name="login"),
    # (2)로그아웃 뷰
    path("logout/", LogoutView.as_view(), name="logout"),
    # CBV를 지정할때는 CBV.as_view()로 지정
    path("create/", AccountCreateView.as_view(), name="create")
]