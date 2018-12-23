# _*_ coding:utf-8 _*_
import uuid
from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

from common.choices import GENDER_CHOICES, IS_DEL_CHOICES

User = get_user_model()


class Singer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    nickname = models.CharField(max_length=20, verbose_name="昵称")
    desc = models.CharField(max_length=100, verbose_name=u"描述")
    avatar = models.ImageField(upload_to="music/singer/avatar/%Y/%m", max_length=100, verbose_name='歌手头像')
    background_img = models.ImageField(upload_to="music/singer/background/%Y/%m", max_length=100, verbose_name='背景图片')
    birthday = models.DateField(null=True, blank=True, verbose_name=u"生日")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6, default="female", verbose_name=u"性别")
    address = models.CharField(max_length=100, default=u"", verbose_name=u"地址")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = "歌手"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class Album(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    name = models.CharField(max_length=20, verbose_name="专辑名")
    desc = models.CharField(max_length=100, verbose_name=u"描述")
    singer = models.ForeignKey(Singer, verbose_name='歌手')
    cover_img = models.ImageField(upload_to="music/album/cover/%Y/%m", max_length=100, verbose_name='专辑页面')
    background_img = models.ImageField(upload_to="music/album/background/%Y/%m", max_length=100, verbose_name='专辑背景图片')
    release_date = models.DateField(default=datetime.now, verbose_name='发行时间')
    release_company = models.CharField(default='', max_length=30, verbose_name='发行公司')
    user = models.ForeignKey(User, verbose_name=u"创建用户")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = "专辑"
        verbose_name_plural = verbose_name

    def get_album_songs_count(self):
        return self.songs.filter(is_del=0).count()

    get_album_songs_count.short_description = '歌曲数量'

    def __str__(self):
        return self.name


class Audio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    name = models.CharField(max_length=20, verbose_name="电台名")
    desc = models.CharField(max_length=100, verbose_name=u"描述")
    singer = models.ForeignKey(Singer, verbose_name='歌手')
    cover_img = models.ImageField(upload_to="music/audio/cover/%Y/%m", max_length=100, verbose_name='电台页面')
    background_img = models.ImageField(upload_to="music/audio/background/%Y/%m", max_length=100, verbose_name='电台背景图片')
    release_date = models.DateField(default=datetime.now, verbose_name='发行时间')
    user = models.ForeignKey(User, verbose_name=u"创建用户")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = "电台"
        verbose_name_plural = verbose_name

    def get_audio_songs_count(self):
        return self.songs.filter(is_del=0).count()

    get_audio_songs_count.short_description = '电台歌曲数量'

    def __str__(self):
        return self.name


class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    name = models.CharField(max_length=20, verbose_name=u"歌名")
    desc = models.CharField(max_length=100, verbose_name=u"描述")
    singer = models.ForeignKey(Singer, verbose_name=u'歌手')
    duration = models.DecimalField(max_digits=6, decimal_places=3, default=0, verbose_name=u"歌曲时长")
    hits = models.IntegerField(default=0, verbose_name=u"播放量")
    file = models.FileField(upload_to="music/song/%Y/%m", verbose_name=u"歌曲文件")
    user = models.ForeignKey(User, verbose_name=u"创建用户")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = u"歌曲"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class AlbumDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    album = models.ForeignKey(Album, related_name='songs', verbose_name=u'专辑')
    song = models.ForeignKey(Song, verbose_name=u'歌曲')
    user = models.ForeignKey(User, verbose_name=u"创建用户")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = u"专辑详情页"
        verbose_name_plural = verbose_name
        unique_together = ("album", "song")

    def __str__(self):
        return self.album.name


class AudioDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    audio = models.ForeignKey(Audio, related_name='songs', verbose_name=u'电台')
    song = models.ForeignKey(Song, verbose_name=u'歌曲')
    user = models.ForeignKey(User, verbose_name=u"创建用户")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = u"电台详情页"
        verbose_name_plural = verbose_name
        unique_together = ("audio", "song")

    def __str__(self):
        return self.audio.name
