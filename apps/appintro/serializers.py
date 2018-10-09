# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/8 22:32'

from rest_framework import serializers

from .models import AppIntro


class AppIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppIntro
        fields = ('title', 'desc', 'link', 'image', )
