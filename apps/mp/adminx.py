# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/8 21:11'
from django.utils.translation import ugettext as _, ungettext
from xadmin.util import model_format_dict, model_ngettext
from xadmin.plugins.actions import BaseActionView
import xadmin

from .models import Banner, Profile, ProfileDetail, ContactDetail


class DeleteSelected(BaseActionView):

    # 这里需要填写三个属性
    action_name = "delete_selected"    #: 相当于这个 Action 的唯一标示, 尽量用比较针对性的名字
    description = _(u'Delete selected %(verbose_name_plural)s') #: 描述, 出现在 Action 菜单中, 可以使用 ``%(verbose_name_plural)s`` 代替 Model 的名字.
    model_perm = 'delete'    #: 该 Action 所需权限

    # 而后实现 do_action 方法
    def do_action(self, queryset):
        n = queryset.count()
        if n:
            queryset.update(is_del=1)
            self.message_user(_("Successfully deleted %(count)d %(items)s.") % {
                        "count": n, "items": model_ngettext(self.opts, n)
                    }, 'success')


class BannerAdmin(object):
    list_display = ['name', 'desc', 'image', 'add_time', 'is_del']
    search_fields = ['name', 'desc', 'image']
    list_filter = ['name', 'desc', 'image', 'add_time']
    # readonly_fields = ['is_del']
    # 详情页面不显示该字段，与readonly_fields冲突，不能同时设置字段
    exclude = ['is_del']
    actions = [DeleteSelected]

    def queryset(self):
        qs = super(BannerAdmin, self).queryset()
        return qs.filter(is_del=0)


class ProfileAdmin(object):
    list_display = ['name', 'desc', 'avatar', 'add_time']
    search_fields = ['name', 'desc', 'avatar']
    list_filter = ['name', 'desc', 'avatar', 'add_time']
    exclude = ['is_del']
    actions = [DeleteSelected]

    def queryset(self):
        qs = super(ProfileAdmin, self).queryset()
        return qs.filter(is_del=0)


class ProfileDetailAdmin(object):
    list_display = ['title', 'content', 'type', 'image', 'order', 'add_time']
    search_fields = ['title', 'content', 'type', 'image']
    list_filter = ['title', 'content', 'type', 'image', 'add_time']
    exclude = ['is_del']
    actions = [DeleteSelected]

    def queryset(self):
        qs = super(ProfileDetailAdmin, self).queryset()
        return qs.filter(type='profile', is_del=0)


class ContactDetailAdmin(object):
    list_display = ['title', 'content', 'type', 'image', 'order', 'add_time']
    search_fields = ['title', 'content', 'type', 'image']
    list_filter = ['title', 'content', 'type', 'image', 'add_time']
    exclude = ['is_del']
    actions = [DeleteSelected]

    def queryset(self):
        qs = super(ContactDetailAdmin, self).queryset()
        return qs.filter(type='contact', is_del=0)


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Profile, ProfileAdmin)
xadmin.site.register(ProfileDetail, ProfileDetailAdmin)
xadmin.site.register(ContactDetail, ContactDetailAdmin)