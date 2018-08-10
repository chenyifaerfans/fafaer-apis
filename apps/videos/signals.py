# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 10:30'

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

# @receiver(post_save, sender=)
def delete_banner(sender, instance=None, created=False, **kwargs):
    pass