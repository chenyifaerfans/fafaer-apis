from django.shortcuts import render

from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from common.permissions import IsOwnerOrReadOnly
from .models import VideoCollection, Video, VideoCollectionDetail
from .paginations import CommonPagination
from .filters import VideoCollectionFilter
from .serializers import VideoCollectionSerializer, VideoSerializer, VideoCollectionDetailSerializer,\
    VideoCollectionListDetailSerializer, VideoCollectionDetail2Serializer


class VideoCollectionViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list:
    获取视频合集列表

    retrieve:
    获取视频合集明细

    create:
    创建视频合集

    """

    queryset = VideoCollection.objects.filter(is_del=0)
    pagination_class = CommonPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = VideoCollectionFilter
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
            return VideoCollectionListDetailSerializer
        return VideoCollectionSerializer


class VideoViewset(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list:
    查询视频列表

    create:
    创建视频

    """
    pagination_class = CommonPagination
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = VideoSerializer

    def get_queryset(self):
        return Video.objects.filter(is_del=0)


class VideoCollectionDetailViewset(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list:
    查询视频合集列表

    create:
    向视频合集中添加视频

    """
    pagination_class = CommonPagination
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        if self.action == "create":
            return VideoCollectionDetail2Serializer
        return VideoCollectionDetailSerializer

    def get_queryset(self):
        return VideoCollectionDetail.objects.filter(is_del=0)
