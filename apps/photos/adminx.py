# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:42'

import xadmin

from .models import Gallery, Photo, GalleryDetail
from common.base import CommonAdmin


class GalleryAdmin(CommonAdmin):
    list_display = ['name', 'desc', 'date', 'add_time']
    search_fields = ['name', 'desc', 'date']
    list_filter = ['name', 'desc', 'date']

    def queryset(self):
        qs = super(GalleryAdmin, self).queryset()
        return qs.filter(is_del=0)


class PhotoAdmin(CommonAdmin):
    list_display = ['name', 'desc', 'date', 'file', 'add_time']
    search_fields = ['name', 'desc', 'date']
    list_filter = ['name', 'desc', 'date']

    def queryset(self):
        qs = super(PhotoAdmin, self).queryset()
        return qs.filter(is_del=0)


class GalleryDetailAdmin(CommonAdmin):
    list_display = ['gallery', 'photo', 'add_time']
    search_fields = ['gallery', 'photo']
    list_filter = ['gallery', 'photo']

    def queryset(self):
        qs = super(GalleryDetailAdmin, self).queryset()
        return qs.filter(is_del=0)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "photo":
            photo_ids = [detail.photo_id for detail in GalleryDetail.objects.filter(is_del=0)]
            kwargs["queryset"] = Photo.objects.exclude(id__in=photo_ids).filter(is_del=0)
        return super(GalleryDetailAdmin, self).formfield_for_dbfield(db_field, **kwargs)


xadmin.site.register(Gallery, GalleryAdmin)
xadmin.site.register(Photo, PhotoAdmin)
xadmin.site.register(GalleryDetail, GalleryDetailAdmin)

