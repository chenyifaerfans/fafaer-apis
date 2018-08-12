# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/12 15:36'
from django.utils.translation import ugettext_lazy as _
from django import forms
from rest_framework import serializers


def validate_fields(field, upload_max_size=0, upload_types=[]):
    names = getattr(field, 'name').split(".")
    field_name = getattr(field, 'field_name')
    if len(names) == 2:
        file_type = names[1]
        if not upload_types or file_type.lower() in upload_types:
            if not upload_max_size or getattr(field, 'size') <= upload_max_size:
                return field
            else:
                raise serializers.ValidationError(_("文件大小不能大于%sMB" % str(upload_max_size / 1024 / 1024)),
                                                  code=_("%s_invalid" % field_name))
        else:
            raise serializers.ValidationError(_("文件必须为'%s'格式" % ','.join(upload_types)),
                                              code=_("%s_invalid" % field_name))
    else:
        raise serializers.ValidationError(_("文件名错误"), code=_("%s_invalid" % field_name))


def clean_fields(field, upload_max_size=0, upload_types=[]):
    names = getattr(field, 'name').split(".")
    field_name = getattr(field, 'field_name')
    if len(names) == 2:
        file_type = names[1]
        if not upload_types or file_type.lower() in upload_types:
            if not upload_max_size or getattr(field, 'size') <= upload_max_size:
                return field
            else:
                raise forms.ValidationError(_("文件大小不能大于%sMB" % str(upload_max_size / 1024 / 1024)),
                                            code=_("%s_invalid" % field_name))
        else:
            raise forms.ValidationError(_("文件必须为'%s'格式" % ','.join(upload_types)), code=_("%s_invalid" % field_name))
    else:
        raise forms.ValidationError(u"文件名错误", code=_("%s_invalid" % field_name))
