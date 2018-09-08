from rest_framework import mixins
from rest_framework import filters
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Article
from .serializers import ArticleSerializer
from .paginations import CommonPagination
from .filters import ArticleFilter


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