from django.db import models
from django.contrib.auth.models import User


# 文章栏目
class Column(models.Model):
    column = models.CharField(verbose_name='栏目名称', max_length=100)
    enabled = models.BooleanField(verbose_name='栏目是否可用', default=True)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = '文章栏目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.column


# 文章类
class Article(models.Model):
    column = models.ForeignKey(Column, verbose_name='文章栏目', on_delete=models.CASCADE, default=1)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE, default=1)
    title = models.CharField(verbose_name='文章标题', max_length=100)
    body = models.TextField(verbose_name='文章内容')
    total_views = models.PositiveIntegerField(verbose_name='浏览量', default=0)
    enabled = models.BooleanField(verbose_name='分类是否可用', default=True)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
