from django.urls import path
from accountapp.views import hello_world

#앱네임 지정
#ex) 127.0.0.1/account/hello_world/ = accountapp:hello_world
app_name = "accountapp"

urlpatterns = [
    path("hello_world/", hello_world, name="hello_world")
]