# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-09 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover_img',
            field=models.ImageField(default=None, upload_to='article/%Y/%m', verbose_name='封面照片文件'),
        ),
    ]