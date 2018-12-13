# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:43'
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from fafaerapis.settings import VIDEO_UPLOAD_MAX_SIZE, VIDEO_UPLOAD_TYPE
from common.base import CommonSerializer
from common.validations import validate_fields
from .models import VideoCollection, Video, VideoCollectionDetail


class VideoCollectionSerializer(CommonSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return obj.videos.filter(is_del=0).count()

    class Meta:
        model = VideoCollection
        fields= ('id', 'name', 'desc', 'date', 'user', 'count', 'add_timestamp', 'update_timestamp')
        # exclude = ('is_del', 'add_time', 'update_time')


class VideoSerializer(CommonSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def validate_file(self, file):
        return validate_fields(file, upload_max_size=VIDEO_UPLOAD_MAX_SIZE, upload_types=VIDEO_UPLOAD_TYPE)

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

    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return obj.videos.filter(is_del=0).count()

    class Meta:
        model = VideoCollection
        fields= ('id', 'name', 'desc', 'date', 'user', 'videos', 'count', 'add_timestamp', 'update_timestamp')
        # exclude = ('is_del', 'add_time', 'update_time')
