from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from common.permissions import IsOwnerOrReadOnly
from .models import Singer, Album, Audio, Song, AlbumDetail, AudioDetail
from .serializers import SingerSerializer, AlbumSerializer, AudioSerializer, SongSerializer, AlbumListDetailSerializer, \
    AudioListDetailSerializer, AlbumDetailSerializer, AlbumDetail2Serializer, AudioDetailSerializer, \
    AudioDetail2Serializer, Album2Serializer, Audio2Serializer, Song2Serializer
from .filters import SingerFilter, AlbumFilter, AudioFilter, SongFilter
from .paginations import CommonPagination


class SingerViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    歌手

    list:
    获取歌手列表

    retrieve:
    获取歌手明细

    create:
    创建歌手
    """
    queryset = Singer.objects.filter(is_del=0).order_by("add_time")
    serializer_class = SingerSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = SingerFilter
    search_fields = ('nickname', 'desc')
    ordering_fields = ('add_time',)

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        return super(SingerViewset, self).get_permissions()


class AlbumViewset(viewsets.ModelViewSet):
    """
    专辑

    list:
    获取专辑列表

    retrieve:
    获取专辑明细

    create:
    创建专辑

    update:
    更新专辑

    destroy：
    删除专辑

    """
    queryset = Album.objects.filter(is_del=0).order_by("add_time")
    pagination_class = CommonPagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = AlbumFilter
    search_fields = ('name', 'desc')
    ordering_fields = ('add_time',)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AlbumListDetailSerializer
        if self.action == "create" or self.action == "update":
            return Album2Serializer
        return AlbumSerializer

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action == "update" or self.action == "partial_update" or self.action == "destroy":
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return super(AlbumViewset, self).get_permissions()


class AudioViewset(viewsets.ModelViewSet):
    """
    电台

    list:
    获取电台列表

    retrieve:
    获取电台明细

    create:
    创建电台

    update:
    更新电台

    destroy：
    删除电台

    """
    queryset = Audio.objects.filter(is_del=0).order_by("add_time")
    pagination_class = CommonPagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = AudioFilter
    search_fields = ('name', 'desc')
    ordering_fields = ('add_time',)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AudioListDetailSerializer
        if self.action == "create" or self.action == "update":
            return Audio2Serializer
        return AudioSerializer

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action == "update" or self.action == "partial_update" or self.action == "destroy":
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return super(AudioViewset, self).get_permissions()


class SongViewset(viewsets.ModelViewSet):
    """
    歌曲

    list:
    获取电台列表

    retrieve:
    获取歌曲明细

    create:
    创建歌曲

    update:
    更新歌曲

    destroy：
    删除歌曲

    """
    queryset = Song.objects.filter(is_del=0).order_by("add_time")
    pagination_class = CommonPagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = SongFilter
    search_fields = ('name', 'desc')
    ordering_fields = ('add_time',)

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return Song2Serializer
        return SongSerializer


class AlbumDetailViewset(viewsets.ModelViewSet):
    """
    专辑详情

    list:
    获取专辑详情列表

    retrieve:
    获取专辑详情明细

    create:
    创建专辑详情

    update:
    更新专辑详情

    destroy：
    删除专辑详情

    """
    pagination_class = CommonPagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return AlbumDetail2Serializer
        return AlbumDetailSerializer

    def get_queryset(self):
        return AlbumDetail.objects.filter(is_del=0, user=self.request.user).order_by("add_time")


class AudioDetailViewset(viewsets.ModelViewSet):
    """
    电台详情

    list:
    获取电台详情列表

    retrieve:
    获取电台详情明细

    create:
    创建电台详情

    update:
    更新电台详情

    destroy：
    删除电台详情

    """
    pagination_class = CommonPagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return AudioDetail2Serializer
        return AudioDetailSerializer

    def get_queryset(self):
        return AudioDetail.objects.filter(is_del=0, user=self.request.user).order_by("add_time")
