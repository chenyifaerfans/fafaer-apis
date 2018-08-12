# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:42'
import xadmin

from .models import VideoCollection, Video, VideoCollectionDetail
from .forms import VideoAdminForm
from common.base import CommonAdmin


class VideoCollectionAdmin(CommonAdmin):
    list_display = ['name', 'desc', 'date', 'get_videos_count', 'user', 'add_time']
    search_fields = ['name', 'desc', 'date']
    list_filter = ['name', 'desc', 'date']
    # list_display_links = ['get_videos_count']
    model_icon = 'fa fa-video-camera'

    def queryset(self):
        qs = super(VideoCollectionAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)


class VideoAdmin(CommonAdmin):
    list_display = ['name', 'desc', 'date', 'user', 'file', 'add_time']
    search_fields = ['name', 'desc', 'date']
    list_filter = ['name', 'desc', 'date']
    form = VideoAdminForm

    def queryset(self):
        qs = super(VideoAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)


class VideoCollectionDetailAdmin(CommonAdmin):
    list_display = ['video_collection', 'video', 'user', 'add_time']
    search_fields = ['video_collection', 'video']
    list_filter = ['video_collection', 'video']

    def queryset(self):
        qs = super(VideoCollectionDetailAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)

    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     if db_field.name == "video":
    #         video_ids = [detail.video_id for detail in VideoCollectionDetail.objects.filter(is_del=0)]
    #         kwargs["queryset"] = Video.objects.exclude(id__in=video_ids).filter(is_del=0)
    #     return super(VideoCollectionDetailAdmin, self).formfield_for_dbfield(db_field, **kwargs)


xadmin.site.register(VideoCollection, VideoCollectionAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(VideoCollectionDetail, VideoCollectionDetailAdmin)
