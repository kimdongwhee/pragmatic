from django.conf import settings #이미지/영상 호출을위해
from django.conf.urls.static import static #이미지/영상 호출을위해
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accountapp.urls")),
    path("profiles/", include("profileapp.urls")),
    path("articles/", include("articleapp.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)