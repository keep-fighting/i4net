from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'article'
urlpatterns = [
    # 文章列表页视图
    path('', views.ArticleListView.as_view(), name='index'),
    path('list/', views.ArticleListView.as_view(), name='list'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
]
