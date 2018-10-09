# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/8 21:11'
import xadmin

from .models import Banner, Profile, ProfileDetail, ContactDetail
from common.base import CommonAdmin


class BannerAdmin(CommonAdmin):
    list_display = ['name', 'desc', 'image', 'add_time', 'is_del']
    search_fields = ['name', 'desc', 'image']
    list_filter = ['name', 'desc', 'image', 'add_time']
    ordering = ['order', 'add_time']
    # readonly_fields = ['is_del']

    def queryset(self):
        qs = super(BannerAdmin, self).queryset()
        return qs.filter(is_del=0)


class ProfileAdmin(CommonAdmin):
    list_display = ['name', 'desc', 'avatar', 'add_time']
    search_fields = ['name', 'desc', 'avatar']
    list_filter = ['name', 'desc', 'avatar', 'add_time']

    def queryset(self):
        qs = super(ProfileAdmin, self).queryset()
        return qs.filter(is_del=0)


class ProfileDetailAdmin(CommonAdmin):
    list_display = ['title', 'content', 'type', 'image', 'order', 'add_time']
    search_fields = ['title', 'content', 'type', 'image']
    list_filter = ['title', 'content', 'type', 'image', 'add_time']
    ordering = ['order', 'add_time']

    def queryset(self):
        qs = super(ProfileDetailAdmin, self).queryset()
        return qs.filter(type='profile', is_del=0)


class ContactDetailAdmin(CommonAdmin):
    list_display = ['title', 'content', 'type', 'image', 'order', 'add_time']
    search_fields = ['title', 'content', 'type', 'image']
    list_filter = ['title', 'content', 'type', 'image', 'add_time']
    ordering = ['order', 'add_time']

    def queryset(self):
        qs = super(ContactDetailAdmin, self).queryset()
        return qs.filter(type='contact', is_del=0)


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Profile, ProfileAdmin)
xadmin.site.register(ProfileDetail, ProfileDetailAdmin)
xadmin.site.register(ContactDetail, ContactDetailAdmin)