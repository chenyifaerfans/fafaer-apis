# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-12 16:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='bg_img',
            new_name='background_img',
        ),
    ]