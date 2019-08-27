import markdown
from django.views import generic
from .models import ArticlePost
from django.db.models import Q
from comment.models import Comment


# 文章列表
class ArticleListView(generic.ListView):
    paginate_by = 20

    def get_queryset(self):
        search = self.request.GET.get('search')
        order = self.request.GET.get('order')
        object_list = ArticlePost.objects.all()
        if search:
            object_list = object_list.filter(Q(title__icontains=search) | Q(body__icontains=search))

        if order == 'total_views':
            object_list = object_list.order_by('-total_views')
        #
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.request.GET)
        return context


# 文章详情
class ArticleDetailView(generic.DetailView):
    model = ArticlePost
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )

    def get_object(self, queryset=None):
        article = super().get_object()
        article.total_views += 1
        article.save(update_fields=['total_views'])
        article.body = self.md.convert(article.body)
        return article

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['toc'] = self.md.toc
        context['comments'] = Comment.objects.filter(article=self.object)
        return context
