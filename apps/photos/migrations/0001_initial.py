# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-11 16:15
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
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='相册名')),
                ('desc', models.CharField(max_length=100, verbose_name='描述')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='日期')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')),
                ('is_del', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='是否删除')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建用户')),
            ],
            options={
                'verbose_name': '相册',
                'verbose_name_plural': '相册',
            },
        ),
        migrations.CreateModel(
            name='GalleryDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')),
                ('is_del', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='是否删除')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='photos.Gallery', verbose_name='相册')),
            ],
            options={
                'verbose_name': '相册明细',
                'verbose_name_plural': '相册明细',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='照片名称')),
                ('desc', models.CharField(max_length=100, verbose_name='照片描述')),
                ('file', models.FileField(upload_to='photo/%Y/%m', verbose_name='照片文件')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='拍摄日期')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')),
                ('is_del', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='是否删除')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建用户')),
            ],
            options={
                'verbose_name': '照片',
                'verbose_name_plural': '照片',
            },
        ),
        migrations.AddField(
            model_name='gallerydetail',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Photo', verbose_name='照片'),
        ),
        migrations.AddField(
            model_name='gallerydetail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建用户'),
        ),
        migrations.AlterUniqueTogether(
            name='gallerydetail',
            unique_together=set([('gallery', 'photo')]),
        ),
    ]
