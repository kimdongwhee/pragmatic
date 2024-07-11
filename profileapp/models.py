from django.contrib.auth.models import User #Django 기본 제공 User 클래스와의 일대일 관계를 위해 임포트
from django.db import models

#profileapp 에 사용할 DB 클래스
class Profile(models.Model):
    #Django 기본제공 클래스 User와 Profile > user 1:1관계 형성. Django 기본 제공 User에서의 사용자가 지워지면 해당 Profile user도 삭제됌(CASCADE).
    #관계명 related_name을 지정함으로써 view에서 손쉽게 request.user.profile 형태로 접근하도록 지정. + request.user.profile.nickname 식으로 활용가능.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to="profile/", null=True) #이미지 필드 > 이미지 저장 파일 경로 : media > profile 식으로 저장됌(media는 settings.py에서 처리)
    nickname = models.CharField(max_length=20, unique=True, null=True) #닉네임 : 유일값, 최대길이 20
    message = models.CharField(max_length=100, null=True) #메세지