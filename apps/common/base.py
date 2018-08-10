# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/10 10:57'
from django.utils.translation import ugettext as _, ungettext
from xadmin.plugins.actions import BaseActionView
from xadmin.util import model_format_dict, model_ngettext


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


class CommonAdmin(object):
    actions = [DeleteSelected]
    readonly_fields = ['add_time']
    # 详情页面不显示该字段，与readonly_fields冲突，不能同时设置字段
    exclude = ['is_del']
    # actions_on_top = True

    def delete_model(self):
        if hasattr(self.obj, 'is_del'):
            self.obj.is_del = 1
            self.obj.save()
        else:
            self.obj.delete()