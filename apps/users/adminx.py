# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/8 17:06'

import xadmin
from xadmin import views

from django.contrib.auth import get_user_model

User = get_user_model()


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "fafaer-Api"
    site_footer = "fafaer-Api"
    menu_style = "accordion"


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)