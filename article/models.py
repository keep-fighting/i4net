from django.db import models
from ckeditor.fields import RichTextField

# 状态选项
from django.utils.safestring import mark_safe

STATUS_CHOICES = ((1, '启用'), (2, '禁用'),)


class ArticleColumn(models.Model):
    title = models.CharField('栏目标题', max_length=100)
    enabled = models.PositiveSmallIntegerField('启用状态', choices=STATUS_CHOICES, default=STATUS_CHOICES[0])
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'article_column'
        verbose_name = '文章栏目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ArticlePost(models.Model):
    column = models.ForeignKey(ArticleColumn, verbose_name='文章栏目', on_delete=models.CASCADE)
    title = models.CharField('文章标题', max_length=100)
    digest = models.CharField('摘要', max_length=255)
    content = RichTextField(verbose_name='文章内容')
    enabled = models.PositiveSmallIntegerField('启用状态', choices=STATUS_CHOICES, default=STATUS_CHOICES[0])
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'article_post'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_full_title(self):
        return f"{self.column.title} - {self.title}"
