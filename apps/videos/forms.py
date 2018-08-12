# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/11 21:49'
from django import forms

from common.validations import clean_fields
from fafaerapis.settings import VIDEO_UPLOAD_MAX_SIZE, VIDEO_UPLOAD_TYPE


class VideoAdminForm(forms.ModelForm):

    def clean_file(self):
        file = self.cleaned_data['file']
        return clean_fields(file, upload_max_size=VIDEO_UPLOAD_MAX_SIZE, upload_types=VIDEO_UPLOAD_TYPE)