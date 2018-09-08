# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/9/8 16:44'
from users.serializers import UserSerializer2
from common.base import CommonSerializer
from .models import Article


class ArticleSerializer(CommonSerializer):
    user = UserSerializer2()

    class Meta:
        model = Article
        exclude = ('is_del', 'add_time', 'update_time')