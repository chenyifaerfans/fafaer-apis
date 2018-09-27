from rest_framework import filters
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


class VideoCollectionViewset(viewsets.ModelViewSet):
    """
    视频合集

    list:
    获取视频合集列表

    retrieve:
    获取视频合集明细

    create:
    创建视频合集

    update:
    更新视频合集

    destroy：
    删除视频合集

    """
    queryset = VideoCollection.objects.filter(is_del=0).order_by("add_time")
    pagination_class = CommonPagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = VideoCollectionFilter
    search_fields = ('name', 'desc')
    ordering_fields = ('add_time',)

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action == "update" or self.action == "destroy":
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return super(VideoCollectionViewset, self).get_permissions()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return VideoCollectionListDetailSerializer
        return VideoCollectionSerializer


class VideoViewset(viewsets.ModelViewSet):
    """
    视频

    list:
    查询视频列表

    retrieve:
    获取视频详情

    create:
    创建视频

    update:
    更新视频

    destroy：
    删除视频

    """
    pagination_class = CommonPagination
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = VideoSerializer

    def get_queryset(self):
        return Video.objects.filter(is_del=0, user=self.request.user).order_by("add_time")


class VideoCollectionDetailViewset(viewsets.ModelViewSet):
    """
    视频合集明细

    list:
    查询视频合集明细列表

    retrieve:
    获取视频合集明细详情

    create:
    向视频合集中添加视频

    update:
    更新视频合集明细

    destroy：
    删除视频合集明细

    """
    pagination_class = CommonPagination
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return VideoCollectionDetail2Serializer
        return VideoCollectionDetailSerializer

    def get_queryset(self):
        return VideoCollectionDetail.objects.filter(is_del=0, user=self.request.user).order_by("add_time")
