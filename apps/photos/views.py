from django.shortcuts import render

from rest_framework import mixins
from rest_framework import filters
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Gallery
from .paginations import CommonPagination
from .filters import GalleryFilter
from .serializers import GallerySerializer, GalleryListDetailSerializer


class GalleryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
    查询所有相册

    retrieve:
    查看某一相册明细

    """

    queryset = Gallery.objects.filter(is_del=0)
    pagination_class = CommonPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GalleryFilter
    search_fields = ('name', 'desc')
    ordering_fields = ('add_time',)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return GalleryListDetailSerializer
        return GallerySerializer
