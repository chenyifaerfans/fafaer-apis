# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 10:30'

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_save

from .models import Song


@receiver(post_save, sender=Song)
def save_song(sender, instance=None, created=False, **kwargs):
    file = instance.file

    # song = AudioSegment.from_mp3(file)
    if created:
        pass