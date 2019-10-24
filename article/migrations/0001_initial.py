# Generated by Django 2.2.6 on 2019-10-24 21:42

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='栏目标题')),
                ('enabled', models.PositiveSmallIntegerField(choices=[(1, '启用'), (2, '禁用')], default=(1, '启用'), verbose_name='启用状态')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '文章栏目',
                'verbose_name_plural': '文章栏目',
                'db_table': 'article_column',
            },
        ),
        migrations.CreateModel(
            name='ArticlePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('digest', models.CharField(max_length=255, verbose_name='摘要')),
                ('content', ckeditor.fields.RichTextField(verbose_name='文章内容')),
                ('enabled', models.PositiveSmallIntegerField(choices=[(1, '启用'), (2, '禁用')], default=(1, '启用'), verbose_name='启用状态')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.ArticleColumn', verbose_name='文章栏目')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'article_post',
            },
        ),
    ]
