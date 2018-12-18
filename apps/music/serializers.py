# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:43'
import datetime
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from fafaerapis.settings import IMAGE_UPLOAD_MAX_SIZE, IMAGE_UPLOAD_TYPE, MUSIC_UPLOAD_MAX_SIZE, MUSIC_UPLOAD_TYPE
from .models import Singer, Album, Audio, Song, AlbumDetail, AudioDetail
from common.base import CommonSerializer
from common.validations import validate_fields


class SingerSerializer(CommonSerializer):

    def validate_avatar(self, avatar):
        return validate_fields(avatar, upload_max_size=IMAGE_UPLOAD_MAX_SIZE, upload_types=IMAGE_UPLOAD_TYPE)

    def validate_background_img(self, background_img):
        return validate_fields(background_img, upload_max_size=IMAGE_UPLOAD_MAX_SIZE, upload_types=IMAGE_UPLOAD_TYPE)

    class Meta:
        model = Singer
        exclude = ('is_del', 'add_time', 'update_time')


class AlbumSerializer(CommonSerializer):
    singer = SingerSerializer()

    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return obj.songs.filter(is_del=0).count()

    class Meta:
        model = Album
        fields= ('id', "name", 'desc', 'singer', 'cover_img', 'background_img', 'release_date', 'release_company',
                 'user', 'count', 'add_timestamp', 'update_timestamp')
        # exclude = ('is_del', 'add_time', 'update_time')


class Album2Serializer(CommonSerializer):
    name = serializers.CharField(required=True, max_length=20, error_messages={
        "blank": "请输入专辑名",
        "required": "请输入专辑名",
        "max_length": "专辑名长度不能超过20"
    }, label="专辑名", help_text="专辑名")
    desc = serializers.CharField(required=True, max_length=100, error_messages={
        "blank": "请输入专辑描述",
        "required": "请输入专辑描述",
        "max_length": "专辑描述长度不能超过20"
    }, label="专辑描述", help_text="专辑描述")
    cover_img = serializers.ImageField(required=True, max_length=100, error_messages={
        "blank": "请输入专辑封面",
        "required": "请输入专辑封面",
        "max_length": "专辑封面长度不能超过100"
    }, label='专辑封面', help_text='专辑封面')
    background_img = serializers.ImageField(required=True, error_messages={
        "blank": "专辑背景图片不能为空",
        "required": "专辑背景图片不能为空",
        "max_length": "专辑背景图片长度不能超过100"
    }, max_length=100, label='专辑背景图片',
                                    help_text='专辑背景图片')
    release_date = serializers.DateField(required=True, initial=datetime.date.today, error_messages={
        "blank": "请输入专辑发行时间",
        "required": "请输入专辑发行时间"
    }, format="YYYY-MM-DD", label='专辑发行时间', help_text='专辑发行时间')
    release_company = serializers.CharField(required=True, max_length=30, error_messages={
        "blank": "请输入专辑发行公司",
        "required": "请输入专辑发行公司",
        "max_length": "专辑发行公司长度不能超过30"
    }, label='发行公司', help_text='发行公司')
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def validate_cover_img(self, cover_img):
        return validate_fields(cover_img, upload_max_size=IMAGE_UPLOAD_MAX_SIZE, upload_types=IMAGE_UPLOAD_TYPE)

    def validate_background_img(self, background_img):
        return validate_fields(background_img, upload_max_size=IMAGE_UPLOAD_MAX_SIZE, upload_types=IMAGE_UPLOAD_TYPE)

    class Meta:
        model = Album
        exclude = ('is_del', 'add_time', 'update_time')


class AudioSerializer(CommonSerializer):
    singer = SingerSerializer()

    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return obj.songs.filter(is_del=0).count()

    class Meta:
        model = Audio
        fields= ('id', 'name', 'desc', 'singer', 'user', 'count', 'add_timestamp', 'update_timestamp')
        # exclude = ('is_del', 'add_time', 'update_time')


class Audio2Serializer(CommonSerializer):
    name = serializers.CharField(required=True, max_length=20, label="电台名", help_text="电台名")
    desc = serializers.CharField(required=True, max_length=100, label="电台描述", help_text="电台描述")
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Audio
        exclude = ('is_del', 'add_time', 'update_time')


class SongSerializer(CommonSerializer):
    singer = SingerSerializer()
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Song
        exclude = ('is_del', 'add_time', 'update_time')


class Song2Serializer(CommonSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def validate_file(self, file):
        return validate_fields(file, upload_max_size=MUSIC_UPLOAD_MAX_SIZE, upload_types=MUSIC_UPLOAD_TYPE)

    class Meta:
        model = Song
        exclude = ('is_del', 'add_time', 'update_time')


class AlbumDetailSerializer(CommonSerializer):
    album = AlbumSerializer(many=False)
    song = SongSerializer(many=False)

    class Meta:
        model = AlbumDetail
        exclude = ('id', 'add_time', 'update_time', 'is_del')


class AlbumDetail2Serializer(CommonSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

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

    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return obj.songs.filter(is_del=0).count()

    class Meta:
        model = Album
        fields= ('id', "name", 'desc', 'singer', 'cover_img', 'background_img', 'release_date', 'release_company',
                 'user', 'songs', 'count', 'add_timestamp', 'update_timestamp')
        # exclude = ('is_del', 'add_time', 'update_time')


class AudioDetailSerializer(CommonSerializer):
    audio = AudioSerializer(many=False)
    song = SongSerializer(many=False)

    class Meta:
        model = AudioDetail
        exclude = ('is_del', 'add_time', 'update_time')


class AudioDetail2Serializer(CommonSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

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

    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return obj.songs.filter(is_del=0).count()

    class Meta:
        model = Audio
        fields= ('id', 'name', 'desc', 'singer', 'user', 'songs', 'count', 'add_timestamp', 'update_timestamp')
        # exclude = ('is_del', 'add_time', 'update_time')
