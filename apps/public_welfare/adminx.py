# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:42'
import xadmin

from .models import Lost
from common.base import CommonAdmin


class LostAdmin(CommonAdmin):
    list_display = ['name', 'age', 'gender', 'desc', 'lost_location', 'lost_date', 'img', 'weibo',
                    'closed', 'closed_explain', 'add_time']
    search_fields = ['name', 'gender', 'desc']
    list_filter = ['name', 'gender', 'desc']
    # list_display_links = ['weibo']
    model_icon = 'fa fa-heart'

    def queryset(self):
        qs = super(LostAdmin, self).queryset()
        return qs.filter(is_del=0)


xadmin.site.register(Lost, LostAdmin)
