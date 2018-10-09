from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import AppIntro
from .filters import AppIntroFilter
from .serializers import AppIntroSerializer


class AppIntroViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    App启动页

    list:
        列表
    """
    queryset = AppIntro.objects.filter(is_del=0)
    serializer_class = AppIntroSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = AppIntroFilter
    ordering_fields = ('order',)
