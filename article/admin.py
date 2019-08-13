from django.contrib import admin
from .models import Column, Article


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ['id', 'column', 'enabled', 'created', 'updated']
    list_display_links = ['id', 'column']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'column', 'author', 'title', 'total_views', 'created', 'updated']
    list_display_links = ['id', 'column', 'author', 'title']
