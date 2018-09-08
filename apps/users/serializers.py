# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/11 10:51'
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("nickname", 'first_name', 'last_name', 'username', "gender", "birthday", "email", "mobile", 'address', 'avatar')


class UserSerializer2(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("nickname", 'username', 'avatar')
