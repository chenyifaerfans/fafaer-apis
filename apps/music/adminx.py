# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:42'

import xadmin

from .models import Singer, Album, Audio, Song, AlbumDetail, AudioDetail
from .forms import SingerAdminForm, AlbumAdminForm, SongAdminForm
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
    form = SingerAdminForm
    model_icon = 'fa fa-music'

    def queryset(self):
        qs = super(SingerAdmin, self).queryset()
        return qs.filter(is_del=0)


class AlbumAdmin(CommonAdmin):
    list_display = ['name', 'desc', 'singer', 'cover_img', 'background_img', 'get_album_songs_count', 'release_date', 'release_company', 'user']
    search_fields = ['name', 'desc', 'singer', 'release_date', 'release_company',]
    list_filter = ['name', 'singer', 'release_date']
    inlines = [AlbumDetailInline]
    form = AlbumAdminForm

    def queryset(self):
        qs = super(AlbumAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)

    def get_model_form(self, **kwargs):
        form = super(AlbumAdmin, self).get_model_form(**kwargs)
        form.base_fields['user'].initial = self.request.user
        return form


class AudioAdmin(CommonAdmin):
    list_display = ['name', 'desc', 'singer', 'get_audio_songs_count', 'user']
    search_fields = ['name', 'desc', 'singer']
    list_filter = ['name', 'desc', 'singer']
    inlines = [AudioDetailInline]

    def queryset(self):
        qs = super(AudioAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)

    def get_model_form(self, **kwargs):
        form = super(AudioAdmin, self).get_model_form(**kwargs)
        form.base_fields['user'].initial = self.request.user
        return form


class SongAdmin(CommonAdmin):
    list_display = ['name', 'desc', 'singer', 'duration', 'hits', 'user', 'file']
    search_fields = ['name', 'desc', 'singer']
    list_filter = ['name', 'desc', 'singer']
    form = SongAdminForm

    def queryset(self):
        qs = super(SongAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)

    def get_model_form(self, **kwargs):
        form = super(SongAdmin, self).get_model_form(**kwargs)
        form.base_fields['user'].initial = self.request.user
        return form


class AlbumDetailAdmin(CommonAdmin):
    list_display = ['album', 'song', 'user', 'add_time']
    search_fields = ['album', 'song']
    list_filter = ['album', 'song']

    def queryset(self):
        qs = super(AlbumDetailAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)

    def get_model_form(self, **kwargs):
        form = super(AlbumDetailAdmin, self).get_model_form(**kwargs)
        form.base_fields['user'].initial = self.request.user
        return form


class AudioDetailAdmin(CommonAdmin):
    list_display = ['audio', 'song', 'user', 'add_time']
    search_fields = ['audio', 'song']
    list_filter = ['audio', 'song']

    def queryset(self):
        qs = super(AudioDetailAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)

    def get_model_form(self, **kwargs):
        form = super(AudioDetailAdmin, self).get_model_form(**kwargs)
        form.base_fields['user'].initial = self.request.user
        return form


xadmin.site.register(Singer, SingerAdmin)
xadmin.site.register(Album, AlbumAdmin)
xadmin.site.register(Audio, AudioAdmin)
xadmin.site.register(Song, SongAdmin)
xadmin.site.register(AlbumDetail, AlbumDetailAdmin)
xadmin.site.register(AudioDetail, AudioDetailAdmin)
