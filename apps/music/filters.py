# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:43'

import django_filters

from .models import Album, Audio


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
