# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/22 23:11'
import xadmin

from .models import Article
from common.base import CommonAdmin
from .forms import ArticleAdminForm


class ArticleAdmin(CommonAdmin):
    list_display = ['title', 'desc', 'date', 'content', 'user', 'hits', 'is_top', 'add_time']
    search_fields = ['title', 'desc', 'date']
    list_filter = ['title', 'desc', 'date']
    form = ArticleAdminForm
    # style_fields = {'content': 'ueditor'}
    # model_icon = 'fa fa-picture-o'

    def queryset(self):
        qs = super(ArticleAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)


xadmin.site.register(Article, ArticleAdmin)