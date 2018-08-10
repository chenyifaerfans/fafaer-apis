# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:43'
from rest_framework.validators import UniqueTogetherValidator

from .models import Singer, Album, Audio, Song, AlbumDetail, AudioDetail
from common.base import CommonSerializer


class SingerSerializer(CommonSerializer):
    class Meta:
        model = Singer
        exclude = ('is_del', 'add_time', 'update_time')


class AlbumSerializer(CommonSerializer):
    singer = SingerSerializer()

    class Meta:
        model = Album
        exclude = ('is_del', 'add_time', 'update_time')


class AudioSerializer(CommonSerializer):
    singer = SingerSerializer()

    class Meta:
        model = Audio
        exclude = ('is_del', 'add_time', 'update_time')


class SongSerializer(CommonSerializer):
    singer = SingerSerializer()

    class Meta:
        model = Song
        # fields = ('name', 'desc', 'singer', 'duration', 'hits', 'file', 'add_time')
        exclude = ('is_del', 'add_time', 'update_time')


class AlbumDetailSerializer(CommonSerializer):
    album = AlbumSerializer(many=False)
    song = SongSerializer(many=False)

    class Meta:
        model = AlbumDetail
        validators = [
            UniqueTogetherValidator(
                queryset=AlbumDetail.objects.filter(is_del=0),
                fields=('album', 'song'),
                message="已添加到该专辑中"
            )
        ]
        exclude = ('id', 'add_time', 'update_time', 'is_del')


class AlbumListDetailSerializer(CommonSerializer):
    songs = AlbumDetailSerializer(many=True)

    class Meta:
        model = Album
        exclude = ('is_del', 'add_time', 'update_time')


class AudioDetailSerializer(CommonSerializer):
    audio = AudioSerializer(many=False)
    song = SongSerializer(many=False)

    class Meta:
        model = AudioDetail
        validators = [
            UniqueTogetherValidator(
                queryset=AudioDetail.objects.filter(is_del=0),
                fields=('audio', 'song'),
                message="已添加到该电台列表中"
            )
        ]
        exclude = ('is_del', 'add_time', 'update_time')


class AudioListDetailSerializer(CommonSerializer):
    songs = AudioDetailSerializer(many=True)

    class Meta:
        model = Audio
        exclude = ('is_del', 'add_time', 'update_time')