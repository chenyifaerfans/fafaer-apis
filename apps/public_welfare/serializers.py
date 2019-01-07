# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:43'

from common.base import CommonSerializer
from .models import Lost


class LostSerializer(CommonSerializer):

    class Meta:
        model = Lost
        exclude = ('is_del', 'add_time', 'update_time')
