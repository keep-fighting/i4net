from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    # 首页，列表页
    path('', views.index, name='index'),
]
