# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 10:30'
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import VideoCollection


@receiver(post_save, sender=VideoCollection)
def save_video_collection(sender, instance=None, created=False, **kwargs):
    pass
