from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

from common.choices import IS_DEL_CHOICES, CONTENT_CHOICES

User = get_user_model()


class Banner(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"标题")
    desc = models.CharField(max_length=100, verbose_name=u"描述")
    image = models.ImageField(upload_to="banner/%Y/%m", max_length=100, verbose_name=u"封面")
    order = models.IntegerField(default=10, verbose_name=u"排序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"标题")
    desc = models.CharField(max_length=100, verbose_name=u"描述")
    avatar = models.ImageField(upload_to="avatar/%Y/%m", max_length=100, default=u"avatar/default.png",
                               verbose_name=u"头像")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = u"简介"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ProfileDetail(models.Model):
    title = models.CharField(max_length=20, verbose_name=u"标题")
    content = models.CharField(max_length=100, verbose_name=u"内容")
    type = models.CharField(choices=CONTENT_CHOICES, max_length=8, verbose_name=u"类型")
    image = models.ImageField(upload_to="content/%Y/%m", max_length=100, verbose_name=u"封面")
    order = models.IntegerField(default=10, verbose_name=u"排序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = u"个人资料"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ContactDetail(ProfileDetail):
    class Meta:
        verbose_name = u"联系方式"
        verbose_name_plural = verbose_name
        proxy = True