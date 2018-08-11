# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:43'
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Gallery, Photo, GalleryDetail
from common.base import CommonSerializer


class GallerySerializer(CommonSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Gallery
        exclude = ('is_del', 'add_time', 'update_time')


class PhotoSerializer(CommonSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

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

    class Meta:
        model = Gallery
        exclude = ('is_del', 'add_time', 'update_time')
