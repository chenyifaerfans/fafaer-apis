# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/11 21:49'

from django import forms

from common.validations import clean_fields
from fafaerapis.settings import IMAGE_UPLOAD_MAX_SIZE, IMAGE_UPLOAD_TYPE


class PhotoAdminForm(forms.ModelForm):

    def clean_file(self):
        file = self.cleaned_data['file']
        return clean_fields(file, upload_max_size=IMAGE_UPLOAD_MAX_SIZE, upload_types=IMAGE_UPLOAD_TYPE)