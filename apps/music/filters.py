# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:43'

import django_filters

from .models import Singer, Album, Audio, Song, AlbumDetail, AudioDetail


class SingerFilter(django_filters.rest_framework.FilterSet):
    nickname = django_filters.CharFilter(field_name='nickname', lookup_expr='icontains', label='歌手名称 模糊查询',
                                     help_text='歌手名称 模糊查询')

    desc = django_filters.CharFilter(field_name='desc', lookup_expr='icontains', label='歌手描述 模糊查询',
                                     help_text='歌手描述 模糊查询')

    class Meta:
        model = Singer
        fields = ('nickname', 'desc')


class AlbumFilter(django_filters.rest_framework.FilterSet):
    singer_id = django_filters.NumberFilter(field_name='singer__id', lookup_expr='exact', label='歌手id =',
                                            help_text='歌手id')

    class Meta:
        model = Album
        fields = ('singer_id',)


class AudioFilter(django_filters.rest_framework.FilterSet):
    singer_id = django_filters.NumberFilter(field_name='singer__id', lookup_expr='exact', label='歌手id =',
                                            help_text='歌手id')

    class Meta:
        model = Audio
        fields = ('singer_id',)


class SongFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='歌曲名称 模糊查询',
                                     help_text='歌曲名称 模糊查询')

    desc = django_filters.CharFilter(field_name='desc', lookup_expr='icontains', label='歌曲描述 模糊查询',
                                     help_text='歌曲描述 模糊查询')

    class Meta:
        model = Song
        fields = ('name', 'desc')


class AlbumDetailFilter(django_filters.rest_framework.FilterSet):
    album_id = django_filters.UUIDFilter(field_name='album__id', lookup_expr='exact', label='专辑id 精准查询',
                                           help_text='专辑id 精准查询')

    class Meta:
        model = AlbumDetail
        fields = ('album_id',)


class AudioDetailFilter(django_filters.rest_framework.FilterSet):
    audio_id = django_filters.UUIDFilter(field_name='audio__id', lookup_expr='exact', label='电台id 精准查询',
                                           help_text='电台id 精准查询')

    class Meta:
        model = AudioDetail
        fields = ('audio_id',)
