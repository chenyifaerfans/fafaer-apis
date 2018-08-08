# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/8 22:32'
import django_filters

from .models import ProfileDetail


class ProfileFilter(django_filters.rest_framework.FilterSet):
    pass


class ProfileDetailFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = ProfileDetail
        fields = ['type']