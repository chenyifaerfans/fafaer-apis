from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from common.permissions import IsOwnerOrReadOnly
from .models import Gallery, Photo, GalleryDetail
from .paginations import CommonPagination
from .filters import GalleryFilter, GalleryDetailFilter
from .serializers import GallerySerializer, PhotoSerializer, GalleryListDetailSerializer, GalleryDetailSerializer, \
    GalleryDetail2Serializer


class GalleryViewset(viewsets.ModelViewSet):
    """
    相册

    list:
    查询所有相册

    retrieve:
    查看某一相册明细

    create:
    添加相册

    update:
    更新相册

    destroy:
    删除相册
    """
    queryset = Gallery.objects.filter(is_del=0).order_by("add_time")
    pagination_class = CommonPagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GalleryFilter
    search_fields = ('name', 'desc')
    ordering_fields = ('add_time',)

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action == "partial_update" or self.action == "update" or self.action == "destroy":
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return super(GalleryViewset, self).get_permissions()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return GalleryListDetailSerializer
        return GallerySerializer


class PhotoViewset(viewsets.ModelViewSet):
    """
    照片

    list:
    查询所有照片

    retrieve:
    查看某一照片明细

    create:
    添加图片

    update:
    更新图片

    destroy:
    删除图片
    """
    pagination_class = CommonPagination
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = PhotoSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_class = GalleryFilter
    search_fields = ('name', 'desc')
    ordering_fields = ('add_time',)

    def get_queryset(self):
        return Photo.objects.filter(is_del=0, user=self.request.user).order_by("add_time")


class GalleryDetailViewset(viewsets.ModelViewSet):
    """
    相册明细

    list:
    查询所有相册详情

    retrieve:
    查看某一相册详情

    create:
    向相册中添加图片

    update:
    更新相册中的图片

    destroy：
    删除相册中的图片

    """
    queryset = GalleryDetail.objects.filter(is_del=0).order_by("add_time")
    pagination_class = CommonPagination
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GalleryDetailFilter
    search_fields = ('photo__name', 'photo__desc')
    ordering_fields = ('add_time',)

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action == "partial_update" or self.action == "update" or self.action == "destroy":
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return super(GalleryDetailViewset, self).get_permissions()

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return GalleryDetail2Serializer
        return GalleryDetailSerializer

    # def get_queryset(self):
    #     return GalleryDetail.objects.filter(is_del=0, user=self.request.user).order_by("add_time")
