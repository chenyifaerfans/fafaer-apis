# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/8 22:32'
import django_filters

from .models import AppIntro


class AppIntroFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = AppIntro
        fields = ['type']