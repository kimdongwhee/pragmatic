from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.views.generic.edit import DeleteView, FormMixin

from commentapp.forms import CommentCreationForm
from .decorators import article_ownership_required
from .models import Article
from .forms import ArticleCreationForm

@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = "articleapp/create.html"

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("article_app:detail", kwargs={"pk": self.object.pk})

#댓글 등록 기능 추가 전
# class ArticleDetailView(DetailView):
#     model = Article
#     context_object_name = "target_article"
#     template_name = "articleapp/detail.html"

#댓글 등록 기능 추가 후 : FormMixin을 활용하여 다중 상속
class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class  = CommentCreationForm
    context_object_name = "target_article"
    template_name = "articleapp/detail.html"

@method_decorator(article_ownership_required, "get")
@method_decorator(article_ownership_required, "post")
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = "target_article"
    template_name = "articleapp/update.html"

    def get_success_url(self):
        return reverse("article_app:detail", kwargs={"pk": self.object.pk})

@method_decorator(article_ownership_required, "get")
@method_decorator(article_ownership_required, "post")
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = "target_article"
    template_name = "articleapp/delete.html"
    success_url = reverse_lazy("article_app:list")

class ArticleListView(ListView):
    model = Article
    context_object_name = "article_list"  # 수정: 템플릿에서 사용할 변수명을 지정
    paginate_by = 10
    template_name = "articleapp/list.html"
