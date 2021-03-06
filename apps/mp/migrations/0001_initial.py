# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-08 22:12
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标题')),
                ('desc', models.CharField(max_length=100, verbose_name='描述')),
                ('image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='封面')),
                ('order', models.IntegerField(default=10, verbose_name='排序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('is_del', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='是否删除')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '内容详情',
                'verbose_name_plural': '内容详情',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标题')),
                ('desc', models.CharField(max_length=100, verbose_name='描述')),
                ('avatar', models.ImageField(default='avatar/default.png', upload_to='avatar/%Y/%m', verbose_name='头像')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('is_del', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '内容',
                'verbose_name_plural': '内容',
            },
        ),
        migrations.CreateModel(
            name='ProfileDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('content', models.CharField(max_length=100, verbose_name='内容')),
                ('type', models.CharField(choices=[('profile', '个人资料'), ('contacts', '联系方式')], max_length=8, verbose_name='类型')),
                ('image', models.ImageField(upload_to='content/%Y/%m', verbose_name='封面')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('is_del', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '个人资料',
                'verbose_name_plural': '个人资料',
            },
        ),
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
            ],
            options={
                'verbose_name': '联系方式',
                'verbose_name_plural': '联系方式',
                'proxy': True,
                'indexes': [],
            },
            bases=('mp.profiledetail',),
        ),
    ]
