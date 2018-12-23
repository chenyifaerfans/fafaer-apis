import uuid
from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

from common.choices import IS_DEL_CHOICES

User = get_user_model()


class VideoCollection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    name = models.CharField(max_length=30, unique=True, verbose_name="视频合集名")
    desc = models.CharField(max_length=100, verbose_name=u"描述")
    date = models.DateField(default=datetime.now, verbose_name=u'日期')
    cover_img = models.ImageField(upload_to="video/collection/cover/%Y/%m", max_length=100, verbose_name='视频集图片')
    background_img = models.ImageField(upload_to="video/collection/background/%Y/%m",
                                       max_length=100, verbose_name='视频集背景图片')
    user = models.ForeignKey(User, verbose_name=u"创建用户")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = '视频合集'
        verbose_name_plural = verbose_name

    def get_videos_count(self):
        return self.videos.filter(is_del=0).count()

    get_videos_count.short_description = '视频数量'

    def __str__(self):
        return self.name


class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    name = models.CharField(max_length=30, unique=True, verbose_name="视频名称")
    desc = models.CharField(max_length=100, verbose_name=u"视频描述")
    file = models.FileField(upload_to="video/collection/%Y/%m", verbose_name=u"视频文件")
    date = models.DateField(default=datetime.now, verbose_name=u'视频日期')
    user = models.ForeignKey(User, verbose_name=u"创建用户")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class VideoCollectionDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    video_collection = models.ForeignKey(VideoCollection, related_name='videos', verbose_name='视频合集')
    video = models.ForeignKey(Video, verbose_name='视频')
    user = models.ForeignKey(User, verbose_name=u"创建用户")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = '视频合集明细'
        verbose_name_plural = verbose_name
        unique_together = ('video_collection', 'video')

    def __str__(self):
        return self.video_collection.name
