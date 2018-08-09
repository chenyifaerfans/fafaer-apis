# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:43'

from rest_framework import serializers

from .models import Singer, Album, Audio, Song, AlbumDetail, AudioDetail


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        exclude = ('is_del',)


class AlbumSerializer(serializers.ModelSerializer):
    singer = SingerSerializer()

    class Meta:
        model = Album
        exclude = ('is_del',)


class AudioSerializer(serializers.ModelSerializer):
    singer = SingerSerializer()

    class Meta:
        model = Audio
        exclude = ('is_del',)


class SongSerializer(serializers.ModelSerializer):
    singer = SingerSerializer()

    class Meta:
        model = Song
        # fields = ('name', 'desc', 'singer', 'duration', 'hits', 'file', 'add_time')
        exclude = ('is_del',)


class AlbumDetailSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(many=False)
    song = SongSerializer(many=False)

    class Meta:
        model = AlbumDetail
        exclude = ('id', 'add_time', 'update_time', 'is_del')


class AlbumListDetailSerializer(serializers.ModelSerializer):
    songs = AlbumDetailSerializer(many=True)

    class Meta:
        model = Album
        exclude = ('is_del',)


class AudioDetailSerializer(serializers.ModelSerializer):
    audio = AudioSerializer(many=False)
    song = SongSerializer(many=False)

    class Meta:
        model = AudioDetail
        exclude = ('is_del',)


class AudioListDetailSerializer(serializers.ModelSerializer):
    songs = AudioDetailSerializer(many=True)

    class Meta:
        model = Audio
        exclude = ('is_del',)