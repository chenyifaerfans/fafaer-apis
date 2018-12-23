import uuid
from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from common.choices import IS_DEL_CHOICES

User = get_user_model()


class Gallery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    name = models.CharField(max_length=20, unique=True, verbose_name="相册名")
    desc = models.CharField(max_length=100, verbose_name=u"描述")
    date = models.DateField(default=datetime.now, verbose_name=u'日期')
    cover_img = models.ImageField(upload_to="photos/gallery/cover/%Y/%m", max_length=100, verbose_name='相册图片')
    background_img = models.ImageField(upload_to="photos/gallery/background/%Y/%m",
                                       max_length=100, verbose_name='相册背景图片')
    user = models.ForeignKey(User, verbose_name=u"创建用户")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = '相册'
        verbose_name_plural = verbose_name

    def get_photos_count(self):
        return self.photos.filter(is_del=0).count()

    get_photos_count.short_description = '照片数量'

    def __str__(self):
        return self.name


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    name = models.CharField(max_length=20, unique=True, verbose_name="照片名称")
    desc = models.CharField(max_length=100, verbose_name=u"照片描述")
    file = models.ImageField(upload_to="photos/photo/%Y/%m", verbose_name=u"照片文件")
    date = models.DateField(default=datetime.now, verbose_name=u'拍摄日期')
    user = models.ForeignKey(User, verbose_name=u"创建用户")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = '照片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GalleryDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    gallery = models.ForeignKey(Gallery, related_name='photos', verbose_name='相册')
    photo = models.ForeignKey(Photo, verbose_name='照片')
    user = models.ForeignKey(User, verbose_name=u"创建用户")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = '相册明细'
        verbose_name_plural = verbose_name
        unique_together = ("gallery", "photo")

    def __str__(self):
        return self.gallery.name
