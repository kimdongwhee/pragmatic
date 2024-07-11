from django.urls import path
from .views import ProfileCreate, ProfileUpdate

#profileapp의 app네입 설정
app_name = "profile_app"

urlpatterns = [
    path("create/", ProfileCreate.as_view(), name="create"),
    #특정 프로필에 대한 수정이므로 url에 pk 지정
    path("update/<int:pk>/", ProfileUpdate.as_view(), name="update")
]