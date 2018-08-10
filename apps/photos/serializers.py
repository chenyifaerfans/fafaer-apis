# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:43'
from rest_framework import serializers

from .models import Gallery, Photo, GalleryDetail


class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        exclude = ('is_del',)


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        exclude = ('is_del',)


class GalleryDetailSerializer(serializers.ModelSerializer):
    gallery = GallerySerializer(many=False)
    photo = PhotoSerializer(many=False)

    class Meta:
        model = GalleryDetail
        exclude = ('is_del',)


class GalleryListDetailSerializer(serializers.ModelSerializer):
    photos = GalleryDetailSerializer(many=True)

    class Meta:
        model = Gallery
        exclude = ('is_del',)
