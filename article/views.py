from django.views import generic

from .models import ArticlePost, ArticleColumn


class ArticleContextMixin:
    article_columns = ArticleColumn.objects.filter(enabled=1)
    extra_context = {'article_columns': article_columns}


# 文章列表
class ArticleListView(ArticleContextMixin, generic.ListView):
    template_name = 'article/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        qs = ArticlePost.objects.filter(enabled=1, column__enabled=1)
        return qs


# 文章详情
class ArticleDetailView(generic.DetailView):
    template_name = 'article/detail.html'
    model = ArticlePost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        column = self.get_object().column
        context['article_list'] = ArticlePost.objects.filter(column=column, enabled=1)
        return context
