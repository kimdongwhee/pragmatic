from django.contrib import admin
# app > model 클래스 호출
from .models import HelloWorld
# admin 페이지에 등록할 model 클래스 등록
admin.site.register(HelloWorld)