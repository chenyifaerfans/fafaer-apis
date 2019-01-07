import uuid
from datetime import datetime
from django.db import models

from common.choices import IS_DEL_CHOICES, GENDER_CHOICES


class Lost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    name = models.CharField(max_length=30, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, default="male", verbose_name="性别")
    desc = models.CharField(max_length=300, verbose_name=u"描述")
    lost_location = models.CharField(max_length=100, verbose_name=u"走失地点")
    lost_date = models.DateTimeField(default=datetime.now, verbose_name=u'走失日期')
    img = models.ImageField(upload_to="public_welfare/lost/%Y/%m", max_length=100, verbose_name='照片')
    weibo = models.URLField(max_length=100, verbose_name="微博地址")
    closed = models.BooleanField(verbose_name="是否结案")
    closed_explain = models.CharField(max_length=300, default="", null=True, blank=True, verbose_name=u"结案详情")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = '走失儿童'
        verbose_name_plural = verbose_name

    # def go_to(self):
    #     from django.utils.safestring import mark_safe
    #     return mark_safe('<a href="http://www.upcwangying.com" target="_blank">链接</a>')
    # go_to.short_description = u'链接'

    def __str__(self):
        return self.name