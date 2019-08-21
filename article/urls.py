from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'article'
urlpatterns = [
    # path函数将url映射到视图
    path('article-list/', views.ArticleListView.as_view(), name='article_list'),

]
