#장고 기본제공 뷰
from django.urls import path
from django.views.generic import TemplateView
from articleapp.views import ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = "article_app"

urlpatterns =[
    path("list/", TemplateView.as_view(template_name="articleapp/list.html"), name="list"),
    path("create/", ArticleCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", ArticleDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", ArticleUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", ArticleDeleteView.as_view(), name="delete")
]