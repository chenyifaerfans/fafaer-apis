# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/7/10 21:29'

IS_DEL_CHOICES = (
    (0, u"未删除"),
    (1, u"已删除")
)

IS_MP_USER_CHOICES = (
    (0, u"否"),
    (1, u"是")
)

GENDER_CHOICES = (
    ("male", u"男"),
    ("female", u"女")
)

IS_VALID_CHOICES = (
    (0, u"无效"),
    (1, u"有效")
)

CONTENT_CHOICES = (
    ("profile", u"个人资料"),
    ("contact", u"联系方式")
)

IS_TOP_CHOICES = (
    (0, u"未置顶"),
    (1, u"已置顶")
)

APP_LAUNCHER_CHOICES = (
    ("intro", u"引导页"),
    ("startup", u"启动页")
)