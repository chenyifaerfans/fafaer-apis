# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/22 23:11'
import xadmin
from markdownx.admin import MarkdownxModelAdmin

from .models import Banner, Article, Topic, Recommend, TopicDetail, RecommendDetail
from common.base import CommonAdmin


class BannerAdmin(CommonAdmin):
    list_display = ['title', 'desc', 'image', 'href', 'order', 'add_time']
    search_fields = ['title', 'desc', 'image', 'href',]
    list_filter = ['title', 'desc', 'image']

    def queryset(self):
        qs = super(BannerAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)


class ArticleAdmin(CommonAdmin):
    list_display = ['title', 'desc', 'date', 'content', 'user', 'hits', 'is_top', 'add_time']
    search_fields = ['title', 'desc', 'date']
    list_filter = ['title', 'desc', 'date']
    # style_fields = {'content': 'ueditor'}
    # model_icon = 'fa fa-picture-o'

    def queryset(self):
        qs = super(ArticleAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)

    def get_model_form(self, **kwargs):
        form = super(ArticleAdmin, self).get_model_form(**kwargs)
        form.base_fields['user'].initial = self.request.user
        return form


class TopicAdmin(CommonAdmin):
    list_display = ['title', 'cover_img', 'desc', 'hits', 'user', 'hits', 'is_recommend', 'add_time']
    search_fields = ['title', 'cover_img', 'desc']
    list_filter = ['title', 'cover_img', 'desc']

    def queryset(self):
        qs = super(TopicAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0, is_recommend=0)
        return qs.filter(is_del=0, is_recommend=0, user=self.request.user)

    def get_model_form(self, **kwargs):
        form = super(TopicAdmin, self).get_model_form(**kwargs)
        form.base_fields['user'].initial = self.request.user
        return form


class RecommendAdmin(CommonAdmin):
    list_display = ['title', 'cover_img', 'desc', 'hits', 'user', 'hits', 'is_recommend', 'add_time']
    search_fields = ['title', 'cover_img', 'desc']
    list_filter = ['title', 'cover_img', 'desc']

    def queryset(self):
        qs = super(RecommendAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0, is_recommend=1)
        return qs.filter(is_del=0, is_recommend=1, user=self.request.user)

    def get_model_form(self, **kwargs):
        form = super(RecommendAdmin, self).get_model_form(**kwargs)
        form.base_fields['user'].initial = self.request.user
        return form


class TopicDetailAdmin(CommonAdmin):
    list_display = ['topic', 'article', 'user', 'add_time']
    search_fields = ['topic', 'article', 'user']
    list_filter = ['topic', 'article', 'user']

    def queryset(self):
        qs = super(TopicDetailAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "topic":
            kwargs["queryset"] = Topic.objects.filter(is_del=0, is_recommend=0)
        return super(TopicDetailAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def get_model_form(self, **kwargs):
        form = super(TopicDetailAdmin, self).get_model_form(**kwargs)
        form.base_fields['user'].initial = self.request.user
        return form


class RecommendDetailAdmin(CommonAdmin):
    list_display = ['recommend', 'article', 'user', 'add_time']
    search_fields = ['recommend', 'article', 'user']
    list_filter = ['recommend', 'article', 'user']

    def queryset(self):
        qs = super(RecommendDetailAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs.filter(is_del=0)
        return qs.filter(is_del=0, user=self.request.user)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "recommend":
            kwargs["queryset"] = Recommend.objects.filter(is_del=0, is_recommend=1)
        return super(RecommendDetailAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def get_model_form(self, **kwargs):
        form = super(RecommendDetailAdmin, self).get_model_form(**kwargs)
        form.base_fields['user'].initial = self.request.user
        return form


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Topic, TopicAdmin)
xadmin.site.register(Recommend, RecommendAdmin)
xadmin.site.register(TopicDetail, TopicDetailAdmin)
xadmin.site.register(RecommendDetail, RecommendDetailAdmin)