from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'article'
urlpatterns = [
    # 文章列表页视图
    path('article-list/', views.ArticleListView.as_view(), name='article_list'),
    # 文章详情页视图
    path('article-detail/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
]
