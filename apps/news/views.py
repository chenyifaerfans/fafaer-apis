from rest_framework import mixins
from rest_framework import filters
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Banner, Article, Topic, Recommend
from .serializers import BannerSerializer, ArticleSerializer, TopicSerializer, TopicSerializer2,\
    RecommendSerializer, RecommendSerializer2
from .paginations import CommonPagination
from .filters import ArticleFilter


class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    新闻轮播图

    list:
    新闻轮播图列表
    """
    queryset = Banner.objects.filter(is_del=0).order_by("add_time")
    serializer_class = BannerSerializer
    pagination_class = CommonPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('add_time', 'order')


class ArticleViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    新闻

    list:
    新闻列表

    retrieve:
    新闻详情
    """
    queryset = Article.objects.filter(is_del=0).order_by("add_time")
    serializer_class = ArticleSerializer
    pagination_class = CommonPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ArticleFilter
    search_fields = ('title', 'desc', 'content')
    ordering_fields = ('add_time',)


class TopicViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    主题

    list:
    主题列表

    retrieve:
    主题详情
    """
    queryset = Topic.objects.filter(is_del=0, is_recommend=0).order_by("add_time")
    pagination_class = CommonPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('add_time', 'update_time')

    def get_serializer_class(self):
        if self.action == "retrieve":
            return TopicSerializer2
        return TopicSerializer


class RecommendViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    编辑推荐

    list:
    编辑推荐列表

    retrieve:
    编辑推荐详情
    """
    queryset = Recommend.objects.filter(is_del=0, is_recommend=1).order_by("add_time")
    serializer_class = RecommendSerializer
    pagination_class = CommonPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('add_time', 'update_time')

    def get_serializer_class(self):
        if self.action == "retrieve":
            return RecommendSerializer2
        return RecommendSerializer
