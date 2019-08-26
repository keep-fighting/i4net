import markdown
from django.views import generic
from .models import ArticlePost


# 文章列表
class ArticleListView(generic.ListView):
    model = ArticlePost
    paginate_by = 20


# 文章详情
class ArticleDetailView(generic.DetailView):
    model = ArticlePost

    def get_object(self, queryset=None):
        article = super().get_object()
        article.body = markdown.markdown(
            article.body,
            extensions=[
                # 包含 缩写、表格等常用扩展
                'markdown.extensions.extra',
                # 语法高亮扩展
                'markdown.extensions.codehilite',
            ])
        return article
