# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:43'
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from common.base import CommonSerializer
from .models import VideoCollection, Video, VideoCollectionDetail


class VideoCollectionSerializer(CommonSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = VideoCollection
        exclude = ('is_del', 'add_time', 'update_time')


class VideoSerializer(CommonSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Video
        exclude = ('is_del', 'add_time', 'update_time')


class VideoCollectionDetailSerializer(CommonSerializer):
    video_collection = VideoCollectionSerializer(many=False)
    video = VideoSerializer(many=False)

    class Meta:
        model = VideoCollectionDetail
        exclude = ('is_del', 'add_time', 'update_time')


class VideoCollectionDetail2Serializer(CommonSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = VideoCollectionDetail
        validators = [
            UniqueTogetherValidator(
                queryset=VideoCollectionDetail.objects.filter(is_del=0),
                fields=('video_collection', 'video'),
                message="已添加到该合辑中"
            )
        ]
        exclude = ('is_del', 'add_time', 'update_time')


class VideoCollectionListDetailSerializer(CommonSerializer):
    videos = VideoCollectionDetailSerializer(many=True)

    class Meta:
        model = VideoCollection
        exclude = ('is_del', 'add_time', 'update_time')
