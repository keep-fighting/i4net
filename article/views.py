from django.views import generic
from .models import ArticlePost


# 文章列表
class ArticleListView(generic.ListView):
    template_name = 'article/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        qs = ArticlePost.objects.filter(enabled=1, column__enabled=1)
        return qs


# 文章详情
class ArticleDetailView(generic.DetailView):
    template_name = 'article/detail.html'
    model = ArticlePost
