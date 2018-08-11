# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:42'

import xadmin

from .models import Singer, Album, Audio, Song, AlbumDetail, AudioDetail
from common.base import CommonAdmin


class AlbumDetailInline(object):
    model = AlbumDetail
    extra = 0


class AudioDetailInline(object):
    model = AudioDetail
    extra = 0


class SingerAdmin(CommonAdmin):
    list_display = ['nickname', 'desc', 'avatar', 'background_img', 'birthday', 'gender', 'address']
    search_fields = ['nickname', 'desc', 'avatar', 'address']
    list_filter = ['nickname', 'desc', 'avatar', 'background_img']

    def queryset(self):
        qs = super(SingerAdmin, self).queryset()
        return qs.filter(is_del=0)


class AlbumAdmin(CommonAdmin):
    list_display = ['name', 'desc', 'singer', 'cover_img', 'bg_img', 'release_date', 'release_company', 'user']
    search_fields = ['name', 'desc', 'singer', 'release_date', 'release_company',]
    list_filter = ['name', 'singer', 'release_date']
    inlines = [AlbumDetailInline]

    def queryset(self):
        qs = super(AlbumAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)


class AudioAdmin(CommonAdmin):
    list_display = ['name', 'desc', 'singer', 'user']
    search_fields = ['name', 'desc', 'singer']
    list_filter = ['name', 'desc', 'singer']
    inlines = [AudioDetailInline]

    def queryset(self):
        qs = super(AudioAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)


class SongAdmin(CommonAdmin):
    list_display = ['name', 'desc', 'singer', 'album', 'audio', 'duration', 'hits', 'user', 'file']
    search_fields = ['name', 'desc', 'singer']
    list_filter = ['name', 'desc', 'singer']

    def queryset(self):
        qs = super(SongAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)


class AlbumDetailAdmin(CommonAdmin):
    list_display = ['album', 'song', 'user', 'add_time']
    search_fields = ['album', 'song']
    list_filter = ['album', 'song']

    def queryset(self):
        qs = super(AlbumDetailAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)


class AudioDetailAdmin(CommonAdmin):
    list_display = ['audio', 'song', 'user', 'add_time']
    search_fields = ['audio', 'song']
    list_filter = ['audio', 'song']

    def queryset(self):
        qs = super(AudioDetailAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)


xadmin.site.register(Singer, SingerAdmin)
xadmin.site.register(Album, AlbumAdmin)
xadmin.site.register(Audio, AudioAdmin)
xadmin.site.register(Song, SongAdmin)
xadmin.site.register(AlbumDetail, AlbumDetailAdmin)
xadmin.site.register(AudioDetail, AudioDetailAdmin)
