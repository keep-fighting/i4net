from django.views import generic
from .models import ArticlePost


# 文章列表
class ArticleListView(generic.ListView):
    template_name = 'article/list.html'
    model = ArticlePost
    context_object_name = 'articles'


# 文章详情
class ArticleDetailView(generic.DetailView):
    template_name = 'article/detail.html'
    model = ArticlePost
    context_object_name = 'article'
