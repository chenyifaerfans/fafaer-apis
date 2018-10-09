import uuid
from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

from common.choices import IS_DEL_CHOICES, APP_LAUNCHER_CHOICES

User = get_user_model()


class AppIntro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    title = models.CharField(max_length=20, verbose_name=u"标题")
    desc = models.CharField(max_length=100, null=True, blank=True, verbose_name=u"描述")
    image = models.ImageField(upload_to="app/intro/%Y/%m", max_length=100, verbose_name=u"封面")
    type = models.CharField(choices=APP_LAUNCHER_CHOICES, default="intro", max_length=10, verbose_name=u"类型",
                            help_text="类型")
    link = models.URLField(max_length=200, null=True, blank=True, verbose_name=u"链接")
    order = models.IntegerField(default=10, verbose_name=u"排序", help_text="排序字段")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = u"App引导页"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class AppStartUpPage(AppIntro):
    class Meta:
        verbose_name = u"App启动页"
        verbose_name_plural = verbose_name
        proxy = True
