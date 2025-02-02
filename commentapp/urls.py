from django.urls import path
from .views import CommentCreateView, CommentDeleteView

app_name = "comment_app"
urlpatterns = [
    path("create/", CommentCreateView.as_view(), name="create"),
    path("delete/<int:pk>", CommentDeleteView.as_view(), name="delete")
]