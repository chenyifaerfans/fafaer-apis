# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:43'
import django_filters

from .models import VideoCollection, VideoCollectionDetail


class VideoCollectionFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='视频合集name 模糊查询',
                                            help_text='视频合集name 模糊查询')

    desc = django_filters.CharFilter(field_name='desc', lookup_expr='icontains', label='视频合集描述 模糊查询',
                                       help_text='视频合集描述 模糊查询')

    class Meta:
        model = VideoCollection
        fields = ('name', 'desc')


class VideoCollectionDetailFilter(django_filters.rest_framework.FilterSet):
    videocollection_id = django_filters.UUIDFilter(field_name='video_collection__id', lookup_expr='exact', label='视频集id 精准查询',
                                           help_text='视频集id 精准查询')

    class Meta:
        model = VideoCollectionDetail
        fields = ('videocollection_id',)