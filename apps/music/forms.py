# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/11 19:13'
from django import forms

from common.validations import clean_fields
from fafaerapis.settings import IMAGE_UPLOAD_MAX_SIZE, IMAGE_UPLOAD_TYPE, MUSIC_UPLOAD_MAX_SIZE, MUSIC_UPLOAD_TYPE


class SingerAdminForm(forms.ModelForm):

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        return clean_fields(avatar, upload_max_size=IMAGE_UPLOAD_MAX_SIZE, upload_types=IMAGE_UPLOAD_TYPE)

    def clean_background_img(self):
        background_img = self.cleaned_data['background_img']
        return clean_fields(background_img, upload_max_size=IMAGE_UPLOAD_MAX_SIZE, upload_types=IMAGE_UPLOAD_TYPE)


class AlbumAdminForm(forms.ModelForm):

    def clean_cover_img(self):
        cover_img = self.cleaned_data['cover_img']
        return clean_fields(cover_img, upload_max_size=IMAGE_UPLOAD_MAX_SIZE, upload_types=IMAGE_UPLOAD_TYPE)

    def clean_background_img(self):
        background_img = self.cleaned_data['background_img']
        return clean_fields(background_img, upload_max_size=IMAGE_UPLOAD_MAX_SIZE, upload_types=IMAGE_UPLOAD_TYPE)


class SongAdminForm(forms.ModelForm):

    def clean_file(self):
        file = self.cleaned_data['file']
        return clean_fields(file, upload_max_size=MUSIC_UPLOAD_MAX_SIZE, upload_types=MUSIC_UPLOAD_TYPE)
