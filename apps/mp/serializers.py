# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/8 22:32'
from rest_framework import serializers

from .models import Banner, Profile, ProfileDetail


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('image', )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'desc', 'avatar')


class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileDetail
        fields = ('title', 'content', 'image')