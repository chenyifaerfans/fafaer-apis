# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/11 19:13'
from django import forms
from django.utils.translation import ugettext_lazy as _

from fafaerapis.settings import IMAGE_UPLOAD_MAX_SIZE, IMAGE_UPLOAD_TYPE


class SingerAdminForm(forms.ModelForm):

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        names = getattr(avatar, 'name').split(".")
        if len(names) == 2:
            image_type = names[1]
            if not IMAGE_UPLOAD_TYPE or image_type.lower() in IMAGE_UPLOAD_TYPE:
                if not IMAGE_UPLOAD_MAX_SIZE or getattr(avatar, 'size') <= IMAGE_UPLOAD_MAX_SIZE:
                    return avatar
                else:
                    raise forms.ValidationError(_("图像大小不能大于%sMB" % str(IMAGE_UPLOAD_MAX_SIZE / 1024 / 1024)),
                                                code="avatar_invalid")
            else:
                raise forms.ValidationError(_("图像必须为'%s'格式" % ','.join(IMAGE_UPLOAD_TYPE)), code="avatar_invalid")
        else:
            raise forms.ValidationError(u"上传文件名错误", code="avatar_invalid")
