from django.shortcuts import render
from django.views import generic
from .models import ArticlePost


class ArticleListView(generic.ListView):
    template_name = 'article/list.html'
    model = ArticlePost
    context_object_name = 'articles'
