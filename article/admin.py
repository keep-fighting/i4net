from django.contrib import admin
from .models import ArticleColumn, ArticlePost


@admin.register(ArticleColumn)
class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'enabled', 'created', 'updated']
    list_display_links = ['id', 'title']


@admin.register(ArticlePost)
class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ['id', 'column', 'title', 'enabled', 'created', 'updated']
    list_display_links = ['id', 'column', 'title']


admin.site.site_title = "个人数据分享"
admin.site.site_header = "个人数据分享后台管理"
