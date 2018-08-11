from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

from common.choices import IS_DEL_CHOICES

User = get_user_model()


class VideoCollection(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="视频合集名")
    desc = models.CharField(max_length=100, verbose_name=u"描述")
    date = models.DateField(default=datetime.now, verbose_name=u'日期')
    user = models.ForeignKey(User, verbose_name=u"创建用户")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = '视频合集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="视频名称")
    desc = models.CharField(max_length=100, verbose_name=u"视频描述")
    file = models.FileField(upload_to="video/%Y/%m", verbose_name=u"视频文件")
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
