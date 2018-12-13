# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:43'
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from fafaerapis.settings import IMAGE_UPLOAD_MAX_SIZE, IMAGE_UPLOAD_TYPE
from .models import Gallery, Photo, GalleryDetail
from common.base import CommonSerializer
from common.validations import validate_fields


class GallerySerializer(CommonSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return obj.photos.filter(is_del=0).count()

    class Meta:
        model = Gallery
        fields= ('id', 'name', 'desc', 'date', 'user', 'count', 'add_timestamp', 'update_timestamp')
        # exclude = ('is_del', 'add_time', 'update_time')


class PhotoSerializer(CommonSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def validate_file(self, file):
        return validate_fields(file, upload_max_size=IMAGE_UPLOAD_MAX_SIZE, upload_types=IMAGE_UPLOAD_TYPE)

    class Meta:
        model = Photo
        exclude = ('is_del', 'add_time', 'update_time')


class GalleryDetailSerializer(CommonSerializer):
    gallery = GallerySerializer(many=False)
    photo = PhotoSerializer(many=False)

    class Meta:
        model = GalleryDetail
        exclude = ('is_del', 'add_time', 'update_time')


class GalleryDetail2Serializer(CommonSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = GalleryDetail
        validators = [
            UniqueTogetherValidator(
                queryset=GalleryDetail.objects.filter(is_del=0),
                fields=('gallery', 'photo'),
                message="已添加到该相册中"
            )
        ]
        exclude = ('is_del', 'add_time', 'update_time')


class GalleryListDetailSerializer(CommonSerializer):
    photos = GalleryDetailSerializer(many=True)
    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return obj.photos.filter(is_del=0).count()

    class Meta:
        model = Gallery
        fields= ('id', 'name', 'desc', 'date', 'user', 'photos', 'count', 'add_timestamp', 'update_timestamp')
        # exclude = ('is_del', 'add_time', 'update_time')
