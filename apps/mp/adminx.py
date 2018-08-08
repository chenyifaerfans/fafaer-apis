# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/8 21:11'

import xadmin

from .models import Banner, Profile, ProfileDetail, ContactDetail


class BannerAdmin(object):
    list_display = ['name', 'desc', 'image', 'add_time']
    search_fields = ['name', 'desc', 'image']
    list_filter = ['name', 'desc', 'image', 'add_time']


class ProfileAdmin(object):
    list_display = ['name', 'desc', 'avatar', 'add_time']
    search_fields = ['name', 'desc', 'avatar']
    list_filter = ['name', 'desc', 'avatar', 'add_time']


class ProfileDetailAdmin(object):
    list_display = ['title', 'content', 'type', 'image', 'order', 'add_time']
    search_fields = ['title', 'content', 'type', 'image']
    list_filter = ['title', 'content', 'type', 'image', 'add_time']

    def queryset(self):
        qs = super(ProfileDetailAdmin, self).queryset()
        return qs.filter(type='profile')


class ContactDetailAdmin(object):
    list_display = ['title', 'content', 'type', 'image', 'order', 'add_time']
    search_fields = ['title', 'content', 'type', 'image']
    list_filter = ['title', 'content', 'type', 'image', 'add_time']

    def queryset(self):
        qs = super(ContactDetailAdmin, self).queryset()
        return qs.filter(type='contact')


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Profile, ProfileAdmin)
xadmin.site.register(ProfileDetail, ProfileDetailAdmin)
xadmin.site.register(ContactDetail, ContactDetailAdmin)