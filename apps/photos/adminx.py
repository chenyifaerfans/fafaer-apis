# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:42'

import xadmin

from .models import Gallery, Photo, GalleryDetail
from .forms import PhotoAdminForm
from common.base import CommonAdmin


class GalleryAdmin(CommonAdmin):
    list_display = ['name', 'desc', 'date', 'get_photos_count', 'user', 'add_time']
    search_fields = ['name', 'desc', 'date']
    list_filter = ['name', 'desc', 'date']
    model_icon = 'fa fa-picture-o'

    def queryset(self):
        qs = super(GalleryAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)

    def get_model_form(self, **kwargs):
        form = super(GalleryAdmin, self).get_model_form(**kwargs)
        form.base_fields['user'].initial = self.request.user
        return form


class PhotoAdmin(CommonAdmin):
    list_display = ['name', 'desc', 'date', 'file', 'user', 'add_time']
    search_fields = ['name', 'desc', 'date']
    list_filter = ['name', 'desc', 'date']
    form = PhotoAdminForm

    def queryset(self):
        qs = super(PhotoAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)

    def get_model_form(self, **kwargs):
        form = super(PhotoAdmin, self).get_model_form(**kwargs)
        form.base_fields['user'].initial = self.request.user
        return form


class GalleryDetailAdmin(CommonAdmin):
    list_display = ['gallery', 'photo', 'user', 'add_time']
    search_fields = ['gallery', 'photo']
    list_filter = ['gallery', 'photo']

    def queryset(self):
        qs = super(GalleryDetailAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "photo":
            photo_ids = [detail.photo_id for detail in GalleryDetail.objects.filter(is_del=0)]
            kwargs["queryset"] = Photo.objects.exclude(id__in=photo_ids).filter(is_del=0)
        return super(GalleryDetailAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def get_model_form(self, **kwargs):
        form = super(GalleryDetailAdmin, self).get_model_form(**kwargs)
        form.base_fields['user'].initial = self.request.user
        return form


xadmin.site.register(Gallery, GalleryAdmin)
xadmin.site.register(Photo, PhotoAdmin)
xadmin.site.register(GalleryDetail, GalleryDetailAdmin)
