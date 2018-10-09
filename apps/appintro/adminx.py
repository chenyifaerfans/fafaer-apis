# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/8 21:11'
import xadmin

from .models import AppIntro, AppStartUpPage
from common.base import CommonAdmin


class AppIntroAdmin(CommonAdmin):
    list_display = ['title', 'desc', 'type', 'image', 'link', 'order', 'add_time']
    search_fields = ['title', 'desc', 'type', 'image']
    list_filter = ['title', 'desc', 'type', 'image', 'add_time']
    ordering = ['order', 'add_time']

    def queryset(self):
        qs = super(AppIntroAdmin, self).queryset()
        return qs.filter(type='intro', is_del=0)


class AppStartUpPageAdmin(CommonAdmin):
    list_display = ['title', 'desc', 'type', 'image', 'link', 'order', 'add_time']
    search_fields = ['title', 'desc', 'type', 'image']
    list_filter = ['title', 'desc', 'type', 'image', 'add_time']
    ordering = ['order', 'add_time']

    def queryset(self):
        qs = super(AppStartUpPageAdmin, self).queryset()
        return qs.filter(type='startup', is_del=0)


xadmin.site.register(AppIntro, AppIntroAdmin)
xadmin.site.register(AppStartUpPage, AppStartUpPageAdmin)