from django.contrib import admin
from .models import ArticlePost


@admin.register(ArticlePost)
class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'created', 'updated']
    list_display_links = ['id', 'author', 'title']
