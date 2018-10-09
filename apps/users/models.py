import uuid
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

from common.choices import GENDER_CHOICES, IS_VALID_CHOICES, IS_DEL_CHOICES, IS_MP_USER_CHOICES
# Create your models here.


class User(AbstractUser):
    """
        用户信息
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=u"主键")
    nickname = models.CharField(max_length=20, default="", verbose_name=u"昵称")
    desc = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"个性签名")
    birthday = models.DateField(null=True, blank=True, verbose_name=u"生日")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6, default="female", verbose_name=u"性别")
    address = models.CharField(max_length=100, default=u"", verbose_name=u"地址")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"手机号")
    avatar = models.ImageField(upload_to="avatar/%Y/%m", max_length=100, default=u"avatar/default.png",
                               verbose_name=u"头像")
    is_mp_user = models.IntegerField(choices=IS_MP_USER_CHOICES, default=0, verbose_name=u"是否是公众号用户")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    is_valid = models.IntegerField(choices=IS_VALID_CHOICES, default=1, verbose_name=u"账号是否有效")
    is_del = models.IntegerField(choices=IS_DEL_CHOICES, default=0, verbose_name=u"是否删除")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
