from django.db import models
from django.contrib.auth.models import User


# 博客文章数据模型
class ArticlePost(models.Model):
    author = models.ForeignKey(User, verbose_name='文章作者', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='文章标题', max_length=100)
    body = models.TextField(verbose_name='文章正文')
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='文章更新时间', auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title
