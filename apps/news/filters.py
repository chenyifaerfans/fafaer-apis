# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/9/8 17:00'
import django_filters

from .models import Article


class ArticleFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='文章名称 模糊查询', help_text='文章名称 模糊查询')

    class Meta:
        model = Article
        fields = ('title', )