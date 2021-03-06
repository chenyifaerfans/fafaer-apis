# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:43'
import django_filters

from .models import Gallery


class GalleryFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='相册name 模糊查询',
                                            help_text='相册name 模糊查询')

    desc = django_filters.CharFilter(field_name='desc', lookup_expr='icontains', label='相册描述 模糊查询',
                                       help_text='相册描述 模糊查询')

    class Meta:
        model = Gallery
        fields = ('name', 'desc')