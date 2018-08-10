from django.shortcuts import render

from rest_framework import mixins
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from common.permissions import IsOwnerOrReadOnly
from .models import Gallery, Photo, GalleryDetail
from .paginations import CommonPagination
from .filters import GalleryFilter
from .serializers import GallerySerializer, PhotoSerializer, GalleryListDetailSerializer, GalleryDetailSerializer, \
    GalleryDetail2Serializer


class GalleryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
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

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return super(self).get_permissions()

    def get_authenticators(self):
        if self.action == "create":
            return [JSONWebTokenAuthentication(), SessionAuthentication()]
        return super(self).get_authenticators()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return GalleryListDetailSerializer
        return GallerySerializer


class PhotoViewset(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list:
    查询所有相册

    retrieve:
    查看某一相册明细
    """
    pagination_class = CommonPagination
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = PhotoSerializer

    def get_queryset(self):
        return Photo.objects.filter(is_del=0)


class GalleryDetailViewset(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list:
    查询所有相册详情

    retrieve:
    查看某一相册详情
    """
    pagination_class = CommonPagination
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        if self.action == "create":
            return GalleryDetail2Serializer
        return GalleryDetailSerializer

    def get_queryset(self):
        return GalleryDetail.objects.filter(is_del=0)
