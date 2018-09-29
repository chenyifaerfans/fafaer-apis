from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from DjangoUeditor.models import UEditorField

from common.choices import IS_DEL_CHOICES, IS_TOP_CHOICES

User = get_user_model()


class Article(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name="文章名")
    desc = models.CharField(max_length=100, verbose_name=u"文章描述")
    date = models.DateField(default=datetime.now, verbose_name=u'日期')
    user = models.ForeignKey(User, verbose_name=u"创建用户")
    # content = UEditorField(width=600, height=300, imagePath="article/ueditor/", filePath="article/ueditor/",
    #                        upload_settings={"imageMaxSize": 1204000}, default="", verbose_name=u"文章详细信息")

    content = models.TextField(verbose_name=u"文章详细信息")

    hits = models.IntegerField(default=0, verbose_name=u"点击量")
    is_top = models.IntegerField(choices=IS_TOP_CHOICES, default=0, verbose_name=u"是否置顶")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
