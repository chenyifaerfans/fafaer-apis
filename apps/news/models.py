import uuid
from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from markdownx.models import MarkdownxField
from DjangoUeditor.models import UEditorField

from common.choices import IS_DEL_CHOICES, IS_TOP_CHOICES, IS_RECOMMEND_CHOICES

User = get_user_model()


class Banner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    title = models.CharField(max_length=20, verbose_name=u"标题")
    desc = models.CharField(max_length=100, verbose_name=u"描述")
    image = models.ImageField(upload_to="article/banner/%Y/%m", max_length=100, verbose_name=u"封面")
    href = models.URLField(max_length=200, null=True, blank=True, verbose_name=u"图片链接")
    order = models.IntegerField(default=10, verbose_name=u"排序", help_text="排序字段")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = u"新闻轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    title = models.CharField(max_length=20, unique=True, verbose_name="文章名")
    cover_img = models.ImageField(upload_to="article/%Y/%m", default=None, verbose_name=u"封面照片文件")
    desc = models.CharField(max_length=100, verbose_name=u"文章描述")
    date = models.DateField(default=datetime.now, verbose_name=u'日期')
    user = models.ForeignKey(User, verbose_name=u"创建用户")
    # content = UEditorField(width=600, height=300, imagePath="article/ueditor/", filePath="article/ueditor/",
    #                        upload_settings={"imageMaxSize": 1204000}, default="", verbose_name=u"文章详细信息")

    content = MarkdownxField(verbose_name=u"文章详细信息")

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


class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    title = models.CharField(max_length=20, unique=True, verbose_name="主题名")
    cover_img = models.ImageField(upload_to="article/topic/%Y/%m", default=None, verbose_name=u"封面照片")
    desc = models.TextField(null=True, blank=True, verbose_name=u"主题描述")
    user = models.ForeignKey(User, verbose_name=u"创建用户")
    hits = models.IntegerField(default=0, verbose_name=u"点击量")
    is_recommend = models.IntegerField(choices=IS_RECOMMEND_CHOICES, default=0, verbose_name=u"是否推荐")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = '主题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Recommend(Topic):
    class Meta:
        verbose_name = u"编辑推荐"
        verbose_name_plural = verbose_name
        proxy = True


class TopicDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    topic = models.ForeignKey(Topic, related_name='topics', verbose_name=u"主题")
    article = models.ForeignKey(Article, verbose_name=u"文章")
    user = models.ForeignKey(User, verbose_name=u"创建用户")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = '主题详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.topic.title


class RecommendDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    recommend = models.ForeignKey(Recommend, related_name='recommends', verbose_name=u"编辑推荐")
    article = models.ForeignKey(Article, verbose_name=u"文章")
    user = models.ForeignKey(User, verbose_name=u"创建用户")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = '编辑推荐详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.recommend.title
